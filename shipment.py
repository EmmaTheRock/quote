"""
Sending a shipment anywhere in the world: quoting and then shipping the package.
"""

import random
from datetime import date


class ShipmentProcess:
    def __init__(self):
        pass


class Shipment:
    def __init__(self, customer_info):
        self.shipment_number = random.randint(1, 100)
        self.customer_name = customer_info["name"]
        self.package_description = customer_info["package_description"]
        self.is_dangerous = customer_info["is_dangerous"]
        self.weight = customer_info["weight"]
        self.volume = customer_info["volume"]
        self.delivery_date = customer_info["delivery_date"]
        self.is_international = customer_info["is_international"]
        self.shipment_status = Quote()
        self.shipping_options = []
        self.shipment_mode = None

    def determine_shipment_options(self):
        self.shipping_options.append(TruckShipment())
        self.shipping_options.append(OceanShipment())
        if not self.is_dangerous:
            self.shipping_options.append(AirShipment())
        else:
            self.shipping_options.append(None)

    def calculate_cost(self):
        pass
        #todo: put air, truck, ocean costs


class ShipmentStatus:
    def __init__(self):
        self.status_date = date.today()


class Quote(ShipmentStatus):
    def __init__(self):
        super().__init__()


class Booking(ShipmentStatus):
    def __init__(self):
        super().__init__()


class Shipping(ShipmentStatus):
    def __init__(self):
        super().__init__()


class ShipmentMode:
    def __init__(self):
        pass


class TruckShipment(ShipmentMode):
    pass


class OceanShipment(ShipmentMode):
    pass


class AirShipment(ShipmentMode):
    pass
