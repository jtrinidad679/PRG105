class OfficeFurniture:
    def __init__(self, category, material, length, height, width, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__height = height
        self.__width = width
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_height(self, height):
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def set_price(self, price):
        self.__price = price

    def get_category(self, category):
        self.__category = category

    def get_material(self, material):
        self.__material = material

    def get_length(self, length):
        self.__length = length

    def get_height(self, height):
        self.__height = height

    def get_width(self, width):
        self.__width = width

    def get_price(self, price):
        self.__price = price

    def __str__(self):
        return "\nCategory: " + self.__category + \
               "\nMaterial: " + self.__material + \
               "\nLength: " + self.__length + "\nHeight: " + self.__height + \
               "\nWidth: " + self.__width + "\nPrice: " + self.__price
