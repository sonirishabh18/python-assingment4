def process_list(lst):
    even_count = 0
    odd_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_sum += num

    return even_count, odd_sum

numbers = [1, 2, 3, 4, 5, 6]
count, total = process_list(numbers)

print("Even Count =", count)
print("Odd Sum =", total)
