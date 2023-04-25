class Cell:

    def __init__(self):
        self.status = 0

    def point_choice(self):
        self.status = "."

    def star_choice(self):
        self.status = "X"

    def __repr__(self):
        return f"{self.status}"


move = 0
SIZE_OF_MAP = 0
PLAYERS_DICT = {0: "X",
                1: "."}

while type(SIZE_OF_MAP) != list:
    print("Введите координаты поля в фомате: x y")
    try:
        SIZE = input().split()
        SIZE_OF_MAP = [int(SIZE[1]), int(SIZE[0])]
    except (ValueError, IndexError):
        print("Следуйте формату ввода: x y")

Map = [[] for i in range(SIZE_OF_MAP[0])]
for i in range(SIZE_OF_MAP[0]):
    for j in range(SIZE_OF_MAP[1]):
        Map[i].append(Cell())

while True:

    for i in range(len(Map)):  # Отрисовка карты
        print(Map[i])

    now_move = move % 2

    print(f"Игрок {now_move+1} введите координыты {PLAYERS_DICT[now_move]} в формате: x y")

    try:
        coordinates = str(input())
        print(coordinates)
        coordinates_x, coordinates_y = coordinates.split(" ")

        try:
            if now_move == 0:                                                                    # Ходит первый игрок x
                Map[SIZE_OF_MAP[1] - int(coordinates_y)][int(coordinates_x) - 1].star_choice()
            else:                                                                                # Ходит второй игрок .
                Map[SIZE_OF_MAP[1] - int(coordinates_y)][int(coordinates_x) - 1].point_choice()
        except IndexError:
            print("Введенные значения вне игравого поля")
            move -= 1

    except ValueError:
        print("Следуйте формату ввода: x y")
        move -= 1

    move += 1
