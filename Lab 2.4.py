# Student ID: 1201201176
# Student Name: Tong Chen Xiang

BP=1.50
GP=5.60

print("Invoice for Fruits Purchase\n---------------------------------")

banana_qty=int(input("\nEnter the quantity (comb) of bananas bought: "))
grape_qty=int(input("Enter the amount (kg) of grapes bought: "))

banana_total=BP*banana_qty
grape_total=GP*grape_qty;

total=banana_total + grape_total

print("\nItem\t\tQty\tPrice\tTotal")
print("Banana (combs)\t{}\tRM{:.2f}\tRM{:.2f}".format(banana_qty, BP, banana_total))
print("Grape (kg)\t{}\tRM{:.2f}\tRM{:.2f}".format(grape_qty, GP, grape_total))

print("\nTotal: RM {:.2f}".format(total))

