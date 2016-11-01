class Menu(object):
    def __init__(self, menu, func):
        assert(len(menu)==len(func))
        self.__menu = menu
        self.__func = func

    def choice(self):
        for content in enumerate(self.__menu, start=1):
            print("%d. %s" % content)
        while True:
            try:
                choice = int(input("Enter a number:")) - 1
                if choice not in range(len(self.__menu)):
                    print("Invalid Choice!")
                    continue
                print()
                return choice
            except:
                print("Invalid Choice!")

    def display(self):
        self.__func[self.choice()]()
