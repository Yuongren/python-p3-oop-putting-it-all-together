class Shoe:
    def __init__(self, brand, size):
        self.brand = brand  
        self.size = size  
        self.condition = "New"  

    @property
    def brand(self):
        """The brand property."""
        return self._brand 

    @brand.setter
    def brand(self, value):
        """Setter for the brand."""
        self._brand = value

    @property
    def size(self):
        """The size property."""
        return self._size  
    
    @size.setter
    def size(self, value):
        """Setter for the size. Ensures size is an integer."""
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        """Repairs the shoe and sets its condition to 'New'."""
        self.condition = "New"
        print("Your shoe is as good as new!")