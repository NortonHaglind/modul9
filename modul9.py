


with open("test.txt" , "r") as f:
    content = f.read()
    active=True
    print(content)
    list1=[content]


while active:
    name = input("skriv nåt roligt (sluta=q)(ta bort=x) ")
    
    if name == "q":
        user_input=input("spara något? ")
        with open("test.txt", "w") as f:
            f.write(user_input)
        break
    else:
        
        list1.append(name)
        print(list1)
        print(len(list1))