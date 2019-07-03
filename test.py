import random

def createOperator():
    operator_arr = []
    for i in range(0, 6):
        rand_num = random.randint(0, 3)
        if rand_num == 0:
            operator_arr.append('+')
        elif rand_num == 1:
            operator_arr.append('-')
        elif rand_num == 2:
            operator_arr.append('/')
        elif rand_num == 3:
            operator_arr.append('*')
        else:
            print(i)
    return operator_arr

def calculate(question):
    question = 
    operator_arr = createOperator()
    answer = eval("1 {} 2 {} 6 {} 2 {} 2 {} 3 {} 8".format(operator_arr[0], operator_arr[1], operator_arr[2], operator_arr[3], operator_arr[4], operator_arr[5]))
    return answer, operator_arr

def execute():
    for i in range(0, 1000000):
        answer, operator_arr = calculate()
        if answer == -61:
            answer_str = "".join(operator_arr)
            print(answer_str)
            break
        else:
            pass
    return answer_str
execute()