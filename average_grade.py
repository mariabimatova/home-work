import abc


def calculateAverageGrade(grades):
    grades_list = []
    for k, v in grades.items():
        for i in v:
            grades_list.append(i)
    
    sum = 0
    for i in grades_list:
        sum = sum+i

    average_grade = sum / len(grades_list)
    return average_grade


grades = {'Python': [5, 7, 9], 'Java': [3, 5], 'Git': [10]}
avg = calculateAverageGrade(grades)
print(grades)
print(avg)

