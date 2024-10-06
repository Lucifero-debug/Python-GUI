import json
# enumerate add index to any data

def load_data():
    try:
        with open('contact.txt','r') as file:
           test= json.load(file)
        #    print("this is test",type(test))
           return test
    except FileNotFoundError:
        return []
    
def save_data_helper(contacts):
    with open('contact.txt','w') as file:
        json.dump(contacts,file)

def list_all_contact(contacts):
    print('\n')
    print("*" *70)
    for index,contact in enumerate(contacts,start=1):
       print(f"{index}. {contact['Name']}, Number:{contact['Number']}, E-mail:{contact['Email']}, Age:{contact['Age']}")
    print('\n')
    print("*" *70)

def add_contact(contacts):
    name=input("Enter Name: ")
    number=input("Enter Number: ")
    email=input("Enter E-mail: ")
    age=input("Enter Age: ")
    contacts.append({"Name":name,"Number":number,"Email":email,"Age":age})
    save_data_helper(contacts)

def update_contact(contacts):
    list_all_contact(contacts)
    index=int(input("Enter the video number to update: "))
    if 1 <= index <= len(contacts):
        name=input("Enter the new Name: ")
        number=input("Enter the new number: ")
        email=input("Enter the new Email: ")
        age=input("Enter the new Age: ")
        contacts[index-1]={'Name':name,'Number':number,'Email':email,'Age':age}
        save_data_helper(contacts)
    else:
        print("Invalid index selected")

def delete_contact(contacts):
    list_all_contact(contacts)
    index=int(input("Enter the contact number to delete: "))
    if 1 <= index <= len(contacts):
        del contacts[index-1]
        save_data_helper(contacts)
    else:
        print("Invalid index selected")
def main():

    contacts=load_data()
    while True:
        print("\n Contact App | choose an option ")
        print("1. List all Contacts ")
        print("2. Add a Contact ")
        print("3. Update a Contact ")
        print("4. Delete a Contact")
        print("5 Exit the app")
        choice=input("Enter your choice:\n")
        # print(videos)
        match choice:
            case '1':
                list_all_contact(contacts)
            case '2':
                add_contact(contacts)
            case '3':
                update_contact(contacts)
            case '4':
                delete_contact(contacts)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__=="__main__":
    main()