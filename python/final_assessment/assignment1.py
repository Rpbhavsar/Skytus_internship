# Smart E-Commerce cart system

products = {
    1: ["laptop", 70000],
    2: ["mobile", 50000],
    3: ["tv", 30000],
    4: ["headphones", 2000],
    5: ["Accessories", 5000],
}

cart = []

while True:
    print("----Smart E-commerce cart----")
    print("1. Show products")
    print("2. Add to cart")
    print("3. View cart")
    print("4. Remove from cart")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available products:")
        for product_id, product in products.items():
            print(f"{product_id}. {product[0]} - ₹{product[1]}")

    elif choice == 2:
        product_id = int(input("Enter product ID: "))
        qty = int(input("Enter quantity: "))

        if product_id in products:
            cart.append({
                "product_id": product_id,
                "name": products[product_id][0],
                "price": products[product_id][1],
                "quantity": qty,
            })
            print(f"Added {qty} {products[product_id][0]}(s) to cart.")
        else:
            print("Invalid product ID.")

    elif choice == 3:
        if not cart:
            print("Your cart is empty.")
        else:
            print("Your cart:")
            for item in cart:
                print(f"{item['product_id']}. {item['name']} - Qty: {item['quantity']} - ₹{item['price'] * item['quantity']}")

    elif choice == 4:
        if not cart:
            print("Your cart is empty.")
        else:
            product_id = int(input("Enter product ID to remove: "))
            for item in cart:
                if item["product_id"] == product_id:
                    cart.remove(item)
                    print(f"Removed {item['name']} from cart.")
                    break
            else:
                print("Product not found in cart.")

    elif choice == 5:
        if not cart:
            print("Your cart is empty, nothing to checkout.")
        else:
            total = 0
            print("Checkout summary:")
            for item in cart:
                subtotal = item["price"] * item["quantity"]
                total += subtotal
                print(f"{item['name']} x {item['quantity']} = ₹{subtotal}")
            print(f"Total bill: ₹{total}")
            print("Thank you for shopping!")
            break

    elif choice == 6:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice, please try again.")
