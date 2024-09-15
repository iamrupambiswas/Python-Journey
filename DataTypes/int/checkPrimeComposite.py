n = int(input("Enter a number: "))
def check(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return "composite!"
            else:
                return "prime!"
    elif n == 1:
        return "neither prime nor composite!" 
    else:
        return "0, try with a positive number greater than 1!"
print(f"The number is {check(n)}")