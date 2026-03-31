

import os
import json
import random
import string
from datetime import datetime



def random_string(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))



def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")



def load_list(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]



def load_json(file_path):
    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r") as f:
        return json.load(f)



def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)



def load_file(file_path):
    if not os.path.exists(file_path):
        return None

    with open(file_path, "rb") as f:
        return f.read()



def save_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(content)


def list_files(directory):
    if not os.path.exists(directory):
        return []

    return [os.path.join(directory, f) for f in os.listdir(directory)]
