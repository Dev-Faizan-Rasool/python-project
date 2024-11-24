class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price, quantity=1):
        if item in self.cart:
            self.cart[item]['quantity'] += quantity
        else:
            self.cart[item] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} of {item} to the cart.")

    def remove_item(self, item, quantity=1):
        if item in self.cart:
            if self.cart[item]['quantity'] > quantity:
                self.cart[item]['quantity'] -= quantity
                print(f"Removed {quantity} of {item} from the cart.")
            elif self.cart[item]['quantity'] == quantity:
                del self.cart[item]
                print(f"Removed {item} from the cart.")
            else:
                print(f"Cannot remove {quantity} of {item}; only {self.cart[item]['quantity']} in the cart.")
        else:
            print(f"{item} not found in the cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Your cart:")
        total = 0
        for item, details in self.cart.items():
            item_total = details['price'] * details['quantity']
            total += item_total
            print(f"{item}: ${details['price']} x {details['quantity']} = ${item_total}")
        print(f"Total: ${total:.2f}")

def main():
    cart = ShoppingCart()
    
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))
            cart.add_item(item, price, quantity)
        
        elif choice == '2':
            item = input("Enter item name to remove: ")
            quantity = int(input("Enter quantity to remove: "))
            cart.remove_item(item, quantity)
        
        elif choice == '3':
            cart.view_cart()
        
        elif choice == '4':
            print("Exiting the shopping cart system.")
            break
        
        else:
            print("Invalid option. Please try .")

if __name__ == "__main__":
    main()
