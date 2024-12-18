import tkinter as tk  # Основной GUI-фреймворк
from tkinter import ttk, messagebox  # Виджеты и всплывающие сообщения
from tkcalendar import Calendar, DateEntry  # Виджеты календаря
import json  # Для работы с файлами JSON
import os  # Для работы с файловой системой

# Имя файла для сохранения событий
FILE_NAME = "events.json"

# Функция загрузки событий из файла
def load_events():
    if os.path.exists(FILE_NAME):  # Проверяем, существует ли файл
        with open(FILE_NAME, "r") as f:  # Открываем файл на чтение
            return json.load(f)  # Загружаем данные
    return {}  # Возвращаем пустой словарь, если файл отсутствует

# Функция сохранения событий в файл
def save_events(events):
    with open(FILE_NAME, "w") as f:  # Открываем файл на запись
        json.dump(events, f)  # Сохраняем данные в файл

# Основной класс приложения
class EventPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Инициализация базового окна
        self.title("Planner")  # Заголовок окна
        self.geometry("400x400")  # Размер окна
        
        self.events = load_events()  # Загрузка существующих событий
        
        # Календарь для выбора даты
        self.cal = Calendar(self, selectmode="day", date_pattern="yyyy-mm-dd", showweeknumbers=False)
        self.cal.pack(pady=20)
        
        # Кнопки управления
        self.add_event_btn = tk.Button(self, text="Add event", command=self.open_add_event_window)
        self.add_event_btn.pack(pady=5)
        
        self.view_event_btn = tk.Button(self, text="See events", command=self.open_view_events_window)
        self.view_event_btn.pack(pady=5)
        
        self.quit_btn = tk.Button(self, text="Exit", command=self.quit)
        self.quit_btn.pack(pady=5)
        
    # Открытие окна добавления события
    def open_add_event_window(self):
        AddEventWindow(self)
        
    # Открытие окна просмотра событий
    def open_view_events_window(self):
        selected_date = self.cal.get_date()  # Получаем выбранную дату
        if selected_date in self.events:  # Проверяем, есть ли события на эту дату
            ViewEventsWindow(self, selected_date, self.events[selected_date])  # Открываем окно событий
        else:
            messagebox.showinfo("Events", "No events on this date")  # Уведомляем об отсутствии событий

# Окно добавления нового события
class AddEventWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)  # Инициализация всплывающего окна
        self.title("Add event")  # Заголовок окна
        self.geometry("300x300")  # Размер окна
        
        # Поля для ввода информации о событии
        self.name_label = tk.Label(self, text="Event name")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)
        
        self.start_date_label = tk.Label(self, text="Date of start")
        self.start_date_label.pack(pady=5)
        self.start_date_entry = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.start_date_entry.pack(pady=5)
        
        self.end_date_label = tk.Label(self, text="Day of end")
        self.end_date_label.pack(pady=5)
        self.end_date_entry = DateEntry(self, date_pattern="yyyy-mm-dd")
        self.end_date_entry.pack(pady=5)
        
        self.desc_label = tk.Label(self, text="Description")
        self.desc_label.pack(pady=5)
        self.desc_entry = tk.Text(self, height=5)
        self.desc_entry.pack(pady=5)

        # Кнопки управления
        self.save_btn = tk.Button(self, text="Save", command=self.save_event)
        self.save_btn.pack(pady=5)
        self.cancel_btn = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_btn.pack(pady=5)
    
    # Сохранение события
    def save_event(self):
        event_name = self.name_entry.get()  # Получаем название события
        start_date = self.start_date_entry.get()  # Дата начала
        end_date = self.end_date_entry.get()  # Дата окончания
        description = self.desc_entry.get("1.0", tk.END).strip()  # Описание
        
        # Проверяем, заполнено ли название
        if not event_name:
            messagebox.showerror("Error", "Name cannot be empty.")
            return
        
        events = self.master.events  # Получаем все события
        if start_date not in events:  # Если даты нет в списке, создаем её
            events[start_date] = []
        events[start_date].append({
            "name": event_name,
            "start": start_date,
            "end": end_date,
            "description": description
        })
        save_events(events)  # Сохраняем в файл
        
        messagebox.showinfo("!", "Event added")  # Уведомление об успешном добавлении
        self.destroy()  # Закрываем окно

# Окно просмотра событий
class ViewEventsWindow(tk.Toplevel):
    def __init__(self, parent, date, events):
        super().__init__(parent)  # Инициализация всплывающего окна
        self.title(f"Events on {date}")  # Заголовок окна
        self.geometry("400x300")  # Размер окна
        
        self.events = events  # Сохраняем события
        self.date = date  # Сохраняем выбранную дату
        
        # Создание таблицы для отображения событий
        self.events_list = ttk.Treeview(self, columns=("name", "start", "end"), show="headings")
        self.events_list.heading("name", text="Name")
        self.events_list.heading("start", text="Start")
        self.events_list.heading("end", text="End")
        
        # Заполнение таблицы данными
        for event in events:
            self.events_list.insert("", "end", values=(event["name"], event["start"], event["end"]))
        
        self.events_list.pack(pady=10)
        
        # Кнопка закрытия
        self.close_btn = tk.Button(self, text="Exit", command=self.destroy)
        self.close_btn.pack(pady=10)

# Запуск приложения
if __name__ == "__main__":
    app = EventPlannerApp()  # Создание экземпляра приложения
    app.mainloop()  # Запуск главного цикла приложения
