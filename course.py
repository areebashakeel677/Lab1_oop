"""Lab 1 starter: complete every TODO."""

#TASK 02

"""class Course:"""
"""A course that stores students and their marks."""
"""
    def __init__(self, name):
        self.name = name
        self.marks = {}            # student name -> marks

    def add_student(self, student, marks):
        # TODO: raise ValueError if marks are not between 0 and 100
        if marks<0 and marks>100:
            raise ValueError(" Marks must be b/ 0 and 100")
        self.marks[student] = marks
        # TODO: store marks in self.marks using the student name as key
        #pass

    def average(self):
        # TODO: return the average of all marks
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)
        #pass

    def top_student(self):
        # TODO: return the name of the student with the highest marks
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)
        #pass

    def __len__(self):
        # TODO: return the number of students
        return len(self.marks)
        #pass


# Create a custom exception class
class InvalidMarksError(Exception):
    pass

c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)"""
"""c.add_student("Bilal",120)"""
"""print(len(c))
print(c.average())
print(c.top_student())"""





#This is above code by using task 2 only some instructions are added
#TASK 03

# Exception class
"""class InvalidMarksError(Exception):
    pass


class Course:
    
    def __init__(self, name):
        self.name = name
        self.marks = {}  # student name -> marks

    def add_student(self, student, marks):
        # Raise custom error if marks are not between 0 and 100
        if not 0 <= marks <= 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )

        # Store marks in self.marks using the student name as key
        self.marks[student] = marks

    def average(self):
        # Return the average of all marks
        if len(self.marks) == 0:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        # Return the name of the student with the highest marks
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)

    def __len__(self):
        # Return the number of students
        return len(self.marks)

    def __str__(self):
        # Return course name, student count and average to 1 decimal place
        return f"{self.name}: {len(self)} students, average {self.average():.1f}"


# Create a Course object
c = Course("Programming for AI")

# Add students and their marks
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

# Test the custom exception
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)

# Print course information
print(c)"""





#This is above code by using task 3 only some instructions are added
# TASK 04


"""class InvalidMarksError(Exception):
    pass


class Course:
    
    def __init__(self, name):
        self.name = name
        self.marks = {}  # student name -> marks

    def add_student(self, student, marks):
        # Raise custom error if marks are not between 0 and 100
        if not 0 <= marks <= 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )
        # Store marks in self.marks using the student name as key
        self.marks[student] = marks
    def average(self):
        # Return the average of all marks
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)
    def top_student(self):
        # Return the name of the student with the highest marks
        if len(self.marks) == 0:
            return None
        return max(self.marks, key=self.marks.get)
    def __len__(self):
        # Return the number of students
        return len(self.marks)
    def __str__(self):
        # Return course name, student count and average to 1 decimal place
        return f"{self.name}: {len(self)} students, average {self.average():.1f}"
def load_course(name, filename):
    course = Course(name)

def load_course(name, filename):
    # Create an empty Course with the given name
    course = Course(name)
    #  Handle FileNotFoundError for the whole file block
    try:
        #  Open the file
        with open(filename) as f:
            #  Read each line from the file
            for line in f:
                line = line.strip()
                # Skip empty lines
                if not line:
                    continue
                # Split the line into student and mark
                student, mark = line.split(",")
                #  Add each student inside its own try
                try:
                    course.add_student(student, int(mark))
                #  Handle non-numeric marks and continue
                except ValueError:
                    print(f"Skipping {student}: marks is not a number")
                    continue
                #  Handle invalid marks and continue
                except InvalidMarksError as e:
                    print(f"Skipping: {e}")
                    continue
    except FileNotFoundError:
        # Print a message if the file does not exist
        print(f"File not found: {filename}")
    # Return the Course object
    return course
# Create a Course object
c = Course("Programming for AI")

# Add students and their marks
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

# Test the custom exception
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)

# Print course information
print(c)
class InvalidMarksError(Exception):
    pass


class Course:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_student(self, student, marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )

        self.marks[student] = marks

    def average(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)

    def __len__(self):
        return len(self.marks)

    def __str__(self):
        return (
            f"{self.name}: {len(self)} students, "
            f"average {self.average():.1f}"
        )
def load_course(name, filename):
    # Step 1: Create an empty Course
    course = Course(name)

    # Step 2 and 7: Open file and handle missing file
    try:
        with open(filename) as f:

            # Step 3: Read each line
            for line in f:
                line = line.strip()

                if not line:
                    continue

                student, mark = line.split(",")

                # Step 4, 5 and 6: Process each student's marks
                try:
                    course.add_student(student, int(mark))

                except ValueError:
                    print(
                        f"Skipping {student}: marks is not a number"
                    )
                    continue

                except InvalidMarksError as e:
                    print(f"Skipping: {e}")
                    continue

    except FileNotFoundError:
        print(f"File not found: {filename}")

    # Step 8: Return the Course
    return course"""









# Custom exception for invalid marks
class InvalidMarksError(Exception):
    pass


# Create a Course class
class Course:
    def __init__(self, name):
        # Store the course name and an empty marks dictionary
        self.name = name
        self.marks = {}

    # Add a student and validate their marks
    def add_student(self, student, marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )

        self.marks[student] = marks

    # Calculate the average marks
    def average(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    # Find the student with the highest marks
    def top_student(self):
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)

    # Return the number of students
    def __len__(self):
        return len(self.marks)

    # Display course information
    def __str__(self):
        return (
            f"{self.name}: {len(self)} students, "
            f"average {self.average():.1f}"
        )


# Load students and marks from a text file
def load_course(name, filename):
    # Create an empty course
    course = Course(name)

    try:
        # Open the file and read each line
        with open(filename) as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                # Separate the student name and marks
                student, mark = line.split(",")

                try:
                    # Convert marks to an integer and add the student
                    course.add_student(student, int(mark))

                except ValueError:
                    # Skip marks that are not numbers
                    print(
                        f"Skipping {student}: marks is not a number"
                    )
                    continue

                except InvalidMarksError as e:
                    # Skip marks outside the allowed range
                    print(f"Skipping: {e}")
                    continue

    except FileNotFoundError:
        # Handle a missing file
        print(f"File not found: {filename}")

    # Return the completed course
    return course


# Run this test only when course.py is executed directly
if __name__ == "__main__":
    test_course = Course("Test")
    test_course.add_student("A", 50)
    print(test_course)




