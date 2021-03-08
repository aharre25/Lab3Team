import pytest
from Invoice_HS import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5, 'employee discount': 3, 'ceo discount': 'y'},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10, 'employee discount': 5, 'ceo discount': 'y'}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateEmployeeDiscount(invoice, products):
    invoice.employeeDiscount(products)
    assert invoice.employeeDiscount(products) == 3.00

def test_CanCalculateCeoDiscount(invoice, products):
    invoice.ceoDiscount(products)
    assert invoice.ceoDiscount(products) == 0.00

