# quick component to convert degrees C to F.
# Function takes in value, does conversion and puts answer in a list


def to_f(from_c):
    fahrenheit = (from_c * 9/5) + 32
    return fahrenheit


# Main Routine
temperatures = [-40,20,50]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degree F".format(item, answer)
    converted.append(ans_statement)

print(converted)