def only_numbers(string, decimal_separator="."):
    return "".join(str(c) for c in string if c.isdigit() or c == decimal_separator)
