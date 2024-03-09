import math
import argparse

IN_PARAM = "Incorrect parameter"


def annuity_loan_principal(i, a, n):
    loan_principal = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    print(f"Your loan principal = {int(loan_principal)}!\n"
          f"Overpayment = {int(a * n - loan_principal)}")


def annuity_monthly_payment(i, p, n):
    monthly_payment = math.ceil(p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
    print(f"Your annuity payment = {monthly_payment}!\n"
          f"Overpayment = {int(monthly_payment * n - p)}")


def annuity_number_monthly_payments(i, a, p):
    num_months = math.ceil(math.log(a / (a - i * p), 1 + i))
    if num_months < 12:
        print(f"It will take {num_months} month{"" if num_months == 1 else "s"} to repay this loan!")
    elif num_months % 12 == 0:
        print(f"It will take {num_months // 12} year{"" if (num_months // 12) == 1 else "s"} to repay this loan!")
    else:
        print(
            f"It will take {math.floor(num_months / 12)} year{"" if math.floor(num_months // 12) == 1 else "s"}"
            f" and {num_months % 12} month{"" if num_months % 12 == 1 else "s"} to repay this loan!")
    print(f"Overpayment = {int(a * num_months - p)}")


def diff_payment(i, p, n):
    overpayment = -p
    for m in range(1, n + 1):
        dm = math.ceil((p / n) + i * (p - ((p * (m - 1)) / n)))
        print(f"Month {m}: payment is {dm}")
        overpayment += dm
    print(f"\nOverpayment = {int(math.ceil(overpayment))}")


parser = argparse.ArgumentParser(description="Debt Repayment Calculator")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--type")

args = parser.parse_args()
args_list = [args.payment, args.principal, args.periods, args.interest, args.type]

# check incorrect parameters
arg_count = 0
negativ = False
for arg in args_list:
    if arg is not None:
        arg_count += 1
        if arg[0] == "-":
            negativ = True
if (args.type is None or
        args.type == "diff" and args.payment is not None or
        args.interest is None or
        arg_count < 4 or
        negativ):
    print(IN_PARAM)
    exit()

nominal_interest = float(args.interest) / 100 / (12 * 1)

if args.type == "diff":
    diff_payment(nominal_interest, float(args.principal), int(args.periods))
    exit()

if args.principal is None:
    annuity_loan_principal(nominal_interest, float(args.payment), int(args.periods))
elif args.payment is None:
    annuity_monthly_payment(nominal_interest, float(args.principal), int(args.periods))
else:
    annuity_number_monthly_payments(nominal_interest, float(args.payment), float(args.principal))
