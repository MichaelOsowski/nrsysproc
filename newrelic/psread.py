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
                singleresponse['rss'] = pinfo['memory_info'][0]
                singleresponse['vms'] = pinfo['memory_info'][1]
                singleresponse['shared'] = pinfo['memory_info'][2]
                singleresponse['mtext'] = pinfo['memory_info'][3]
                try:
                    singleresponse['lib'] = pinfo['memory_info'][4]
                    singleresponse['data'] = pinfo['memory_info'][5]
                    singleresponse['dirty'] = pinfo['memory_info'][6]
                except Exception:
                    pass    
                singleresponse['pid'] = pinfo['pid']
                singleresponse['memory'] = pinfo['memory_percent']
                singleresponse['commandline'] = pinfo['cmdline']
                response.append(singleresponse)
                
#                print(singleresponse)
            

            
    return response  


          
    

