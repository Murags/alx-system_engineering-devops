#!/usr/bin/python3
"""Script that exports to csv file
    """

import json
from requests import get
from sys import argv


def main():
    task_res = get("https://jsonplaceholder.typicode.com/todos")
    user_res = get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    employee_name = user_res.json().get("username")
    filename = argv[1] + ".json"

    with open(filename, "w") as f:
        final_dict = {}
        task_list = []
        for task in task_res.json():
            if task.get("userId") == int(argv[1]):
                temp = {}
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                temp["username"] = employee_name
                task_list.append(temp)

        final_dict[argv[1]] = task_list
        json.dump(final_dict, f)


if __name__ == "__main__":
    main()
