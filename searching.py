from pathlib import Path
import json

from fontTools.ttLib.tables.otTables import AATStateTable


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

def binary_search(number_list, target_number):
    new_list = sorted(number_list)
    middle_index = len(new_list) / 2
    number_in_middle = new_list[middle_index]
    if number_in_middle == target_number:
        i = new_list[number_in_middle]
        return i
    if number_in_middle < target_number:
        for i, number in range(new_list[number_in_middle], len(new_list)):
            if number == target_number:
                return i
    if number_in_middle > target_number:
        for i, number in range(0, new_list[number_in_middle]):
            if number == target_number:
                return i


def pattern_search(sequence, target_sample):
    result = {}
    i = 0
    for i, sample in enumerate(sequence, i+len(target_sample)):
        if sample == target_sample:
            result.append(i)
        i = i + len(target_sample)

        return result










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

    target_sample = "ATA"
    dna_sequence = "ATGACGGAATATAAGCTAGGTGGTGGCTGGGCAGTCCGCGCTGATAGGGCAAGAGTGCGCGTACCATACCACGCTAAGCCATATAGGGCATCAGTCAGCCTGGCA"
    print(pattern_search(dna_sequence, target_sample))


#
# if __name__ == "__main__":
#     main()

import time

numbers = [4, 8, 15, 16, 23, 42, 55, 78, 91, 120]
target = 78

start = time.perf_counter()

for number in numbers:
    if number == target:
        break

end = time.perf_counter()

duration = end - start
print(f"Měření trvalo {duration:.8f} s")






