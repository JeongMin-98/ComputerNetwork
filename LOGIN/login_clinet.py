"""
Login client는 로그인 정보를 튜플 형태의 데이터로 전송하여
Login server에서 ID 유뮤, Password 유무를 확인한다.

확인 된 경우 로그인 성공이라는 메세지를 server가 client에게 전송한다.

    로그인 ID, password는 튜플 형식으로 리스트에 저장한다.
    member = []
    loginInfo = (id, password)

"""

from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
# login_id = input("Input your id: ")
# password = input("Input your password: ")


with clientSocket as s:
    s.connect((serverName, serverPort))
    while True:
        serverResponse = s.recv(1024).decode()
        login_id = input(serverResponse)
        s.send(login_id.encode())
        serverResponse = s.recv(1024).decode()
        password = input(serverResponse)
        s.send(password.encode())
        login_result = s.recv(1024).decode()
        if login_result == "Incorrect your id":
            new_id_res = input("Can you create new account? [y][n]")
            s.send(new_id_res.encode())
            login_result = s.recv(1024).decode()

        print(login_result)
    s.close()
