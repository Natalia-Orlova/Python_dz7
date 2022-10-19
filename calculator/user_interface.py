import compl as com
import model_sum as s
import model_sub as sub
import model_mult as mul
import model_div as div
import model_pow as p
import model_sqrt as sq 
import logger as log
    
def view_data(data):
    print (f"result = {data}")

def menu():
    while True:
        print(("Select numbers to work with: \n"
        "1. Complex \n2. Rational\n0. Exit\n"))
        c = input("Enter choice: ")
        if c == '0':
            break
        if c == '1':
            print("Working with complex numbers")
        elif c == '2':
            print("Working with rational numbers")
        else:
            print("Command doesn't exist") 
            continue
        
        while True:
            print("Select operation: \n"
            "1. +\n2. -\n3. *\n4. /\n"
            "5. pow\n6. sqrt\n0. previous menu\n")

            op = input("Enter number of operation: ")
            if op == '0':
                break

            if op in ('1','2','3','4','5'):
                a = com.compl() if c == '1' else float(input("Enter 1 number: "))
                b = com.compl() if c == '1' else float(input("Enter 2 number: "))

            if op == '1':
                result = s.sum(a, b)
                view_data(result)
                data = (f"sum; {a} + {b} = {result}")
                log.logger(data)

            elif op == '2':
                result = sub.sub(a, b)
                view_data(result)
                data = (f"substraction; {a} - {b} = {result}")
                log.logger(data)

            elif op == '3':
                result = mul.mult(a, b)
                view_data(result)
                data = (f"multiplication; {a} * {b} = {result}")
                log.logger(data)

            elif op == '4':
                if b !=0:
                    result = div.div(a, b)
                    view_data(result)
                    data = (f"division; {a} / {b} = {result}")
                    log.logger(data)
                else:
                    print("Can't divide by zero!\n")

            elif op == '5':
                result = p.pow(a, b)
                view_data(result)
                data = (f"exponentiation; {a} ^ {b} = {result}")
                log.logger(data)

            elif op == '6':
                a = com.compl() if c == '1' else float(input("Enter 1 number: "))
                result = sq.sqrt(a)
                view_data(result)
                data = (f"square root; {a} = {result}")
                log.logger(data)
            else:
                print("Command doesn't exist")  
    return
