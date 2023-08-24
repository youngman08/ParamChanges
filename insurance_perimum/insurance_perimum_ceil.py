import pandas as pd
from enums import MaxWageUpgrade
from tabulate import tabulate

from helper import (
    calc_gorn_percentage,
    format_three_digit,
    get_percentage,
    rial_to_hunder_toman,
)


class insurancePerimumCeil:
    def __init__(
        self,
        ceil: MaxWageUpgrade,
        data: pd.DataFrame,
        govern_percentage: float,
        save_as_csv: bool = True,
    ) -> None:
        self.ceil = ceil
        self.data = data
        self.govern_percentage = govern_percentage
        self.save_as_csv = save_as_csv

        self.total_number_of_people = data.loc["total_number"].sum()

    def main(self):

        if self.ceil == MaxWageUpgrade.One_x:
            unsuported = self.data.drop("min_wage", axis=1)
            self.data = self.data[["min_wage"]]
            max_supported_salary = self.data["min_wage"]["avg_wage"]

        elif self.ceil == MaxWageUpgrade.Two_x:
            unsuported = self.data.drop(["min_wage", "1_2x"], axis=1)
            self.data = self.data[["min_wage", "1_2x"]]
            max_supported_salary = self.data["min_wage"]["avg_wage"] * 2

        elif self.ceil == MaxWageUpgrade.Three_x:
            unsuported = self.data.drop(columns=["min_wage", "1_2x", "2_3x"])
            self.data = self.data[["min_wage", "1_2x", "2_3x"]]
            max_supported_salary = self.data["min_wage"]["avg_wage"] * 3

        max_govern_share_pay = rial_to_hunder_toman(
            calc_gorn_percentage(max_supported_salary, self.govern_percentage)
        )

        effected_people = unsuported.loc["total_number"].sum()
        self.percentage_of_effected_people = get_percentage(
            effected_people, self.total_number_of_people
        )

        unsuported.loc["Should pay on new ceil (hunder toman)"] = round(
            unsuported.loc["original_govern_share (hunderd toman)"]
            - max_govern_share_pay
        )
        unsuported.loc["Should pay on new ceil (Percentage of wage)"] = get_percentage(
            unsuported.loc["Should pay on new ceil (hunder toman)"],
            unsuported.loc["avg_wage"],
        )

        unsuported.loc["Goverment pay per group"] = (
            unsuported.loc["Should pay on new ceil (hunder toman)"]
            * unsuported.loc["total_number"]
        )

        total_govern_pay = unsuported.loc["Goverment pay per group"].sum()

        self.print_log(max_govern_share_pay, unsuported, total_govern_pay)

    def print_log(self, max_govern_share_pay, unsuported_people, total_govern_pay):
        print(
            f"\n\nThe {self.ceil.name} ceil will effect {self.percentage_of_effected_people}% of current people"
        )
        print(
            f"For those people govern only pay {format_three_digit(max_govern_share_pay)} Hunder Toman per person"
        )

        print(tabulate(unsuported_people, headers="keys", tablefmt="psql"))

        print(
            f"Goverment save on new ceil {format_three_digit(total_govern_pay)} Hunderds Toman"
        )

        if self.save_as_csv:
            unsuported_people.to_csv(f"./csv/unsuported_people_{self.ceil.name}.csv")
