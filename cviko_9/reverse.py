def reverse(string):
    if len(string) == 1:
        return string

    first, rest = string[0], string[1:]

    rest = reverse(rest)
    return f"{rest}{first}"


print(reverse("Hello world"))
