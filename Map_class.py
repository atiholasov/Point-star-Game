import Cell_class as Cell


class Out_of_field_coordinates(Exception):
    pass


class Map:
    def __init__(self):
        self.size = ()
        self.grid = []

    def creating_empty_map(self):

        while type(self.size) != list:
            print("Введите координаты поля в фомате: x y")
            try:
                SIZE = input().split()
                self.size = [int(SIZE[1]), int(SIZE[0])]
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
        if player_number == 0:              # Ходит первый игрок x
            self.grid[write_y_coordinate][write_x_coordinate].star_choice()
        else:                               # Ходит второй игрок .
            self.grid[write_y_coordinate][write_x_coordinate].point_choice()

    def zone_check(self):
        pass
