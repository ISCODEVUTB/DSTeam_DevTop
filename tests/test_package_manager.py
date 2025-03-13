import pytest
import pandas as pd
from controllers.PackagesManager import PackageManager


@pytest.fixture
def package_manager():
    return PackageManager()


def test_add_package(package_manager):
    package_manager.add_package(
        description="Test Package",
        sizes="10x10x10",
        weight=1.5,
        type="Normal"
    )
    # Verificar que el registro se guardó en el CSV
    df = pd.read_csv("./data/Packages.csv")
    assert not df.empty
    assert df.iloc[-1]["Description"] == "Test Package"


def test_update_package(package_manager):
    # Asumiendo que existe un paquete en el CSV
    package_manager.update_package("P001", description="Updated Package")
    df = pd.read_csv("./data/Packages.csv")
    package = df[df["ID"] == "P001"]
    assert not package.empty
    assert package.iloc[0]["Description"] == "Updated Package"


def test_delete_package(package_manager):
    # Asumiendo que existe un paquete en el CSV
    package_manager.delete_package("P001")
    df = pd.read_csv("./data/Packages.csv")
    package = df[df["ID"] == "P001"]
    assert package.empty


def test_search_package(package_manager):
    result = package_manager.search_package({"ID": "P001"})
    assert isinstance(result, pd.DataFrame)
