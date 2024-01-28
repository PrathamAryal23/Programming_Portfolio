def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    pizza_price = 12
    delivery_cost = 2.5
    discount_tuesday = 0.5
    discount_app = 0.25

    if is_tuesday:
        pizza_price *= (1 - discount_tuesday)

    total_price = num_pizzas * pizza_price

    if delivery_required and num_pizzas < 5:
        total_price += delivery_cost

    if used_app:
        total_price *= (1 - discount_app)

    return round(total_price, 2)

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas = get_positive_integer_input("How many pizzas ordered? ")
    delivery_required = get_yes_no_input("Is delivery required? (Y/N) ")
    is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ")
    used_app = get_yes_no_input("Did the customer use the app? (Y/N) ")

    total_price = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()