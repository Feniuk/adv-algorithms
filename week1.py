hospitals = {
    "Atlanta": ["Xavier", "Zeus", "Yam"], 
    "Boston": ["Yam", "Xavier", "Zues"], 
    "Detroit": ["Zeus", "Yam", "Xavier"]
}

students = {
    "Xavier": ["Boston", "Atlanta", "Detroit"],
    "Yam": ["Atlanta", "Detroit", "Boston"],
    "Zues": ["Detroit", "Boston", "Atlanta"]
}

def gale_shapley_students_hospitals(students, hospitals):
    """
    students: dict[str, list[str]]
        student -> preference list of hospitals
    hospitals: dict[str, list[str]]
        hospital -> preference list of students

    returns: list of (student, hospital) pairs
    """

    hospital_match = {h: None for h in hospitals}

   
    next_proposal = {s: 0 for s in students}

    free_students = list(students.keys())

    while free_students:
        student = free_students.pop(0)

        hospital = students[student][next_proposal[student]]
        next_proposal[student] += 1

        if hospital_match[hospital] is None:
            hospital_match[hospital] = student
        else:
            current_student = hospital_match[hospital]

            if hospitals[hospital].index(student) < hospitals[hospital].index(current_student):
                hospital_match[hospital] = student
                free_students.append(current_student)
            else:
                free_students.append(student)

    return [(student, hospital) for hospital, student in hospital_match.items()]


matches = gale_shapley_students_hospitals(students, hospitals)

for student, hospital in matches:
    print(f"{student} → {hospital}")
