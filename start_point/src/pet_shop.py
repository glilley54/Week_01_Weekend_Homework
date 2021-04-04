# WRITE YOUR FUNCTIONS HERE
# STARTING WITH WHAT WE HAVE:
#WE HAVE SEPERATES LISTS 
#FIRST IS A LIST OF DICTIONARIES CALLED CUSTOMERS AND HAS 3 DICTIONARIES INSITE IT
#SECOND - WE HAVE SEPERATE DICTIONARY CALLED NEW_PET
#THIRD - WE HAVE DICTIONARY CONTAINING LISTS CALL CC_PET_SHOP 


#FUNCTION 1:

#def test_pet_shop_name(self):
        #name = get_pet_shop_name(self.cc_pet_shop)
        #self.assertEqual("Camelot of Pets", name)

        #OUR FUNCTION:
#1 FUNCTION NAME IS pet_shop_name so we need to define function called this.
#2we need get pet shop name so search lists 
#we need to retun the pet shop name Camelot of Pets  

def get_pet_shop_name(pet_shop):
    print(pet_shop["name"])
    return(pet_shop["name"])

#Function 2:

#def test_total_cash(self):
        #sum = get_total_cash(self.cc_pet_shop)
        #self.assertEqual(1000, sum)

def get_total_cash(pet_shop):
    print(pet_shop["admin"]["total_cash"])
    return(pet_shop["admin"]["total_cash"])

#FUNCTION 3: 

#def test_add_or_remove_cash__add(self):
       # add_or_remove_cash(self.cc_pet_shop,10)
        #cash = get_total_cash(self.cc_pet_shop)
        #self.assertEqual(1010, cash)

def add_or_remove_cash(pet_shop,addional_cash):
    pet_shop["admin"]["total_cash"] += addional_cash

    #FUNCTION 4 = function 3 will pass this test

#function 5

#def test_pets_sold(self):
        #sold = get_pets_sold(self.cc_pet_shop)
        #self.assertEqual(0, sold)

def get_pets_sold(pet_shop):
    return(pet_shop["admin"]["pets_sold"])

#function 6

#def test_increase_pets_sold(self):
        #increase_pets_sold(self.cc_pet_shop,2)
        #sold = get_pets_sold(self.cc_pet_shop)
        #self.assertEqual(2, sold)

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

#function 7

#def test_stock_count(self):
        #count = get_stock_count(self.cc_pet_shop)
        #self.assertEqual(6, count)

def get_stock_count(pet_shop):
    count = len(pet_shop["pets"])
    return count

#function 8

#def test_all_pets_by_breed__found(self):
        #pets = get_pets_by_breed(self.cc_pet_shop, "British Shorthair")
        #self.assertEqual(2, len(pets))



def get_pets_by_breed(pet_shop, breed):
    number_to_find = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            number_to_find.append(breed)
    return number_to_find


#Function 9


#function 10

   #def test_find_pet_by_name__returns_pet(self):
        #pet = find_pet_by_name(self.cc_pet_shop, "Arthur")
        #self.assertEqual("Arthur", pet["name"])

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

#function remove pet name

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet ["name"] == name:
            pet_shop["pets"].remove(pet)

            

    