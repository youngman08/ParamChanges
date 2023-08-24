import pandas as pd
from utils import *
from formulas import basic_bazneshastegi_rule
from report import print_general_report

# Bazneshasteha
bazneshasteh = pd.read_excel(
    "./csv/bazneshaste_bimepardaz_just_all.xlsx"
)
bazneshasteh = add_death_rate(bazneshasteh)
# Bimeh pardazha
bimehPardaz = pd.read_excel("./csv/sabeghe_bimepardaz_just_all.xlsx")
# ---------------------------------------------

# Start Simulation
INFLATION_RATE = 0.46
year = 1400
for i in range(5):
    print_general_report(bazneshasteh, bimehPardaz, year)
    # Inflation
    bazneshasteh = add_inflation_to_salaries(bazneshasteh, INFLATION_RATE)
    bimehPardaz = add_inflation_to_salaries(bimehPardaz, INFLATION_RATE)

    # Kills
    bazneshasteh = calculate_deaths(bazneshasteh)
    bazneshasteh = add_death_rate(bazneshasteh)

    # Bazneshastegi
    bazneshasteh = calculate_Bazneshasteha(
        bimehPardaz, bazneshasteh, basic_bazneshastegi_rule
    )

    # Aging
    bazneshasteh = add_to_ages(bazneshasteh)
    bimehPardaz = add_to_ages(bimehPardaz)

    # NEXT year
    year += 1
