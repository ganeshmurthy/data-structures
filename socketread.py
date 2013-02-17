import socket

def socketread():
    s = socket.socket()
    s.connect(("ec2-23-20-43-81.compute-1.amazonaws.com",9999))
    line = s.recv(256)
    notdone = True
    intheader = False
    floatheader = False
    while ( notdone  ) :
      
    	#receive the first line
        line = s.recv(256)
        
        if(not line):
            notdone=False
        else:
            print line
            
    s.close()
    
if(__name__=="__main__"):
    socketread()


