import math


# loan_principal = int(input("Enter the loan principal: "))
what_to_calculate = input("What do you want to calculate?\n"
                    "type 'n' for number of monthly payments,\n"
                    "type 'a' for annuity monthly payment amount,\n"
                    "type 'p' for loan principal: ")

if what_to_calculate == 'n':

    loan_principal = float(input("Enter the loan principal: "))
    monthly_payment_amount = int(input("Enter the monthly payment: "))
    loan_interst = float(input("Enter the loan interest: "))
    interest_rate = 0.1 / (12 * 1) 
    number_of_months = math.log(float(monthly_payment_amount) / (float(monthly_payment_amount) - interest_rate * float(loan_principal)), 1 + interest_rate)
    
    solution = math.ceil(number_of_months)
    m = solution % 12
    y = solution // 12

    if solution < 12:
        if m == 1:
            print(f"It will take {m} month to repay this loan!")
        else:
            print(f"It will take {m} months to repay this loan!")
    elif solution == 12:
        print(f"It will take 1 year to repay this loan!")
    elif solution == 13:
        print(f"It will take {y} year and {m} month to repay this loan!")
    else:
        if m == 0 and y > 1:
            print(f"It will take {y} years to repay this loan!")
        elif m == 1 and y > 1:
            print(f"It will take {y} years and {m} month to repay this loan!")   
        elif m > 1 and y > 1:
            print(f"It will take {y} years and {m} months to repay this loan!")
        

if what_to_calculate == 'a':
    loan_principal = float(input("Enter the loan principal: "))
    number_of_months = float(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    nominal_interest = float(((loan_interest) * (0.01) / 12))
    Num = nominal_interest * (1 + nominal_interest) ** number_of_months
    Deno = ((1 + nominal_interest) ** number_of_months) - 1
    annuity = loan_principal * (Num / Deno)
    print(f"Your monthly payment = {math.ceil(annuity)}!")


if what_to_calculate == 'p': # loan principal
    annuity_payment = float(input("Enter the annuity payment: "))
    number_of_months = float(input("Enter the number of periods: "))
    loan_interest = float(input("Enter the loan interest: "))
    nominal_interest = loan_interest / 12 / 100
    loan_principal = annuity_payment / ((nominal_interest * math.pow(1 + nominal_interest, number_of_months)) /
    (math.pow(1 + nominal_interest, number_of_months) -1))
    print(f"Your loan principal = {math.floor(loan_principal)}!")

m = input() # current payment moth
mth_diff_payment = (loan_principal / number_of_months) + (nominal_interest * (loan_principal - ((loan_principal * (m -1)) / number_of_months)))
