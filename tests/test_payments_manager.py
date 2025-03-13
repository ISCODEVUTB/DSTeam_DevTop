import pytest
import pandas as pd
from controllers.PaymentsManager import PaymentsManager


@pytest.fixture
def payments_manager():
    return PaymentsManager()


def test_add_payment(payments_manager):
    payment = {
        "payment_id": "PAY001",
        "amount": 100.0
    }
    payments_manager.AddPayment(payment)
    df = pd.read_csv("./data/Payments.csv")
    assert not df.empty
    assert abs(df.iloc[-1]["amount"] - 100.0) < 1e-9


def test_show_payments(payments_manager):
    # Solo verifica que el método existe y puede ser llamado
    payments_manager.ShowPayments()
    # La verificación real sería ver el contenido del CSV
    df = pd.read_csv("./data/Payments.csv")
    assert isinstance(df, pd.DataFrame)
