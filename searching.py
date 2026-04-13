from pathlib import Path
import json


def read_data(file_name, field):

    with open("sequential.json", "r") as file:
        data = json.load(file)

    return data[field]

def linear_search(sequence, number):
    linear_result = {"positions": [],
              "count": 0}
    for i, element in enumerate(sequence):
        if element == number:
            linear_result["positions"].append(i)
            linear_result["count"] += 1
    return linear_result




    """
    Reads a JSON file and returns data for a given field.
    
    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
#     cwd_path = Path.cwd()
#
#     file_path = cwd_path / file_name
#
#
def main():
    unordered = read_data("sequential.json", "unordered_numbers")
    target = 5
    linear_result = linear_search(unordered, target)
    print(linear_result)

#
#
# if __name__ == "__main__":
#     main()
