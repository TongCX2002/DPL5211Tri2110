# Student ID: 1201201176
# Student Name: Tong Chen Xiang

def cm_to_meter(cm):
    meter = cm/100
    return meter;

def get_cm():
    cm = float(input("\nEnter centimeter: "))
    m = cm_to_meter(cm)
    print("\n{:.2f} centimeters equals to {:.2f} meters".format(cm, m))

def meter_to_cm(meter):
    cm = meter*100;
    return cm;

def get_meter():
    meter = float(input("\nEnter meter: "))
    cm = meter_to_cm(meter)
    print("\n{:.2f} meters equals to {:.2f} centimeters".format(meter, cm))

def main():
    print("======================================")
    print("            MENU                    ")
    print("======================================")
    print("1.    Convert centimeter to meter")
    print("2.    Convert meter to centimeter")
    print("======================================")
    
    choice=input("\nEnter your choice: ")

    if(choice=="1"):
        get_cm()

    else:
        get_meter()

if __name__ == "__main__":
    main()