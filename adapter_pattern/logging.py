import sys
import syslog

# The initial class.
class Logger(object):
    def __init__(self, file):
        self.file = file

    def log(self, message):
        self.file.write(message + "\n")
        self.file.flush()

# Two more classes, that send messages elsewhere.
class SocketLogger(Logger):
    def __init__(self, sock):
        self.sock = sock
    
    def log(self, message):
        self.sock.sendall((message + '\n').encode('ascii'))

class SyslogLogger(Logger):
    def __init__(self, priority):
        self.priority = priority

    def log(self, message):
        syslog.syslog(self.priority, message)

class FilteredLogger(Logger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)

    def log(self, message):
        if self.pattern in message:
            super().log(message)

f = FilteredLogger('Error', sys.stdout)
f.log('Ignored: this is not important')
f.log('Error: but you want to see this')