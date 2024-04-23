import string


def capital_letters(line=input()):
    """принимает на вход строки и возвращает ее со всеми заглавными буквами"""

    return line.upper()


print(capital_letters())


def capital_letter_1(line=input()):
    """делает заглавными первые буквы каждого слова в строке"""

    return string.capwords(line)


print(capital_letter_1())
