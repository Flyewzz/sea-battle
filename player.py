from field import Field


class Player:
    def __init__(self, name, field: Field = None):
        if field is None:
            self.field = Field()
        else:
            self.field = field
        self.name = name