class TermDuplicityError(Exception):
    def __init__(self, duplicate_term):
        self.message = f'The term "{duplicate_term}" already exists. Try again:'
        super().__init__(self.message)


class DefDuplicityError(Exception):
    def __init__(self, duplicate_def):
        self.message = f'The definition "{duplicate_def}" already exists. Try again:'
        super().__init__(self.message)


class Card:
    deck = {}

    def __init__(self, front, back):
        self.front = front
        self.back = back

    @staticmethod
    def add_card():
        print('The Card:\n')
        while True:
            term = input()
            try:
                if term in (value.front for value in Card.deck.values()):
                    raise TermDuplicityError(term)
                break
            except TermDuplicityError as termerr:
                print(termerr)

        print(f'The definition of the card:\n')
        while True:
            definition = input()
            try:
                if definition in (value.back for value in Card.deck.values()):
                    raise DefDuplicityError(definition)
                break
            except DefDuplicityError as deferr:
                print(deferr)
        Card.deck[term] = definition

    def remove_card(self):
        pass

    def import_card(self):
        pass

    def export_card(self):
        pass

    def ask_card(self):
        for _ in range(int(input('How many times to ask:\n'))):
            answer = input(f'Print the definition of "{self.front}":\n')
            if answer == self.back:
                print('Correct')
            elif answer != self.back and answer in [Card.deck[j].back for j in Card.deck.keys()]:
                print(f'Wrong.The right answer is "{self.back}", but your definition is correct ' \
                      f'for "{Card.get_correct_term(answer)}".')
            else:
                print(f'Wrong. The right answer is "{self.back}"')

    @staticmethod
    def exit_program():
        exit()

    @staticmethod
    def get_correct_term(unknown_definition):
        for j in Card.deck.keys():
            if unknown_definition == Card.deck[j].back:
                return Card.deck[j].front
        return 'Unknown'

    commands = {'add': add_card, 'remove': remove_card, 'import': import_card, 'export': export_card,
                'ask': ask_card, 'exit': exit_program, }

    @staticmethod
    def card_main(name):
        Card.commands.get(name, lambda: 'Invalid')()


if __name__ == '__main__':
    # card_count = int(input('Input the number of cards:\n'))
    while True:
        action = input('Input the action (add, remove, import, export, ask, exit):\n')
        Card.commands[action]()
