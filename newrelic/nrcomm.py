'''
Created on Jan 26, 2016

@author: newrelic
'''

import json
import urllib2
import logging

def nrPost(injson, inurl, inlickey,inlogging):
    
    req = urllib2.Request(inurl)
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-Insert-Key', inlickey)

    try:
        siteresponse=urllib2.urlopen(req,json.dumps(injson))
#        print(siteresponse.getcode())
        return siteresponse.read()
    except Exception:
        pass
        inlogging.error("failed NR HTTP Call")
        noResult=""
        return noResult
