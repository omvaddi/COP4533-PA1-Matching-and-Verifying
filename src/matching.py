def read_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())

        hospitals = []
        for _ in range(n):
            hospitals.append(list(map(int, f.readline().strip().split())))
        
        students = []
        for _ in range(n):
            students.append(list(map(int,f.readline().strip().split())))

    return n, hospitals, students
            


if __name__ == "__main__":
    print(read_input('tests/test1.txt'))