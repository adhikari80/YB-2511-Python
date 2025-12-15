import sqlite3

class ClinicSystem:
    def __init__(self):
        self.conn = sqlite3.connect("clinic.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    # ---------------- CREATE TABLES ----------------
    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patient (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT,
            contact_number TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Doctor (
            doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            contact_number TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Appointment (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            appointment_date TEXT,
            patient_id INTEGER,
            doctor_id INTEGER,
            FOREIGN KEY(patient_id) REFERENCES Patient(patient_id),
            FOREIGN KEY(doctor_id) REFERENCES Doctor(doctor_id)
        )
        """)
        self.conn.commit()

    # ---------------- INSERT DATA ----------------
    def add_patient(self, name, age, gender, contact):
        self.cursor.execute(
            "INSERT INTO Patient (full_name, age, gender, contact_number) VALUES (?, ?, ?, ?)",
            (name, age, gender, contact)
        )
        self.conn.commit()

    def add_doctor(self, name, specialization, contact):
        self.cursor.execute(
            "INSERT INTO Doctor (full_name, specialization, contact_number) VALUES (?, ?, ?)",
            (name, specialization, contact)
        )
        self.conn.commit()

    # ---------------- REQUIRED FUNCTIONS ----------------
    def list_senior_patients(self):
        print("\n--- Senior Patients (Age > 65) ---")
        self.cursor.execute("SELECT * FROM Patient WHERE age > 65")
        patients = self.cursor.fetchall()

        if not patients:
            print("No senior patients found.")
        else:
            for p in patients:
                print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}, Contact: {p[4]}")

    def count_ophthalmology_doctors(self):
        self.cursor.execute("""
        SELECT COUNT(*) FROM Doctor
        WHERE LOWER(specialization) = 'ophthalmology'
        """)
        count = self.cursor.fetchone()[0]
        print("\nTotal Doctors Specialised in Ophthalmology:", count)

    # ---------------- CLOSE CONNECTION ----------------
    def close(self):
        self.conn.close()


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    clinic = ClinicSystem()

    # ---- Sample Patients ----
    clinic.add_patient("Ram Sharma", 70, "Male", "9851222000")
    clinic.add_patient("Sita Koirala", 60, "Female", "9843299890")
    clinic.add_patient("Hari Adhikari", 75, "Male", "9038879893")

    # ---- Sample Doctors ----
    clinic.add_doctor("Dr. Smith", "Ophthalmology", "022-111111")
    clinic.add_doctor("Dr. Brown", "Cardiology", "022-222222")
    clinic.add_doctor("Dr. Lee", "Ophthalmology", "022-333333")

    # ---- Required Outputs ----
    clinic.list_senior_patients()
    clinic.count_ophthalmology_doctors()

    clinic.close()
