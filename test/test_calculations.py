import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount,InsufficientFunds

@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1,num2,result",[(3,2,5),(7,1,8),(12,4,16)])
def test_add(num1,num2,result):
    print("testing add function")
    # assert 
    # sum  = add(5,3)
    # # sum == 8
    # assert sum == 8
    assert add(num1,num2) == result


def test_subtract():
    assert subtract(8,3) == 5
 

def test_multiply():
    assert multiply(4,3) == 12
 

def test_divide():
    assert divide(8,2) == 4
 
def test_bank_set_initial_amount(bank_account):
    # bank_account = BankAccount(50)
    # assert bank_account.balance == 50
    assert bank_account.balance == 50


def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    # assert bank_account.balance == 0
    print("testing my bank account")
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    # bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):
    # bank_account = BankAccount(50)
    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55


@pytest.mark.parametrize("deposited,withdraw,result",[(200,100,100),(50,10,40),(1200,200,1000)])

def test_bank_transaction(zero_bank_account,deposited,withdraw,result):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)

    assert zero_bank_account.balance == result


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
       bank_account.withdraw(200)

# test_add()