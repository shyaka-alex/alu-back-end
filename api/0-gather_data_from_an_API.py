#!/usr/bin/python3
"""Returns information about an employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    done = [todo.get("title") for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
