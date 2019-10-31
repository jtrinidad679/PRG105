import office_furniture
import desk_furniture


def main():
    chair = office_furniture.OfficeFurniture('Chair', 'Oak Wood', '25 inches', '40 inches', '25 inches', '$89.99')
    print(chair)


main()


def main2():
    desk = desk_furniture.Desk('Desk', 'Oak Wood', '60 inches', '30 inches', '24 inches', '$299.99', 'Right and Left', '4')
    print(desk)


main2()
