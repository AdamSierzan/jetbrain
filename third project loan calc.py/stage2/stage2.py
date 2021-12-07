from math import ceil

loan_principal = int(input("Enter the loan principal: "))
what_to_calculate = input("What do you want to calculate?\ntype 'm' for number of monthly payments,\ntype 'p' for the monthly payment: ")
if what_to_calculate == 'm':
    monthly_payment = int(input("Enter the monthly payment: "))
    num_of_payments = ceil(loan_principal/monthly_payment)
    if num_of_payments == 1:
        print(f"It will take {(num_of_payments)} month to repay the loan")
    else:
        print(f"It will take {(num_of_payments)} months to repay the loan")

else:
    number_of_months = int(input("Enter the number of months: "))
    payment = ceil(loan_principal/number_of_months)
    last_payment = loan_principal - (number_of_months - 1) * payment
    if last_payment != payment:
        print(f"Your monthly payment = {(payment)} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {int(payment)}")






