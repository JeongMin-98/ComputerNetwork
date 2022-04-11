"""
Login server는 clinet에게 ID, password 정보를 입력 받아
없는 경우 새로이 아이디 패스워드를 생성하고,
있는 경우 아이디와 패스워드가 각각 일치 하는지 확인하는 과정을 거친다.

확인 된 경우 로그인 성공이라는 메세지를 server가 client에게 전송한다.

    로그인 ID, password는 튜플 형식으로 리스트에 저장한다.
    member = []
    loginInfo = (id, password)

"""

from socket import *

member = {"min" : '1234', "jeong":"1123994"}

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

print("server open")

with serverSocket as s:
    s.bind(('localhost', serverPort))
    s.listen()

    connectionSocket, addr = s.accept()

    with connectionSocket:
        print(f"Connected by {addr}")
        while True:
            id_message = "Input your id: "
            connectionSocket.send(id_message.encode())
            login_id = connectionSocket.recv(1024).decode()
            password_message = "Input your password: "
            connectionSocket.send(password_message.encode())
            password = connectionSocket.recv(1024).decode()
            if login_id not in member.keys():
                message = "Incorrect your id"
                connectionSocket.send(message.encode())
                print(member)
                response = connectionSocket.recv(1024).decode()
                if response == "y":
                    member[login_id] = password
                    message = "success create new account!!"
                    connectionSocket.send(message.encode())
                    print(member)
                else:
                    message = "Server don't create new account!"
                    connectionSocket.send(message.encode())
            else:
                if password == member[login_id]:
                    message = "success login!!"
                    connectionSocket.send(message.encode())
                else:
                    message = "incorrect your password"
                    connectionSocket.send(message.encode())

        # connectionSocket.close()



