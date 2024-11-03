class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("Square footage: {}".format(self.square_feet))
        print("Bedrooms: {}".format(self.num_bedrooms))
        print("Bathrooms: {}".format(self.num_baths))
        print()

    @staticmethod
    def prompt_init():
        return dict(
            square_feet=input("Enter the square feet: "),
            beds=input("Enter number of bedrooms: "),
            baths=input("Enter number of baths: ")
        )


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("Laundry: %s" % self.laundry)
        print("Has balcony: %s" % self.balcony)

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? ({})".format(
                ", ".join(Apartment.valid_balconies)))
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("Garage: {}".format(self.garage))
        print("Fenced yard: {}".format(self.fenced))

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        parent_init.update({
            "fenced": fenced,
            "garage": garage
        })
        return parent_init


class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("Selling price: {}".format(self.price))
        print("Estimated taxes: {}".format(self.taxes))

    @staticmethod
    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? ")
        )


class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("Rent: {}".format(self.rent))
        print("Estimated utilities: {}".format(self.utilities))
        print("Furnished: {}".format(self.furnished))

    @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ", ("yes", "no"))
        )


class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()
