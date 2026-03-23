"""
SCHOOL MANAGEMENT SYSTEM - STUDENT TEMPLATE
===========================================
Instructions: Fill in the missing code in the methods marked with TODO.
Follow the comments to complete each class.
"""

# ============================================
# STEP 1: STUDENT CLASS
# ============================================


class Student:
    """
    TODO: Create a class to represent a student.

    Instructions:
    1. Create the __init__ method with parameters: self, student_id, name, grade_level
    2. Store these as instance variables
    3. Create a display_info method that prints student details
    4. Create __str__ method for string representation
    """

    def __init__(self, student_id, name, grade_level):
        # Initialize the attributes
        self.student_id = student_id
        self.name = name
        self.grade_level = grade_level

    def display_info(self):
        # Print student information in a formatted way
        # Example: "ID: 1001 | Name: Alice | Grade: 10"
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade_level}")

    def __str__(self):
        # Return a string representation of the student
        # Example: "Student(ID: 1001, Name: Alice, Grade: 10)"
        return f"Student(ID: {self.student_id}, Name: {self.name} , Grade: {self.grade_level}"


# ============================================
# STEP 2: CLASS CLASS (School Course)
# ============================================


class Class:
    """
    TODO: Create a class to represent a school course.

    Instructions:
    1. Initialize with class_id, class_name, teacher
    2. Create an empty list for enrolled_students
    3. Create methods to add/remove students
    4. Create method to list all students in the class
    """

    def __init__(self, class_id, class_name, teacher):
        # Initialize attributes and an empty list for enrolled students
        self.class_id = class_id
        self.class_name = class_name
        self.teacher = teacher
        self.enrolled_students = []

    def add_student(self, student):
        # Add a student to the enrolled_students list
        # Check if student is already enrolled to avoid duplicates
        # Print success or warning message
        if student in self.enrolled_students:
            print("Student already enrolled")
        else:
            self.enrolled_students.append(student)
            print("Student successfully added")

    def remove_student(self, student):
        # Remove a student from the enrolled_students list
        # Check if student exists before removing
        # Print appropriate messages
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print("Student seccessfully removed")
        else:
            print("Student not found")

    def list_students(self):
        # Display all students enrolled in this class
        # Handle case when no students are enrolled
        if not self.enrolled_students:
            print("No students enrolled")
        else:
            for student in self.enrolled_students:
                print(
                    f"- {student.name} (ID: {student.student_id}, Grade: {student.grade_level})"
                )

    def __str__(self):
        # Return string representation of the class
        # Include class ID, name, teacher, and number of students
        return f"Class ID: {self.class_id}, Name: {self.class_name}, Teacher: {self.teacher}, Number of students: {len(self.enrolled_students)}"


# # ============================================
# # STEP 3: GRADE CLASS
# # ============================================


class Grade:
    """
    TODO: Create a class to represent a student's grade in a class.

    Instructions:
    1. Initialize with grade_id, student, class_obj, score
    2. Create a method to convert numerical score to letter grade
    3. Create a method to display grade information
    """

    def __init__(self, grade_id, student, class_obj, score):
        # TODO: Initialize all attributes
        self.grade_id = grade_id
        self.student = student
        self.class_obj = class_obj
        self.score = score

    def get_letter_grade(self):
        """
        Convert numerical score to letter grade.
        Use this scale:
        90-100: A
        80-89: B
        70-79: C
        60-69: D
        Below 60: F
        """
        # Return the appropriate letter grade based on self.score
        if self.score >= 90:
            return "A"
        if self.score >= 80 and self.score <= 89:
            return "B"
        if self.score >= 70 and self.score <= 79:
            return "C"
        if self.score >= 60 and self.score <= 69:
            return "D"
        else:
            return "F"

    def display_grade(self):
        # Print grade information including letter grade
        # Example: "Grade ID: 301 | Student: Alice | Class: Math | Score: 95 | Letter: A"
        print(
            f"Grade ID: {self.grade_id} | Student: {self.student.name} | Class: {self.class_obj.class_name} | Score: {self.score} | Letter: {self.get_letter_grade()}"
        )

    def __str__(self):
        # Return string representation of the grade
        # Include letter grade in the string
        return f"Grade ID: {self.grade_id} | Student: {self.student.name} | Class: {self.class_obj.class_name} | Score: {self.score} | Letter: {self.get_letter_grade()}"


