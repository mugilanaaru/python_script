#Simple grocery list app

grocery_list= []

while True:
    print("\nOptions: add / remove / show / exit")
    action=input("Enter the option to do")

    if action=="add":
       item=input("Enter the item to add")
       grocery_list.append(item)
       print(f"{item} added")

    elif action=="remove":
         item=input("Enter the item to remove")
         if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} removed")
         else:
             print("item not found")

    elif action=="show":
        print("Your grocery list")
        for i in grocery_list:
            print("-",i)

    elif action=="exit":
        break

    else:
        print("invalid option")
    
        



