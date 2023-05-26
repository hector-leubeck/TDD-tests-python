def baconWithEggsVerifier(x):
    assert isinstance(x, (int)), "x precisa ser INT"

    multiple_of_3 = True if x % 3 == 0 else False
    multiple_of_5 = True if x % 5 == 0 else False

    if multiple_of_3 and multiple_of_5:
        return 'Bacon com ovos!'

    if multiple_of_3:
        return "Bacon!"

    if multiple_of_5:
        return "Ovos!"

    return "Passou Fome!"
