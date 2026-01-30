import random

def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())

        hospital_preferences = []
        for _ in range(n):
            hospital_preferences.append(list(map(int, f.readline().strip().split())))
        
        student_preferences = []
        for _ in range(n):
            student_preferences.append(list(map(int,f.readline().strip().split())))

    return n, hospital_preferences, student_preferences
            

def gale_shapley(filename):
    n, hospital_preferences, student_preferences = read_input(filename)

    student_ranks = [[0] * n for _ in range(n)]
    for s in range(n):
        for rank, h in enumerate(student_preferences[s]):
            student_ranks[s][h] = rank

    hospitals = [-1] * n
    students = [-1] * n

    free_hospitals = list(range(n))

    next_proposal = [0] * n

    while free_hospitals:
        h = free_hospitals.pop(0)

        s = hospital_preferences[h][next_proposal[h]]
        next_proposal[h] += 1

        if students[s] == -1:
            hospitals[h] = s
            students[s] = h
        else:
            current_hospital = students[s]
            if student_ranks[s][h] < student_ranks[s][current_hospital]:
                hospitals[h] = s
                students[s] = h
                hospitals[current_hospital] = -1
                free_hospitals.append(current_hospital)
            else:
                free_hospitals.append(h)

    for i in range(len(hospitals)):
        print(i, hospitals[i])

    return hospitals, students, hospital_preferences, student_preferences

def verifier(hospitals, students, hospital_preferences, student_preferences):
    n = len(hospitals)

    if -1 in hospitals:
        return False, "INVALID: Unmatched hospital"
    
    if -1 in students:
        return False, "INVALID: Unmatched student"
    
    if(len(set(hospitals))) != n:
        return False, "INVALID: Student matched to multiple hospitals"
    
    if(len(set(students))) != n:
        return False, "INVALID: Hospital matched to multiple students"
    
    hospital_ranks = [[0] * n for _ in range(n)]
    student_ranks = [[0] * n for _ in range(n)]

    for h in range(n):
        for rank, s in enumerate(hospital_preferences[h]):
            hospital_ranks[h][s] = rank

    for s in range(n):
        for rank, h in enumerate(student_preferences[s]):
            student_ranks[s][h] = rank

    for h in range(n):
        current_student = hospitals[h]
        for s in range(n):
            if s == current_student:
                continue
            if hospital_ranks[h][s] < hospital_ranks[h][current_student]:
                current_hospital = students[s]
                if student_ranks[s][h] < student_ranks[s][current_hospital]:
                    return False, f"UNSTABLE: hospital {h}, student {s}"
                
    return True, "VALID STABLE"

def generate_input(filename, n):
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        for _ in range(n):
            prefs = list(range(n))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")
        for _ in range(n):
            prefs = list(range(n))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")

if __name__ == "__main__":
    gale_shapley('tests/test1.txt')
    print("-----")
    
    gale_shapley('tests/test2.txt')
    print("-----")

    gale_shapley('tests/test3.txt')
    print("-----")

    gale_shapley('tests/test4.txt')
    print("-----")

    gale_shapley('tests/test5.txt')
    print("-----")
    