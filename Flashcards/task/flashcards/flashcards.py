class Card:
    def __init__(self, front='Term', back='Definition'):
        self.front = front
        self.back = back

    def main(self):
        print('Card:', self.front, 'Definition:', self.back, sep='\n')


if __name__ == '__main__':
    example = Card()
    example.main()
