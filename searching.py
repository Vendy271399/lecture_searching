
import json
import time
import matplotlib.pyplot as plt

from generators import unordered_sequence
from generators import ordered_sequence
from generators import dna_sequence


def read_data(file_name, field):

    with open(file_name, "r") as file:
        data = json.load(file)

    if field in data.keys():
        return data[field]
    else:
        return None


def linear_search(sequential_data, find_number):
    dict_data = {}
    position = []

    for i, number in enumerate(sequential_data):
        if number == find_number:
            position.append(i)

    counter = sequential_data.count(find_number)

    dict_data["positions "] = position
    dict_data["count"] = counter

    return dict_data

def binary_search(sequential_data, find_number):
    counter = 0
    sequential_data.sort()

    while True:
        for i, number in enumerate(sequential_data):
            counter += i

        middle = counter // 2

        if sequential_data[middle] == find_number:
            return middle

        elif sequential_data[middle] < find_number:
            sequential_data = sequential_data[middle:]

        elif sequential_data[middle] > find_number:
            sequential_data = sequential_data[:middle]

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    linear = linear_search(sequential_data, 18)
    print(linear)


linear_times = []
binary_times = []
sizes = [100, 500]

sequence_1 = unordered_sequence(max_len=100)
sequence_2 = unordered_sequence(max_len=500)


start_1 = time.perf_counter()
linear_search_sequence = linear_search(sequence_1, 21)
end_1 = time.perf_counter()
duration_1 = end_1 - start_1

linear_times.append(duration_1)

start = time.perf_counter()
binary_search_sequence = binary_search(sequence_1, 21)
end = time.perf_counter()
duration_2 = end - start

binary_times.append(duration_2)


plt.plot(sizes, linear_times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()


if __name__ == "__main__":
    print(main())




