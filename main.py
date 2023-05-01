CONTACTS = {}

# DECORATOR
def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError as e:
            return f"This user {e} is not exist! Please Add user before using this command!"
        except ValueError:
            return 'Give me name and phone please!'
        except IndexError:
            return 'You enter not corrent name or this name is not exist!'
        except TypeError:
            return 'Please enter name and phone!'
    return inner

def command_hello(*args):
    return 'How can I help you?'

@input_error
def command_add(contacts: dict, name, phone):
    if name in contacts:
        return f'Sorry, but {name.title()} is already created! Please enter another name!'
    contacts[name] = phone

    return f'{name.title()} {phone} successfully added!'

@input_error
def command_change(contacts: dict, name, phone):
    old_phone = contacts[name]
    contacts[name] = phone
    return f'User {name.title()} change number from {old_phone} to {contacts[name]} successfully!'

@input_error
def command_phone(contacts: dict, name):
    return f'{name.title()}\'s number: {contacts[name]}'

def command_show_all(contacts: dict):
    print(f'{"NAME":<10}{"PHONE":<20}')
    print(f'{"_"*30}')
    if len(CONTACTS) < 1:
        return 'You don\'t have contacts at this moment!'
    
    for key, value in contacts.items():
        print(f'{key.title():<10}{value:<20}')

    return ''

def command_unknown(command):
    return f'Command [{command}] is not exist!'

COMMANDS = {
    'hello': command_hello,
    'add': command_add,
    'change': command_change,
    'phone': command_phone,
    'show all': command_show_all
}

def main():
    while True:
        command = input('Enter command: ').lower()
        if command in ['exit', 'good bye', 'close']:
            print('Good bye!')
            break
        if command:
            current_command = filter(lambda comanda: command.startswith(comanda), [c for c in COMMANDS.keys()])
            func = ''
            
            try:
                func = command[:len(list(current_command)[0])]
            except IndexError:
                pass
            
            if COMMANDS.get(func):
                handler = COMMANDS.get(func)
                data = command[len(func):].strip()

                if data:  
                    data = data.split(' ')
                result = handler(CONTACTS, *data)
            else:
                result = command_unknown(command)  
            print(result, '\n')
        else:
            print('Please write something!', '\n')

if __name__ == '__main__':
    main()
