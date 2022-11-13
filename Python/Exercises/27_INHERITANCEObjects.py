class partyanimal:
    x = 0
    name = ''

    def __int__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


# INHERITANCE is a ability to create a new class by extending an existing class

class futebolfan(partyanimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7  # Soma 7 aos pontos existentes
        self.party()
        print(self.name, 'points', self.points)
