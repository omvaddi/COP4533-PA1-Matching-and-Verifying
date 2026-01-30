import random
from collections import deque
import verifier

def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())

        hospital_preferences = [[]]
        for _ in range(n):
            hospital_preferences.append(list(map(int, f.readline().strip().split())))
        
        student_preferences = [[]]
        for _ in range(n):
            student_preferences.append(list(map(int,f.readline().strip().split())))

    return n, hospital_preferences, student_preferences
            

def gale_shapley(filename):
    n, hospital_preferences, student_preferences = read_input(filename)

    student_ranks = [[0] * (n + 1) for _ in range(n + 1)]
    for s in range(1, n + 1):
        for rank, h in enumerate(student_preferences[s]):
            student_ranks[s][h] = rank

    hospitals = [0] * (n + 1)
    students = [0] * (n + 1)

    free_hospitals = deque(range(1, n + 1))
    next_proposal = [0] * (n + 1)

    while free_hospitals:
        h = free_hospitals.popleft()
        s = hospital_preferences[h][next_proposal[h]]
        next_proposal[h] += 1

        if students[s] == 0:
            hospitals[h] = s
            students[s] = h
        else:
            current_hospital = students[s]
            if student_ranks[s][h] < student_ranks[s][current_hospital]:
                hospitals[h] = s
                students[s] = h
                hospitals[current_hospital] = 0
                free_hospitals.append(current_hospital)
            else:
                free_hospitals.append(h)

    for i in range(1, n + 1):
        print(i, hospitals[i])

    return hospitals, students, hospital_preferences, student_preferences


def generate_input(filename, n):
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        for _ in range(n):
            prefs = list(range(1, n + 1))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")
        for _ in range(n):
            prefs = list(range(1, n + 1))
            random.shuffle(prefs)
            f.write(" ".join(map(str, prefs)) + "\n")


if __name__ == "__main__":
    filename = input("Enter input filename: ")
    output = gale_shapley(filename)
    verifier.verifier(*output)