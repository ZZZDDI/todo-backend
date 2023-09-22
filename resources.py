import json
import os


def print_with_indent(value, indent=0):
    indentation = "\t" * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def json(self):
        res = {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries]
        }
        return res

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def save(self, path):
        file_name = os.path.join(path, f'{self.title}.json')

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.json(), f)

    @classmethod
    def from_json(cls, value: dict):
        new_entry = Entry(value['title'])
        for item in value.get('entries', []):
            new_entry.add_entry(cls.from_json(item))
        return new_entry

    @classmethod
    def load(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = json.load(f)
        return cls.from_json(content)


category = Entry('Еда')

category.add_entry(Entry('Морковь'))
category.add_entry(Entry('Капуста'))

category.json()
