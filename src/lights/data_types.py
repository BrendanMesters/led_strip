
class led_section:
    def __init__(self, id, size, data, starting_point=0, priority=0):
        
        # Check that the size of data and the data variable are equal, return error if false.

        self.id = id
        self.size = size
        self.data = data
        self.start = starting_point
        self.priority = priority
        
