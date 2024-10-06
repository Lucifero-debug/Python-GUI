import random

move=['Rock','Paper','Scissor']

def main():
    choice=int(input("Enter Your Move = Rock, Paper, Scissor:\n"))
    num=random.randint(0,2)
    match choice:
        case 1:
            print(f"User Choice: {move[0]} and Computer Choice: {move[num]}")
        case 2:
             print(f"User Choice: {move[1]} and Computer Choice: {move[num]}")
        case 3:
             print(f"User Choice: {move[2]} and Computer Choice: {move[num]}")
        case _:
            print("Invalid choice")
            # user:-rock com:-paper c win
    if(choice==1 and num==1):  
        print("Computer Wins")
        # user:-scissor com:-paper u win
    elif(num==1 and choice==3):
        print("User Wins")
        # user:-paper com:-rock u win
    elif(num==0 and choice==2):
        print("User Wins")
        # user:-rock com:-scissor u win
    elif(num==2 and choice==1):
        print("User Wins")
        # user:-paper com:-scissor c win
    elif(num==2 and choice==2):
        print("Computer Wins")
        # user:-paper  com:-rock c win
    elif(num==0 and choice==3):
        print("Computer Wins")
    elif((choice-1)==num):
        print("Match Tied")

if __name__=="__main__":
    main()
