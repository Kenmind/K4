#!/usr/bin/python3
""" Uses a REST API for a given employee ID
    Returns information about their TODO list
"""
import json
import requests as r
import sys


def make_json(user_list=None, todo_list=None, u=None):
    """ Converts payloads into JSON formated file """
    t_list = []
    with open(sys.argv[1] + ".json", "w") as f:
        for i in todo_list:
            t_list.append({"task": i.get("title"),
                           "completed": i.get("completed"),
                           "username": user_list[0].get("username")})
        t_json = {str(u): t_list}
        json.dump(t_json, f)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args = {"id": sys.argv[1]}
        user_list = r.get("https://jsonplaceholder.typicode.com/users",
                          params=args).json()
        args = {"userId": sys.argv[1]}
        todo_list = r.get("https://jsonplaceholder.typicode.com/todos",
                          params=args).json()
        make_json(user_list, todo_list, sys.argv[1])
