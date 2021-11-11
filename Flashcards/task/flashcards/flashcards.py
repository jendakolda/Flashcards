import random
from io import StringIO


class DuplicityError(Exception):
    def __init__(self, duplicate):
        self.message = f'This {duplicate} already exists. Try again:'
        super().__init__(self.message)


def add_card():
    log_and_print('The Card:')
    while True:
        term = log_and_input()
        try:
            if term in deck.keys():
                raise DuplicityError('term')
            break
        except DuplicityError as err:
            log_and_print(str(err))

    log_and_print(f'The definition of the card:')
    while True:
        definition = log_and_input()
        try:
            if definition in [value[0] for value in deck.values()]:
                raise DuplicityError('definition')
            break
        except DuplicityError as err:
            log_and_print(str(err))
    deck[term] = [definition, 0]
    log_and_print(f'The pair ("{term}":"{definition}") has been added')


def remove_card():
    card_to_remove = log_and_input('Which card?\n')
    try:
        deck.pop(card_to_remove)
        log_and_print('The card has been removed.')
    except KeyError:
        log_and_print(f'Can\'t remove "{card_to_remove}": there is no such card.')


def import_card():
    import_file = log_and_input('File name:\n')
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
        log_and_print(f'{counter} cards have been loaded.')
    except FileNotFoundError:
        log_and_print('File not found.')


def export_card():
    export_file = log_and_input('File name:\n')
    with open(export_file, 'w') as f:
        counter = 0
        for key, value in deck.items():
            print(key, value[0], value[1], file=f)
            counter += 1
    log_and_print(f'{counter} cards have been saved.')


def ask_card():
    for i in range(int(log_and_input('How many times to ask:\n'))):
        random_key = random.choice(list(deck.keys()))
        answer = log_and_input(f'Print the definition of "{random_key}":\n')
        if answer == deck[random_key][0]:
            log_and_print('Correct')
        elif answer != deck[random_key][0] and answer in [value[0] for value in deck.values()]:
            correct_key = [k for k in deck.keys() if answer == deck[k][0]]
            log_and_print(f'Wrong.The right answer is "{deck[random_key][0]}", but your definition is correct '
                          f'for "{correct_key[0]}".')
            deck[random_key][1] += 1
        else:
            log_and_print(f'Wrong. The right answer is "{deck[random_key][0]}"')
            deck[random_key][1] += 1


def exit_program():
    log_and_print('Bye bye!')
    exit()


def log():
    log_file = log_and_input('File name:\n')
    with open(log_file, 'w') as f:
        output = log_buffer.getvalue()
        for line in output:
            f.write(line)
    log_and_print('The log has been saved.')


def log_and_print(message):
    log_buffer.write(message + '\n')
    print(message)


def log_and_input(message=''):
    log_buffer.write(message + '\n')
    return input(message)


def hardest_card():
    try:
        hardest_score = max(deck.values(), key=lambda value: value)[1]
    except ValueError:
        hardest_score = 0
    hardest_terms = [term for term, value in deck.items() if value[1] == hardest_score]
    if hardest_score == 0:
        log_and_print('There are no cards with errors.')
    elif len(hardest_terms) == 1:
        log_and_print(f'The hardest card is "{hardest_terms[0]}". You have {hardest_score} errors answering it')
    elif len(hardest_terms) >= 2:
        hardest_terms = ['"' + term + '"' for term in hardest_terms]
        log_and_print(f"The hardest card is {', '.join(hardest_terms)}. You have {hardest_score} errors answering it")


def reset_stats():
    for value in deck.values():
        value[1] = 0
    log_and_print('Card statistics have been reset.')


def get_action():
    action = log_and_input(f"Input the action ({', '.join(commands.keys())}):\n")
    card_main(action)


def card_main(name):
    commands.get(name, lambda: 'unknown_command')()


deck = {}
commands = {'add': add_card, 'remove': remove_card, 'import': import_card, 'export': export_card,
            'ask': ask_card, 'exit': exit_program, 'log': log, 'hardest card': hardest_card, 'reset stats': reset_stats}
log_buffer = StringIO()

if __name__ == '__main__':
    while True:
        get_action()
