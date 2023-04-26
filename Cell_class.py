class RechoiceError(Exception):
    pass


class Cell:
    def __init__(self):
        self.status = "."

    def point_choice(self, ):

        if self.status == ".":
            self.status = "0"
        else:
            raise RechoiceError("")

    def star_choice(self):
        if self.status == ".":
            self.status = "X"
        else:
            raise RechoiceError("")

    def __repr__(self):
        return self.status
