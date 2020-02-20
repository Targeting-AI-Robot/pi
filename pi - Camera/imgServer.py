import socket
import cv2
import numpy

TCP_IP = ''
TCP_PORT = 8282

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(True)
conn, addr = sock.accept()

# just read jpg frame at test
frame = cv2.imread('testImg.jpg')
encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
result, imgencode = cv2.imencode('.jpg', frame, encode_param)
data = numpy.array(imgencode)
stringData = data.tostring()


while True:
    req = conn.recv(1024)
	# send frame when it receive 'req'
    if req.decode() == 'req':
        conn.send( str(len(stringData)).ljust(16));
        conn.send( stringData );
