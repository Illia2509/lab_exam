import pytest  # Импортируем библиотеку pytest для тестирования
from Bank import BankAccount  # Импортируем класс BankAccount из файла Bank.py

# Тест создания счета с начальным балансом
def test_create_account_with_initial_balance():
    account = BankAccount(100)  # Создаем счет с балансом 100
    assert account.get_balance() == 100  # Проверяем, что баланс равен 100

# Тест внесения средств на счет
def test_deposit_funds_and_check_balance():
    account = BankAccount(100)  # Создаем счет с балансом 100
    account.deposit(50)  # Вносим на счет 50
    assert account.get_balance() == 150  # Проверяем, что баланс стал 150

# Тест снятия средств со счета
def test_withdraw_funds_and_check_balance():
    account = BankAccount(100)  # Создаем счет с балансом 100
    account.withdraw(50)  # Снимаем со счета 50
    assert account.get_balance() == 50  # Проверяем, что баланс стал 50

# Тест снятия суммы, превышающей баланс
def test_withdraw_more_than_balance():
    account = BankAccount(100)  # Создаем счет с балансом 100
    with pytest.raises(ValueError, match="Insufficient funds."):  # Ожидаем ошибку при снятии средств
        account.withdraw(150)  # Пытаемся снять 150, что больше доступного баланса

# Тест внесения отрицательной суммы
def test_deposit_negative_amount():
    account = BankAccount(100)  # Создаем счет с балансом 100
    with pytest.raises(ValueError, match="Deposit amount must be positive."):  # Ожидаем ошибку при отрицательном депозите
        account.deposit(-50)  # Пытаемся внести -50

# Тест снятия отрицательной суммы
def test_withdraw_negative_amount():
    account = BankAccount(100)  # Создаем счет с балансом 100
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):  # Ожидаем ошибку при отрицательном снятии
        account.withdraw(-50)  # Пытаемся снять -50

# Тест создания счета с отрицательным начальным балансом
def test_create_account_with_negative_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):  # Ожидаем ошибку при отрицательном балансе
        BankAccount(-100)  # Пытаемся создать счет с балансом -100
