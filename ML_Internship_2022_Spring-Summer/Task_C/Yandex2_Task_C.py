import statistics
fin = open('input.txt', 'r', encoding='utf8')
text_line = []
for line in fin:
    text_line.append(line)
fin.close()
numbers = []
for line in text_line[1:]:
    numbers.append(int(line))
mse = statistics.mean(numbers)
mae = statistics.median(numbers)
print(mse)
print(mae)
print(mae)