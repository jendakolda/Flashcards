import random


class DuplicityError(Exception):
    def __init__(self, duplicate):
        self.message = f'This {duplicate} already exists. Try again:'
        super().__init__(self.message)


def add_card():
    print('The Card:')
    while True:
        term = input()
        try:
            if term in deck.keys():
                raise DuplicityError('term')
            break
        except DuplicityError as err:
            print(err)

    print(f'The definition of the card:')
    while True:
        definition = input()
        try:
            if definition in deck.values():
                raise DuplicityError('definition')
            break
        except DuplicityError as err:
            print(err)
    deck[term] = list(definition, 0)
    print(f'The pair ("{term}":"{definition}") has been added')


def remove_card():
    card_to_remove = input('Which card?\n')
    try:
        deck.pop(card_to_remove)
        print('The card has been removed.')
    except KeyError:
        print(f'Can\'t remove "{card_to_remove}": there is no such card.')


def import_card():
    import_file = input('File name:\n')
    try:
        with open(import_file, 'r') as f:
            counter = 0
            for line in f:
                try:
                    key, value, score = line.split()
                except ValueError:
                    key, value = line.split()
                    score = 0
                deck[key] = [value, int(score)]
                counter += 1
        print(f'{counter} cards have been loaded.')
    except FileNotFoundError:
        print('File not found.')


def export_card():
    export_file = input('File name:\n')
    with open(export_file, 'w') as f:
        counter = 0
        for key, value in deck.items():
            print(key, value[0], value[1], file=f)
            counter += 1
    print(f'{counter} cards have been saved.')


def ask_card():
    for i in range(int(input('How many times to ask:\n'))):
        random_key = random.choice(list(deck.keys()))
        answer = input(f'Print the definition of "{random_key}":\n')
        if answer == deck[random_key][0]:
            print('Correct')
        elif answer != deck[random_key][0] and answer in [value[0] for value in deck.values()]:
            correct_key = [k for k in deck.keys() if answer == deck[k]]
            print(f'Wrong.The right answer is "{deck[random_key]}", but your definition is correct '
                  f'for "{correct_key[0]}".')
        else:
            print(f'Wrong. The right answer is "{deck[random_key]}"')


def exit_program():
    print('Bye bye!')
    exit()


def log():
    log_file = input('File name:\n')
    with open(log_file, 'w') as f:
        pass
    print('The log has been saved.')


def hardest_card():
    pass


def reset_stats():
    pass


def get_action():
    action = input('Input the action (add, remove, import, export, ask, exit):\n')
    card_main(action)


def card_main(name):
    commands.get(name, lambda: 'unknown_command')()


deck = {}
commands = {'add': add_card, 'remove': remove_card, 'import': import_card, 'export': export_card,
            'ask': ask_card, 'exit': exit_program, 'log': log, 'hardest_card': hardest_card, 'reset stats': reset_stats}

if __name__ == '__main__':
    while True:
        get_action()
