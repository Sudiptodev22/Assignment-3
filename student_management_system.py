class Student:
    """Base class for all students."""

    def __init__(self, name, student_id, email, age, department):
        self.name = name
        self.student_id = student_id
        self.__email = email  # Private attribute (encapsulation)
        self.age = age
        self.department = department
        self.__marks = []

    # Getter and setter methods provide controlled access to private email.
    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" not in new_email:
            raise ValueError("Please enter a valid email address.")
        self.__email = new_email

    def add_marks(self, *marks):
        """Add one or more marks (variable number of arguments)."""
        for mark in marks:
            if not isinstance(mark, (int, float)) or not 0 <= mark <= 100:
                raise ValueError("Each mark must be a number between 0 and 100.")
            self.__marks.append(mark)

    def calculate_result(self, *marks):
        """
        Calculate the average result.
        Pass marks directly, or call without arguments to use marks
        previously added with add_marks().
        """
        selected_marks = list(marks) if marks else self.__marks

        if not selected_marks:
            return "No marks available"

        average = sum(selected_marks) / len(selected_marks)

        if average >= 80:
            grade = "A+"
        elif average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "A-"
        elif average >= 50:
            grade = "B"
        elif average >= 40:
            grade = "C"
        elif average >= 33:
            grade = "D"
        else:
            grade = "F"

        return f"Average: {average:.2f}, Grade: {grade}"

    def get_student_type(self):
        return "General Student"

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Student Type: {self.get_student_type()}")
        print(f"Result: {self.calculate_result()}")


class UndergraduateStudent(Student):
    """Represents an undergraduate student."""

    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester

    # Method overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


class GraduateStudent(Student):
    """Represents a graduate student."""

    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    # Method overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")


def main():
    # Creating objects from the classes
    undergraduate = UndergraduateStudent(
        "Rahim", "UG101", "rahim@example.com", 20, "CSE", "4th"
    )
    graduate = GraduateStudent(
        "Karim", "GR201", "karim@example.com", 25, "CSE",
        "Artificial Intelligence in Healthcare"
    )

    # Add marks using *args (method overloading-style flexibility)
    undergraduate.add_marks(85, 78, 92)
    graduate.add_marks(90, 88, 95)

    # Polymorphism: the same methods behave differently for each object.
    students = [undergraduate, graduate]
    for student in students:
        student.display_info()

    # Demonstrate encapsulation through the public getter/setter.
    print("\n--- Encapsulation Demo ---")
    print("Undergraduate email:", undergraduate.get_email())
    undergraduate.set_email("rahim.new@example.com")
    print("Updated email:", undergraduate.get_email())

    # Demonstrate flexible calculate_result():
    print("\nResult using marks passed directly:",
          undergraduate.calculate_result(70, 80, 90))


if __name__ == "__main__":
    main()
