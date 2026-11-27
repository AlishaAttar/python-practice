class Student:

    def __init__(self, name, roll_no, marks):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks

    def get_details(self):
        print("Name:", self._name)
        print("Roll Number:", self._roll_no)
        print("Marks:", self._marks)

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks")


s1 = Student("Aarav", 101, 85)

s1.get_details()

s1.set_marks(95)

print("\nUpdated Details:")
s1.get_details()