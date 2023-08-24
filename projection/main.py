import pandas as pd
from utils import *
from formulas import basic_bazneshastegi_rule
from report import print_general_report

# Bazneshasteha
bazneshasteh_age_to_salary_history_record = pd.read_excel(
    "./csv/bazneshaste_bimepardaz_just_all.xlsx"
)
bazneshasteh = add_death_rate(bazneshasteh_age_to_salary_history_record)
# Bimeh pardazha
bimehPardaz = pd.read_excel("./csv/sabeghe_bimepardaz_just_all.xlsx")
# ---------------------------------------------

# Start Simulation
INFLATION_RATE = 0.46
for i in range(10):
    print_general_report(bazneshasteh, bimehPardaz)
    # Inflation
    bazneshasteh = add_inflation_to_salaries(bazneshasteh, INFLATION_RATE)
    bimehPardaz = add_inflation_to_salaries(bimehPardaz, INFLATION_RATE)

    # Kills
    bazneshasteh = calculate_deaths(bazneshasteh)

    # Bazneshastegi
    bazneshasteh = calculate_Bazneshasteha(
        bimehPardaz, bazneshasteh, basic_bazneshastegi_rule
    )
