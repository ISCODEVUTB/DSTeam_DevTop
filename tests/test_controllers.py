from controllers import UsersManager, ShipmentManager, PackagesManager


def test_user_controller():
    controller = UsersManager()
    user_id = controller.create_user("Test User", "test@example.com", "pass123")
    assert controller.get_user(user_id) is not None
    assert controller.authenticate("test@example.com", "pass123")


def test_shipment_controller():
    controller = ShipmentManager()
    shipment_id = controller.create_shipment("Origin", "Destination", "Standard")
    assert controller.get_shipment(shipment_id) is not None
    assert controller.update_status(shipment_id, "In Transit")


def test_package_controller():
    controller = PackagesManager()
    package_id = controller.create_package("Test Item", 1.5, "Medium")
    assert controller.get_package(package_id) is not None
    assert controller.update_package(package_id, weight=2.0)
