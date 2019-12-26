print("今有一物，不知其数，三三剩二，五五剩三，七七剩二，数为几何？")

for number in range(0, 300):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
        print(number)
