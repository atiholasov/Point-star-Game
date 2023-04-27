import Cell_class as Cell


class Out_of_field_coordinates(Exception):
    pass
class None_brothers_in_area(Exception):
    pass
class Some_brothers_in_area(Exception):
    pass
class Winner(Exception):
    pass


class Map:
    def __init__(self):
        self.size = ()
        self.grid = []

    def creating_empty_map(self):
        while type(self.size) != list:
            print("Введите координаты поля со значениями от 2 до 100 в фомате: x y")
            try:
                SIZE = input().split()
                self.size = [int(SIZE[1]), int(SIZE[0])]
                if (not 2 <= self.size[0] <= 100) or (not 2 <= self.size[1] <= 100):
                    print("Значения размеров должны быть в диапазоне от 2 до 100")
                    self.size = ()
            except (ValueError, IndexError):
                print("Следуйте формату ввода: x y")

        self.grid = [[] for i in range(self.size[0])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.grid[i].append(Cell.Cell())

    def print_map(self):
        for i in range(self.size[0]-1, -1, -1):
            print(self.grid[i])

    @staticmethod
    def check_coordinates(coordinates_x, coordinates_y):
        if int(coordinates_x) <= 0 or int(coordinates_y) <= 0:
            raise Out_of_field_coordinates("NotLiquid numbers")

    def player_turn(self, coordinates_x, coordinates_y, player_number):
        write_y_coordinate = int(coordinates_y) - 1
        write_x_coordinate = int(coordinates_x) - 1
        if player_number == 0:
            self.grid[write_y_coordinate][write_x_coordinate].star_choice()
        else:
            self.grid[write_y_coordinate][write_x_coordinate].point_choice()

    def zone_check(self, coordinates_x, coordinates_y, player_number, win_seq_size, PLAYERS_DICT):
        y = int(coordinates_y) - 1
        x = int(coordinates_x) - 1
        surrounding_area = [(y+1,x), (y+1,x+1), (y,x+1),(y-1,x+1),(y-1,x),(y-1,x-1),(y,x-1),(y+1,x-1)]
        subsequence_numbers = 1
        while subsequence_numbers != win_seq_size:
            for coordinates in surrounding_area:
                try:
                    if self.grid[coordinates[0]][coordinates[1]] == PLAYERS_DICT[player_number]:
                        subsequence_numbers += 1
                except IndexError:
                    pass
            if subsequence_numbers == 1:
                raise None_brothers_in_area("")
            elif 1 < subsequence_numbers < win_seq_size:
                raise Some_brothers_in_area("")
            else:
                raise Winner("")


