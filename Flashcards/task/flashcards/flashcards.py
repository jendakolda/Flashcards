class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def main(self):
        answer = input(f'Print the definition of "{self.front}":\n')
        print('Correct' if self.back == answer else f'Wrong. The right answer is "{self.back}"')


if __name__ == '__main__':
    deck = {}
    card_count = int(input('Input the number of cards:\n'))
    for i in range(card_count):
        deck[str(i)] = Card(input(f'The term for card #{i + 1}:\n'),
                            input(f'The definition for card #{i + 1}:\n'))

    for value in deck.values():
        value.main()
