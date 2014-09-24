# -*- coding: utf-8 -*-
'''
Created on 16.09.2014

@author: roland
'''
import hl7
import sys
import psycopg2
from Functions import *
import json


_filename_in = ""
_filename_out = ""

_message = ''
_message_array = []

_patient_data = {}

_HL7_to_JSON = True

if(len(sys.argv) != 3):
    _use_stdin = True
else:
    _use_stdin = False
    _filename_in = sys.argv[1]
    _filename_out = sys.argv[2]
    

   


if not _use_stdin:
    lines = [line.rstrip('\n') for line in open(_filename_in)]
    for string in lines:
        _message += string
else:
    for line in sys.stdin:
        _message += line[:-1]

if(checkHL7Message(_message) or (_filename_in[-3:] == "hl7")):
    _HL7_to_JSON = True
else:
    _HL7_to_JSON = False

if(_HL7_to_JSON):
    _h = hl7.parse(_message)
    print getNames(_h)
    PatientBookfull = {getNames(_h):_h}
    PatientBookfull[getNames(_h)] = _h
    PatientBookSimple = {getNames(_h):getObservablen(_h)}
    Untersuchungen = getObservablen(_h)
    
    for i, elem in enumerate(Untersuchungen):
        _patient_data[elem] = _h[i]
    
    _JSON = createJSONObject(_h)
    if(_use_stdin):
        print _JSON
    else:
        with open(_filename_out, "w") as text_file:
            text_file.write(_JSON)
else:
    _MSH_message, _primary_separator, _secondary_separator = createMSHMessage(_message)
    _HL7_message = createHL7Message(_message)
    if(_use_stdin):
        print _HL7_message
    else:
        outfile = open(_filename_out, "w")
        outfile.write(_HL7_message)
        outfile.close()

    



