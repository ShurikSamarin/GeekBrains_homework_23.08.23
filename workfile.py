import os
def write(text):
    with open ("data.txt", "a+", encoding="utf-8") as f:
        f.writelines(text)
        f.writelines("\n")
        print("Successfully")

def clear_all():
    with open ("data.txt", "w", encoding="utf-8") as f:
        if input("Sure? Y/N ") == 'Y':
            clear = list()
            f.writelines(clear)
        else: return    


def clear_first_name():
    with open ("data.txt", "r", encoding="utf-8") as f:
        line = f.readlines()
        del line[0]
    with open ("data.txt", "w", encoding="utf-8") as f:
        f.writelines(line)    

def clear_name(name):
    with open ("data.txt", "r", encoding="utf-8") as f:
        line = f.readlines()
        #print(name)
        #print(line)
        for i in range(len(line)):
            if name in line[i]:
                del line[i]
        #print(name)
    with open ("data.txt", "w", encoding="utf-8") as f:
        f.writelines(line) 

def edit_name(name):
    with open ("data.txt", "r", encoding="utf-8") as f:
        line = f.readlines()
        for i in range(len(line)):
            if name in line[i]:
                new_data = input("Input new data (FIO, tel) ")
                line[i] = new_data
    with open ("data.txt", "w", encoding="utf-8") as f:
        f.writelines(line)
        f.writelines("\n")
        print("Successfully")


def read_all():
    #if "data.txt".exists("data.txt"):
        with open ("data.txt", "r", encoding="utf-8") as f:
            #f.readlines()
            for line in f:
                print(line[:-1])

def get_by_name(name):
    with open ("data.txt", "r", encoding="utf-8") as f:
        flag = False
        for line in f:
            if name in line:
                print(line)
                flag = True
            #else:
        if flag == False:
            print("No item") 

def choose(choice):
    if choice == '1': return write(input("Input your data (FIO, tel) "))
    if choice == '2': return read_all()
    if choice == '3': return get_by_name(input("Input name or surname for search "))
    if choice == '4': return clear_first_name()
    if choice == '5': return clear_name(input("Input name or surname to delete "))
    if choice == '6': return edit_name(input("Input name or surname to edit "))
    if choice == '7': clear_all()

    else: exit()