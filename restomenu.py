
menu={'Burger':'Rs60','Pizza':'Rs40','Pasta':'Rs50','Cofee':'Rs80','Salad':'Rs70'}

def main():
    print("Welcome to our restaurant. Here's the menu:")
    for i,( key,value) in enumerate(menu.items(),1):
        print(key,":",value)
        total=0
    while True:
        choice=input("Enter Your Choice: ")
        match choice:
            case '1':
                total+=60
                print("Burger Has Been Successfully Added\n")
            case '2':
                total+=40
                print("Pizza Has Been Successfully Added\n")
            case '3':
                total+=50
                print("Pasta Has Been Successfully Added\n")
            case '4':
                total+=80
                print("Cofee Has Been Successfully Added\n")
            case '5':
                total+=70
                print("Salad Has Been Successfully Added\n")
            case '6':
                print("Your total bill for the order is:",total)
                print("Thankyou For Ordering Your Order Will Be Served Quickly!")
                break
        print("Your total bill is:",total)




if __name__=="__main__":
    main()