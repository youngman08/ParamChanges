from consts import ONE_HEMAT


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
    return wage * govern_percentage


def get_percentage(num1, num2) -> float:
    return round(num1 / num2, 3) * 100
