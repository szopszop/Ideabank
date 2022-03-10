import sys
filename = 'list_of_ideas.txt'


def open_file():
    try:    
        with open(filename, 'r') as file:
            the_list = file.readlines()
            return the_list
    except FileNotFoundError:
        file = open(filename, 'w')
        file.close()


def get_index():
    with open(filename) as file:
        the_list = file.readlines()
    index = 0
    for idea in the_list:
        index += 1
    return index + 1


def add_idea():
    with open(filename, 'a') as file:
        index = get_index()
        idea = input("\nWhat is your new idea?\n:")
        file.write(idea + '\n')
        index += 1


def delete_idea(number_to_delete):
    the_list = open_file()
    for line in range(len(the_list)):
        if line == number_to_delete:
            del the_list[(int(number_to_delete))-1]
    with open(filename, 'w') as file:
        file.write("".join(the_list))
    

def print_ideas():
    the_list = open_file()
    print("\nHere's the list of all ideas:")
    for number, line in enumerate(the_list):
        print(f'{number + 1}. {line}', end='')


def main_menu():
    print('Welcome to the Idea Bank!')
    print_ideas()
    while True:
        add_idea()
        print_ideas()


if len(sys.argv) == 1:
    main_menu()

if len(sys.argv) == 2:
    operation_type = sys.argv[1]
    if operation_type == '--list':
        print_ideas()
    if operation_type == '--delete':
        print('Specify a number after --delete')

if len(sys.argv) == 3:
    operation_type = sys.argv[1]
    number_to_delete = int(sys.argv[2])
    if operation_type == '--delete':
        index = get_index()
        if number_to_delete in range(index):
            delete_idea(number_to_delete)
            print_ideas()
        else:
            print('Specify a number after --delete')

