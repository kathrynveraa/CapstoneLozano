#problem 4
#capstone

class Product:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        """Update the quantity of the product in stock."""
        self.quantity = new_quantity
    
    def display(self):
        """Display product details."""
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.product_description}")
        print(f"Price per unit: ₱{self.price:.2f}")
        print(f"Stock quantity: {self.quantity}")
        print()

    def total_value(self):
        """Calculate the total value of the product in stock."""
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product_id, name, product_description, price, quantity):
        """Add a new product to the inventory."""
        new_product = Product(product_id, name, product_description, price, quantity)
        self.products.append(new_product)
        print(f"Product '{name}' added to inventory.\n")
    
    def update_product_quantity(self, product_id, new_quantity):
        """Update the stock quantity of a product."""
        for product in self.products:
            if product.product_id == product_id:
                product.update_quantity(new_quantity)
                print(f"Updated stock quantity for product ID {product_id}.\n")
                return
        print(f"Product with ID {product_id} not found.\n")
    
    def display_all_products(self):
        """Display details of all products in inventory."""
        if not self.products:
            print("No products in inventory.\n")
            return
        for product in self.products:
            product.display()
    
    def total_inventory_value(self):
        """Calculate the total value of all products in inventory."""
        total_value = sum(product.total_value() for product in self.products)
        print(f"Total value of inventory: ₱{total_value:.2f}\n")


def main():
    inventory = Inventory()
    
    while True:
        print("Inventory Management System")
        print("1. Add a Product")
        print("2. Update Product Stock")
        print("3. Display All Products")
        print("4. Calculate Total Inventory Value")
        print("5. Exit program")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            product_description = input("Enter product description: ")
            price = float(input("Enter price per unit: "))
            quantity = int(input("Enter stock quantity: "))
            inventory.add_product(product_id, name, product_description, price, quantity)
        
        elif choice == '2':
            product_id = input("Enter product ID to update stock: ")
            new_quantity = int(input("Enter new stock quantity: "))
            inventory.update_product_quantity(product_id, new_quantity)
        
        elif choice == '3':
            inventory.display_all_products()
        
        elif choice == '4':
            inventory.total_inventory_value()
        
        elif choice == '5':
            print("Exiting the system.")
            print('have a nice day!')
            break
    
        else:
            print("Invalid option. Please try again by choosing 1-5.")

if __name__ == "__main__":
    main()
