from collections import UserDict
from models.record import Record

class AddressBook(UserDict):
    # A class for storing and managing addresses.
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def search_record(self, name: str) -> Record:
        return self.data[name]

    def delete_by_name(self, name):
        del self.data[name]