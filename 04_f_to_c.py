# quick component to convert degrees F to C.
# Function takes in value, does conversion and puts answer in a list


def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    return celsius


# Main Routine
temperatures = [-40,20,50]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degree C".format(item, answer)
    converted.append(ans_statement)

print(converted)