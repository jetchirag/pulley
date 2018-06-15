import logging

import pexpect


class SFTP(object):
    """
    Requires openssh_client. Spawns process to execute sftp command.
    """

    def __init__(self, username, host, port, password):
        self.username = username
        self.host = host
        self.port = port
        self.password = password

    def get_files(self, remote_path, local_path):
        """
        Connect to connection_id and download all files in the remote path.
        :param remote_path: The remote path to sync
        :param local_path: The local dir to store files
        :return: None
        """
        logging.info('sftp get %s to: %s' % (remote_path, local_path))

        child = None

        try:
            logging.debug('spawning child')
            child = pexpect.spawn('/usr/bin/sftp -r -P ' + self.port + ' ' + self.username + '@' + self.host + ':' + remote_path + ' ' + local_path,
                timeout=14400)
            print '==='
            print child
            print '==='
            self._handle_sftp_prompt(child)
            child.expect(pexpect.EOF)
        finally:
            if child:
                child.close()
                if child.isalive():
                    logging.warning('Child did not exit gracefully.')
                else:
                    logging.debug('Child exited gracefully.')
        if child:
            if child.status > 0:
                raise Exception('sftp command exited')
            else:
                logging.info('download complete')

    def _handle_sftp_prompt(self, child):
        logging.debug('expecting prompt...')
        i = child.expect(['.*password:.*', '.*continue connecting.*', '.*Connected.*'])
        if i == 0:
            logging.info('supplying pass to sftp server')
            child.sendline(self.password)
            logging.debug('sent pw')
            self._handle_sftp_prompt(child)
        elif i == 1:
            logging.info('answering yes to host check')
            child.sendline('yes')
            logging.debug('sent yes')
            self._handle_sftp_prompt(child)
        elif i == 2:
            logging.info('connected to sftp server')

login = SFTP('demo', 'test.rebex.net', '22', 'password')

login.get_files('readme.txt', '/root')