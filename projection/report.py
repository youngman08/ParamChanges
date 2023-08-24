from utils import *
from colorama import Fore, Style


def print_seprated_red_line():
    print(
        Fore.GREEN + "----------------------------------------------------------------"
    )
    print(Style.RESET_ALL + "\t")


def print_general_report(bazneshasteh, bimehPardaz):
    payment_obligation = get_df_salary_sum(bazneshasteh)
    payment_obligation_in_hemat = rial_to_hemat(payment_obligation)

    print_seprated_red_line()
    print(
        f"""Bazneshaste Report:
    Payment Obligation : {payment_obligation_in_hemat} Hemat
    Alive Population:    {format_three_digit(bazneshasteh["number"].sum())}"""
    )
    print_seprated_red_line()

    # -----------------------------------------------------------------------
    people_income = get_df_salary_sum(bimehPardaz)
    people_income_in_hemat = rial_to_hemat(people_income)

    sandogh_income = convert_income_to_sandogh_income(people_income)
    sandogh_income_in_hemat = rial_to_hemat(sandogh_income)
    print(
        f"""Bimeh pardaz Report:
    People Income  : {people_income_in_hemat} Hemat
    Sandogh Income : {sandogh_income_in_hemat} Hemat
    Alive Population:    {format_three_digit(bimehPardaz["number"].sum())} """
    )
    print_seprated_red_line()
