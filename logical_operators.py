# AND
# If age is between 20 and 33 
#     You are a young man
# Otherwise
#     Not eligible

# OR
# If age is less than 18 or more than 60
#     You aren't eligible to work
# Otherwise
#     Please forward your CV    

# NOT

age = 60

if age > 19 and age < 34:
    print("you are a young man")
else:
    print("not eligible")


if not age < 18 or not age > 60:
    print("you aren't eligible to work")
else:
    print("foward you CV")


if not age > 60:
    print("foward you CV")


And  - both conditions true
OR  -  need at least one true