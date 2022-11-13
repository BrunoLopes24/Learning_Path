class partyanimal:
    x = 0

    def __int__(self):  # Constructor
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far: ', self.x)

    def __del__(self):  # Destructor
        print('I am destructed', self.x)

an = partyanimal()
an.party()
an.party()
an = 42
print('AN contains: ', an)
