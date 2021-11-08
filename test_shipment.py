import shipment


def test_create_shipment_valid():
    customer_info = {
        "name": "john",
        "package_description": "book",
        "is_dangerous": False,
        "weight": 50,
        "volume": 40,
        "delivery_date": "12/24/21",
        "is_international": True
    }
    my_shipment = shipment.Shipment(customer_info)

    assert my_shipment.customer_name == "john"
    assert my_shipment.package_description == "book"
    assert my_shipment.is_dangerous is False
    assert my_shipment.weight == 50
    assert my_shipment.volume == 40
    assert my_shipment.delivery_date == "12/24/21"
    assert my_shipment.is_international is True


def test_create_shipment_invalid():
    customer_info = {
        "name": "mariana",
        "package_description": "heavy machine",
        "is_dangerous": False,
        "weight": 50,
        "volume": 130,
        "delivery_date": "12/24/21",
        "is_international": True
    }
    my_shipment = shipment.Shipment(customer_info)


