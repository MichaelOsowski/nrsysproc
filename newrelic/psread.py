from subprocess import Popen, PIPE
import subprocess
import json
import socket
import re
import logging
import psutil

        

def getps(inRegex,inlogging,shostname):
    
    psresultlist=[]
    response=[]
    pinfo=[]
    
   
    
    regex=re.compile(inRegex)
    
    
    
    if len(shostname) < 1:
        pshost=socket.gethostname()
    else:
        pshost=shostname  
        
    for p in psutil.process_iter():
        try:
            pinfo = p.as_dict(['username', 'nice', 'memory_info',
                                'memory_percent', 'cpu_percent',
                                'cpu_times', 'name','cmdline', 'status','pid'])
            
            
        except psutil.NoSuchProcess:
            pass
        else:
            testexe = str(pinfo['cmdline'])
            if regex.search(testexe) is not None:
                singleresponse={}
                singleresponse['eventType'] = "SystemStat"
                singleresponse['hostname'] = pshost
                singleresponse['cpu'] = pinfo['cpu_percent']
                singleresponse['pid'] = pinfo['pid']
                singleresponse['memory'] = pinfo['memory_percent']
                singleresponse['commandline'] = pinfo['cmdline']
                response.append(singleresponse)
                
#                print(singleresponse)
            

            
    return response  


          
    

