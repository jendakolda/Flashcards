class Card:
    def __init__(self, front, back, answer):
        self.front = front
        self.back = back
        self.answer = answer

    def main(self):
        print('Your answer is right!' if self.back == self.answer else 'Your answer is wrong...')


if __name__ == '__main__':
    example = Card(input(), input(), input())
    example.main()
