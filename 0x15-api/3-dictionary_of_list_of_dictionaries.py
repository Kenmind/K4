#!/usr/bin/python3
""" Uses a REST API for a given employee ID
    Returns information about their TODO list
"""
import json
import requests as r


if __name__ == "__main__":
    web = "https://jsonplaceholder.typicode.com/"
    user_list = r.get(web + "users").json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({users.get("id"): [{
                           "task": todos.get("title"),
                           "completed": todos.get("completed"),
                           "username": users.get("username")}
                           for todos in r.get(web + "todos",
                                              params={"userId":
                                                      users.get("id")}).json()]
                   for users in user_list}, f)
