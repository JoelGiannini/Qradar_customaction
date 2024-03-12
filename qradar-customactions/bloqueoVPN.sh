#!/bin/bash
 
# constantes
# ejecucion desde custom action
SCRIPT_PATH=custom_action_scripts
# ejecucion desde cli
# SCRIPT_PATH=.
 
# variables externas
LEGAJO=$1
 
#variables internas
SERVER=76.253.223.25
SENDER=no-reply@bbva.com
SUBJECT="Notificación bloqueo usuario/token VPN"
TEXT="El usuario $LEGAJO se ha bloqueado en el acceso a la VPN por sucesivos intentos fallido. Por favor, canalizar a través de su supervisor y/o referente del banco un \"Desbloqueo / Blanqueo de Consola RSA\" vía CRM"
 
#resolución email
export LDAP_URL='ldap://76.254.133.136:10389'
export LDAPUSER='cn=UPRORSAQ,ou=People,c=arg,o=BBVA'
export LDAPPASS="$2"
export LDAPBASEDN='ou=People,c=arg,o=BBVA'
 
MAIL=$( python3 "$SCRIPT_PATH/ldapLookup.py" --user "$LEGAJO" )
 
if [ "$MAIL" == "desconocido" ]; then
  MAIL="ciberseguridad-arg@bbva.com"
  SUBJECT="$SUBJECT - ERROR"
fi
 
#echo "Enviando a $MAIL"
python3 "$SCRIPT_PATH/sendmail.py" --server "$SERVER" --dest "$MAIL" --sender "$SENDER" --subject "$SUBJECT" --text "$TEXT"


