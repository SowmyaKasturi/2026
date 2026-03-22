# remainder in reverse order
def convert_to_basen(number, base):
    if not 2 <= base <= 36:
        return "Invalid base"
    if number == 0:
        return "0"
    is_negative = 1 if number < 0 else 0
    basennumber = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_n = ""
    number = abs(number)
    while number >= base:
        base_n = basennumber[number % base] + base_n
        number //= base
    base_n = str(number) + base_n
    return "-" + base_n if is_negative else base_n

print(convert_to_basen(123, 3))