def display_border(text):
    border = '*' * (len(text) + 4)
    print(border)
    print('* {text} *')
    print(border)

def main():
    # Task 1: Personal information
    display_border("Your Information")
    print("Last Name: John")
    print("First Name: Doe")
    print("Student ID: 3435536")

    # Task 2: Prompt user to enter number of orders
    while True:
        try:
            num_interior = int(input("Enter the number of interior mural orders (0-30): "))
            if 0 <= num_interior <= 30:
                break
            else:
                print("Please enter a number between 0 and 30.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            num_exterior = int(input("Enter the number of exterior mural orders (0-30): "))
            if 0 <= num_exterior <= 30:
                break
            else:
                print("Please enter a number between 0 and 30.")
        except ValueError:
            print("Please enter a valid number.")

    # Task 3: Calculate and display total revenue
    interior_price = 500.00
    exterior_price = 750.00
    total_interior_revenue = num_interior * interior_price
    total_exterior_revenue = num_exterior * exterior_price
    total_revenue = total_interior_revenue + total_exterior_revenue

    print("Number of Interior Murals Ordered: {num_interior}")
    print("Number of Exterior Murals Ordered: {num_exterior}")
    print("Expected Revenue for Interior Murals: ${total_interior_revenue}")
    print("Expected Revenue for Exterior Murals: ${total_exterior_revenue}")
    print("Total Revenue: ${total_revenue}")

    # Task 4: Display statement based on specified condition
    if num_exterior > num_interior:
        print("Exterior murals are becoming more attractive!")
    elif num_exterior < num_interior:
        print("Interior murals are becoming popular!")
    else:
        print("Both types are equally preferred!")

    # Task 5: Input information for interior mural orders
    interior_mural_orders = []
    mural_codes = ['L', 'S', 'A', 'O']

    for i in range(num_interior):
        while True:
            customer_name = input("Enter customer name for interior mural order {i + 1}: ")
            mural_code = input("Enter mural code (L for Landscape, S for Seascape, A for Abstract, O for Others) for order {i + 1}: ").upper()

            if mural_code in mural_codes:
                interior_mural_orders.append((customer_name, mural_code))
                break
            else:
                print("Invalid code. Please enter a valid code.")

    # Display count of customers ordering each type of interior mural
    counts = {code: 0 for code in mural_codes}
    for _, code in interior_mural_orders:
        counts[code] += 1

    for code, count in counts.items():
        print("Number of customers ordering {code} mural: {count}")

    # Task 5: Continuously prompt for mural code until sentinel value
    while True:
        mural_code = input("Enter a mural code (or 'Q' to quit): ").upper()
        if mural_code == 'Q':
            break

        if mural_code in mural_codes:
            customers = [name for name, code in interior_mural_orders if code == mural_code]
            if customers:
                print(f"Customers ordering {mural_code} mural: {', '.join(customers)}")
            else:
                print(f"No customers ordered {mural_code} mural.")
        else:
            print("Invalid code. Please enter a valid code.")

if __name__ == "__main__":
    main()
