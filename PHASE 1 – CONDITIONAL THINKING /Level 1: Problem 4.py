number = float(input("Enter the number:"))

if(number%5==0 and number%3==0):
    print(f"The given {number} is divisible by both 3 & 5.")
else:
    print(f"The given {number} is not divisible by both 3 & 5.")
