while True:
    x = int(input("enter \n1 for addtion\n2 for subtraction\n3 for muliplicaion\n4 for division\n5 for power of\n6 for area of square\n7 for perimetre of square\n8 for area of rectangle\n9 for perimetre of rectangle\n10 for area of circle\n11 for circumferance of circle\n"))
    
    if x <= 0 or x >=12:
        print("this number or word doesnt exist choose from 1 to 11")
    if x == 1:
        sum1 = float(input("enter 1st number\n"))
        sum2 = float(input("enter 2nd number\n"))
        sum3 = sum1 + sum2
        print("the sum is", sum3)
    if x == 2:
        difference1 = float(input("enter 1st number\n"))
        difference2 = float(input("enter 2nd number\n"))
        difference3 = difference1 - difference2
        print("the difference is", difference3)
    if x == 3:
        product1 = float(input("enter 1st number\n"))
        product2 = float(input("enter 2nd number\n"))
        product3 = product1 * product2
        print("the product is", product3)
    if x == 4:
        qoutient1 = float(input("enter 1st number\n"))
        qoutient2 = float(input("enter 2nd number\n"))
        qoutient3 = qoutient1 / qoutient2
        print("the qoutient is", qoutient3)
    if x == 5:
        powerof1 = float(input("enter 1st number\n"))
        powerof2 = float(input("to the power of\n"))
        powerof3 = powerof1 ** powerof2
        print(powerof1 ,"to the power of", powerof2, "is", powerof3)
    if x == 6:
        areaofsquare1 = float(input("enter a side of a square\n"))
        areaofsquare3 = str(input("enter in unit measuring in\n"))
        if isinstance(areaofsquare3, str) and areaofsquare3.isdigit():
             print("units is measured not measured in numbers please enter proper units")
             areaofsquare3 = str(input("enter in unit measuring in\n"))
        areaofsquare2 = areaofsquare1 * areaofsquare1
        print("area of this particular square with side of", areaofsquare1, "is", areaofsquare2, "square", areaofsquare3)
    if x == 7:
        perimetreofsquare1 = float(input("enter a side of square\n"))
        perimetreofsquare3 = str(input("enter the unit measuring in\n"))
        if isinstance(perimetreofsquare3, str) and perimetreofsquare3.isdigit():
            print("units is measured not measured in numbers please enter proper units")
            perimetreofsquare3 = str(input("enter the unit measuring in\n"))
        perimetreofsquare2 = perimetreofsquare1 * 4
        print("perimetre of this particular square with side of", perimetreofsquare1, "is", perimetreofsquare2, perimetreofsquare3)
    if x == 8:
        areaofrectangle1 = float(input("enter the length of a rectangle\n"))
        areaofrectangle2 = float(input("enter the breath of a rectangle\n"))
        areaofrectangle4 = str(input("ente the unit measuring in\n"))
        if isinstance(areaofrectangle4, str) and areaofrectangle4.isdigit():
            print("units is measured not measured in numbers please enter proper units")
            areaofrectangle4 = str(input("ente the unit measuring in\n"))
        areaofrectangle3 = areaofrectangle1 * areaofrectangle2
        print("area of this particular rectangle with sides", areaofrectangle1, "and", areaofrectangle2, "is", areaofrectangle3, "square", areaofrectangle4)
    if x == 9:
        perimetreofrectangle1 = float(input("enter the length of a rectangle\n"))
        perimetreofrectangle2 = float(input("enter the breath of a rectangle\n"))
        perimetreofrectangle4 = str(input("enter the unit measuring in\n"))
        if isinstance(perimetreofrectangle4, str) and perimetreofrectangle4.isdigit():
            print("units is measured not measured in numbers please enter proper units")
            perimetreofrectangle4 = str(input("enter the unit measuring in\n"))
        perimetreofrectangle3 = (perimetreofrectangle1 + perimetreofrectangle2)*2.0
        print("perimetre of this particular rectangle with sides", perimetreofrectangle1, "and", perimetreofrectangle2, "is", perimetreofrectangle3, perimetreofrectangle4)
    if x == 10:
        areaofcircle1 = float(input("enter the radius of the circle\n"))
        areaofcircle3 = str(input("enter t unit measuring in\n"))
        if isinstance(areaofcircle3, str) and areaofcircle.isdigit():
            print("units is measured not measured in numbers please enter proper units")
            areaofcircle3 = str(input("enter t unit measuring in\n"))
        areaofcircle2 = 3.14159 * (areaofcircle1 * areaofcircle1)
        print("area of this particular circle with radius of", areaofcircle1, "is", areaofcircle2, "square", areaofcircle3)
    if x == 11:
        circumferanceofcircle1 = float(input("enter the radius of the circle\n"))
        circumferanceofcircle3 = str(input("enter the unit mesuring in\n"))
        if isinstance(circumferanceofcircle3, str) and circumferanceofcircle3.isdigit():
            print("units is measured not measured in numbers please enter proper units")
            circumferanceofcircle3 = str(input("enter the unit mesuring in\n"))
        circumferanceofcircle2 = 2 * (3.14159 * circumferanceofcircle1)
        print("circumferance of this particular circle with radius of", circumferanceofcircle1, "is", circumferanceofcircle2, circumferanceofcircle3)
        
    
        
