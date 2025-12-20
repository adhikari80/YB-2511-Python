
# Base Class-
class Person:
    """
    Person is the base class.
    """

    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}"



# Student Class (inherits from Person)

class Student(Person):
    """
    Student class inherits from Person.
    """

    def __init__(self, student_id, name):
        # Call the parent (Person) constructor
        super().__init__(student_id, name)
        self.student_id = student_id

    def display_info(self):
        return f"Student ID: {self.student_id}, Name: {self.name}"



# Staff Class (inherits from Person)

class Staff(Person):
    """
    Staff class inherits from Person.
    """

    def __init__(self, staff_id, name, tax_num):
        # Call the parent (Person) constructor
        super().__init__(staff_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}, Tax No: {self.tax_num}"


# General Staff Class (inherits from Staff)

class General(Staff):
    """
    General staff inherits from Staff.
    """

    def __init__(self, staff_id, name, tax_num, rate_of_pay):
        # Call Staff constructor
        super().__init__(staff_id, name, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_info(self):
        return (
            f"General Staff ID: {self.staff_id}, "
            f"Name: {self.name}, "
            f"Tax No: {self.tax_num}, "
            f"Rate of Pay: {self.rate_of_pay}"
        )



# Academic Staff Class (inherits from Staff)
class Academic(Staff):
    """
    Academic staff inherits from Staff.
    """

    def __init__(self, staff_id, name, tax_num, publications):
        # Call Staff constructor
        super().__init__(staff_id, name, tax_num)
        self.publications = publications

    def display_info(self):
        return (
            f"Academic Staff ID: {self.staff_id}, "
            f"Name: {self.name}, "
            f"Tax No: {self.tax_num}, "
            f"Publications: {self.publications}"
        )


# Main Program (Demonstration)

if __name__ == "__main__":
    # Create objects of each class
    student = Student(101, "Bhaskar")
    general_staff = General(201, "Ram", "TX123", 40.5)
    academic_staff = Academic(301, "Sita", "TX999", 12)

    # Display information
    print(student.display_info())
    print(general_staff.display_info())
    print(academic_staff.display_info())
