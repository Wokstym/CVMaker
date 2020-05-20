import json
import re
from datetime import datetime


def pretty_print_json(json_string):
    print(json.dumps(json_string, indent=4))

def datetime_to_string():
    return datetime.now().strftime("%d/%m/%Y, %H:%M")


def string_to_datetime(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y, %H:%M")
