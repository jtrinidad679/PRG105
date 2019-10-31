import office_furniture


class Desk(office_furniture.OfficeFurniture):
    def __init__(self, category, material, length, height, width, price, location, number):
        super().__init__(category, material, length, height, width, price)
        self.__location_of_drawers = location
        self.__number_of_drawers = number

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def get_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def get_number_of_drawers(self, number_of_drawers):
        self.__number_of_drawers = number_of_drawers

    def __str__(self):
        return "\nCategory: " + self.__category + \
               "\nMaterial: " + self.__material + \
               "\nLength: " + self.__length + "\nHeight: " + self.__height + \
               "\nWidth: " + self.__width + "\nPrice: " + self.__price + \
               "\nLocation of Drawers: " + self.__location_of_drawers + "\nNumber of Drawers: " + self.__number_of_drawers
