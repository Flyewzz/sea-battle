class Field:
    def __init__(self):
        self.field_size = 10
        self.ships = []
        
    
    def create_field(self):
        field = self.field_size * [self.field_size * [None]]
        return field
