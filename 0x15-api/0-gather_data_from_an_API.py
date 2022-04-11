#!/usr/bin/python3
""" Uses a REST API for a given employee ID
    Returns information about their TODO list
"""
import requests as r
import sys


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
        print("Employee {} is done with tasks({}/{}):".format(
            user_list[0].get("name"), t_len, len(todo_list)))
        for i in t_arr:
            print("\t {}".format(i.get("title")))
