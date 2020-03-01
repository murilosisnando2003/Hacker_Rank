#!/usr/bin/env python3

def main():
    N = int(input())
    students = []
    for i in range(N):
        name = input()
        mark = float(input())
        students.append([name, mark])
    
    print('teste1')
    print(students[:])

    students.sort(key=lambda student: (student[1], student[0]))

    print('teste2')
    print(students[:])
    # print(student[1])
    # print(student[0])

    second_lowest_mark = [student[1] for student in students if student[1] != students[0][1]][0]
    print('teste2.1')
    print(students[:])
    print(students[0][1])
    print([student[1] for student in students if student[1] != students[0][1]][0])
    print(second_lowest_mark)
    
    
    print("Go1 " + str(second_lowest_mark))
    for s in [student for student in students if student[1] == second_lowest_mark]:
        print("Go2" + str(s[0]))

    print("Go3 " + str(s))
    
if __name__ == '__main__':
    main()
