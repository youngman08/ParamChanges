import matplotlib.pyplot as plt


def plot_insurance_perimum_diff(data):
    plt.bar(data.loc['original_govern_share (hunderd toman)'].index, data.loc['original_govern_share (hunderd toman)'].array)
    plt.ylabel("Wage")
    plt.title("goverment insurance perimum share per person")
    plt.show()
