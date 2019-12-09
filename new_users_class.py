class NewUsers():

    def __init__(self, name):
        self.name = name

    def output_text_file(self, file_name, age, fav_colour):
        try:
            with open(file_name, 'w+') as file_to_create:
                file_to_create.write(f"The name of this user is {self.name}"
                                     f"The users' age is {age} "
                                     f"and their favourite colour is {fav_colour}.")
        # except TypeError as error:
        #     print('Ensure you have inputted all arguments')
        #     print(error)

        finally:
            print('Program closing - execution done!')




