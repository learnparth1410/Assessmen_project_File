from fruit_manager import FruitManager

class Customer:
    @staticmethod
    def display_menu():
        print("\nFruit Store Console Application")
        print("1. Add fruit to cart")
        print("2. View cart")
        print("3. Checkout")
        print("4. Exit")

    @staticmethod
    def run():
        try:
            while True:
                Customer.display_menu()
                choice = input("Enter your choice (1-4): ")

                if choice == '1':
                    fruit = input("Enter the fruit name: ").lower()
                    quantity = int(input("Enter the quantity: "))
                    FruitManager.add_fruit_stock(fruit, quantity)
                elif choice == '2':
                    FruitManager.view_fruit_stock()
                elif choice == '3':
                    # Additional customer logic for checkout can be added here
                    pass
                elif choice == '4':
                    print("Exiting the Fruit Store Console. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    Customer.run()
