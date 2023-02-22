import matplotlib.pyplot as plt


def plot_insurance_perimum_diff(data):
    plt.bar(data.loc['original_govern_share'].index, data.loc['original_govern_share'].array)
    plt.ylabel("Wage")
    plt.title("insurance perimum share")
    plt.show()
