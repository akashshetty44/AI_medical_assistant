# database.py

import sqlite3

DATABASE_NAME = "medical_assistant.db"


def create_database():
    """
    Creates the patients table if it doesn't already exist.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            symptoms TEXT,
            predicted_disease TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_patient(name, age, gender, symptoms, predicted_disease):
    """
    Saves patient information into the database.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients
        (name, age, gender, symptoms, predicted_disease)
        VALUES (?, ?, ?, ?, ?)
    """, (name, age, gender, symptoms, predicted_disease))

    conn.commit()
    conn.close()


def get_all_patients():
    """
    Returns all patient records.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    records = cursor.fetchall()

    conn.close()

    return records


def get_patient_by_id(patient_id):
    """
    Returns a single patient record.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE id=?",
        (patient_id,)
    )

    patient = cursor.fetchone()

    conn.close()

    return patient


def delete_patient(patient_id):
    """
    Deletes a patient record.
    """

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,)
    )

    conn.commit()
    conn.close()


# Test the database
if __name__ == "__main__":
    create_database()

    save_patient(
        "Akash",
        22,
        "Male",
        "fever,cough,headache",
        "Common Cold"
    )

    print(get_all_patients())
