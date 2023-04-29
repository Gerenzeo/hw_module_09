import sys

CONTACTS = []

# DECORATOR
def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return "No user"
        except ValueError:
            return 'Give me name and phone please!'
        except IndexError:
            return 'You enter not corrent name or this name is not exist!'
    return inner

def command_hello(data=''):
    return 'How can I help you?'

@input_error
def command_add(data=''):
    name, phone = data.strip().split(' ')
    if name.title() in list(map(lambda name: name['name'], CONTACTS)):
        return f'Name {name.title()} already exist! Try another name!'

    CONTACTS.append({'name': name.title(), 'phone': phone})

    return f'Contact ({name.title()} {phone}) successfully added!'

@input_error
def command_change(data=''):
    name, phone = data.strip().split(' ')
    
    user_index = [index for index, elements in enumerate(CONTACTS) if elements['name'] == name.title()][0]
    old_phone = CONTACTS[user_index]['phone']
    CONTACTS[user_index]['phone'] = phone

    return f'For contact {name.title()} you changed phone from ({old_phone}) to ({phone}).'

@input_error
def command_phone(data=''):
    if len(CONTACTS) >= 1:
        user_index = [index for index, elements in enumerate(CONTACTS) if elements['name'] == data.title()][0]

        return f'Name: {data.title()}\nContact number: {CONTACTS[int(user_index)]["phone"]}'
    
    return 'You don\'t have a contacts! Please add contact before using this command!'

def command_show_all(data=''):
    if len(CONTACTS) == 0:
        return 'You don\'t have a contacts! Please add contact before using this command!'
    
    print(f'{" "*5}|{" "*20}|{" "*20}|')
    print(f'{"№":^5}|{"NAME":^20}|{"PHONE":^20}|')
    print(f'{"_"*5}|{"_"*20}|{"_"*20}|')
    for index, elements in enumerate(CONTACTS):
        index += 1
        print(f'{" "*5}|{" "*20}|{" "*20}|')
        print(f'{index:^5}|{elements["name"].title():^20}|{elements["phone"]:^20}|')
        print(f'{"_"*5}|{"_"*20}|{"_"*20}|')

    return ''

def command_good_bye(data=''):
    return sys.exit('Good bye!')

def command_unknown(data=''):
    return f'Command [{data}] is not exist!'

COMMANDS = {
    'hello': command_hello,
    'add': command_add,
    'change': command_change,
    'phone': command_phone,
    'show all': command_show_all,
    'good bye': command_good_bye,
    'exit': command_good_bye,
    'close': command_good_bye
}

def commands_run(command):
    current_command = ''.join([c for c in COMMANDS.keys() if command.startswith(c)])
    if current_command in COMMANDS.keys():
        current_argument = command[len(current_command):].strip()
        return COMMANDS[current_command], current_argument
    else:
        return command_unknown, command

def main():
    while True:
        user = input('Enter command: ')
        if user != '':
            func, arg = commands_run(user.lower())
            print(func(arg), '\n')
        else:
            print('Please enter command!', '\n')

if __name__ == '__main__':
    main()
