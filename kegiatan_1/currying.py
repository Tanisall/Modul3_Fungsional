def convert_to_minutes(weeks, days, hours, minutes):
    return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes

# Fungsi curry untuk mengambil argumen satu per satu
def curry(func):
    def curried(*args):
        if len(args) == func.__code__.co_argcount:
            return func(*args)
        else:
            return lambda x: curried(*(args + (x,)))
    return curried

# Fungsi ini akan mengkonversi string "X minggu Y hari Z jam W menit" menjadi menit
def convert_string_to_minutes(input_str):
    parts = input_str.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    return convert_to_minutes(weeks, days, hours, minutes)

# Daftar data
data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Gunakan fungsi curry untuk mengaplikasikan convert_string_to_minutes pada setiap data
output_data = [curry(convert_string_to_minutes)(item) for item in data]

print(output_data)