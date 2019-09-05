def fun1():
    print("今有一物，不知其数，三三剩二，五五剩三，七七剩二，数为几何？")

    none = True
    number = 0

    while none:
        number += 1

        if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
            print("这个数是：" + str(number))

            none = False

    pass


def fun2():
    print("今有一物，不知其数，三三剩二，五五剩三，七七剩二，数为几何？")

    none = True
    number = 0

    while none:
        number += 1

        if number % 3 == 2:
            if number % 5 == 3:
                if number % 7 == 2:
                    print(number)

                    none = False
                else:
                    continue
            else:
                continue
        else:
            continue

    pass


if __name__ == "__main__":
    fun2()

    pass
