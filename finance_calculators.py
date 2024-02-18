#finance_calculators
#Calculation of interest on an investment, or bond repayment

#import math library
import math

#Prompt user to select Investment calculation or Bond calculation,
#Depending on the selection, either calculate future value of investment based on simple/compound interest or,
#Calculate the amount required for individual bond repayments depending on specified values

input_string = input("Please chose Investment or Bond: ")
if input_string.lower() == "investment":
    P = float(input("Please enter the initial deposit amount: "))
    r = float(input("Please enter the annual interest rate: "))/100
    t = float(input("Please enter the number of years that the money is being invested for: "))
    s_or_c = input("Please select simple or compound interest: ")
    if s_or_c.lower() == "simple":
        A = round(P*(1+r*int(t)),2)
        print(f"The future value of the investment, with simple interest at a rate of {r}, for {t} years, will be {A}")
#Conversion of interest compounded annually to a continous compound interest formula to allow for float values of t
    elif s_or_c.lower() == "compound":
        cont_r = math.log(1+r)
        A = round(P*math.exp(cont_r*t),2)
        print(f"The future value of the investment, with counpound interest at a rate of {r}, for {t} years, will be {A}")
    else:
        print("Please select simple or compound interest.")
elif input_string.lower() == "bond":
    P = float(input("Please enter the present value of the property: "))
    i = float(input("Please enter the interest rate: "))/100
    n = int(input("Please enter the time it will take for the bond to be repaid (number of months): "))
    repayment = round((i*P)/(1-(1+i)**(-n)),2)
    print(f"For the specified property, repaid over a period of {n} months, the monthly bond payment amount is {repayment}")
    
