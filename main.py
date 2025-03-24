import products
import store


def display_menu():
    """Displays the main menu options."""
    print("\nWelcome to Best Buy!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    """Lists all available products in the store."""
    print("\nAvailable Products:")
    for product in store_obj.get_all_products():
        print(product.show())


def show_total_quantity(store_obj):
    """Displays the total quantity of products in the store."""
    print(f"\nTotal quantity in store: {store_obj.get_total_quantity()}")


def make_order(store_obj):
    """Handles the order process by allowing the user to select and purchase products."""
    shopping_list = []
    products_list = store_obj.get_all_products()
    print("\nEnter product numbers to buy (or type 'done' to finish):")
    for i, product in enumerate(products_list, start=1):
        print(f"{i}. {product.show()}")

    while True:
        choice = input("Product number: ")
        if choice.lower() == "done":
            break

        try:
            product_index = int(choice) - 1
            if product_index < 0 or product_index >= len(products_list):
                print("Invalid choice. Try again.")
                continue
            quantity = int(input("Enter quantity: "))
            shopping_list.append((products_list[product_index], quantity))
        except ValueError:
            print("Invalid input. Try again.")

    try:
        total_price = store_obj.order(shopping_list)
        print(f"\nOrder placed successfully! Total cost: {total_price} dollars.")
    except Exception as e:
        print(f"Error: {e}")


def start(store_obj):
    """Starts the store user interface loop."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total_quantity(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)
