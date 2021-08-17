class Field:
    FIELD_SIZE = 10
    def __init__(self):        
        self.matrix = Field.FIELD_SIZE * [Field.FIELD_SIZE * [None]]
        