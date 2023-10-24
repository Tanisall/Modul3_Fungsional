def extract_integers(input_str):
    parts = input_str.split()
    integers = [int(part) for part in parts if part.isdigit()]
    return integers

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Menggunakan filter untuk mengambil nilai integer dari setiap elemen dalam data
integer_data = list(filter(lambda x: len(extract_integers(x)) > 0, data))

# Mencetak nilai integer dari setiap elemen dalam data
for item in integer_data:
    integers = extract_integers(item)
    print(integers)