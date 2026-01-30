def verifier(hospitals, students, hospital_preferences, student_preferences):
    n = len(hospitals) - 1

    if 0 in hospitals[1:]:
        print("INVALID: Unmatched hospital")
    
    if 0 in students[1:]:
        print("INVALID: Unmatched student")
    
    if(len(set(hospitals[1:]))) != n:
        print("INVALID: Student matched to multiple hospitals")
    
    if(len(set(students[1:]))) != n:
        print("INVALID: Hospital matched to multiple students")
    
    hospital_ranks = [[0] * (n + 1) for _ in range(n + 1)]
    student_ranks = [[0] * (n + 1) for _ in range(n + 1)]

    for h in range(1, n + 1):
        for rank, s in enumerate(hospital_preferences[h]):
            hospital_ranks[h][s] = rank

    for s in range(1, n + 1):
        for rank, h in enumerate(student_preferences[s]):
            student_ranks[s][h] = rank

    for h in range(1, n + 1):
        current_student = hospitals[h]
        for s in range(1, n + 1):
            if s == current_student:
                continue
            if hospital_ranks[h][s] < hospital_ranks[h][current_student]:
                current_hospital = students[s]
                if student_ranks[s][h] < student_ranks[s][current_hospital]:
                    print(f"UNSTABLE: hospital {h}, student {s}")
                
    print("VALID STABLE")