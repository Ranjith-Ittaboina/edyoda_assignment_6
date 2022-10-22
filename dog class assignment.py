class dog:
    def __init__(self, name = None, age = None, coat_color = None):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("name is : ", self.name, "\n" "age is : ", self.age)

    def get_info(self):
        print("coat color is : ", self.coat_color)    
    
    
class jackRussellterrier(dog):

    def creature(self):
        print("It is a Dog")

    def type(self):
        print("Breed is : JackRussellTerrier")

class bulldog(dog):
    
    def creature(self):
        print("It is a Dog")

    def type(self):
        print("Breed is : Bulldog")

jackRussellterrier_obj = jackRussellterrier("puppy", 4, "brown")
print(jackRussellterrier_obj.description())
print(jackRussellterrier_obj.get_info())
print(jackRussellterrier_obj.creature())
print(jackRussellterrier_obj.type())

bulldog_obj = bulldog("doggy", 5, "black")
print(bulldog_obj.description())
print(bulldog_obj.get_info())
print(bulldog_obj.creature())
print(bulldog_obj.type())