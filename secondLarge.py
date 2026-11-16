numbers = [12, 45, 89, 23, 67, 89, 10]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[-2])
else:
    print("Second largest number does not exist")