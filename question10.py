try:
    with open("numbers.txt", "r") as file:
        numbers = [int(x) for x in file.read().split()]

        total = sum(numbers)
        average = total / len(numbers)

        print("Total =", total)
        print("Average =", average)

except FileNotFoundError:
    print("File does not exist.")
