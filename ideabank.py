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
    for line in the_list:
        index += 1
    return index 


def add_idea():
    with open(filename, 'a') as file:
        index = get_index()
        idea = input("\nWhat is your new idea?\n:")
        file.write('\n' + str(index) + '. ' + idea)
        index += 1


def print_ideas():
    the_list = open_file()
    print("\nHere's the list of all ideas:")
    for line in the_list:
        print(line, end="")


def main_menu():
    print('Welcome to the Idea Bank!')
    print_ideas()
    while True:
        add_idea()
        print_ideas()


argv_command = -1
if len(sys.argv) == 2:
    argv_command = sys.argv[1]
    if argv_command == '--list':
        print_ideas()



















# if __name__ == '__main__':
#     main_menu()