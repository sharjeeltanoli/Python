class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)


if __name__ == "__main__":
    student1 = Student("Sharjeel" , 85)
    student1.display()

       
    