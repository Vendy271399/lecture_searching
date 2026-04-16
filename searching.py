
import json

def read_data(file_name, field):

    with open(file_name, "r") as file:
        data = json.load(file)

    if field in data.keys():
        return data[field]
    else:
        return None



def main():
    pass


if __name__ == "__main__":
    data = read_data("sequential.json", "unordered_numbers")
    print(data)

