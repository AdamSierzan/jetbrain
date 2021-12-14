import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--principal', type=float) # loan_principal
parser.add_argument('--periods', type=int) # number of months
parser.add_argument('--interest', type=int) # interest 
parser.add_argument('--payment', type=float) # montly payment 
parser.add_argument('--type')
args = parser.parse_args()


# def mth_diff_payment():
#     diff_payment = (loan_principal / number_of_months) + (interest_rate * (loan_principal - ((loan_principal * (m -1)) / number_of_months)))
#     print(diff_payment)


if args.type == 'annuity':
   
    print(f'Your annuity payment = {args.periods * args.payment}!')

elif args.type == 'diff':
    interest_rate = args.interest * (0.01) / 12
    m = 1
    for i in range(args.periods):
        mth_diff_payment = (args.principal / args.periods) + (interest_rate * (args.principal - (args.principal * (m -1)) / args.periods))
        m += 1
        print(mth_diff_payment)





# m = input() # current payment moth
# mth_diff_payment = (loan_principal / number_of_months) + (nominal_interest * (loan_principal - ((loan_principal * (m -1)) / number_of_months)))
# if what_to_calculate == 'a':
#     loan_principal = float(input("Enter the loan principal: "))
#     number_of_months = float(input("Enter the number of periods: "))
#     loan_interest = float(input("Enter the loan interest: "))
#     nominal_interest = float(((loan_interest) * (0.01) / 12))
#     Num = nominal_interest * (1 + nominal_interest) ** number_of_months
#     Deno = ((1 + nominal_interest) ** number_of_months) - 1
#     annuity = loan_principal * (Num / Deno)
#     print(f"Your monthly payment = {math.ceil(annuity)}!")
# mth_diff_payment = (loan_principal / number_of_months) + (interest_rate * (loan_principal - ((loan_principal * (m -1)) / number_of_months)))
