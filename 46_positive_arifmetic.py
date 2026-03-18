numbers = [12, -3, 56, 89, -6, -78, 98]
pos_numbers = []
for number in numbers:
	if number >0:
		pos_numbers.append(number)
print(pos_numbers)
total_sum = 0
for pos_number in pos_numbers:
	total_sum += pos_number
print(total_sum)
orta_arif = total_sum / len(pos_numbers)
print(orta_arif)