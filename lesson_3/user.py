class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def print_name(self):
        print('Имя:', self.last_name)
    
    def print_surname(self):
       print('Фамилия:', self.last_name)

    def print_name_surname(self):
       print('Имя и фамилия:', self.first_name, self.last_name)