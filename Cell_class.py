class RechoiceError(Exception):
    pass


class Cell:
    def __init__(self):
        self.status = "."

    def __eq__(self, other):
        if self.status == other:
            return True
        else:
            return False

    def __repr__(self):
        return self.status

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
