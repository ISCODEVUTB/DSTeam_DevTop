import pytest
import pandas as pd
from controllers.ShipmentManager import ShipmentManager


@pytest.fixture
def shipment_manager():
    return ShipmentManager()


def test_create_shipment(shipment_manager):
    shipment_manager.create_shipment(
        user_id="U001",
        package_id="P001",
        cost=100.0,
        date="2024-01-01",
        state="En proceso"
    )
    df = pd.read_csv("./data/Shipments.csv")
    assert not df.empty
    assert df.iloc[-1]["user_id"] == "U001"


def test_update_shipment_state(shipment_manager):
    shipment_manager.update_shipment_state("S001", "Entregado")
    df = pd.read_csv("./data/Shipments.csv")
    shipment = df[df["shipment_id"] == "S001"]
    assert not shipment.empty
    assert shipment.iloc[0]["state"] == "Entregado"


def test_search_shipment(shipment_manager):
    result = shipment_manager.search_shipment({"shipment_id": "S001"})
    assert isinstance(result, pd.DataFrame)
