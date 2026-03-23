
## 🏗️ The Exercise

# 🏫 School Management System — Python OOP Exercise

You will build a **School Management System** step by step. The final program will:

1. Manage students, classes, and grades
2. Enroll students into classes
3. Record and display grades
4. Calculate student averages
5. Run an interactive menu for the user

---

## 🧱 Classes You Will Build

### Step 1 — Create the `Student` Class

### Step 2 — Create the `Class` Class

### Step 3 — Create the `Grade` Class

### Step 4 — Create the `School` Class



Methods to implement:

**Student Management**

| Method | What it does |
|---|---|
| `add_student(student_id, name, grade_level)` | Create and add student, check for duplicate ID |
| `find_student(student_id)` | Search list and return student, or `None` |
| `list_all_students()` | Print all students |

**Class Management**

| Method | What it does |
|---|---|
| `add_class(class_id, class_name, teacher)` | Create and add class, check for duplicate ID |
| `find_class(class_id)` | Search list and return class, or `None` |
| `list_all_classes()` | Print all classes with enrollment count |

**Enrollment Management**

| Method | What it does |
|---|---|
| `enroll_student_in_class(student_id, class_id)` | Find both objects, call `cls.add_student()`, return `True`/`False` |

**Grade Management**

| Method | What it does |
|---|---|
| `find_grade(grade_id)` | Search list and return grade, or `None` |
| `add_grade(grade_id, student_id, class_id, score)` | Verify all exist, check enrollment, create Grade |
| `list_grades_for_student(student_id)` | Print all grades for one student |
| `list_grades_for_class(class_id)` | Print all grades for one class |
| `calculate_student_average(student_id)` | Calculate and return average score |

---

## ▶️ Sample Output

```
============================================================
🏫 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM 🏫
============================================================

========================================
       SCHOOL MANAGEMENT SYSTEM
========================================
1.  List all students
2.  List all classes
3.  Add a new student
...
========================================

Student(ID: 1, Name: Ellyse , Grade: 10)
Student(ID: 2, Name: Hanna , Grade: 11)

Student: Ellyse | ID: 1
Class: Math | Score: 95
Class: Chemistry | Score: 88

=== Grades for Class: Math (ID: 101) ===
Student: Ellyse | Score: 95 | Letter: A
Student: Hanna | Score: 76 | Letter: C

Student: Ellyse | Average: 91.50
```

---
