Contacts = {
    "Mohamed" : "0545879632"
}
Person = input("Enter a name .\nThe name : ").strip().capitalize()
if Person in Contacts:
    print("The person exists.")
    while True:
        try:
            Decision_1 = input("Do you want to append a new contact?\nEnter yes or no.\nThe answer: ").strip().capitalize()
            if Decision_1 not in ["Yes", "No"]:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
            
            if Decision_1 == "Yes":
                name = input("Enter the name of person : ").strip().capitalize()
                if not name.isalpha() :
                    raise ValueError("The name should contain only letters . Please Enter a valid name .")
                if name in Contacts :
                    raise ValueError(f"The name {name} already exists . Please enter a different name .")
                number = input("Enter the numberphone : ")
                Contacts[name] = number
                continue  

            elif Decision_1 == "No":
                break

        except ValueError as e:
            print(e)
else :
    print("The person doesn't exist")
    while True :
        try :
            Decision_2 = input("Do you want to append a new contact ?\nEnter yes or no .\nThe answer : ").strip().capitalize()
            if Decision_2 not in ["Yes", "No"] :
                raise ValueError("Invalid input, please enter yes or no .")
            if Decision_2 == "Yes" :
                name = input("Enter the name of person : ").strip().capitalize()
                if not name.isalpha() :
                    raise ValueError("The name should contain only letters . Please Enter a valid name .")
                if name in Contacts :
                    raise ValueError(f"The name {name} already exists . Please enter a different name .")
                number = input("Entrez le numéro de téléphone : ")
                Contacts[name] = number
                continue 
            elif Decision_2 == "No" :
                break
        except ValueError as e :
            print(e)

print(Contacts)

























































# my_dict = {'fruits': ['apple', 'banana']}
#  my_dict.setdefault('fruits', []).append('orange')  # Adds 'orange' to the list under 'fruits' key
#  my_dict.setdefault('vegetables', []).append('carrot')  # Creates 'vegetables' key and adds 'carrot'
# print(my_dict)
