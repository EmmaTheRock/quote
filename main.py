"""
provides quotes related to shipping

TODO:
* commit this (single class hierarchy)
* rework this as a single class with state patterns for the inherited variables
* some variables naturally fit into shipment and some do not. might need another class other than shipment
* for the state classes, might want to use VALUE OBJECTS (multiple shipments can access and use the same quote object
(same quote for same day, for example))
"""

import random
from datetime import datetime, timedelta


URGENCY_TIMEFRAME = 5
URGENCY_TIMEFRAME = timedelta(days=URGENCY_TIMEFRAME)

AIR_COST_PER_KG = 10
AIR_COST_PER_CUBIC_M = 20
TRUCK_COST_STANDARD = 25
TRUCK_COST_URGENT = 45
OCEAN_COST = 30


class Quote:
    def __init__(self, customer_info):
        try:
            if customer_info["weight"] >= 10 and customer_info["volume"] >= 125:
                raise ValueError()
        except ValueError:
            print("Packages can only be shipped if they weigh less than 10Kg "
                  "or are smaller than 5x5x5 meters (125 cubic meters).")
        else:
            self.id = random.randint(1, 100)
            self.cost = None
            self.customer_info = customer_info

    def print_quote(self):
        pass

    def save_to_file(self):
        pass


class AirQuote(Quote):
    def __init__(self, customer_info):
        self.valid_air_quote = True
        try:
            if customer_info["is_dangerous"] is True:
                self.valid_air_quote = False
                raise ValueError()
        except ValueError:
            print("Dangerous package cannot be sent via air. Quote for air shipping option failed.")
        else:
            super().__init__(customer_info)
            self.cost = None
            self.is_dangerous = customer_info["is_dangerous"]
            self.calculate_air_cost()

    def calculate_air_cost(self):
        weight = self.customer_info["weight"]
        weight_cost = AIR_COST_PER_KG * weight
        volume = self.customer_info["volume"]
        volume_cost = AIR_COST_PER_CUBIC_M * volume
        if weight_cost >= volume_cost:
            self.cost = weight_cost
        else:
            self.cost = volume_cost


class TruckQuote(Quote):
    def __init__(self, customer_info):
        super().__init__(customer_info)
        self.delivery_date = None
        self.is_urgent = None
        self.format_delivery_date()
        self.determine_urgency()
        self.determine_cost()

    def format_delivery_date(self):
        delivery_date = self.customer_info["delivery_date"]
        formatted_date = datetime.strptime(delivery_date, '%m/%d/%y')
        self.delivery_date = formatted_date

    def determine_urgency(self):
        now = datetime.now()
        timeframe = self.delivery_date - now
        if timeframe <= URGENCY_TIMEFRAME:
            self.is_urgent = True
        else:
            self.is_urgent = False

    def determine_cost(self):
        if self.is_urgent is True:
            self.cost = TRUCK_COST_URGENT
        else:
            self.cost = TRUCK_COST_STANDARD


class OceanQuote(Quote):
    def __init__(self, customer_info):
        super().__init__(customer_info)
        self.cost = 30


def main():
    customer_info = {
        "name": "john",
        "package_description": "book",
        "is_dangerous": True,
        "weight": 50,
        "volume": 40,
        "delivery_date": "10/24/21",
        "is_international": True
    }

    print("AIR QUOTE TEST")
    quote1 = AirQuote(customer_info)
    if quote1.valid_air_quote:
        print(f"air quote: ${quote1.cost}\n\n")

    print("TRUCK QUOTE TEST")
    quote2 = TruckQuote(customer_info)
    print(f"truck quote: ${quote2.cost}\n\n")

    print("OCEAN QUOTE TEST")
    quote3 = OceanQuote(customer_info)
    print(f"ocean quote: ${quote3.cost}\n\n")


if __name__ == '__main__':
    main()
