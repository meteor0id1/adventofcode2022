table = list.split("\n")

totals = [0]
row = 0

for value in table:
    if value != "":
        totals[row] = totals[row] + int(value)
    else:
        row += 1
        totals.append(0)

max = 0
max2 = 0
max3 = 0

for total in totals:
    if total > max:
        max3 = max2
        max2 = max
        max = total


print(max+max2+max3)
