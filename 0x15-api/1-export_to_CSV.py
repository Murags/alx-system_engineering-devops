#!/usr/bin/python3
"""Script that exports to csv file
    """

import csv
from requests import get
from sys import argv


def main():
    task_res = get("https://jsonplaceholder.typicode.com/todos")
    user_res = get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    employee_name = user_res.json().get("username")
    filename = argv[1] + ".csv"

    with open(filename, "w", newline='') as csvfile:
        for task in task_res.json():
            if task.get("userId") == int(argv[1]):
                    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                    writer.writerow([argv[1], employee_name, task.get(
                        "completed"), task.get("title")])


if __name__ == "__main__":
    main()
