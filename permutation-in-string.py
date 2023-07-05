def permutate(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    if s1 == s2:
        return True

    sorted_s1 = "".join(sorted(s1))

    to_check = "".join(sorted(s2[: len(s1)]))
    rest = s2[1:]

    while rest != "":
        if to_check == sorted_s1:
            return True
        else:
            to_check = "".join(sorted(rest[: len(s1)]))
            rest = rest[1 :]

    return False


if permutate("abc", "bbbca"):
    print("permutates")
else:
    print("doesnt permuate")
