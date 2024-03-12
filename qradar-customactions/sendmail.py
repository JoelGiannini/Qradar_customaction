#!/usr/bin/python
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import argparse
import os
import sys

def send_mail(send_from, send_to, subject, text, files=None,server="127.0.0.1"):
  assert isinstance(send_to, list)
  msg = MIMEMultipart()
  msg['From'] = send_from
  msg['To'] = COMMASPACE.join(send_to)
  msg['Date'] = formatdate(localtime=True)
  msg['Subject'] = subject

  msg.attach(MIMEText(text))

  for f in files or []:
    with open(f, "rb") as fil:
      part = MIMEApplication(fil.read(), Name=basename(f))
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    msg.attach(part)

  smtp = smtplib.SMTP(server)
  smtp.sendmail(send_from, send_to, msg.as_string())
  smtp.close()

my_parser = argparse.ArgumentParser(description='Send an email')

my_parser.add_argument('--server', type=str, help='Smtp server')
my_parser.add_argument('--dest', 	nargs='+', type=str, help='Recipient')
my_parser.add_argument('--sender', type=str, help='Sender')
my_parser.add_argument('--files',  nargs='+', type=str, help='File to attach')
my_parser.add_argument('--subject',type=str, help='Subject of the email')
my_parser.add_argument('--text', type=str, help='Message')

args = my_parser.parse_args()

server_email  = args.server
to_email      = args.dest
from_email    = args.sender
files_email   = args.files
subject_email = args.subject
text_email    = args.text

send_mail( from_email, to_email, subject_email, text_email, files_email, server_email)
