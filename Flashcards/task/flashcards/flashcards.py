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

    def card_check(self):
        answer = input(f'Print the definition of "{self.front}":\n')
        if answer == self.back:
            return 'Correct'
        elif answer != self.back and answer in [Card.deck[j].back for j in Card.deck.keys()]:
            return f'Wrong.The right answer is "{self.back}", but your definition is correct ' \
                   f'for "{Card.get_correct_term(answer)}".'
        else:
            return f'Wrong. The right answer is "{self.back}"'

    @staticmethod
    def get_correct_term(unknown_definition):
        for j in Card.deck.keys():
            if unknown_definition == Card.deck[j].back:
                return Card.deck[j].front
        return 'Unknown'


if __name__ == '__main__':
    # deck = {}
    card_count = int(input('Input the number of cards:\n'))
    for i in range(card_count):
        print(f'The term for card #{i + 1}:')
        while True:
            term = input()
            try:
                if term in (value.front for value in Card.deck.values()):
                    raise TermDuplicityError(term)
                break
            except TermDuplicityError as termerr:
                print(termerr)

        print(f'The definition for card #{i + 1}:')
        while True:
            definition = input()
            try:
                if definition in (value.back for value in Card.deck.values()):
                    raise DefDuplicityError(definition)
                break
            except DefDuplicityError as deferr:
                print(deferr)

        Card.deck[str(i)] = Card(term, definition)

    for value in Card.deck.values():
        print(value.card_check())


