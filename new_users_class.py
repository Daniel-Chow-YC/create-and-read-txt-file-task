class NewUsers():

    def __init__(self, name):
        self.name = name

    def output_text_file(self, file_name, item):
        try:
            with open(file_name, 'w+') as file_to_create:
                file_to_create.write(f'The name of this user is {self.name} ')
        finally:
            print('Program closing - execution done!')




