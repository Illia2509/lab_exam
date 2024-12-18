class User:  # Определение класса User для представления пользователя
    def __init__(self, username, role):  # Инициализация объекта с именем пользователя и ролью
        self.username = username  # Сохранение имени пользователя
        self.role = role  # Сохранение роли пользователя

    def __repr__(self):  # Определение строкового представления объекта
        return f"User(username='{self.username}', role='{self.role}')"  # Возвращение форматированной строки

# Определение декоратора для проверки роли пользователя
def requires_role(required_role):
    def decorator(func):  # Декоратор, который принимает функцию
        def wrapper(user, *args, **kwargs):  # Обертка для функции
            if user.role == required_role:  # Проверка, совпадает ли роль пользователя с требуемой
                return func(user, *args, **kwargs)  # Вызов функции, если роли совпадают
            else:
                return f"\n ! Access denied. {user.username} is not {required_role}."  # Сообщение об отказе в доступе
        return wrapper  # Возвращение обертки
    return decorator  # Возвращение декоратора

# Функция-фильтр для получения пользователей с заданной ролью
def user_filter(users, role):
    for user in users:  # Перебор списка пользователей
        if user.role == role:  # Проверка, соответствует ли роль пользователя заданной
            yield user  # Возврат пользователя, если роль совпадает

# Создание списка пользователей с разными ролями
users = [
    User("A", "admin"),  # Пользователь с ролью admin
    User("B", "editor"),  # Пользователь с ролью editor
    User("C", "editor"),  # Пользователь с ролью editor
    User("D", "viewer"),  # Пользователь с ролью viewer
    User("E", "viewer")   # Пользователь с ролью viewer
]

# Определение функции с доступом только для администраторов
@requires_role("admin")
def adminsmth(user):
    return f"\nAdmin {user.username} made something "  # Сообщение при успешном доступе

# Определение функции с доступом только для редакторов
@requires_role("editor")
def edit(user):
    return f"\n{user.username} Edited something"  # Сообщение при успешном доступе

# Проверка доступа к функции для администратора
print(adminsmth(users[0]))  # Доступ разрешен
print(adminsmth(users[2]))  # Доступ запрещен (не админ)
print(edit(users[2]))  # Доступ разрешен (редактор)
print(edit(users[4]))  # Доступ запрещен (не редактор)

# Фильтрация пользователей с ролью admin
filtered_admins = user_filter(users, "admin")
print("\nList of admins:", list(filtered_admins))  # Вывод списка администраторов

# Фильтрация пользователей с ролью editor
filtered_editors = user_filter(users, "editor")
print("List of editors:", list(filtered_editors))  # Вывод списка редакторов

# Фильтрация пользователей с ролью viewer
filtered_viewers = user_filter(users, "viewer")
print("list of viewers:", list(filtered_viewers))  # Вывод списка зрителей
