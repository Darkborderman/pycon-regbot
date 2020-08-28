import os
import csv
from dotenv import load_dotenv
load_dotenv()

CORPORATE_FILE = os.getenv("CORPORATE_FILE_PATH")
INDIVIDUAL_FILE = os.getenv("INDIVIDUAL_FILE_PATH")
RESERVED_FILE = os.getenv("RESERVED_FILE_PATH")
USED_FILE = os.getenv("USED_FILE_PATH")

def import_all_token():
    token_dict = dict()
    
    # Corporate Ticket
    with open(CORPORATE_FILE, newline='') as f:
        rows = csv.reader(f)
        for ticket_type, token in rows:
            token_dict[token] = ticket_type

    # Individual Ticket
    with open(INDIVIDUAL_FILE, newline='') as f:
        rows = csv.reader(f)
        for ticket_type, token in rows:
            token_dict[token] = ticket_type

    # Reserved Ticket
    with open(RESERVED_FILE, newline='') as f:
        rows = csv.reader(f)
        for ticket_type, token in rows:
            token_dict[token] = ticket_type

    return token_dict

def read_used_list():
    try:
        with open(USED_FILE, 'r') as f:
            used_list = f.read().splitlines()
        return used_list
    except IOError as e:
        print(f"{USED_FILE} not exist, create one!")
        f = open(USED_FILE, 'w+')
        f.close()
        return list()