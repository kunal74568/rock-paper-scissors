
def generate_receipt():
    print("Payment Receipt Generator\n")
    
    # Customer details
    customer_name = input("Enter customer name: ")
    
    # Item details
    items = []
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_price = float(input(f"Enter price for {item_name}: "))
        items.append((item_name, item_price))
    
    # Calculate total amount
    total_amount = sum(item[1] for item in items)
    print("\nTotal Amount:", total_amount)
    
    # Payment details
    amount_paid = float(input("Enter amount paid: "))
    change = amount_paid - total_amount
    
    # Generate receipt
    print("\n" + "="*30)
    print("          PAYMENT RECEIPT")
    print("="*30)
    print(f"Customer Name: {customer_name}")
    print("\nItems Purchased:")
    for item in items:
        print(f" - {item[0]}: ₹{item[1]:.2f}")
    print("\nTotal Amount: ₹{:.2f}".format(total_amount))
    print("Amount Paid: ₹{:.2f}".format(amount_paid))
    print("Change Due: ₹{:.2f}".format(change))
    print("="*30)
    print("Thank you for your purchase!")
    print("="*30)

# Run the function
generate_receipt()