import Cell_class as Cell
import Map_class

move = 0
PLAYERS_DICT = {0: "X",
                1: "0"}

Map = Map_class.Map()
Map.creating_empty_map()

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
        except Cell.RechoiceError:
            print("Выберите другую точку, данная уже занята")
            move -= 1

    except ValueError:
        print("Следуйте формату ввода: x y")
        move -= 1

    move += 1
