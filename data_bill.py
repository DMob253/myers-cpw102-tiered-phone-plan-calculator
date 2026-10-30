'''
Phone Data Bill Calculator
Asks for data used, base plan cost and premium membership status then shows the usage category
and the total monthly bill.
'''
# CONSTANTS
DATA_LIMIT = 10      # GB LIMIT OF BASE PLAN
MODERATE_LIMIT = 5   # GB OVER LIMIT THAT COUNTS AS MODERATE

# RETURNS TRUE IF DATA USED IS OVER GB LIMIT, FALSE OTHERWISE
def is_over_limit(gb_used):
    return gb_used > DATA_LIMIT

# RETURNS RATE BASED ON IF USER HAS PREMIUM PLAN OR NOT
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
    # INPUTS: USER ENTERS DATA USAGE, BASE COST AND MEMBERSHIP STATUS
    gb_used = float(input("How much data did you use (GB)?: "))
    base_cost = float(input("What is your base cost?: "))

    premium_answer = input("Do you have a premium membership?: (yes or no) ").lower()

    has_premium = premium_answer == "yes"

    # STARTS THE BILL AT THE BASE PLAN COST
    total_cost = base_cost
    gb_over = 0
    overage_cost = 0

    # USES BOOLEAN FUNCTION
    if is_over_limit(gb_used):

        # FIGURES OUT HOW MANY GB THE CUSTOMER WENT OVER
        gb_over = gb_used - DATA_LIMIT
        print(f"You are {gb_over:.1f} GB over your limit.")

        # NESTED IF: UP TO 5 GB OVER IS MODERATE; MORE THAN 5 IS HIGH
        if gb_over <= MODERATE_LIMIT:
            print("Moderate extra usage.")
        else:
            print("High extra usage.")

        # OVERAGE RATE CALCULATION
        overage_rate = get_overage_rate(gb_used, has_premium)
        overage_cost = gb_over * overage_rate

        # ADDS OVERAGE COST TO BASE PLAN
        total_cost = base_cost + overage_cost

        # PREMIUM MEMBERSHIP RECOMMENDATION
        if not has_premium:
            print("You should really upgrade to a premium membership.")

    # CUSTOMER STAYED WITHIN LIMIT, BILL IS JUST BASE COST
    else:
        print("You are within your data limit.")
        overage_rate = 0

    # BILLING DETAILS
    print(f"GB over limit: {gb_over:.1f}")
    print(f"Overage rate: ${overage_rate:.2f} per GB")
    print(f"Overage cost: ${overage_cost:.2f}")

    # SHOWS TOTAL BILL
    print(f"Your total bill is: ${total_cost:.2f}")

main()