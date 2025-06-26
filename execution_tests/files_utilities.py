import csv
import json


def load_cvs(filename, delimiter="\t"):
    file = open(filename) #, encoding="utf8")
    rate = csv.reader(file, delimiter=delimiter)
    header = []
    rows = []
    for i, row in enumerate(rate):
        if i == 0:
            header = row
        if i > 0:
            rows.append(row)
    return [header, rows]


def save_csv(filename, data_table, header=None):
    if header is not None:
        data_table.insert(0, header)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(data_table)


def write_csv(filename_, content):
    with open(filename_, 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(content)


def load_json(file_name):
    try:
        with open(file_name, "r", encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in file: {e}")
    except IOError as e:
        print(f"I/O error: {e}")
    return {}


def write_json(file__name, content):
    with open(file__name, "w", encoding="utf-8") as text_file:
        print(json.dumps(content, indent=4), file=text_file)


def write_jsonl(file__name, content):
    with open(file__name, "a", encoding="utf-8") as text_file:
        print(json.dumps(content), file=text_file)
