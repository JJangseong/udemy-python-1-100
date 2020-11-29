

# Date Types

#String

# print("Hello"[0])


# print("123" + "346")


# print(123 + 456)

# ====================================

# num_char = len(input("What is your name?"))
# print(type(num_char))
# print("Your name has " + str(num_char) + " characters.")

# a = 123
# print(type(a))

# print(70 + float("100.5"))


# number = input("Tow Number Input Me.")

# first = int(number[0])
# second = int(number[1])

# print(first + second)

# ====================================

# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))

# bmi = weight / height ** 2

# print(bmi)

age = input("What is your current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")