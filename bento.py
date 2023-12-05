import json
import pandas

categories = ["carb", "protein", "fruit", "raw veggie", "itamemono", "tsukemono", "agemono", "yakimono", "norimaki"]

data = pandas.read_json("subbox_data.json", orient="records")

def options(tag):
    return data[data.tag==tag]
# return every item name in json list with corresponding tag

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
       # while response != "return":
          #  print(info(response))
            #response = input("Enter 'return' to go back:")
    
    selection = input("Enter selection for container",count)
    containers.insert(index, selection)
    # selection is inserted into list at the current box 
    count -= 1
