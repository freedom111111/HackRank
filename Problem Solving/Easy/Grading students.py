# Python 3
def gradingStudents(grades):
    grader_lst = []
    for x in grades:
        if x<38:
            grader_lst.append(x)
        else:
            mod = x%5
#        print(mod)
            if mod >2:
                grader_lst.append(x+5-mod)
            else:
                grader_lst.append(x)
    return grader_lst
