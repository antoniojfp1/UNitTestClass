import pytest
import bank

user = bank.User(1, "Fernandez", 1000000)

def test_ok_debit():
    assert user.debit(1000) == 1001000

def test_missing_debit():
    assert user.debit(1000) == 1003000

def test_ok_credit():
    assert user.credit(1000) == 99000

def test_missing_credit():
    assert user.credit(1500000) == 0