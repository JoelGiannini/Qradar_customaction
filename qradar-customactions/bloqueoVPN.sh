#!/bin/bash
 
# constantes
# ejecucion desde custom action
SCRIPT_PATH=custom_action_scripts
# ejecucion desde cli
# SCRIPT_PATH=.
 
# variables externas
LEGAJO=$1
 
#variables internas
SERVER=IP
SENDER=no-reply@mail.com
SUBJECT="Notificación bloqueo usuario/token VPN"
TEXT="El usuario $LEGAJO se ha bloqueado en el acceso a la VPN por sucesivos intentos fallido. Por favor, canalizar a través de su supervisor y/o referente del banco un \"Desbloqueo / Blanqueo de Consola RSA\" vía CRM"
 
#resolución email
export LDAP_URL='ldap://LDAPIP:10389'
export LDAPUSER='cn=UPRORSAQ,ou=People,c=arg,o='
export LDAPPASS="$2"
export LDAPBASEDN='ou=People,c=arg,o='
 
MAIL=$( python3 "$SCRIPT_PATH/ldapLookup.py" --user "$LEGAJO" )
 
if [ "$MAIL" == "desconocido" ]; then
  MAIL="ciberseguridad-arg@mail.com"
  SUBJECT="$SUBJECT - ERROR"
fi
 
#echo "Enviando a $MAIL"
python3 "$SCRIPT_PATH/sendmail.py" --server "$SERVER" --dest "$MAIL" --sender "$SENDER" --subject "$SUBJECT" --text "$TEXT"


