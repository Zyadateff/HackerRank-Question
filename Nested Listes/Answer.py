if __name__ == '__main__':
    list_student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_student.append([name, score])
    lowest = min(s[1] for s in list_student)
    filtered = [s for s in list_student if s[1] != lowest]
    second_lowest = min([s[1] for s in filtered])
    names = sorted([s[0] for s in filtered if s[1] == second_lowest])
    for n in names:
        print(n)
