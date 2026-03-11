# Conditional statements are used to make decisions in a program.
'''
Types of Conditional Statements
1) if
2) if-else
3) if-elif-else
4) Nested if
'''

# 1) if
'''if condition:
    statement'''

age = 18

if age >= 18:
    print("You can vote")
print("\n")
   

# 2) if-else
'''if condition:
    statement
else:
    statement'''

age = 16

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
print("\n")


# 3) if-elif-else
# Used when multiple conditions are checked.
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
print("\n")


# 4) Nested if statements
# An if inside another if.
'''if condition1:
    if condition2:
        if condition3:
            print("All conditions are true!")'''

a = 10

if a > 5:
    print("a is greater than 5")
    if a > 8:
        print("a is also greater than 8")
        if a > 9:
            print("a is also greater than 9")
