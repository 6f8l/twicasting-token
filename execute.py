import requests

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImYzZTU1Y2EzYTY3MGY2ZjUwYmQ0NDMxNTdhY2JiMjM0Zjc4OTkxZWRmNGRlMzIzM2Y5OGZmYTg3ZWMxZWQ3YzQ4NDNiZWIwNTk0ZDM2ZGFiIn0.eyJhdWQiOiIxODIyMjQ5MzguMjNhNzJmNDA2NzI4M2I0OWY5NjZmOTMyMzViMTg2NDQzN2VjNWY2YTlmY2M5NjVlOGIzOTM5MGRmNWQ2YWE5NCIsImp0aSI6ImYzZTU1Y2EzYTY3MGY2ZjUwYmQ0NDMxNTdhY2JiMjM0Zjc4OTkxZWRmNGRlMzIzM2Y5OGZmYTg3ZWMxZWQ3YzQ4NDNiZWIwNTk0ZDM2ZGFiIiwiaWF0IjoxNTYyMTU3NzMyLCJuYmYiOjE1NjIxNTc3MzIsImV4cCI6MTU3NzcwOTczMiwic3ViIjoiMTY2NzQ4MzgyNyIsInNjb3BlcyI6WyJyZWFkIl19.HK1uK_Su3pX-B8gSM16L6x1lA5Itb_-c0Qik4EPczFF5jlAGLqfQmakEfwwoWacwyv3avVmbDminkEZO8P8hlF9aY9I5s_XYmr4ez8mdduEJ920crtD8O925TWpPtxkET_WV4IAEf83-hEPiB1xztGEiT7MT73DtbWVi1rockDt-z7tzsIJa5NX67KU2yGjMKmzEXtLXeVFa1s2MVuLmNiVFIIr95VMP8hXB9dgj9d9d09Nj0VI3DMl4XT2Ae4iWW3Dfcp8x4-gk7646xN53Jh6vAxUI0YX_EOQaXQgyNAmRxoUNsDTROTZUeF7SUAlR1hxrc50b6qnL65us0ErslA'

def initProblem():
    header = {
        'Authorization': 'Bearer {}'.format(token)
    }
    response = requests.get(
        url = 'https://apiv2.twitcasting.tv/internships/2019/games?level=3',
        headers = header
    )
    print(response.text)


if __name__ == '__main__':
    initProblem()