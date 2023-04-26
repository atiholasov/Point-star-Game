import Cell_class as Cell
import Map_class


number_of_move = 0
PLAYERS_DICT = {0: "X",
                1: "0"}

Map = Map_class.Map()
Map.creating_empty_map()

while True:

    Map.print_map()

    player_number = number_of_move % 2
    print(f"Игрок {player_number+1} введите координыты {PLAYERS_DICT[player_number]} в формате: x y")

    try:
        coordinates = str(input())
        coordinates_x, coordinates_y = coordinates.split(" ")
        Map.check_coordinates(coordinates_x, coordinates_y)

        try:
            Map.player_turn(coordinates_x, coordinates_y, player_number)                       
        except IndexError:
            print("Введенные значения вне игравого поля")
            number_of_move -= 1          
        except Cell.RechoiceError:
            print("Выберите другую точку, данная уже занята")
            number_of_move -= 1

    except ValueError:
        print("Следуйте формату ввода: x y")
        number_of_move -= 1
    except Map_class.Out_of_field_coordinates:
        print("Вводите положительные координаты")
        number_of_move -= 1

    number_of_move += 1
