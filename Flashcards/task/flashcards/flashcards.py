class TermDuplicityError(Exception):
    def __init__(self, duplicate_term):
        self.message = f'The term "{duplicate_term}" already exists. Try again:'
        super().__init__(self.message)


class DefDuplicityError(Exception):
    def __init__(self, duplicate_def):
        self.message = f'The definition "{duplicate_def}" already exists. Try again:'
        super().__init__(self.message)


class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def card_check(self):
        answer = input(f'Print the definition of "{self.front}":\n')
        print('Correct' if self.back == answer else f'Wrong. The right answer is "{self.back}"')


if __name__ == '__main__':
    deck = {}
    card_count = int(input('Input the number of cards:\n'))
    for i in range(card_count):
        print(f'Term for card #{i + 1}:')
        while True:
            term = input()
            try:
                if term in (value.front for value in deck.values()):
                    raise TermDuplicityError(term)
                break
            except TermDuplicityError as termerr:
                print(termerr)

        print(f'The definition for card #{i + 1}:')
        while True:
            definition = input()
            try:
                if definition in (value.back for value in deck.values()):
                    raise DefDuplicityError(definition)
                break
            except DefDuplicityError as deferr:
                print(deferr)

        deck[str(i)] = Card(term, definition)

    for value in deck.values():
        value.card_check()
