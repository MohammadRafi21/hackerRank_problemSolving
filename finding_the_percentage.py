if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    newList = []
    newList = student_marks[query_name] 
    total = 0
    for i in newList:
        total += i
    avg = total/len(newList)
    print(f"{avg:.2f}")