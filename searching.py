
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





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == "__main__":
    result = main()



