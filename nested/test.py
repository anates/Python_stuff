'''
Created on 16.09.2014

@author: roland
'''
import hl7
import sys
from Functions import getNames
from Functions import getObservablen



message = ''
# message2 = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
# message2 += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
# message2 += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
# message2 += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F'
for line in sys.stdin:
    message += line[:-1]

#print message
h = hl7.parse(message)

#print isinstance(h, hl7.Message)
#print type(h)
#-------------------------------------------------------- print h.segment("PID")
#--------------------------------------------------- print len(h.segment("PID"))
#------------------------------------------------ print len(h.segment("PID")[5])
#--------------------------------------------- print len(h.segment("PID")[5][0])
#------------------------------------------ print len(h.segment("PID")[5][0][0])
#--------------------------------------- print len(h.segment("PID")[5][0][0][0])
print getNames(h)
PatientBookfull = {getNames(h):h}
PatientBookfull[getNames(h)] = h
PatientBookSimple = {getNames(h):getObservablen(h)}
Untersuchungen = getObservablen(h)
print PatientBookfull.keys()
print Untersuchungen
print PatientBookSimple

