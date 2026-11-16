numbers = [2, 4, 5, 2, 8, 4, 2, 9, 4, 4]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print("Frequency:", frequency)
print("Most frequent number:", most_frequent)
print("Occurrences:", frequency[most_frequent])