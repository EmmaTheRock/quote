"""
Sending a shipment anywhere in the world: quoting, then booking, then shipping the package.
"""

import random
from datetime import date, datetime, timedelta

URGENCY_TIMEFRAME = 5
URGENCY_TIMEFRAME = timedelta(days=URGENCY_TIMEFRAME)

AIR_COST_PER_KG = 10
AIR_COST_PER_CUBIC_M = 20
TRUCK_COST_STANDARD = 25
TRUCK_COST_URGENT = 45
OCEAN_COST = 30


class ShipmentProcess:
    def __init__(self, customer_info):
        try:
            if customer_info["weight"] >= 10 and customer_info["volume"] >= 125:
                raise ValueError()
        except ValueError:
            print("Packages can only be shipped if they weigh less than 10 kg"
                  "or are smaller than 5x5x5 meters (125 cubic meters).")
        else:
            shipment = Shipment(customer_info)
            shipment.determine_urgency()
            shipment.determine_shipment_options()
            shipment.calculate_cost()
            shipment.display_info()


class Shipment:
    def __init__(self, customer_info):
        self.shipment_number = random.randint(1, 100)
        self.customer_name = customer_info["name"]
        self.package_description = customer_info["package_description"]
        self.is_dangerous = customer_info["is_dangerous"]
        self.weight = customer_info["weight"]
        self.volume = customer_info["volume"]
        self.delivery_date = customer_info["delivery_date"]
        self.is_urgent = None
        self.is_international = customer_info["is_international"]
        self.shipment_status = Quote()
        self.shipping_options = []
        self.shipment_mode = None

    def display_info(self):
        print("YOUR SHIPMENT\n===============")
        print("Shipment number: ", self.shipment_number)
        print("Customer name: ", self.customer_name)
        print("Package description: ", self.package_description)
        print("Dangerous: ", self.is_dangerous)
        print("Weight: ", self.weight)
        print("Volume: ", self.volume)
        print("Delivery date: ", self.delivery_date)
        print("Urgent: ", self.is_urgent)
        print("International: ", self.is_international)
        print("Shipment status: ", self.get_status())
        print("Shipment options: ", [i.cost for i in self.shipping_options])
        print("Shipment mode: ", self.shipment_mode)
        print()

    def get_status(self):
        return self.shipment_status.get_status()

    def determine_shipment_options(self):
        self.shipping_options.append(TruckShipment())
        self.shipping_options.append(OceanShipment())
        if not self.is_dangerous:
            self.shipping_options.append(AirShipment())
        else:
            self.shipping_options.append(None)

    def calculate_cost(self):
        # truck cost
        if self.is_urgent is True:
            truck_cost = TRUCK_COST_URGENT
        else:
            truck_cost = TRUCK_COST_STANDARD
        self.shipping_options[0].set_cost(truck_cost)

        # ocean cost
        self.shipping_options[1].set_cost(OCEAN_COST)

        # air cost
        if self.shipping_options[2] is not None:
            weight_cost = AIR_COST_PER_KG * self.weight
            volume_cost = AIR_COST_PER_CUBIC_M * self.volume
            if weight_cost >= volume_cost:
                air_cost = weight_cost
            else:
                air_cost = volume_cost
            self.shipping_options[2].set_cost(air_cost)

    def determine_urgency(self):
        formatted_date = datetime.strptime(self.delivery_date, '%m/%d/%y')
        now = datetime.now()
        timeframe = formatted_date - now
        if timeframe <= URGENCY_TIMEFRAME:
            self.is_urgent = True
        else:
            self.is_urgent = False


class ShipmentStatus:
    def __init__(self):
        self.status_date = date.today()
        self.status = None

    def get_status(self):
        return self.status


class Quote(ShipmentStatus):
    def __init__(self):
        super().__init__()
        self.status = "quote"


class Booking(ShipmentStatus):
    def __init__(self):
        super().__init__()
        self.status = "booking"


class Shipping(ShipmentStatus):
    def __init__(self):
        super().__init__()
        self.status = "shipping"


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


def main():
    # valid case
    customer_info = {
        "name": "john",
        "package_description": "book",
        "is_dangerous": False,
        "weight": 50,
        "volume": 40,
        "delivery_date": "10/24/21",
        "is_international": True
    }
    shipment = ShipmentProcess(customer_info)
    shipment.determine_urgency()
    shipment.determine_shipment_options()
    shipment.calculate_cost()
    shipment.display_info()

    # invalid case
    customer_info = {
        "name": "mariana",
        "package_description": "heavy machine",
        "is_dangerous": False,
        "weight": 50,
        "volume": 130,
        "delivery_date": "10/24/21",
        "is_international": True
    }
    shipment = Shipment(customer_info)
    shipment.determine_urgency()
    shipment.determine_shipment_options()
    shipment.calculate_cost()
    shipment.display_info()


if __name__ == '__main__':
    main()
