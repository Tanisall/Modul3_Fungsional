random_list = [105, 3.1, "Hello", 737, "Python", "World", 412, 5.5, "AI"]

# Filter untuk memisahkan float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_list = list(filter(lambda x: isinstance(x, str), random_list))

# Fungsi untuk memetakan nilai integer menjadi satuan, puluhan, ratusan
def map_integer(x):
    satuan = x % 10
    puluhan = (x // 10) % 10
    ratusan = x // 100
    return {"Satuan": satuan, "Puluhan": puluhan, "Ratusan": ratusan}

int_values_mapped = list(map(map_integer, int_values))

print("Data Float :", float_values)
print("Data Int: ")
for item in int_values_mapped:
    print(item)
print("Data String :", string_list)