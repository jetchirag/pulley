import os     
import paramiko

class SFTP:
    def __init__(self, hostname, port, username, password):
        """ Constructor for values provided to class """
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        
    def login(self):
        try:
            sftp = self.sftp_open(self.hostname, int(self.port), self.username, self.password)
        except BaseException, msg:
            sftp = [0, msg]
        return sftp
    
    def verify(self, sftp, path):
        if not sftp:
            return [0, "Invalid SFTP object"]
        
        """ Ensure that given path exists on remote server """
        """ Also changes the directory in sftp instance """
        try:
            sftp.chdir(path)
            return True
        except:
            return [0, "Unable to change directory to given path"]
        
    def transport(self, hostname, port, username, password):
        """ acquire a transport to use SFTP over """
        transport = paramiko.Transport((hostname, port ))
        transport.set_keepalive(5)
        transport.connect( username=username, password=password)
        transport.use_compression(True)
        return transport
    
    def sftp_open(self, hostname, port, username, password):
        """ get an open SFTP session object """
        sftp = paramiko.SFTPClient.from_transport(self.transport( hostname, port, username, password))
        return sftp
            
# login = SFTP('test.rebex.net', '22', 'demo', 'password')
# sftp = login.login()
# print sftp.listdir()