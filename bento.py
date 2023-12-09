import json
import pandas

categories = ["carb", "protein", "fruit", "veggie", "itamemono", "tsukemono", "agemono", "yakimono", "norimaki"]

data = pandas.read_json("subbox_data.json", orient="records")

def options(tag):
    return data[data.tag==tag]
# return every item name in json list with corresponding tag

count = int(input ("Hello! To begin creating your bento enter how many containers are in your box: "))
containers = []
index =0

while index < count:
    print("Each container can be filled by one of the following categories.\n", categories)
    
    response = ""
    while response != "select":
        response = input("Enter category for a list of options.\n")
        print(options(response))
        # search list for tag and print results
        
        response = input("View categories again or enter 'select' to make a selection.\n")

    selection = ""
    while selection not in list(data.title):
        selection = input("Enter selection for container.\n")
        if(selection in list(data.title)):
            containers.insert(index, selection)
            break
        else:
            print("Enter valid selection.\n")

    # valid selection is inserted into list at the current box 
    print("Box",index+1,"is now filled with",selection,"!")
    index +=1

print("Here is your completed bento :",containers)

ingredients = []
for item in containers:
       ingredients.append(data[data.title == item].ingredients.values[0])
print("List of ingredients :",ingredients)
