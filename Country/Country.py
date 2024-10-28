# Victor Cruzat CIS261 Country

# Create the User Men with options
def show_menu():
    print("\nCountry Dictionary Program")
    print("1. View a country")
    print("2. Add a country")
    print("3. Delete a country")
    print("4. Exit")
    
#Create the dicitionary for the user to select from
def init_dictionary():
    countries = {
        "USA": "United States of America",
        "UK": "United Kingdoms",
        "CAN": "Canada",
    }
    return countries

#Call a function to view a country and display the country keys
def view_country(countries):
    print("\nAvailable countries: ")
    for code in countries.keys():
        print(code)
    
    key = input("\nEnter the country code to view: ").upper()
    for code in countries:
        if code == key:
           print(f"{code}: {countries[code]}")
           return
    else: 
        print("Invalid key! Country not found.")

def add_country(countries):
    #Part 3: Display all keys and prompt the user to view a country
    
    key = input("\nEnter the new country code: ").upper()
    for code in countries:
        if code == key:
            print("This key already exits. Try again.")
            return
            
    else:
        name=input("Enter the country name: ")
        countries[key] = name
        print(f"{name} has been added with code {key}.")
        
def delete_country(countries):
    #Display all country codes
    print("\nAvailable countries: ")
    for code in countries.keys():
        print (code)
        
    #Prompt user to enter the country code to delete
    key=input("\nEnter the country code to delete: ").upper()
    deleted_country = countries.pop(key)
    if deleted_country:
        print(f"{deleted_country} has been deleted from the dictionary.")
    else:
        print("Invalid key! Country not found.")
        
def main():
    countries = init_dictionary()
    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            view_country(countries)
        elif choice == '2':
            add_country(countries)
        elif choice == '3':
            delete_country(countries)
        elif choice == '4':
            print("Exiting Progam.")
            break
    else:
        print ("Invalid command! Please try again.")
            
main()


    
