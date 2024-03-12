
##Qradar custom-action for blocked users

####Problem:

- When a blocking action is executed in qradar it does not inform the user of the blocking


- Solution:
     Generate 3 scripts:
      ldapLookup.py 
      This script receives the user name of qradar and checks its email in ldap.

	   sendmail.py
	   This script send an email informing the user of the blocking
	   through the mail obtained by the previous script

	   lockVPN.sh
	   This script interacts with qradar and executes the previous scripts.
Requirements:
Transport ldap user:
UPRORSAQ


