class Paperboy:
    """class describing a paperboy"""


    def __init__ (self, name, experience, earnings):
        self.name = name
        self.experience = experience
        self.earnings = earnings

    def __str__ (self):
        return "name: {} experience: {} earnings: {}".format(self.name, self.experience, self.earnings)


bob = Paperboy('Tony', 'tons', 'lots')

print(bob)
