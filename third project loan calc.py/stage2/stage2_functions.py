from math import ceil

def main_menu():
    principal = int(input("Enter the loan principal: "))
    what_to_calculate = input("What do you want to calculate?\ntype 'm' for number of monthly payments,\ntype 'p' for the monthly payment: ")
    choice_dict[what_to_calculate](principal)




def monthly_payment(principal):
    monthly_payment = int(input("Enter the monthly payment: "))
    num_of_payments = ceil(principal/monthly_payment)
    print(f"It will take {(num_of_payments)} months to repay the loan")

def number_of_months(principal):
    number_of_months = int(input("Enter the number of months: "))
    payment = ceil(principal/number_of_months)
    last_payment = principal - (number_of_months - 1) * payment
    if last_payment != payment:
        print(f"Your monthly payment = {(payment)} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {int(payment)}")

choice_dict = { "m" : monthly_payment,
                "p" : number_of_months}

main_menu()


