import string, random
from sets import Set

class String_Creator():
    def create_string(self, length):
        result = ""
        for i in range(length):
            result += random.choice(string.hexdigits)
        return result

    def random_list(self, number, length):
        result = Set()
        for i in range(number):
            randomstring = self.create_string(length)
            while randomstring in result:
                randomstring = self.create_string(length)
            result.add(randomstring)
        return list(result)