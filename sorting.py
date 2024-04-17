import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {"series_1":[], "series_2":[], "series_3":[]}
        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))
    return data

def selection_sort(my_list, direction="ascending"):
    # print(my_list)
    # i = 0
    # minimum = my_list[0]
    # sorted_list = []
    # for number in my_list:
    #     if number < minimum:
    #         minimum, number = number, minimum
    #         i += 1
    #         sorted_list.append(number)
    #     else:
    #         sorted_list.append(minimum)
    # return sorted_list
    for i in range(len(my_list)):
        min_idx = i
        for num_idx in range(i + 1, len(my_list)):
            if direction == "ascending":
                if my_list[min_idx] > my_list[num_idx]:
                    min_idx = num_idx
            elif direction == "descending":
                if my_list[min_idx] < my_list[num_idx]:
                    min_idx = num_idx
    # print(my_list)
    # print(min_idx)
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    # print(my_list)
    return my_list


def bubble_sort(list):
    print(list)
    # sorted_list = []
    for idx in range(len(list)):
        for i in range(len(list) - idx - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list

def main():
    numbers = read_data("numbers.csv")
    # print(numbers)
    sorting = selection_sort(numbers["series_1"], "descending")
    # print(sorting)
    bubble_sorted = bubble_sort(numbers["series_2"])
    print(bubble_sorted)
if __name__ == '__main__':
    main()
