import requests
import json
import random

# Configure token.
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImYzZTU1Y2EzYTY3MGY2ZjUwYmQ0NDMxNTdhY2JiMjM0Zjc4OTkxZWRmNGRlMzIzM2Y5OGZmYTg3ZWMxZWQ3YzQ4NDNiZWIwNTk0ZDM2ZGFiIn0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6ImYzZTU1Y2EzYTY3MGY2ZjUwYmQ0NDMxNTdhY2JiMjM0Zjc4OTkxZWRmNGRlMzIzM2Y5OGZmYTg3ZWMxZWQ3YzQ4NDNiZWIwNTk0ZDM2ZGFiIiwiaWF0IjoxNTYyMTU3NzMyLCJuYmYiOjE1NjIxNTc3MzIsImV4cCI6MTU3NzcwOTczMiwic3ViIjoiMTY2NzQ4MzgyNyIsInNjb3BlcyI6WyJyZWFkIl19.HK1uK_Su3pX-B8gSM16L6x1lA5Itb_-c0Qik4EPczFF5jlAGLqfQmakEfwwoWacwyv3avVmbDminkEZO8P8hlF9aY9I5s_XYmr4ez8mdduEJ920crtD8O925TWpPtxkET_WV4IAEf83-hEPiB1xztGEiT7MT73DtbWVi1rockDt-z7tzsIJa5NX67KU2yGjMKmzEXtLXeVFa1s2MVuLmNiVFIIr95VMP8hXB9dgj9d9d09Nj0VI3DMl4XT2Ae4iWW3Dfcp8x4-gk7646xN53Jh6vAxUI0YX_EOQaXQgyNAmRxoUNsDTROTZUeF7SUAlR1hxrc50b6qnL65us0ErslA'
header = {
    'Authorization': 'Bearer {}'.format(token)
}

def startAPI():
    response = requests.get(
        url = 'https://apiv2.twitcasting.tv/internships/2019/games?level=3',
        headers = header
    )
    r = response.json()
    question = r['question']
    q_arr = question.split("=")
    formula, value = q_arr[0], q_arr[1]
    game_id = r['id']
    return formula, value, game_id

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

def calculate(formula):
    operator_arr = createOperator()
    answer = eval(formula.format(operator_arr[0], operator_arr[1], operator_arr[2], operator_arr[3], operator_arr[4], operator_arr[5]))
    return answer, operator_arr

def answerStr(formula, value):
    formula = formula.replace("?", "{}")
    for i in range(0, 100000000):
        answer, operator_arr = calculate(formula)
        if float(answer) == float(value):
            answer_str = "".join(operator_arr)
            return answer_str
        else:
            pass

def answerAPI():
    formula, value, game_id = startAPI()
    data = {
        "answer": answerStr(formula, value)
    }
    response = requests.post(
        url = 'https://apiv2.twitcasting.tv/internships/2019/games/{}'.format(game_id),
        data = json.dumps(data),
        headers = header
    )
    print(response.text)
    return response.text

def deleteAPI():
    response = requests.delete(
        url = 'https://apiv2.twitcasting.tv/internships/2019/games/',
        headers = header
    )
    return response.text

if __name__ == '__main__':
    answerAPI()