# # ============================================
# # STEP 4: SCHOOL MANAGEMENT SYSTEM
# # ============================================

class School:
    """
    TODO: Create the main school management class.

    This class will manage all students, classes, and grades.
    """

    def __init__(self, school_name):
        # Initialize school name and empty lists for students, classes, and grades
        self.school_name = school_name
        self.students_list = []
        self.classes_list = []
        self.grades_list = []


#     # ---------- STUDENT MANAGEMENT ----------

    def add_student(self, student_id, name, grade_level):
        # Create a new Student object and add to students list
        # Check if student_id already exists
        # Return the new student or None if failed
        for student in self.students_list:
          if student.student_id == student_id:
            return ("Student already exists")
          
        new_student = Student(student_id, name, grade_level) #create a new student
        self.students_list.append(new_student)
        return new_student

    def find_student(self, student_id):
        # Find and return a student by ID
        # Return None if not found
        for student in self.students_list:
          if student.student_id == student_id:
            return student
        return None

    def list_all_students(self):
        # Display all students in the school
        # Handle empty list case
        if not self.students_list:
            print ("No students found")
        else:
            for student in self.students_list:
              print (student)


#     # ---------- CLASS MANAGEMENT ----------

    def add_class(self, class_id, class_name, teacher):
        # Create a new Class object and add to classes list
        # Check if class_id already exists
        # Return the new class or None if failed
        for cls in self.classes_list:
          if cls.class_id == class_id:
            return ("Class already exist")
        
        new_class = Class(class_id, class_name, teacher)
        self.classes_list.append(new_class)
        return new_class
          
    def find_class(self, class_id):
        # Find and return a class by ID
        # Return None if not found
        for cls in self.classes_list:
            if cls.class_id == class_id:
                return cls
        return None

    def list_all_classes(self):
        # Display all classes in the school
        # Include number of students enrolled in each class
        if not self.classes_list:
            return ("No class found")
        for cls in self.classes_list:
            print (f"ID: {cls.class_id} | Name: {cls.class_name} | Students: {len(cls.enrolled_students)}")


    # ---------- ENROLLMENT MANAGEMENT ----------

    def enroll_student_in_class(self, student_id, class_id):
        # Enroll a student in a class
        # Find both student and class first
        # Use the class's add_student method
        # Return True if successful, False otherwise
        student = self.find_student(student_id)
        if not student:
            return False
        
        cls_obj = self.find_class(class_id)
        if not cls_obj:
            return False
        
        cls_obj.add_student(student)  #add student to class
        return True

        
#     # ---------- GRADE MANAGEMENT ----------
    
    def find_grade(self, grade_id):        
        for grade in self.grades_list:
            if grade.grade_id == grade_id:
                return grade
        return None

    def add_grade(self, grade_id, student_id, class_id, score):
        # Add a grade for a student in a class
        # Verify student and class exist
        # Verify student is enrolled in the class
        # Check if grade_id already exists
        # Create and add new Grade object
        grade = self.find_grade(grade_id)
        if grade:
            return False
        
        student = self.find_student(student_id)
        if not student:
            return False
        
        cls_obj = self.find_class(class_id)
        if not cls_obj:
            return False
        
        if student not in cls_obj.enrolled_students:  # check enrollment
            return False
    
        new_grade = Grade(grade_id, student, cls_obj, score)
        self.grades_list.append(new_grade)
        return new_grade
        

    def list_grades_for_student(self, student_id):
        # Display all grades for a specific student
        student = self.find_student(student_id)
        if not student:
            print ("Student not found")
            return None

        print(f"Student: {student.name} | ID: {student.student_id}")
        for grade in self.grades_list:
            if grade.student.student_id == student_id:
                print(f"Class: {grade.class_obj.class_name} | Score: {grade.score}")


    def list_grades_for_class(self, class_id):
        # Display all grades for a specific class
        cls_obj = self.find_class(class_id)
        if not cls_obj:
            print("Class not found")
            return
        
        print(f"=== Grades for Class: {cls_obj.class_name} (ID: {cls_obj.class_id}) ===")
        found = False
        for grade in self.grades_list:
            if grade.class_obj.class_id == class_id:
                found = True
                print(f"Student: {grade.student.name} | Score: {grade.score} | Letter: {grade.get_letter_grade()}")
    
        if not found:
            print("No grades recorded for this class.")


    def calculate_student_average(self, student_id):
        # Calculate and display average grade for a student
        # Return the average or None if no grades
        student = self.find_student(student_id)
        if not student:
            print("Student not found")
            return None
        
        student_grades = []
        for grade in self.grades_list:
            if grade.student.student_id == student_id:
                student_grades.append(grade.score)
    
        if not student_grades:
            print("No grades found for this student")
            return None
        
        average = sum(student_grades) / len(student_grades)
        print(f"Student: {student.name} | Average: {average:.2f}")
        return average



