class Coffee:
    def __init__(self, name, description, base_price):
        self.name = name
        self.description = description
        self.base_price = base_price

    def __str__(self):
        # Return a string like: "Latte - A creamy espresso with steamed milk - $3.50"
        return f"{self.name} - {self.description} - ${self.base_price}"


class Order:
    def __init__(self, coffee, size):
        self.coffee = coffee
        self.size = size
        self.price = self.calculate_price()  # automatically calculate the price

    def calculate_price(self):
        # Start with the coffee's base price
        # Return the final price
        # Add extra cost based on size
        if self.size == "Medium":
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
        self.menu = []       
        self.orders = []     
        self.tax_rate = tax_rate

    def add_to_menu(self, coffee):
        """Add a Coffee object to the menu list."""
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
        print(f"===={self.name}====")
        for i, coffee in enumerate(self.menu):
            print(f"{i}.{coffee.name:<15}     - {coffee.description: <35}  - ${coffee.base_price:.2f}")

    def display_sizes(self):
        """Print the available sizes."""
        # Show the three sizes and their extra costs
        print("Sizes available:")
        print("  Small  - no extra cost")
        print("  Medium - +$0.50")
        print("  Large  - +$1.00")

    def add_order(self, coffee, size):
        """Create a new Order and add it to the orders list."""
        new_order = Order(coffee, size)
        self.orders.append(new_order)
        print(f"\n✅ Added: {new_order}")

    def calculate_subtotal(self):
        """Add up the price of every order and return the total."""
        # Loop through self.orders and sum all the prices
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

        print("=" * 42)
        print(f"       {self.name} — YOUR BILL")
        print("=" * 42)
        for order in self.orders:
            print(f"  {order.size} {order.coffee.name:<25} ${order.price:.2f}")
        print("-" * 42)
        print(f"  Subtotal:                       ${subtotal:.2f}")
        print(f"  Tax ({self.tax_rate*100:.0f}%):                       ${tax:.2f}")
        print(f"  Tip ({tip_percent}%):                      ${tip:.2f}")
        print("=" * 42)
        print(f"  TOTAL:                          ${total:.2f}")
        print("=" * 42)

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
 # Create cafe   
SIZES = ["Small", "Medium", "Large"]

cafe = Cafe("Time for Break Café")

# Add coffees to menu
cafe.add_to_menu(Coffee("Espresso", "Strong and bold shot of coffee", 2.50))
cafe.add_to_menu(Coffee("Latte", "A creamy espresso with steamed milk", 3.50))
cafe.add_to_menu(Coffee("Cappuccino", "Espresso with steamed milk foam", 3.75))
cafe.add_to_menu(Coffee("Americano", "Espresso diluted with hot water", 3.00))

print(f"\nWelcome to {cafe.name}! ☕")

while True:
    print("\n" + "="*40)
    print("What would you like to do?")
    print("1. View menu and order a drink")
    print("2. View current order")
    print("3. Checkout and pay")
    print("="*40)

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        # Show menu
        cafe.display_menu()

        # Ask the customer to pick a drink (validate input!)
        drink_input = input("\nEnter the number of the drink you want (or 0 to cancel): ").strip()

        if drink_input == "0":
            continue   # go back to the top of the while loop

        # Check that the input is a valid number
        if not drink_input.isdigit():
            print("❌ Please enter a number.")
            continue

        drink_index = int(drink_input) - 1   # subtract 1 because lists start at 0

        if drink_index < 0 or drink_index >= len(cafe.menu):
            print("❌ That number is not on the menu. Try again.")
            continue

        selected_coffee = cafe.menu[drink_index]

        # Show sizes
        cafe.display_sizes()
        size_input = input("Enter the number of the size you want: ").strip()

        if not size_input.isdigit():
            print("❌ Please enter a number.")
            continue

        size_index = int(size_input) - 1

        if size_index < 0 or size_index >= len(SIZES):
            print("❌ Invalid size. Try again.")
            continue

        selected_size = SIZES[size_index]

        # Add the order
        cafe.add_order(selected_coffee, selected_size)

    elif choice == "2":
        if not cafe.orders:
            print("\n🛒 Your order is empty.")
        else:
            print("\n--- Your Current Order ---")
            for i, order in enumerate(cafe.orders, start=1):
                print(f"  {i}. {order}")
            print(f"  Subtotal so far: ${cafe.calculate_subtotal():.2f}")

    elif choice == "3":
        if not cafe.orders:
            print("\n❌ You have not ordered anything yet!")
            continue

        # Ask for tip percentage
        print("\nHow much would you like to tip?")
        print("1. 10%    2. 15%    3. 20%    4. No tip")
        tip_choice = input("Enter your choice (1/2/3/4): ").strip()

        tip_map = {"1": 10, "2": 15, "3": 20, "4": 0}
        tip_percent = tip_map.get(tip_choice, 0)

        cafe.print_bill(tip_percent)
        print("\nThank you for visiting! Have a great day! ☕\n")
        break   # Exit the while loop — we are done!

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")

