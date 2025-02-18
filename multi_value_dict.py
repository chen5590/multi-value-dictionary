import os

class MultiValueDictionary:
    def __init__(self):
        self.data = {}
        os.system("cls")

    def keys(self):
        if not self.data:
            return [") empty set"]
        return [f"{i+1}) {key}" for i, key in enumerate(self.data.keys())]

    def members(self, key):
        if key not in self.data:
            return [") ERROR, key does not exist."]
        return [f"{i+1}) {member}" for i, member in enumerate(self.data[key])]

    def add(self, key, member):
        if key in self.data and member in self.data[key]:
            return f") ERROR, member already exists for key"
        self.data.setdefault(key, []).append(member)
        return ") Added"

    def remove(self, key, member):
        if key not in self.data:
            return ") ERROR, key does not exist"
        if member not in self.data[key]:
            return ") ERROR, member does not exist"

        self.data[key].remove(member)
        if not self.data[key]:  # If the list is empty, remove the key
            del self.data[key]
        return ") Removed"

    def remove_all(self, key):
        if key not in self.data:
            return ") ERROR, key does not exist"
        del self.data[key]
        return ") Removed"

    def clear(self):
        self.data.clear()
        return ") Cleared"

    def key_exists(self, key):
        return ") " + str(key in self.data).lower()

    def member_exists(self, key, member):
        return ") " + str(key in self.data and member in self.data[key]).lower()

    def all_members(self):
        members = [m for members in self.data.values() for m in members]
        if not members:
            return [") empty set"]
        return [f"{i+1}) {member}" for i, member in enumerate(members)]

    def items(self):
        if not self.data:
            return [") empty set"]

        # Here we need a counter to count the all the members in keys
        result = []
        count = 1  
        for key, members in self.data.items():
            for member in members:
                result.append(f"{count}) {key}: {member}")
                count += 1  
        return result

    # This will reset the App and clear the console screen
    def reset(self):
        self.data.clear()
        os.system("cls")


