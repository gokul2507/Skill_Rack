name = input().strip()
age = int(input().strip())
try:
    if len(name) > 20:
        raise MaximumLengthExceededException("name cannot contain more than 20 characters")
    if age <= 0:
        raise NegativeValueException("age cannot be negative or zero")
    print(name, age)
except (MaximumLengthExceededException, NegativeValueException) as e:
    print(e)
