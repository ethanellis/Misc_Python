while True:
    number = [int(x) for x in list(input('input number: '))]
    count = 0
    z = True

    def multiply(n):
        product = 1
        for x in n:
            product *= x
        return product

    while z == True:
        r = multiply(number)
        new_number = str(r)
        if len(new_number) != 1:
            count += 1
            number = [int(x) for x in list(str(r))]
        else:
            z = False
            count += 1
            print(f'persistence is {count}')
            
