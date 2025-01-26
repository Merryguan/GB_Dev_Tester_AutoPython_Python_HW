"""
 Семинар 14. Основы тестирования.

 Задание №1. Тестирование класса с использованием pytest.

 Условие:
 Напишите класс BankAccount,
 который управляет балансом счета.
 Он должен поддерживать следующие методы:
 - deposit(amount): добавляет указанную сумму к балансу.
 - withdraw(amount): снимает указанную сумму с баланса,
 если достаточно средств.
 - get_balance(): возвращает текущий баланс счета.
 При попытке снять больше средств, чем доступно на счете,
 должно выбрасываться исключение InsufficientFundsError.
 Напишите как минимум 5 тестов для проверки работы классов и его методов.
"""

# Решение:
import pytest


class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__("Недостаточно средств на счете.")


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError()
        self.balance -= amount

    def get_balance(self):
        return self.balance


def bank_account():
    return BankAccount(100)

def test_initial_balance(bank_account):
    assert bank_account.get_balance() == 100

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.get_balance() == 150

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 70

def test_withdraw_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFundsError):
        bank_account.withdraw(200)

def test_deposit_negative_amount(bank_account):
    with pytest.raises(ValueError):
        bank_account.deposit(-10)