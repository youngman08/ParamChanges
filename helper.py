import pandas as pd

from consts import ONE_HEMAT, average_income_1400, number_of_bimey_shodegan_1400
from enums import MaxWageUpgrade


def format_three_digit(number):
    number = str(int(number))

    result = ""
    for i, value in enumerate(number[::-1]):
        if i % 3 == 0 and i != 0:
            result += "_"
        result += value
    return result[::-1]


def rial_to_hemat(number):
    number = int(number)

    return round(number / ONE_HEMAT, 3)


def rial_to_hunder_toman(number):
    return round(number / 10000)


def calc_gorn_percentage(wage, govern_percentage=0.03):
    return wage * 0.3 * govern_percentage


def print_govern_total(GOVERN_PERCENTAGE):
    print(
        "Government 3% Insurance premium in 1400:",
        format_three_digit(
            calc_gorn_percentage(average_income_1400, GOVERN_PERCENTAGE)
            * number_of_bimey_shodegan_1400
        ),
        "Rial",
        "|",
        rial_to_hemat(
            calc_gorn_percentage(average_income_1400, GOVERN_PERCENTAGE)
            * number_of_bimey_shodegan_1400
        ),
        "Hemat",
    )


def get_percentage(num1, num2) -> float:
    return round(num1 / num2, 3) * 100


def insurance_perimum_ceil(
    ceil: MaxWageUpgrade, data: pd.DataFrame, govern_percentage: float
):
    total_people = data.loc["total_number"].sum()

    if ceil == MaxWageUpgrade.One_x:
        unsuported = data.drop("min_wage", axis=1)
        data = data[["min_wage"]]
        max_supported_salary = data["min_wage"]["avg_wage"]

    elif ceil == MaxWageUpgrade.Two_x:
        unsuported = data.drop(["min_wage", "1_2x"], axis=1)
        data = data[["min_wage", "1_2x"]]
        max_supported_salary = data["1_2x"]["avg_wage"]

    elif ceil == MaxWageUpgrade.Three_x:
        unsuported = data.drop(columns=["min_wage", "1_2x", "2_3x"])
        data = data[["min_wage", "1_2x", "2_3x"]]
        max_supported_salary = data["2_3x"]["avg_wage"]

    max_govern_share_pay = rial_to_hunder_toman(
        calc_gorn_percentage(max_supported_salary, govern_percentage)
    )

    effected_people = unsuported.loc["total_number"].sum()
    print(
        f"\n\nThe {ceil.name} ceil will effect {get_percentage(effected_people,total_people)}% of current people"
    )
    print(
        f"For those people govern only pay {format_three_digit(max_govern_share_pay)} Rial per person"
    )

    unsuported.loc["Should pay on new ceil (hunder toman)"] = round(
        unsuported.loc["original_govern_share"] - max_govern_share_pay
    )
    unsuported.loc["Should pay on new ceil (Percentage of wage)"] = get_percentage(
        unsuported.loc["Should pay on new ceil (hunder toman)"], unsuported.loc["avg_wage"]
    )
    print(unsuported)
