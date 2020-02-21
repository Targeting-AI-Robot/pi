import socket
import cv2
import numpy as np

TCP_IP = ''
TCP_PORT = 8282

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(True)
conn, addr = sock.accept()

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

# get two frame and return
# return frame1, frame2
# Not implemented yet
def getFrame():
    return None, None

while True:
    req = conn.recv(1024)
    # send frame when it receive 'req'
    if req.decode() == 'req':
        frame1, frame2 = getFrame()
        
        result1, imgencode1 = cv2.imencode('.jpg', frame1, encode_param)
        data1 = np.array(imgencode1)
        stringData1 = data1.tostring()
        
        result2, imgencode2 = cv2.imencode('.jpg', frame2, encode_param)
        data2 = np.array(imgencode2)
        stringData2 = data2.tostring()
    
        conn.send( str(len(stringData1)).ljust(16));
        conn.send( stringData1 );
        
        conn.send( str(len(stringData2)).ljust(16));
        conn.send( stringData2 );
