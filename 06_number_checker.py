def temp_check (question):

    error = "You need a number"

    valid = False
    while not valid:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print(error)

numl = temp_check("enter a number ")
print(numl)