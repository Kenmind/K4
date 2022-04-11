#!/usr/bin/python3
""" Uses a REST API for a given employee ID
    Returns information about their TODO list
"""
import csv
import requests as r
import sys


def make_csv(user_list=None, todo_list=None):
    """ Converts payloads into CSV formated file """
    titles = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open(sys.argv[1] + ".csv", "w") as f:
        write = csv.DictWriter(f, fieldnames=titles, quoting=csv.QUOTE_ALL)
        for i in todo_list:
            write.writerow({"USER_ID": i.get("userId"),
                           "USERNAME": user_list[0].get("username"),
                            "TASK_COMPLETED_STATUS": i.get("completed"),
                            "TASK_TITLE": i.get("title")})


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args = {"id": sys.argv[1]}
        user_list = r.get("https://jsonplaceholder.typicode.com/users",
                          params=args).json()
        args = {"userId": sys.argv[1]}
        todo_list = r.get("https://jsonplaceholder.typicode.com/todos",
                          params=args).json()
        t_len = 0
        t_arr = []
        for j in todo_list:
            if j.get("completed"):
                t_arr.append(j)
                t_len += 1
        make_csv(user_list, todo_list)
