import pandas as pd

from enums import MaxWageUpgrade
from helper import calc_gorn_percentage, insurance_perimum_ceil, print_govern_total
from plot import plot_insurance_perimum_diff

GOVERN_PERCENTAGE = 3 / 100

print_govern_total(GOVERN_PERCENTAGE)

table_4 = pd.DataFrame(
    {
        "min_wage": [2006314, 26554950],
        "1_2x": [9000649, 37606547],
        "2_3x": [2073051, 65309427],
        "3_4x": [1084292, 91277697],
        "4_5x": [466518, 117642390],
        "5_6x": [223549, 144758064],
        "6_7x": [275624, 177765024],
    },
    index=["total_number", "avg_wage"],
)

table_4.loc["original_govern_share"] = round(
    calc_gorn_percentage(table_4.loc["avg_wage"], GOVERN_PERCENTAGE)
)

plot_insurance_perimum_diff(table_4)
insurance_perimum_ceil(MaxWageUpgrade.One_x, table_4, GOVERN_PERCENTAGE)
insurance_perimum_ceil(MaxWageUpgrade.Two_x, table_4, GOVERN_PERCENTAGE)
insurance_perimum_ceil(MaxWageUpgrade.Three_x, table_4, GOVERN_PERCENTAGE)
