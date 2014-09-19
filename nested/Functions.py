'''
Created on 19.09.2014

@author: roland
'''

import hl7
#Zieht sich die Namen des Patienten aus der HL7-Nachricht
def getNames(parsed_message):
    if(isinstance(parsed_message, hl7.Message) == False):
        return ('','')
    else:
        return (str(parsed_message.segment("PID")[5][0][1][0]), str(parsed_message.segment("PID")[5][0][0][0]))


#Gibt sämtliche vorgenommenen Untersuchungen (ohne weitere Infos) aus
def getObservablen(parsed_message):
    Observables = {}
    if(isinstance(parsed_message, hl7.Message) == False):
        return ('','')
    else:
        for elem in xrange(len(parsed_message) + 1):
            if elem >= 3:
                Observables[elem-3] = parsed_message[elem-1][0][0]
    return Observables


#Noch nicht in Funktion, da medizinischer Background fehlt
def getWhatHappened(parsed_message):
    Observables = {}
    if(isinstance(parsed_message, hl7.Message) == False):
        return ('','')
    else:
        for elem in xrange(len(parsed_message) + 1):
            if elem >= 3:
                Observables[elem-3] = parsed_message[elem-1][0][0]
    return Observables
                