from FieldElement import FieldElement

if __name__=="__main__": 
    a = FieldElement(3, 31)
    b = FieldElement(24, 31)

    # check division
    div1 = 3 * pow(24, 31 - 2, 31) % 31
    print(div1)
    div2 = (a / b).num
    print(div1 == div2)

    # check exp
    a = FieldElement(7, 13)
    b = FieldElement(8, 13)
    print(a**-3)

    print(pow(7, 3, 13)**11 % 13)