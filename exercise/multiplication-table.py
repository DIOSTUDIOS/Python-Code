def multable():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(j) + ' x ' + str(i) + ' = ' + str(i*j) + '\t', end='')
        print('')

    pass


if __name__ == '__main__':
    multable()

    pass
