from ftplib import FTP, FTP_TLS
import paramiko

def testFTP(hostname, username, password, port, directory, passive):
    try:
        ftp = FTP()
        ftp.connect(hostname, port, timeout=10)
        ftp.login(username, password)
        ftp.set_pasv(passive)
        ftp.cwd("/")
        files = ftp.dir()
        ftp.quit()
        return True
    except BaseException as error:
        return error

def testFTPS(hostname, username, password, port, directory, passive):
    try:
        ftp = FTP_TLS()
        ftp.connect(hostname, port)
        ftp.login(username, password)
        ftp.prot_p()
        ftp.set_pasv(passive)
        ftp.cwd("/")
        files = ftp.dir()
        ftp.quit()
        return True
    except BaseException as error:
        return error

def testSFTP(hostname, username, password, port, directory):
    try:
        transport = paramiko.Transport((hostname, int(port)))
        transport.connect(username=username, password=password)
#         sftp = paramiko.SFTPClient.from_transport(transport)

#         sftp.chdir(directory)
#         files = sftp.listdir()
#         sftp.close()
        return True
    except BaseException as error:
        return error

# print testFTP('test.rebex.net', 'demo', 'password', 21, '/', True)
# print testFTPS('test.rebex.net', 'demo', 'password', 21, '/', True)
print testSFTP('test.rebex.net', 'demo', 'password', 222, '/')