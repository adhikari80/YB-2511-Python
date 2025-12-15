import sqlite3

# Database Manager Class (OOP)

class DatabaseManager:
    def __init__(self, db_name="mse.db"):
        """Initialize database connection"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        """Create Students, Courses, and Teachers tables"""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course_code TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            course_code TEXT NOT NULL
        )
        """)

        self.conn.commit()

    def insert_sample_data(self):
        """Insert sample records into tables"""

        # Insert courses
        courses = [("MSE800",), ("MSE801",)]
        self.cursor.executemany(
            "INSERT INTO Courses(course_code) VALUES (?)", courses
        )

        # Insert students (5 records)
        students = [
            ("Ram", "MSE800"),
            ("Sita", "MSE800"),
            ("Hari", "MSE800"),
            ("Gita", "MSE801"),
            ("John", "MSE801")
        ]
        self.cursor.executemany(
            "INSERT INTO Students(name, course_code) VALUES (?, ?)", students
        )

        # Insert teachers
        teachers = [
            ("Dr. Smith", "MSE801"),
            ("Prof. Brown", "MSE801"),
            ("Ms. Lee", "MSE800")
        ]
        self.cursor.executemany(
            "INSERT INTO Teachers(name, course_code) VALUES (?, ?)", teachers
        )

        self.conn.commit()

    def get_student_count_by_course(self, course_code):
        """Return total number of students enrolled in a given course"""
        self.cursor.execute(
            "SELECT COUNT(*) FROM Students WHERE course_code = ?",
            (course_code,)
        )
        return self.cursor.fetchone()[0]

    def get_teachers_for_mse801(self):
        """Return list of teachers teaching MSE801"""
        self.cursor.execute(
            "SELECT name FROM Teachers WHERE course_code = 'MSE801'"
        )
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        """Close database connection"""
        self.conn.close()


# Main Application

def main():
    db = DatabaseManager()

    # Create tables and insert sample data
    db.create_tables()
    db.insert_sample_data()

    # Get total students for each course
    mse800_count = db.get_student_count_by_course("MSE800")
    mse801_count = db.get_student_count_by_course("MSE801")

    # Get teachers teaching MSE801
    teachers_mse801 = db.get_teachers_for_mse801()

    # Display results
    print(f"Total students enrolled in MSE800: {mse800_count}")
    print(f"Total students enrolled in MSE801: {mse801_count}")

    print("Teachers teaching MSE801:")
    for teacher in teachers_mse801:
        print(f"- {teacher}")

    db.close()


if __name__ == "__main__":
    main()