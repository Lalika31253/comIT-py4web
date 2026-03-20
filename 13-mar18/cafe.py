class Coffee:
    def __init__(self, name, description, base_price):
        # YOUR CODE HERE
        self.name = name
        self.description = description
        self.base_price = base_price

    def __str__(self):
        # Return a string like: "Latte - A creamy espresso with steamed milk - $3.50"
        # YOUR CODE HERE
        return f"{self.name} - {self.description} - ${self.base_price}"


class Order:
    def __init__(self, coffee, size):
        self.coffee = coffee
        self.size = size
        self.price = self.calculate_price()  # automatically calculate the price

    def calculate_price(self):
        # Start with the coffee's base price
        # Return the final price
        # YOUR CODE HERE
        # Add extra cost based on size
        if self.size == "Medium":
            # cal_price = self.coffee.base_price + self.size
            return self.coffee.base_price + 0.5
        elif self.size == "Large":
            return self.coffee.base_price + 1
        else:
            return self.coffee.base_price
           

    def __str__(self):
        # Return a string like: "Medium Latte - $4.00"
        # YOUR CODE HERE
       
       return f"{self.size} {self.coffee.name} - ${self.calculate_price()}"
    
class Cafe:
    def __init__(self, name, tax_rate=0.08):
        self.name = name
        self.menu = []       # empty list — we will fill it with coffees
        self.orders = []     # empty list — orders are added as the customer shops
        self.tax_rate = tax_rate

    def add_to_menu(self, coffee):
        """Add a Coffee object to the menu list."""
        # YOUR CODE HERE
        self.menu.append(coffee)
        print(f"{coffee.name} added to the menu")

      

    def display_menu(self):
        """Print the full menu with numbers so the customer can pick."""
        # Print a header with the café name
        # Loop through self.menu with enumerate() to show numbers
        # Example output:
        #   === SUNNY BEAN CAFÉ MENU ===
        #   1. Espresso       - Strong and bold shot of coffee    - $2.50
        #   2. Americano      - Espresso diluted with hot water   - $3.00
        # YOUR CODE HERE
        print(f"===={self.name}====")
        for coffee in self.menu:
            print(f"{coffee.name}     - {coffee.description}  - ${coffee.base_price}")

    def display_sizes(self):
        """Print the available sizes."""
        # Show the three sizes and their extra costs
        # YOUR CODE HERE
        print(f"{Order.size} + {}")

    def add_order(self, coffee, size):
        """Create a new Order and add it to the orders list."""
        new_order = Order(coffee, size)
        self.orders.append(new_order)
        print(f"\n✅ Added: {new_order}")

    def calculate_subtotal(self):
        """Add up the price of every order and return the total."""
        # Loop through self.orders and sum all the prices
        # YOUR CODE HERE
        total = 0
        for order in self.orders:
            total += order.price
            return total

      

    def print_bill(self, tip_percent):
        """Print a formatted receipt with subtotal, tax, tip, and grand total."""
        subtotal = self.calculate_subtotal()
        tax = subtotal * self.tax_rate
        tip = subtotal * (tip_percent / 100)
        total = subtotal + tax + tip

        # Print a formatted receipt
        # Example output:
        # ==========================================
        #        SUNNY BEAN CAFÉ — YOUR BILL
        # ==========================================
        #  Medium Latte                      $4.00
        #  Large Cappuccino                  $5.50
        # ------------------------------------------
        #  Subtotal:                         $9.50
        #  Tax (8%):                         $0.76
        #  Tip (15%):                        $1.43
        # ==========================================
        #  TOTAL:                           $11.69
        # ==========================================
        #
        # YOUR CODE HERE
        pass
