from collections import UserDict

class Record:
    # A class for storing information about a contact, including name and phone list.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    
    def add_phone():
        pass

    def remove_phone():
        pass

    def edit_phone():
        pass

    def find_phone():
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"