# ============================================
# STEP 5: MAIN PROGRAM WITH SAMPLE DATA
# ============================================

def main():
    """
    TODO: Create the main program with sample data and menu system.

    Instructions:
    1. Create a School object
    2. Add sample data (students, classes, enrollments, grades)
    3. Create an interactive menu system
    """

    print("=" * 60)
    print("🏫 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM 🏫")
    print("=" * 60)

    school = School("Python High School")

    # Add sample students
    school.add_student(1, "Ellyse", 10)
    school.add_student(2, "Hanna", 11)
    school.add_student(3, "Bob", 10)
    school.add_student(4, "Ron", 12)

    # Add sample classes
    school.add_class(101, "Math", "Mr. Smith")
    school.add_class(102, "Chemistry", "Ms. Johnson")
    school.add_class(103, "English", "Mrs. Blake")

    # Enroll students in classes
    school.enroll_student_in_class(1, 101)
    school.enroll_student_in_class(1, 102)
    school.enroll_student_in_class(2, 101)
    school.enroll_student_in_class(3, 103)
    school.enroll_student_in_class(4, 102)

    # Add sample grades
    school.add_grade(301, 1, 101, 95)
    school.add_grade(302, 1, 102, 88)
    school.add_grade(303, 2, 101, 76)
    school.add_grade(304, 3, 103, 91)
    school.add_grade(305, 4, 102, 83)

    # Interactive menu
    while True:
        print("\n" + "=" * 40)
        print("       SCHOOL MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1.  List all students")
        print("2.  List all classes")
        print("3.  Add a new student")
        print("4.  Add a new class")
        print("5.  Enroll student in class")
        print("6.  Add a grade")
        print("7.  View student grades")
        print("8.  View class grades")
        print("9.  Calculate student average")
        print("10. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            school.list_all_students()

        elif choice == "2":
            school.list_all_classes()

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            grade_level = int(input("Enter grade level: "))
            result = school.add_student(student_id, name, grade_level)
            print(f"Student added: {result}" if result else "Failed to add student")

        elif choice == "4":
            class_id = int(input("Enter class ID: "))
            class_name = input("Enter class name: ")
            teacher = input("Enter teacher name: ")
            result = school.add_class(class_id, class_name, teacher)
            print(f"Class added: {result}" if result else "Failed to add class")

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            class_id = int(input("Enter class ID: "))
            result = school.enroll_student_in_class(student_id, class_id)
            print("Enrolled successfully" if result else "Enrollment failed")

        elif choice == "6":
            grade_id = int(input("Enter grade ID: "))
            student_id = int(input("Enter student ID: "))
            class_id = int(input("Enter class ID: "))
            score = float(input("Enter score: "))
            result = school.add_grade(grade_id, student_id, class_id, score)
            print("Grade added successfully" if result else "Failed to add grade")

        elif choice == "7":
            student_id = int(input("Enter student ID: "))
            school.list_grades_for_student(student_id)

        elif choice == "8":
            class_id = int(input("Enter class ID: "))
            school.list_grades_for_class(class_id)

        elif choice == "9":
            student_id = int(input("Enter student ID: "))
            school.calculate_student_average(student_id)

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again")


# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()


# # ============================================
# # BONUS CHALLENGES (Optional)
# # ============================================

# """
# Once you complete the basic system, try these challenges:

# 1. Add a Teacher class with attributes (teacher_id, name, subjects)
# 2. Add a method to calculate class average
# 3. Add search functionality (find students by name)
# 4. Add data persistence (save to and load from a file)
# 5. Add a report card generator
# 6. Add GPA calculation (4.0 scale)
# 7. Add attendance tracking
# 8. Add student schedules/timetables
# """

# # ============================================
# # ANSWER KEY (For teachers)
# # ============================================

# """
# The complete solution is available in the tutorial document.
# Students should refer to the tutorial for guidance but try to
# write the code themselves first.
# """
