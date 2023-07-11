from files import CSV_FILE_PATH
from files import JSON_FILE_PATH
import csv
import json


def book_data_prep():
    """ Preparing a list of the books to be distributed."""
    with open(CSV_FILE_PATH, newline='') as csv_file:
        csv_file.seek(0)
        csv_reader = csv.reader(csv_file)
        header: list[str] = [str(smth).lower() for smth in next(csv_reader)
                             if smth != 'Publisher']

        new_list = []
        for element in csv_reader:
            new_list.append(dict(zip(header, element)))

        book_data: list[dict[str, str]] = [
            {'title': obj['title'],
             'author': obj['author'],
             'pages': obj['pages'],
             'genre': obj['genre']}
            for obj in new_list]
        return book_data


def book_distribution(users: dict, books: list):
    """
    Function to distribute the book_data from book_data_prep()
    among the users in the dictionary.
    """
    for item in (range(0, len(users))):
        users[item]['books'] = []
    number_of_cycles: int = len(books['books']) // len(users)
    while number_of_cycles != 0:
        for item in range(0, (len(users))):
            users[item]['books'].append(books['books'][item])
        del books['books'][0:len(users)]
        number_of_cycles -= 1
    for i in range(0, len(books['books'])):
        users[i]['books'].append(books['books'][i])
    data: list[dict[str, str]] = [
        {'name': obj['name'],
         'gender': obj['gender'],
         'address': obj['address'],
         'age': obj['age'],
         'books': obj['books']
         }
        for obj in users]
    return data


def file_with_book_distribution():
    """ Creating a JSON file with the distributed books."""
    with open(JSON_FILE_PATH) as users:
        users_data = json.load(users)
        books_data = {
            "books": book_data_prep()
        }
        data = book_distribution(users_data, books_data)

        with open("final_solution.json", "w") as f:
            s = json.dumps(data, indent=4)
            f.write(s)


file_with_book_distribution()
