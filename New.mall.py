print("-----welcom to our system------- ")

def print_name(name):
    print(f" hi {name} this system can help you to calculate the cost of your new mall in seconds!")

name =input(" ---Enter your name --- ")   
print_name(name)


def mall_place_cost(governorate_name):
    if governorate_name =="Capital Governorate" :
        return 3000
    
    elif governorate_name == "Hawalli Governorate" :
        return 2000
    
    elif governorate_name == "Mubarak Al-kabeer Governorate" :
        return 1500
    
    elif governorate_name== "Ahmadi Governorate" :
        return 1000
    
    elif governorate_name == "Farwaniya Governorate" :
        return 1300
    
    elif governorate_name == "Jahra Governorate" :
        return 850
    else:
        False

def mall_space_cost(mall_space):
    if mall_space >0 or mall_space <=500 :
        return 300
    elif mall_space >=501 or mall_space<=1000 :
        return 500
    elif mall_space >=1001 or mall_space<=2000 :
        return 700
    elif mall_space >2000 :
        return 900
     
    else:
        False

def mall_floors_cost(mall_floors):
    if mall_floors == 1 :
        return 200
    elif mall_floors == 2 :
        return 250
    elif mall_floors == 3 :
         return 300
    elif mall_floors >3 :
        return 450
    else :
        False

def mall_stores_cost(mall_stores):
    if mall_stores > 0 or mall_stores <=100 :
       return 380
    elif mall_stores >100 or mall_stores <=400 :
        return 550
    elif mall_stores >400 :
        return 770
    else:
        False

def mall_parking_cost(mall_parking):
    if mall_parking >0 or mall_parking <=100 :
        return 200
    elif mall_parking >100 or mall_parking <=500 :
        return 500
    elif mall_parking >500:
        return 850
    else:
        False

def mall_total_cost():
    governorate_name=input("Enter the governorate name :")
    mall_space=int(input("Enter the number of the mall space :"))
    mall_floors=int(input("Enter the number of the mall floors :"))
    mall_stores=int(input("Enter the number of the mall stores :"))
    mall_parking=int(input("Enter the number of the mall parking :"))
    result=mall_place_cost(governorate_name)+mall_space_cost(mall_space)+mall_floors_cost(mall_floors)+mall_stores_cost(mall_stores)+mall_parking_cost(mall_parking)
    return f"the total cost is {result}"

print(mall_total_cost())

stores_names = ["Zara" , "H&M" , "Doir" , "Hermes" , "Chanel" , "Sephora"]
stores_names.append("NYX")
print("you can chose your stores names ")
for stores_name in stores_names :
    print(stores_name)

name = input("chose your stores name :")
print("wow nice store!")

class Brand:
    # Name= "Hermes"
    # Founder ="Thierry Hermes"
    # Year = 1837
    def NeworOld (self):
        if self.Year >=2000:
           print("this brand is New :")
        else:
            print("this brand is old  ")
    def __init__(self, Name , Founder , Year)   :
        self.Name = Name 
        self.Founder = Founder
        self.Year = Year
    def __str__(self)  :
        return f" the brand is {self.Name} , and Founder by {self.Founder} in {self.Year} "    
      

brand = Brand("Hermes" ,"Thierry Hermes" , 1837)  
print(brand.Name)    
brand.NeworOld()
print(Brand("Hermes", "Thierry Hermes" , 1837))

   


         
