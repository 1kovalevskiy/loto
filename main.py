import random
import pprint

class UniqueNumbers:
    def __init__(self):
        self.number_list = [i for i in range(1, 91)]

    def get_new_number(self):
        number = random.sample(self.number_list, 1)[0]
        self.number_list.remove(number)
        return number

class LotoCard:
    nrange = ((1, 9), (10, 19), (20, 29), (30, 39), (40, 49),
              (50, 59), (60, 69), (70, 79), (80, 90))

    def __init__(self):
        self.card = [['' for i in range(9)] for i in range(3)]

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
        card_for_print = [['  ' for i in range(9)] for i in range(3)]
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


def game():
    uniq = UniqueNumbers()
    user_card = LotoCard()
    comp_card = LotoCard()
    print("Лото. Супер игра!")
    print("Стартовая карта компьютера")
    print(comp_card)
    print("Стартовая карта игрока")
    while user_card.check_available_num() and comp_card.check_available_num():
        number = uniq.get_new_number()
        print(user_card)
        # print(f"Номер {number}. Есть такой? y/n")
        # answer = input()
        comp_card.check_num(number)
        user_card_checked = user_card.check_num(number)
        # if answer == 'y' and user_card_checked:
        #     print("Правильно" + "\n\n\n")
        # elif answer == 'n' and not user_card_checked:
        #     print("Правильно" + "\n\n\n")
        # else:
        #     print("Ошибочка")
    else:
        if not (user_card.check_available_num()
                or comp_card.check_available_num()):
            print("Закончили одновременно")
            print("Игрок:")
            print(user_card)
            print("Компьютер:")
            print(comp_card)
        elif user_card.check_available_num():
            print("Победил компьютер. Вам осталось:")
            print(user_card)
        elif comp_card.check_available_num():
            print("Победил игрок. Компьютеру осталось:")
            print(comp_card)


if __name__ == '__main__':
    game()