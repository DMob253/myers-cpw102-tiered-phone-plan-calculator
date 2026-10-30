'''
Phone Data Bill Calculator
Asks for data used and base plan cost, then shows the usage category
and the total monthly bill.
'''

# Constants
DATA_LIMIT = 10      # GB of data included in the base plan

MODERATE_LIMIT = 5   # most GB over the limit that still counts as moderate

# Returns True if the data used is over the 10 GB limit, False otherwise
def is_over_limit(gb_used):
    return gb_used > DATA_LIMIT

# Returns rate based on if user has premium plan or not
def get_overage_rate(gb_used, has_premium):

    if gb_used <= DATA_LIMIT:
        return 0

    elif gb_used <= 20:

        if has_premium:
            return 1
        else:
            return 2

    else:

        if has_premium:
            return 2
        else:
            return 3

def main():
    # Inputs: User enters data usage, base cost, and membership status
    gb_used = float(input("How much data did you use (GB)?: "))
    base_cost = float(input("What is your base cost?: "))


    premium_answer = input("Do you have a premium membership?: (yes or no) ").lower()

    has_premium = premium_answer == "yes"

    # Starts the bill at the base plan cost
    total_cost = base_cost
    gb_over = 0
    overage_cost = 0

    # Uses the Boolean function is_over_limit to decide if overage processing is needed
    if is_over_limit(gb_used):

        # Figures out how many GB the customer went over the limit
        gb_over = gb_used - DATA_LIMIT
        print(f"You are {gb_over:.1f} GB over your limit.")

        # Nested if: up to 5 GB over is moderate, more than 5 is high
        if gb_over <= MODERATE_LIMIT:
            print("Moderate extra usage.")
        else:
            print("High extra usage.")

        # Adds $2 for each GB over the limit to base cost
        total_cost = base_cost + gb_over * 2
    else:
        # Customer stayed within the limit, bill is just base cost
        print("You are within your data limit.")

    # Shows the total bill with 2 decimal places
    print(f"Your total bill is: ${total_cost:.2f}")

main()

