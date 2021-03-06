import json
path = r'Code/Desi/data/contacts.json'
#did with Lexi

def load_contacts(path):
    with open(path, 'r') as file: # open the file
        text = file.read() # read the text out of the file
    contacts = json.loads(text) # convert the text containing json into a dictionary python understands
    contacts = contacts['contacts'] # extract the list inside the dictionary
    return contacts

#write to json file
def save_contacts(path, contacts):
    contacts = {'contacts': contacts} # put the list of contacts in to a dictionary
    with open(path, 'w') as file: # open the file
        text = json.dumps(contacts, indent=4, sort_keys=True) # convert our list of python dictionaries back into json
        file.write(text) # write the json to the file

def retrieve_contacts(contacts):
    #contacts = {'contacts': contacts}
    for i in range(0, len(contacts)): #start at 0
        #if [i] == [j]:
        print(i, contacts[i]) # printing individual dictionary
        print(contacts[i]['name']) # using key to get the value of the dictionary
        print(contacts[i]['age'])
        print(contacts[i]['email'])
        print(contacts[i]['favorite color'])

while True:
    command = input("What is your command? ") # get the command from user
    if command == "create":
        #get the new contact's information from the user
        name = input("what is the contacts name? ")
        age = int(input("what is the contacts age? "))
        email = input("what is the contacts email? ")
        fav_color = input("What is the contacts favorite color? ")
        #create a new contact as a dictionary
        
contacts = {"contacts": [
        {
            "name": "joe",
            "age": 34,
            "email": "joe@gmail.com",
            "favorite color": "blue"
        },
        {
            "name": "jane", 
            "age": 43,
            "email": "jane@email.com",
            "favorite color": "green",
        },
        {
            "name": "christina",
            "age": 65,
            "email": "christina@email.com",
            "favorite color": "orange"
        }
    ]   
}

        

