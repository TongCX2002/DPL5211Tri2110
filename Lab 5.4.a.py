# Student ID: 1201201176
# Student Name: Tong Chen Xiang

def rectangle(w, l):
    area=w*l
    return area

def triangle(w, l):
    area=1/2*w*l
    return area

def main():
    length = float(input("Enter width  : "))
    width = float(input("Enter length : "))

    rect=rectangle(width, length)
    tria=triangle(width, length)

    print("\nRectangle area : {:.2f}".format(rect))
    print("Triangle area  : {:.2f}".format(tria))

if __name__ == "__main__":
    main()