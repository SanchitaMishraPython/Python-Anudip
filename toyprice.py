def compute_discount():
    print("1.Battery based Toys")
    print("2.Key based Toys")
    print("3.Electric charging based Toys")
    opt = int(input("Enter the product code (1,2 or 3)?:"))
    amt = int(input("Enter the amount:"))
    if opt==1:
        if amt>1000:
            dis = amt * 0.1
        else:
            dis = 0
    elif opt==2:
        if amt>100:
            dis = amt * 0.05
        else:
            dis=0
    elif opt==3:
        if amt>500:
            dis = amt*0.1
        else:
            dis = 0
    else:
        print("Product is not available")
    bill_amt= amt - dis
    print("Customer has to pay:",bill_amt)
compute_discount()