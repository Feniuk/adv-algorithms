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

# for student, hospital in matches:
#     print(f"{student} → {hospital}")

def cube_algorithm (n):
    for i in range(n):
        for j in range(n):
            for z in range(n):
                print(i, j, z)


def log_func_recursive (n):
    if n == 0:
        return "Done"
    n = n // 2
    return  log_func_recursive(n) 

def log_func (n):
    while n > 1:
        n //= 2
    return "Done"


def mergeSort(arr) :
    if len(arr) < 2:
        return arr
    
    middleIndex = len(arr) // 2
    leftArr = arr[:middleIndex]
    rightArr = arr[middleIndex:]

    return merge(mergeSort(leftArr), mergeSort(rightArr))

def merge(leftArr, rightArr):
    mergedArr = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergedArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergedArr.append(rightArr[rightIndex])
            rightIndex += 1

    mergedArr.extend(leftArr[leftIndex:])
    mergedArr.extend(rightArr[rightIndex:])
    return mergedArr


def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonachi(n -1) + fibonachi(n - 2)



lectures = {
    'a': [9, 10.5],
    'b': [9, 12.5],
    'c': [9, 10.5],
    'd': [11, 12.5],
    'e': [11, 14],
    'f': [13, 14.5],
    'g': [13, 14],
    'h': [14, 16.5],
    'i': [15, 16.5],
    'j': [15, 16.5]
}

def first_value(item):
    return item[1][0]

def intervalPartioning(some_lectures):
    sorted_lectures = sorted(some_lectures.items(), key=first_value)
    schedule = {}
    depth = 0
    next_room_id = 0

    for lect in sorted_lectures:
        
        assigned = False
        for room_id, lectures_in_room in schedule.items():
            last_lecture = lectures_in_room[-1]
            last_end_time = last_lecture[1][1]

            if last_end_time <= lect[1][0]:
                lectures_in_room.append(lect)
                assigned = True
                break

        if not assigned:
            next_room_id += 1
            new_list = []
            new_list.append(lect)
            schedule[next_room_id] = new_list
            depth += 1


    return schedule, depth


print(intervalPartioning(lectures))