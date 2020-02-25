# Display output using int / float


to_round = [1/1, 214343.3563, 1/3]
print("**** Number to round ****")
print(to_round)

print()
print("*** rounded number ***")

for item in to_round:
    if item%1 == 0:
        print("{:.0f}".format(item))
    else:
        print("{:.1f}".format(item))