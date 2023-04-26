import Cell_class as Cell


class Map:
    def __init__(self):
        self.size = 0
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
