
while True:

    try:

        x = float(input("frist_number: "))

        y = float(input("second_number: "))

        op = input("operation:")

        output = 0
        if op == "+" :
            output = x + y
        elif op == "-":
            output = x - y
        elif op == "*":
            output = x * y
        elif op == "/":
            if y==0 :
                print("y can not be zero")
                continue 
            else:
                output = x / y
        else:
            print("Not valid")
            continue
        

        print(f"output:{output}")

 
    
    except ValueError:
        print("Input is not Valid")
        continue
    