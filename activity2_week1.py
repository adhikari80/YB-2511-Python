
def calculate_tax(gross_pay):

    if gross_pay <= 15600:
        tax = gross_pay * 10.5 / 100 
        # 10.5% tax for 0-15600
    elif gross_pay <= 53500:
        tax = gross_pay * 17.5 / 100  
        # 17.5% tax for 15601-53500
    elif gross_pay <= 78100:
        tax = gross_pay * 30 / 100    
        # 30% tax for 53501-78100
    elif gross_pay <= 180000:
        tax = gross_pay * 33 / 100  
        # 33% tax for 78101-180000
    else:
        tax = gross_pay * 39 / 100   

    return tax  


def main():

    #main function to get user input, calculate gross pay, tax and net pay and print results.

    # Get user input
    hours_worked=float(input("Enter the hours worked in a week:"))
    hourly_rate=float(input("Enter the hourly rate you get:"))

    #calculate gross_pay
    gross_pay= hours_worked* hourly_rate

    #calculate tax and net pay
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax

    # Print results
    print(f"Gross pay:{gross_pay}")
    print(f"Tax:{tax}")
    print(f"Net Pay:{net_pay}")
     
    input("\nPress Enter to exit...")   
if __name__ == "__main__":
    main()