class BankAccount:  # Класс банковского счета
    def __init__(self, initial_balance=0):
        # Проверяем, что начальный баланс не отрицательный
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")  # Ошибка, если баланс отрицательный
        self.balance = initial_balance  # Устанавливаем начальный баланс

    def deposit(self, amount):
        # Проверяем, что сумма депозита положительная
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")  # Ошибка, если сумма депозита <= 0
        self.balance += amount  # Увеличиваем баланс на сумму депозита

    def withdraw(self, amount):
        # Проверяем, что сумма снятия положительная
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")  # Ошибка, если сумма снятия <= 0
        
        # Проверяем, что на счету достаточно средств
        if amount > self.balance:
            raise ValueError("Insufficient funds.")  # Ошибка, если средств недостаточно
        
        self.balance -= amount  # Уменьшаем баланс на сумму снятия

    def get_balance(self):
        # Возвращаем текущий баланс
        return self.balance


# Тестовый код для проверки работы класса BankAccount

# Создание счета с начальным балансом
account = BankAccount(100)
print("Начальный баланс:", account.get_balance())  # Ожидается: 100

# Пополнение счета
account.deposit(50)
print("Баланс после депозита 50:", account.get_balance())  # Ожидается: 150

# Снятие средств
account.withdraw(30)
print("Баланс после снятия 30:", account.get_balance())  # Ожидается: 120

# Попытка снять сумму больше баланса
try:
    account.withdraw(200)
except ValueError as e:
    print("Ошибка:", e)  # Ожидается: Insufficient funds.

# Попытка внести отрицательный депозит
try:
    account.deposit(-20)
except ValueError as e:
    print("Ошибка:", e)  # Ожидается: Deposit amount must be positive.

# Попытка создать счет с отрицательным балансом
try:
    invalid_account = BankAccount(-50)
except ValueError as e:
    print("Ошибка:", e)  # Ожидается: Initial balance cannot be negative.
