import json
# Пока не разобрался как поместить это в class
import pathlib
from pathlib import Path
path = Path(pathlib.Path.cwd().parent, "resources", "data.json")
"""Вместо пути к файлу можно подставить просто значение path with open(path, 'r') as f:"""
with open("../resources/data.json", 'r') as f:
    secret_variables = json.load(f)

NAME_ADMIN = secret_variables['name']
PASSWORD_ADMIN = secret_variables['password']
URL_ENDPOINT = secret_variables['endpoint']

"""User data we create"""
USER_POPRAVKA = secret_variables['user_name_popravka']
PASSWORD_POPRAVKA = secret_variables['user_password_popravka']


