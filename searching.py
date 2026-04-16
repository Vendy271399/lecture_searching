
import json

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


if __name__ == "__main__":
    result = main()
    print(main())



