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
            if student_preferences[s].index(h) < student_preferences[s].index(current_hospital):
                hospitals[h] = s
                students[s] = h
                hospitals[current_hospital] = -1
                free_hospitals.append(current_hospital)
            else:
                free_hospitals.append(h)
        
    return hospitals, students
        
        





if __name__ == "__main__":
    print(gale_shapley('tests/test1.txt'))