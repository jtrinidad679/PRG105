

def main():
    user_name = input("Please enter your name in the format First Middle Last: ")
    name_list = user_name.split()
    print(name_list)
    new = []
    for name in name_list:
        n = (name[0].upper() + ". ")
        print(n)
        new.append(n)

    print(new)


main()
