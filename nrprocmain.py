'''
Created on Jan 14, 2016

@author: newrelic
'''
import logging
import time
import psutil

from daemonize import Daemonize

from newrelic import psread, nrcomm, getConfig
from newrelic.psread import getps
import json

pid = "/tmp/nrproc.pid"

def main():
       
    
    config = {}
    config = getConfig.parseConfig("nrprocConfig.conf")
    logging.basicConfig(filename='nrproc.log', level=logging.INFO)
    systemLog = logging.getLogger("__NR___")
    logging.info("Start")
    
    while True:
 


         response = getps(config['processsearch'],systemLog,config['hostname'])

    
         print(json.dumps(response))
    
         response = nrcomm.nrPost(response, config['nrurl'] , config['nrinsertkey'],systemLog)
         print(response)
        
         time.sleep(float(config['checkspeedsecs']))
    

main()

#daemon = Daemonize(app="nrproc", pid=pid, action=main())
#daemon.start()
    

        
        
        
