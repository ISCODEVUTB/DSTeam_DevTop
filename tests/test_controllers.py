from controllers.controllers import UserController
from controllers.controllers import ShipmentController
from controllers.controllers import PackageController


def test_user_controller():
    controller = UserController()
    user_id = controller.create_user("Test User", "test@example.com", "pass123")
    assert controller.get_user(user_id) is not None
    assert controller.authenticate("test@example.com", "pass123")


def test_shipment_controller():
    controller = ShipmentController()
    shipment_id = controller.create_shipment("Origin", "Destination", "Standard")
    assert controller.get_shipment(shipment_id) is not None
    assert controller.update_status(shipment_id, "In Transit")


def test_package_controller():
    controller = PackageController()
    package_id = controller.create_package("Test Item", 1.5, "Medium")
    assert controller.get_package(package_id) is not None
    assert controller.update_package(package_id, weight=2.0)
