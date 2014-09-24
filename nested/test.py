# -*- coding: utf-8 -*-
'''
Created on 16.09.2014

@author: roland
'''
import hl7
import sys
import psycopg2
from Functions import *
from __builtin__ import str
import json



_filename_in = ""
_filename_out = ""

_message = ''
_message_array = []

_patient_data = {}

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

#parse message
_h = hl7.parse(_message)

#print isinstance(h, hl7.Message)
#print type(h)
#-------------------------------------------------------- print h.segment("PID")
#--------------------------------------------------- print len(h.segment("PID"))
#------------------------------------------------ print len(h.segment("PID")[5])
#--------------------------------------------- print len(h.segment("PID")[5][0])
#------------------------------------------ print len(h.segment("PID")[5][0][0])
#--------------------------------------- print len(h.segment("PID")[5][0][0][0])
print getNames(_h)
PatientBookfull = {getNames(_h):_h}
PatientBookfull[getNames(_h)] = _h
PatientBookSimple = {getNames(_h):getObservablen(_h)}
Untersuchungen = getObservablen(_h)

print _h[0]

for i, elem in enumerate(Untersuchungen):
    _patient_data[elem] = _h[i]

_JSON = createJSONObject(_h)
if(_use_stdin):
    print _JSON
else:
    with open(_filename_out, "w") as text_file:
        text_file.write(_JSON)
#===============================================================================
# print PatientBookfull.keys()
# print Untersuchungen
# print PatientBookSimple
# 
# print "Existiert die Datenbank?"
# print checkIfDatabaseExists("testdb", "test", "localhost", "abcd")
# print "Existiert die Tabelle?"
# print checkIfTableExists("testdb", "test", "localhost", "abcd", "cars")
# delTable("testdb", "test", "localhost", "abcd", "cars")
#===============================================================================

Patient = {'name':'Mustermann', 'surname':'Max', 'birthdate': '01011990', 'PID': 99999999}

#createNewTable("testdb", "test", "localhost", "abcd", "ErsterPatient", Patient)

cars = (
    ('Audi', 1, 52642),
    ('Mercedes', 2, 57127),
    ('Skoda', 3, 9000),
    ('Volvo', 4, 29000),
    ('Bentley', 5, 350000),
    ('Citroen', 6, 21000),
    ('Hummer', 7, 41400),
    ('Volkswagen', 8, 21600)
)
    
con = None
    
try:
         
    con = psycopg2.connect(database='testdb', user='test', password="abcd")  
       
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("CREATE TABLE cars(id INT PRIMARY KEY, name TEXT, price INT)")
    query = "INSERT INTO cars (name, id, price) VALUES (%s, %s, %s)"
    cur.executemany(query, cars)
        
    con.commit()
        
    
except psycopg2.DatabaseError, e:
        
    if con:
        con.rollback()
        
    print 'Error %s' % e    
    sys.exit(1)
        
        
finally:
        
    if con:
        con.close()
         


