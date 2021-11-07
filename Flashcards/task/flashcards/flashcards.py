class TermDuplicityError(Exception):
    def __init__(self, duplicate_term):
        self.message = f'The term "{duplicate_term}" already exists. Try again:\n'
        super().__init__(self.message)


class DefDuplicityError(Exception):
    def __init__(self, duplicate_def):
        self.message = f'The definition "{duplicate_def}" already exists. Try again:\n'
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
        # msg = [, f'The definition for card #{i + 1}:\n']
        print(f'Term for card #{i + 1}:\n')
        while True:
            term = input()
            try:
                if term in (value.front for value in deck.values()):
                    raise TermDuplicityError(term)

                if definition in (value.back for value in deck.values()):
                    raise DefDuplicityError
                deck[str(i)] = Card(term, definition)
                break
            except TermDuplicityError(term):
                msg[0] = f'The term "{term}" already exists. Try again:\n'
            except DefDuplicityError:
                print('dupladef')

    print([value.front for value in deck.values()])
    for value in deck.values():
        value.card_check()
