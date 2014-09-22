'''
Created on 19.09.2014

@author: roland
'''

import hl7
import psycopg2
from numpy.distutils.mingw32ccompiler import _TABLE
#Zieht sich die Namen des Patienten aus der HL7-Nachricht
def getNames(parsed_message):
    if(isinstance(parsed_message, hl7.Message) == False):
        return ('','')
    else:
        return (str(parsed_message.segment("PID")[5][0][1][0]), str(parsed_message.segment("PID")[5][0][0][0]))


#Gibt saemtliche vorgenommenen Untersuchungen (ohne weitere Infos) aus
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

#Schaut, ob Datenbank ueberhaupt vorhanden ist
def checkIfDatabaseExists(_database, _user, _host, _password):
    con = None
    con = psycopg2.connect(database=_database, user=_user, host=_host, password=_password)
    cur = con.cursor()
    cur.execute("SELECT exists(SELECT 1 from pg_catalog.pg_database where datname = %s)", (_database,))
    ver = cur.fetchone()[0]
    return ver

#Schaut, ob Tabelle in Datenbank vorhanden ist
def checkIfTableExists(_database, _user, _host, _password, _table):
    con = None
    con = psycopg2.connect(database=_database, user=_user, host=_host, password=_password)
    cur = con.cursor()
    cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (_table,))
    ver = cur.fetchone()[0]
    return ver
                