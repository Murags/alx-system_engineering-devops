#!/usr/bin/python3
"""Script that exports to json file
    """

import json
from requests import get


def main():
    task_res = get("https://jsonplaceholder.typicode.com/todos")
    user_res = get(
        "https://jsonplaceholder.typicode.com/users")
    filename = "todo_all_employees.json"

    with open(filename, "w") as f:
        final_dict = {}
        for user in user_res.json():
            employee_name = user.get("username")
            employee_id = user.get("id")
            task_list = []
            for task in task_res.json():
                if task.get("userId") == employee_id:
                    temp = {}
                    temp["username"] = employee_name
                    temp["task"] = task.get("title")
                    temp["completed"] = task.get("completed")
                    task_list.append(temp)

            final_dict[employee_id] = task_list
        json.dump(final_dict, f)


if __name__ == "__main__":
    main()
