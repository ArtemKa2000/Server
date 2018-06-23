import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
print("started")
conn, addr = sock.accept()

conn.send("Success".encode())

conn.close()