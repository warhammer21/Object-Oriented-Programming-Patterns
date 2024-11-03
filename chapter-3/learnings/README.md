
![property_management_uml](https://github.com/user-attachments/assets/3f59fed4-1c54-4e32-8b52-3a88d042405d)
# Housing Property Design Pattern

## Overview

This document outlines the design pattern used for a housing property system implemented in Python. The system utilizes Object-Oriented Programming (OOP) principles such as encapsulation, inheritance, and polymorphism. It defines various types of properties (e.g., Apartments and Houses) along with their respective purchase and rental details.

## Class Structure

### 1. `Property` (Abstract Class)

- **Purpose**: Base class for all property types.
- **Attributes**:
  - `square_feet`: Size of the property.
  - `num_bedrooms`: Number of bedrooms.
  - `num_baths`: Number of bathrooms.
- **Methods**:
  - `display()`: Prints property details.
  - `prompt_init()`: Prompts user input for property details.

### 2. `Apartment` (Inherits from `Property`)

- **Purpose**: Represents an apartment property.
- **Attributes**:
  - `balcony`: Indicates if there is a balcony.
  - `laundry`: Specifies laundry facilities.
- **Methods**:
  - `display()`: Overrides `Property.display()` to include apartment-specific details.
  - `prompt_init()`: Collects additional input for apartment-specific attributes.

### 3. `House` (Inherits from `Property`)

- **Purpose**: Represents a house property.
- **Attributes**:
  - `num_stories`: Number of stories in the house.
  - `garage`: Type of garage (attached, detached, none).
  - `fenced`: Indicates if the yard is fenced.
- **Methods**:
  - `display()`: Overrides `Property.display()` to include house-specific details.
  - `prompt_init()`: Collects additional input for house-specific attributes.

### 4. `Purchase` (Composition)

- **Purpose**: Represents the purchase details of a property.
- **Attributes**:
  - `price`: Selling price of the property.
  - `taxes`: Estimated taxes on the purchase.
- **Methods**:
  - `display()`: Displays purchase details.
  - `prompt_init()`: Collects purchase-related information.

### 5. `Rental` (Composition)

- **Purpose**: Represents the rental details of a property.
- **Attributes**:
  - `furnished`: Indicates if the property is furnished.
  - `rent`: Monthly rent amount.
  - `utilities`: Estimated utility costs.
- **Methods**:
  - `display()`: Displays rental details.
  - `prompt_init()`: Collects rental-related information.

### 6. `ApartmentRental` (Inherits from `Rental` and `Apartment`)

- **Purpose**: Combines rental details with apartment attributes.
- **Method**:
  - `prompt_init()`: Collects input for both rental and apartment attributes.

### 7. `ApartmentPurchase` (Inherits from `Purchase` and `Apartment`)

- **Purpose**: Combines purchase details with apartment attributes.
- **Method**:
  - `prompt_init()`: Collects input for both purchase and apartment attributes.

### 8. `HousePurchase` (Inherits from `Purchase` and `House`)

- **Purpose**: Combines purchase details with house attributes.
- **Method**:
  - `prompt_init()`: Collects input for both purchase and house attributes.

### 9. `Agent`

- **Purpose**: Represents a real estate agent managing a list of properties.
- **Attributes**:
  - `property_list`: A list to store properties.
- **Methods**:
  - `display_properties()`: Displays all properties in the agent's list.

## Example Usage

To utilize the classes, you can run the following code snippet in the main file:

```python
def main():
    # Create instances of properties
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
    
    # Create an agent and add properties
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
