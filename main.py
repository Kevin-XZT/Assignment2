"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER


def worth_it_cost_per_credit(annual_cost, credits):
    return cost_per_credit(annual_cost, credits)

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter your credits this semester: "))

    while True:
        # Show your menu here.
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS1430 class")
        print("6. What does one credit cost?")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            amount = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${amount:,.2f}")
        elif choice == "2":
            amount = cost_per_month(annual_cost)
            print(f"Cost per month: ${amount:,.2f}")
        elif choice == "3":
            amount = cost_per_day(annual_cost)
            print(f"Cost per class day: ${amount:,.2f}")
        elif choice == "4":
            amount = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${amount:,.2f}")
        elif choice == "5":
            amount = cost_per_class(annual_cost, credits)
            print(f"Cost per CS1430 class: ${amount:,.2f}")
        elif choice == "6":
            amount = worth_it_cost_per_credit(annual_cost, credits)
            print(f"One credit costs ${amount:,.2f} this semester.")
        else:
            print("Invalid choice")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
