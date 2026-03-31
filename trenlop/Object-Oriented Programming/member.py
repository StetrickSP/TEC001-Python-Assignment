class Member:
    def __init__(self, name):
        self.name = name
    
    def greet(self): print("Hello, my name is", self.name)
    

class Student(Member):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def greet(self):
        fname, maj = self.name, self.major
        print(f"Hello my name is {fname} and I am a {maj} student.")

mem1 = Member("Tai")
student1 = Student("Khai", "Semiconductor")
student1.greet()