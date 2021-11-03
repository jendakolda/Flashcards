class TermDuplicityError(Exception):
    pass


class DefDuplicityError(Exception):
    pass


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
        try:
            term = input(f'Term for card #{i + 1}:\n')
            definition = input(f'The definition for card #{i + 1}:\n')
            deck[str(i)] = Card(term, definition)
        except TermDuplicityError:
        except DefDuplicityError:

    for value in deck.values():
        value.card_check()
