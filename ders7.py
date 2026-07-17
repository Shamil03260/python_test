i = 0

number = int(input("Number: "))
if number > 10 or number == 0:
    print("Error")
    
else:
    while i < 10:
        i += 1
        answer = number * i 
        print(number, "x", i, "=", answer)