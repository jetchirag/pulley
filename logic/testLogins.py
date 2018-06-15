from ftplib import FTP, FTP_TLS
import paramiko
import sftpAPI

def testFTP(hostname, username, password, port, path, passive):
    try:
        ftp = FTP()
        ftp.connect(hostname, port, timeout=10)
        ftp.login(username, password)
        ftp.set_pasv(passive)
        ftp.cwd(path)
        files = ftp.dir()
        ftp.quit()
        return True
    except BaseException as error:
        return error

def testFTPS(hostname, username, password, port, path, passive):
    try:
        ftp = FTP_TLS()
        ftp.connect(hostname, port)
        ftp.login(username, password)
        ftp.prot_p()
        ftp.set_pasv(passive)
        ftp.cwd(path)
        files = ftp.dir()
        ftp.quit()
        return True
    except BaseException as error:
        return error

def testSFTP(hostname, username, password, port, path):
    login = sftpAPI.SFTP(hostname, port, username, password)
    sftp = login.login()
    if login.verify(sftp, path) == True:
        return True
    else:
        return False

# print testFTP('test.rebex.net', 'demo', 'password', 21, '/', True)
# print testFTPS('test.rebex.net', 'demo', 'password', 21, '/', True)
# print testSFTP('test.rebex.net', 'demo', 'password', 22, '/')