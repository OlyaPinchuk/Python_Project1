import os
import json
from django.shortcuts import render

from .models import User

# Create your views here.

name = 'Max'
names = ['Jack', 'Ann']
db_path = os.path.join('users', 'db.json')


def home(request):
    # print(request)
    return render(request, 'users/home.html', {'names': names})


def users(request):
    # file = open(db_path, 'r')
    # data = json.load(file)
    # file.close()

    with open(db_path, 'r') as file:
        users_list = [User(**item) for item in json.load(file)]
    return render(request, 'users/users.html', {'users': users_list})

# 1 варіант отр даних
# def create_user(request, id, name, age):
#     print(id)
#     print(name)
#     print(age)
#     return render(request, 'users/users.html')

# 2 варіант отр даних


def create_user(request, **kwargs):
    with open(db_path, 'r+') as file:
        user = User(**kwargs)
        users = json.load(file)
        users.append(kwargs)
        file.seek(0)
        json.dump(users, file)
        # file.write(json.dumps(users))
        file.truncate()
        # file.write(json.dumps(users))
        # json.dump(kwargs, file)
    # with open(db_path, 'r') as file:
    #     user = User(**json.load(file))
    return render(request, 'users/users.html', {'user': user})



