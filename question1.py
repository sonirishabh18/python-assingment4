numbers = [2, 3, 4, 5, 6, 7, 11, 15, 17]

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
