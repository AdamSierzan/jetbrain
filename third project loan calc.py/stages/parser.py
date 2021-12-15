import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--principal', type=float) # loan_principal
parser.add_argument('--periods', type=int) # number of months
parser.add_argument('--interest', type=float) # interest 
parser.add_argument('--payment', type=float) # montly payment 
parser.add_argument('--type')
args = parser.parse_args()




if args.type == 'annuity':
    #to calculate annual payment
    if args.payment == None:
        if args.interest == None:
            print("Incorrect parameters")
        else:
            interest_rate = args.interest * (0.01) / 12
            Num = interest_rate * (1 + interest_rate) ** args.periods
            Deno = ((1 + interest_rate) ** args.periods) - 1
            annuity = math.ceil(args.principal * (Num / Deno))
            print(f'Your annuity payment = {math.ceil(annuity)}!')
            print(f'Overpayment = {math.ceil((annuity * args.periods) - args.principal)}')


    #to calculate principal
    if args.principal == None:
        interest_rate = args.interest * (0.01) / 12
        loan_principal = args.payment / ((interest_rate * math.pow(1 + interest_rate, args.periods)) /
        (math.pow(1 + interest_rate, args.periods) -1))
        Num = interest_rate * (1 + interest_rate) ** args.periods
        Deno = ((1 + interest_rate) ** args.periods) - 1
        annuity = math.ceil(loan_principal * (Num / Deno))
        print(f"Your loan principal = {math.floor(loan_principal)}!")
        print(f'Overpayment = {math.ceil((annuity * args.periods) - loan_principal)}')

    #to calculate time needed to pay the loan
    if args.periods == None:
        interest_rate = args.interest * (0.01) / 12
        number_of_months = math.log((args.payment) / ((args.payment) - interest_rate * (args.principal)), 1 + interest_rate)
        # number_of_months = math.log((monthly_payment_amount) / ((monthly_payment_amount) - interest_rate * (loan_principal)), 1 + interest_rate)

        solution = math.ceil(number_of_months)
        m = solution % 12
        y = solution // 12

        Num = interest_rate * (1 + interest_rate) ** number_of_months
        Deno = ((1 + interest_rate) ** number_of_months) - 1
        annuity = math.ceil(args.principal * (Num / Deno))

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

        print(f'Overpayment = {math.ceil((annuity * number_of_months) - args.principal)}')

elif args.type == 'diff':
    if args.payment != None:
        print("Incorrect parameters")
    else:
        interest_rate = args.interest * (0.01) / 12
        m = 1
        sum_of_payments = 0
        for i in range(args.periods):
            mth_diff_payment = (args.principal / args.periods) + (interest_rate * (args.principal - (args.principal * (m -1)) / args.periods))
            sum_of_payments += math.ceil(mth_diff_payment)
            print(f"Month {m}: payment is {math.ceil(mth_diff_payment)}")
            m += 1
        print(f'\nOverpayment = {math.ceil(sum_of_payments - args.principal)}')

elif args.type == None:
    print("Incorrect parameters")




