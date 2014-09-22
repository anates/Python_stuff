# -*- coding: utf-8 -*-
'''
Created on 19.09.2014

@author: roland
'''

import hl7
import psycopg2
from numpy.distutils.mingw32ccompiler import _TABLE
from httplib2 import _entry_disposition

def getNames(parsed_message):
    '''Zieht sich die Namen des Patienten aus der HL7-Nachricht (funktioniert)'''
    if(isinstance(parsed_message, hl7.Message) == False):
        return ('','')
    else:
        return (str(parsed_message.segment("PID")[5][0][1][0]), str(parsed_message.segment("PID")[5][0][0][0]))

def getObservablen(parsed_message):
    '''Gibt sämtliche vorgenommenen Untersuchungen (ohne weitere Infos) zurück (funktioniert)'''
    Observables = {}
    if(isinstance(parsed_message, hl7.Message) == False):
        return ('','')
    else:
        for elem in xrange(len(parsed_message) + 1):
            if elem >= 3:
                Observables[elem-3] = parsed_message[elem-1][0][0]
    return Observables

def getWhatHappened(parsed_message):
    '''Noch nicht in Funktion, da medizinischer Background fehlt'''
    Observables = {}
    if(isinstance(parsed_message, hl7.Message) == False):
        return ('','')
    else:
        for elem in xrange(len(parsed_message) + 1):
            if elem >= 3:
                Observables[elem-3] = parsed_message[elem-1][0][0]
    return Observables

def checkIfDatabaseExists(_database, _user, _host, _password):
    '''Schaut, ob Datenbank überhaupt vorhanden ist (funktioniert)'''
    con = None
    con = psycopg2.connect(database=_database, user=_user, host=_host, password=_password)
    cur = con.cursor()
    cur.execute("SELECT exists(SELECT 1 from pg_catalog.pg_database where datname = %s)", (_database,))
    ver = cur.fetchone()[0]
    return ver

def checkIfTableExists(_database, _user, _host, _password, _table):
    '''Schaut, ob Tabelle in Datenbank vorhanden ist (funktioniert)'''
    con = None
    con = psycopg2.connect(database=_database, user=_user, host=_host, password=_password)
    cur = con.cursor()
    cur.execute("select exists(select * from information_schema.tables where table_name=%s)", (_table,))
    ver = cur.fetchone()[0]
    return ver

def checkIfEntryExists(_database, _user, _host, _password, _table, _entry):
    '''Schaut, ob der Eintrag bereits vorhanden ist'''
    con = None
    con = psycopg2.connect(database=_database, user=_user, host=_host, password=_password)
    cur = con.cursor()
    cur.execute("select count(*) from 'testdb' where name = %s", (_entry,))
    ver = cur.fetchone()[0]
    return ver

def printColumnNames(_database, _user, _host, _password, _table):
    '''Gibt die Zeilennamen der Datenbank auf die Konsole aus'''
    con = None
    con = psycopg2.connect(database=_database, user=_user, host=_host, password=_password)
    cur = con.cursor()
    query = 'select column_name from information_schema.columns where table_name=cars'
    cur.execute(query)
    ver = cur.fetchone()[0]
    return ver
            
def delTable(_database, _user, _host, _password, _table):
    '''Löscht die Tabelle, falls vorhanden (funktioniert)'''
    con = None    
    con = psycopg2.connect(database=_database, user=_user, password=_password)  
    cur = con.cursor()    
    query = "DROP TABLE IF EXISTS %s" % _table
    cur.execute(query)

def createNewTable(_database, _user, _host, _password, _tablename):
    '''Legt einen neuen Patienten an'''
    con = None    
    con = psycopg2.connect(database=_database, user=_user, password=_password)  
    cur = con.cursor()
    if(checkIfTableExists(_database, _user, _host, _password, _tablename)):
        return False
    else:
        #query = "CREATE TABLE %s(name TEXT PRIMARY KEY, surname TEXT, price INT)"
        #Hier kann ich leider noch nichts einfügen, da ich mich noch nicht so gut in HL7 auskenne...
        return True