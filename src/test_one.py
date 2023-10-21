"""
Build a simple database for the data modeling discussion and SQL test.
"""

import sqlite3

con = sqlite3.connect("test-one.db")
cur = con.cursor()

try:
    cur.execute(
        "CREATE TABLE patient(\
        patient_id INTEGER NOT NULL PRIMARY KEY,\
        patient_name,\
        patient_address)"
    )
    cur.execute(
        "CREATE TABLE diagnosis(\
        diag_id INTEGER NOT NULL PRIMARY KEY,\
        patient_id INTEGER,\
        med_id INTEGER,\
        condition_id INTEGER,\
        FOREIGN KEY (patient_id) REFERENCES patient (patient_id)\
            ON DELETE CASCADE ON UPDATE NO ACTION\
        FOREIGN KEY (med_id) REFERENCES medication (med_id)\
            ON DELETE CASCADE ON UPDATE NO ACTION\
        FOREIGN KEY (condition_id) REFERENCES condition (condition_id)\
            ON DELETE CASCADE ON UPDATE NO ACTION)"
    )
    cur.execute(
        "CREATE TABLE medication(\
        med_id INTEGER NOT NULL PRIMARY KEY,\
        med_name)"
    )
    cur.execute(
        "CREATE TABLE condition(\
        condition_id INTEGER NOT NULL PRIMARY KEY,\
        condition_name)"
    )
    cur.execute(
        "CREATE TABLE doctor(\
        doctor_id INTEGER NOT NULL PRIMARY KEY,\
        patient_id INTEGER,\
        doctor_name,\
        FOREIGN KEY(patient_id) REFERENCES patient(patient_id)\
            ON DELETE CASCADE ON UPDATE NO ACTION)"
    )

    # add patients
    data = [
        (1, "John", "1982 Well St"), 
        (2, "Jill", "1983 Well St"), 
        (3, "Jasper", "1984 Well St"),
        (4, "Janine", "1985 Well St"), # fever
        (5, "Kato", "10 Willow St"), 
        (6, "Leonard", "19 Marcus St"), 
        (7, "Lillian", "233 First St"),
        (8, "Mathilda", "1985 Well St"),
        (9, "Nancy", "1982 Well St"),
        (10, "Ophelia", "1982 Well St"),
    ]
    cur.executemany("INSERT INTO patient VALUES(?, ?, ?)", data)
    con.commit()

    # add medications
    data = [
        (1, "Tylenol"),
        (2, "NyQuil"),
        (3, "Beta blocker"),
        (4, "Doxycycline")
    ]
    cur.executemany("INSERT INTO medication VALUES(?, ?)", data)
    con.commit()

    # add conditions
    data = [
        (1, "Fever"),
        (2, "Cold"),
        (3, "Plague"),
        (4, "Tachycardia"),
        (5, "Fatigue"),
        (6, "Munchausen's")
    ]
    cur.executemany("INSERT INTO condition VALUES(?, ?)", data)
    con.commit()

    # add diagnoses (diag_id, patient_id, med_id, condition_id)
    data = [
        (1, 10, 4, 3),
        (2, 9, 4, 3),
        (3, 8, 2, 5),
        (4, 1, 4, 3),
        (5, 2, 4, 3),
        (6, 4, 2, 1),
        (7, 7, 2, 2),
        (8, 5, 1, 6),
        (9, 6, 3, 4),
        (10, 3, 2, 5)
    ]
    cur.executemany("INSERT INTO diagnosis VALUES(?, ?, ?, ?)", data)
    con.commit()

except Exception as e:
    con.close()
    raise(e)