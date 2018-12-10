""""
   Unix Password Cracker
   Author : Chirag Sonkamble 
"""
import sys,os
import crypt
from subprocess import call 

#Code for calculating SHA512 Hash Shadow
def testPass_SHA512(hashValue,salt2):
    input_salt = '$6$'+str(salt2)
    dictFile = raw_input("Enter dictionary: ") 
    passwordfile = open(dictFile,'r')
    for line in passwordfile.readlines():
        line = line.split("\n")[0]
        calcHashValue = crypt.crypt(line,input_salt)
        if hashValue == calcHashValue:
            print "*"*60
            print "Congrats!\nPassword Found"
            print "-"*60
            print "Password is "+line
            sys.exit(0)
        else:
            print "Invalid Password"

#Code for calculating MD5 Hash Shadow
def testPass_MD5(hashValue):
    input_salt = 'X0'
    dictFile = raw_input("Enter dictionary: ")
    passwordfile = open(dictFile,'r')
    for line in passwordfile.readlines():
        line = line.split("\n")[0]
        calcHashValue = crypt.crypt(line,input_salt)
        if hashValue == calcHashValue:
            print "*"*60
            print "Congrats!\nPassword Found"
            print "-"*60
            print "Password is "+line
            sys.exit(0)
        else:
            print "Invalid Password"

path = os.getcwd()
path1 = path.split("/")[2]
#If any error occurs please provide absolute path instead of 'path1' nd 'path' to create password file.s
call("unshadow /etc/passwd /etc/shadow > ~/"+path1+"/fileToCrack" , shell=True)
ip_user = raw_input("Enter user\t: ")
userfile = open("/"+path+"/fileToCrack",'r')
f = 0
for usr in userfile.readlines():
    usr = usr.split("\n")[0]
    user = usr.split(":")[0]
    if user == ip_user:
        f =1
        hashValue = usr.split(":")[1]
        if hashValue[0:2] == 'X0':
            testPass_MD5(hashValue)
        else:
            salt2 = hashValue.split("$")[2]
            testPass_SHA512(hashValue,salt2)

if f == 0:        
    print "User not found"
    
"""

root@kali:~/Downloads# python UnixCracker.py 
Enter user	: root
Enter dictionary: dictionary.txt
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
Invalid Password
************************************************************
Congrats!
Password Found
------------------------------------------------------------
Password is toor

"""
