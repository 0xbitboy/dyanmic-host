import socket
from urllib import request,parse
import platform
class Agent:
    
    def __init__(self,agent_key,server,scheme):
        self.agent_key = agent_key
        self.server = server
        self.scheme = scheme
        self.report_url = "%s://%s/public/v1/agents/%s"%(scheme,server,agent_key)

    def getLocalIp(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
             s.close()
        return ip

    def getHostname(self):
       return platform.uname()[1]

    def report(self,hostname,ip):
        if hostname is None or hostname=='':
            hostname = self.getHostname();

        data = {
            'ip':ip,
            'host_name':hostname
        }
        data = parse.urlencode(data).encode('utf-8')
        print("Prepare to report agent info to the cloud.->"+self.report_url)
        req = request.Request(self.report_url, data=data)
        page = request.urlopen(req).read()
        page = page.decode('utf-8') 
        print("Result:"+page)
    def syncHostFile(self):
        pass

