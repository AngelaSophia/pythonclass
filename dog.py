class Dog:
    dog="Glory"
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def barks(self):
        return f"Hello,  {self.name} barks very  loudly" 

    def change_gender(self):
        return f"Hello, {self.name} was changed to male {self.gender}"   


