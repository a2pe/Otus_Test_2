from files import CSV_FILE_PATH
from files import JSON_FILE_PATH
import csv
import json


def csv_file_prep_upd():
    with open(CSV_FILE_PATH, newline='') as csv_file:
        csv_file.seek(0)
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        header_formatted_list = []
        for el in header:
            header_formatted_list.append(str(el).lower())
        new_list = []
        for element in csv_reader:
            new_list.append(dict(zip(header_formatted_list, element)))
        return new_list


data = {
    "books": csv_file_prep_upd()
}

with open("books_upd.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)

with open("books_upd.json") as books:
    with open(JSON_FILE_PATH) as users:
        books_data = json.load(books)
        users_data = json.load(users)
        for new_item in (range(0, len(users_data))):
            users_data[new_item]['books'] = []
        number_of_cycles = len(books_data['books']) // len(users_data)
        while number_of_cycles != 0:
            for item in range(0, (len(users_data))):
                users_data[item]['books'].append(books_data['books'][item])
            del books_data['books'][0:len(users_data)]
            number_of_cycles -= 1
        for i in range(0, len(books_data['books'])):
            users_data[i]['books'].append(books_data['books'][i])
        print(users_data)

        with open("final_solution.json", "w") as f:
            s = json.dumps(users_data, indent=4)
            f.write(s)
