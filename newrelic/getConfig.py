'''
Created on Jan 26, 2016

@author: newrelic
'''
import ConfigParser


def parseConfig(InFile):
    confDict = {}
    config= ConfigParser.ConfigParser()
    config.read(InFile)
    options = config.options("NRCONFIG")
    for option in options:
        try:
            confDict[option] = config.get("NRCONFIG",option)
           
        except:
            print("Missing Config  values")
        
    return confDict