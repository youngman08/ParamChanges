from consts import MIN_MONTHLY_INCOME_1396_RIAL, PERSON_MONTH_IN_1396
from helper import rial_to_hemat


def calc_monthly_unimployment_wage():
    return round(MIN_MONTHLY_INCOME_1396_RIAL * 0.55, 3)


def easy_way():
    print("Cost for unemployment Insurance in 1396 =>")
    cost_in_rial = 40_329_138 * 1000_000  # Convert milion rial to rial
    print(f"{rial_to_hemat(cost_in_rial )} Hemat")
    print("-" * 50)


def hard_way():
    goverment_cost_yearly = PERSON_MONTH_IN_1396 * calc_monthly_unimployment_wage()
    print(f"{rial_to_hemat(goverment_cost_yearly)} Milion Rial")
    print("-" * 50)


easy_way()
hard_way()
