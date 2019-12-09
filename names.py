from new_users_class import *

# def open_print_close(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 print(line.strip('\n'))
#     except FileNotFoundError as error:
#         print('Check file name &/or path - File cannot be found')
#         print(error)
#     finally:
#         print('Program closing - execution done!')

# open_print_close('names.txt')

new_users = []

opened_file = open('names.txt', 'r')
lines = opened_file.readlines()
for line in lines:
    new_users.append(NewUsers(line))
print(new_users)
opened_file.close()

new_users[1].output_text_file('info1.txt', 22, 'red')
