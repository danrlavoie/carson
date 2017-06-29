#!/usr/bin/env python

# Email-specific imports
import smtplib
from email.message import EmailMessage
from email.headerregistry import Address

class Notify:
	def __init__(self):
		pass
	def send_email(self, subject, message, from_display_name, from_address, to_address):
		msg = EmailMessage()
		msg['Subject'] = subject
		msg['From'] = Address(display_name=from_display_name, addr_spec=from_address)
		msg['To'] = Address(addr_spec=to_address)
		msg.set_content(message)
		# Send the message via local SMTP server.
		# TODO: Set up a local SMTP server to work with this function.
		with smtplib.SMTP('localhost') as s:
			s.send_message(msg)

def main():
	n = Notify()
	# n.send_email('Test', 'HELLO WORLD', 'Carson', 'dan.r.lavoie@gmail.com', 'dan.r.lavoie@gmail.com')
if __name__ == '__main__':
	main()