import random


class UniqueNumbers:
    number_list = [i for i in range(1, 91)]

    def get_new_number(self):
        number = random.sample(self.number_list, 1)[0]
        self.number_list.remove(number)
        return number


class LotoCard:
    nrange = ((1, 9), (10, 19), (20, 29), (30, 39), (40, 49),
              (50, 59), (60, 69), (70, 79), (80, 90))

    def __init__(self):
        self.card = [['' for _ in range(9)] for _ in range(3)]

        # Заполняем карточку числами в правильном порядке
        for column in range(9):
            numlist = random.sample(range(self.nrange[column][0],
                                          self.nrange[column][1]), 3)
            for row in range(3):
                self.card[row][column] = numlist[row]

        for row in range(3):
            for column in random.sample(range(0, 9), 4):
                self.card[row][column] = "_"

    def __str__(self):
        card_for_print = [['  ' for _ in range(9)] for _ in range(3)]
        output = ""
        for row in range(3):
            for column in range(9):
                card_for_print[row][column] = str(self.card[row][column])
                if column != 0 and card_for_print[row][column] == "_":
                    card_for_print[row][column] = "__"
                if column != 0 and card_for_print[row][column] == "X":
                    card_for_print[row][column] = "XX"
            output += " ".join(card_for_print[row]) + '\n'
        return output

    def check_num(self, num):
        for row in range(3):
            for column in range(9):
                if num == self.card[row][column]:
                    self.card[row][column] = "X"
                    return True
        return False

    def check_available_num(self):
        for row in range(3):
            for column in range(9):
                if isinstance(self.card[row][column], int):
                    return True
        return False


class Game:
    def __init__(self, hard_mode=True, auto_mode=False):
        self.user_card = LotoCard()
        self.computer_card = LotoCard()
        self.random_number = UniqueNumbers()
        self.hard_mode = hard_mode
        self.auto_mode = auto_mode

    def game(self):
        print(f"Карточка противника \n{self.computer_card}")
        print(f"Карточка игрока \n{self.user_card}")
        while (self.computer_card.check_available_num()
               and self.user_card.check_available_num()):
            try:
                self.step()
            except ValueError:
                break
        else:
            if not (self.user_card.check_available_num()
                    or self.computer_card.check_available_num()):
                print("Закончили одновременно")
                print("Игрок:")
                print(self.user_card)
                print("Компьютер:")
                print(self.computer_card)
            elif self.user_card.check_available_num():
                print("Победил компьютер. Вам осталось:")
                print(self.user_card)
            elif self.computer_card.check_available_num():
                print("Победил игрок. Компьютеру осталось:")
                print(self.computer_card)

    def step(self):
        number = self.random_number.get_new_number()
        if not self.auto_mode:
            print(f'Число - {number}. Есть такая? "y/n"')
            user_answer = input()
            card_answer = self.user_card.check_num(number)
            self.computer_card.check_num(number)
            self.check_answer(user_answer, card_answer)
        else:
            self.user_card.check_num(number)
            self.computer_card.check_num(number)

    def check_answer(self, user_answer, card_answer):
        if user_answer == "y" and card_answer is True:
            print(f"Правильно. Такое число есть\n{self.user_card}\n")
        elif user_answer == "n" and card_answer is False:
            print(f"Правильно. Такого числа нет\n{self.user_card}\n")
        elif self.hard_mode:
            print("Ошибочка")
            raise ValueError("Неправильный ответ")
        else:
            print(f"Ошибочка\n{self.user_card}\n")


if __name__ == '__main__':
    game = Game(hard_mode=False)
    game.game()
