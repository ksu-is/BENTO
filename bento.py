import json
import pandas

def load_data():
    # load subbox data from JSON file
    with open("subbox_data.json") as f:
        subbox_data = json.loads(f.read())

    # create items, store them in list
    subboxes_in_db = []
    for subbox in subbox_data:
        tag, title, ingredients = (
            subbox["tag"],
            subbox["title"],
            subbox["ingredients"],
        )

        db_subbox = subbox.create_subbox(tag, title, ingredients)
        subboxes_in_db.append(db_subbox)
load_data()

categories = ["carb", "protein", "fruit", "raw veggie", "itamemono", "tsukemono", "agemono", "yakimono", "norimaki"]
def options():
    subbox.query.get(tag)
# return every item name in json list with corresponding tag
info = # return rest of information from item name in list

count = int(input ("Hello! To begin creating your bento enter how many containers are in your box: "))
# enter number of containers
containers = []
index = (count -1)

while count > 0:
    print("Each container can be filled by one of the following categories.\n", categories)
    response = input("Enter category for a list of options.\n")
    
    while response != "go back":
        
        print(options(response))
        # search list for tag and print results
        
        response = input("Enter option for more information or 'go back'.\n")
        while response != "return":
            print(info(response))
            response = input("Enter 'return' to go back:")
    
    selection = input("Enter selection for container",count)
    containers.insert(index, selection)
    # selection is inserted into list at the current box 
    count -= 1
  
