# Student ID: 1201201176
# Student Name: Tong Chen Xiang

def get_bonus(unit_sold, salary):
    if(unit_sold>1000):
        bonus=0.2
    else:
        bonus=0.1

    return bonus*salary

def get_nett_salary(bonus, salary):
    return bonus+salary

def display(id, salary, unit_sold, bonus, nett_salary):
    print("\n```````````````````````````````````")
    print("            SALARY SLIP            ")
    print("```````````````````````````````````")
    print("Staff ID         : {}".format(id))
    print("Staff salary     : RM {:.2f}".format(salary))
    print("Units sold       : {}".format(unit_sold))
    print("Bonus            : RM {:.2f}".format(bonus))
    print("Net Salary       : RM {:.2f}".format(nett_salary))

def main():
    print("```````````````````````````````````")
    print("            DATA ENTRY             ")
    print("```````````````````````````````````")

    id=int(input("Enter staff id         : "))
    salary=float(input("Enter staff salary      : RM "))
    unit_sold=int(input("Enter total units sold : "))

    bonus=get_bonus(unit_sold, salary)
    nett_salary=get_nett_salary(bonus, salary)
    
    display(id, salary, unit_sold, bonus, nett_salary)

if __name__ == "__main__":
    main()