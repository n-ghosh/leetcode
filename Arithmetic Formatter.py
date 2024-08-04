# Arithmetic Formatter
# FreeCodeCamp's Python project

""" Algorithm """

def arithmetic_arranger(arrProblems, willShow=False):
    if len(arrProblems) > 5:
        return "Error: Too many problems."
    arranged = ""
    for s in arrProblems:
        # Input validation
        problem = s.split(' ')
        if len(problem) != 3:
            print(problem)
            return "\nNot sure what problem^ is "
        if problem[1] != "+" and problem[1] != "-":
            return "Error: Operator must be '+' or '-'."
        
        sizes = [len(problem[0]), len(problem[2])]
        try:
            problem[0] = int(problem[0])
            problem[2] = int(problem[2])
        except:
             return "Error: Numbers must only contain digits."
        if sizes[0] >4 or sizes[1] >4:
            return "Error: Numbers cannot be more than four digits."
        
        # Output formatting
        maxSize = max(sizes) + 1
        for i in range(maxSize - sizes[0] + 1):
            arranged += " "
        arranged += str(problem[0]) + "\n"
        arranged += problem[1] + " "
        for i in range(maxSize - sizes[1] - 1):
            arranged += " "
        arranged += str(problem[2]) + "\n"
        for i in range(maxSize + 1):
            arranged += '-'
        arranged += "\n"
        if willShow:
            answer = ""
            if problem[1] == '+':
                answer = str(problem[0] + problem[2])
            else:
                answer = str(problem[0] - problem[2])
            for i in range(maxSize - len(answer) + 1):
                arranged += ' '
            arranged += answer + "\n\n"
    return arranged

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))