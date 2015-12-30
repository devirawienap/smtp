import socket
import base64

mail_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mail_socket.connect (('mail.its-sby.edu',587))
print 'S: ', mail_socket.recv(1024).strip()

username = base64.b64encode('tes@its-sby.edu'.encode('utf-8'))
password = base64.b64encode('tesprogjar'.encode('utf-8'))
commands = ['HELO mail.its\r\n', 'AUTH LOGIN\r\n', username + '\r\n', password + '\r\n', 'MAIL FROM: <tes@its-sby.edu\r\n', 'RCPT TO: <kuliah.progjar@gmail.com>\r\n', 'DATA\r\n', 'from: tes@its-sby.edu\nto: kuliah.progjar@gmail.com\nsubject: Progjar\r\n have successfully implemented SMTP via raw socket.\r\n.\r\n','QUIT\r\n']

for command in commands:
    mail_socket.send[command]
    #print 'C :', command.strip()
    print 'S : ', mail_socket.recv(1024).strip()

mail_socket.close()
