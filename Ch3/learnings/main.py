# main.py
from classes import (  # Replace 'your_module' with the actual module name
    Property, Apartment, House,
    Rental, Purchase,
    ApartmentRental, ApartmentPurchase, HousePurchase, Agent
)

def main():
    # Create instances using the mixin classes with example data
    apartment_rental = ApartmentRental(
        square_feet="600",
        beds="1",
        baths="1",
        balcony="no",
        laundry="ensuite",
        rent="1200",
        utilities="150",
        furnished="yes"
    )

    apartment_purchase = ApartmentPurchase(
        square_feet="800",
        beds="2",
        baths="1",
        balcony="yes",
        laundry="coin",
        price="250000",
        taxes="5000"
    )

    house_purchase = HousePurchase(
        square_feet="2000",
        beds="4",
        baths="3",
        num_stories="2",
        garage="detached",
        fenced="no",
        price="500000",
        taxes="15000"
    )

    # Create an agent and add properties to their list
    agent = Agent()
    agent.property_list.extend([
        apartment_rental,
        apartment_purchase,
        house_purchase
    ])

    # Display all properties
    agent.display_properties()

if __name__ == "__main__":
    main()
