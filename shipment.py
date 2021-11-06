"""
Sending a shipment anywhere in the world: quoting and then shipping the package.
"""

import random
from datetime import date, timedelta

URGENCY_TIMEFRAME = 5
URGENCY_TIMEFRAME = timedelta(days=URGENCY_TIMEFRAME)

AIR_COST_PER_KG = 10
AIR_COST_PER_CUBIC_M = 20
TRUCK_COST_STANDARD = 25
TRUCK_COST_URGENT = 45
OCEAN_COST = 30


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
        weight_cost = AIR_COST_PER_KG * self.weight
        volume_cost = AIR_COST_PER_CUBIC_M * self.volume
        if weight_cost >= volume_cost:
            air_cost = weight_cost
        else:
            air_cost = volume_cost
        #self.shipping_options[2]


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
        self.cost = None

    def set_cost(self, cost):
        self.cost = cost


class TruckShipment(ShipmentMode):
    def __init__(self):
        super().__init__()


class OceanShipment(ShipmentMode):
    def __init__(self):
        super().__init__()


class AirShipment(ShipmentMode):
    def __init__(self):
        super().__init__()
