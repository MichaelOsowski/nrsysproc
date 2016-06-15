'''
Created on Jan 26, 2016

@author: newrelic
'''

import json
import urllib2
import logging

def nrPost(injson, inurl, inlickey,inlogging,inConfig):
    
    if (len(inConfig['proxyserver'])>0):
        proxyString = inConfig['username'] + ":" + inConfig['password'] + "@" + inConfig['proxyserver'] + ":" + inConfig['proxyport']
        proxystuff={'http':[],'https':[]}
        proxystuff['http'].append(proxyString)
        proxystuff['https'].append(proxyString)

        proxy = urllib2.ProxyHandler(proxystuff)
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        
    
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
