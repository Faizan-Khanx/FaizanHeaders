#!/usr/bin/python3

import email
import re,sys
import argparse
from colorama import Fore, Back, Style

print(Fore.GREEN+"""
                                                                                                                                         
@@@@@@@@   @@@@@@   @@@  @@@@@@@@   @@@@@@   @@@  @@@     @@@  @@@  @@@@@@@@   @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@     @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!       @@!  @@@  @@!       @@!  @@!  @@@  @@!@!@@@     @@!  @@@  @@!       @@!  @@@  @@!  @@@  @@!       @@!  @@@  !@@       
!@!       !@!  @!@  !@!      !@!   !@!  @!@  !@!!@!@!     !@!  @!@  !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@!       
@!!!:!    @!@!@!@!  !!@     @!!    @!@!@!@!  @!@ !!@!     @!@!@!@!  @!!!:!    @!@!@!@!  @!@  !@!  @!!!:!    @!@!!@!   !!@@!!    
!!!!!:    !!!@!!!!  !!!    !!!     !!!@!!!!  !@!  !!!     !!!@!!!!  !!!!!:    !!!@!!!!  !@!  !!!  !!!!!:    !!@!@!     !!@!!!   
!!:       !!:  !!!  !!:   !!:      !!:  !!!  !!:  !!!     !!:  !!!  !!:       !!:  !!!  !!:  !!!  !!:       !!: :!!        !:!  
:!:       :!:  !:!  :!:  :!:       :!:  !:!  :!:  !:!     :!:  !:!  :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!      !:!   
 ::       ::   :::   ::   :: ::::  ::   :::   ::   ::     ::   :::   :: ::::  ::   :::   :::: ::   :: ::::  ::   :::  :::: ::   
 :         :   : :  :    : :: : :   :   : :  ::    :       :   : :  : :: ::    :   : :  :: :  :   : :: ::    :   : :  :: : :    
                                                                                                                                
                                                                                                                                                                                                                                    
                               Made With Love By Faizan Khan
                               
          INSTGRAM : EthicalFaizan || Cyber Crime Investigator , Ethical hacker & OSINT specialist                                    
   
     Faizan Headers Is A tool to analyze Email header to identify spoofed emails 
	""")

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file", help="enter the raw(original) email file",type=str)
args=parser.parse_args()

# Reading the file Need to take the file as command line arguments argparse
try:
    with open(args.file, 'r') as f:
        msg = email.message_from_file(f)
except FileNotFoundError:
    print(Fore.RED + "File not found" + Style.RESET_ALL)
    sys.exit(1)
except Exception as e:
    print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)
    sys.exit(1)

#if len(sys.argv) == 1:
#    parser.print_help()
#    sys.exit()


#f = open(args.file)
#msg = email.message_from_file(f)
#f.close()
#parser.print_help()
#parser = email.parser.HeaderParser()

headers = email.parser.HeaderParser().parsestr(msg.as_string())


meta={
	"message-id":"",
	"spf-record":False,
	"dkim-record":False,
	"dmarc-record":False,
	"spoofed":False,
	"ip-address":"",
	"sender-client":"",
	"spoofed-mail":"",
	"dt":"",
	"content-type":"",
	"subject":""
}

for h in headers.items():
	field = h[0].lower()
	value = h[1]

	# Message ID
	if field =="message-id":
		meta["message-id"]= value


	# Mail server sending the mail
	if field =="received":
		meta["sender-client"]= value

	# Authentication detected by mail server
	if field =="authentication-results":

		if(re.search("spf=pass",value)):
			meta["spf-record"]=True;

		if(re.search("dkim=pass",value)):
			meta["dkim-record"]=True
	
		if(re.search("dmarc=pass",value)):
			meta["dmarc-record"]=True

		if(re.search("does not designate",value)):
			meta["spoofed"]=True
		ip_check = re.search(r"(\d{1,3}\.){3}\d{1,3}", value)
		if ip_check:
			meta["ip-address"]= ip_check.group()


	if field =="reply-to":
		meta["spoofed-mail"]= value

	if field =="date":
		meta["dt"]= value

	if field =="content-type":
		meta["content-type"]= value

	if field =="subject":
		meta["subject"]= value

print(Fore.BLUE+"\n=========================Results=========================\n"+Style.RESET_ALL)

print(Fore.GREEN+"[+] Message ID"+meta["message-id"])

if(meta["spf-record"]):
	print(Fore.GREEN+"[+] SPF Records: PASS")
else:
	print(Fore.RED+"[+] SPF Records: FAIL")

if(meta["dkim-record"]):
	print(Fore.GREEN+"[+] DKIM: PASS")
else:
	print(Fore.RED+"[+] DKIM: FAIL")

if(meta["dmarc-record"]):
	print(Fore.GREEN+"[+] DMARC: PASS")
else:
	print(Fore.RED+"[+] DMARC: FAIL")

if(meta["spoofed"] and (not meta["spf-record"]) and (not meta["dkim-record"]) and (not meta["dmarc-record"])):
	print(Fore.RED+"[+] Spoofed Email Received")
	print(Fore.RED+"[+] Mail: "+meta["spoofed-mail"])
	print(Fore.RED+"[+] IP-Address:  "+meta["ip-address"])
else:
	print(Fore.GREEN+"[+] Authentic Email Received")
	print(Fore.GREEN+"[+] IP-Address:  "+meta["ip-address"])

print(Fore.GREEN+"[+] Provider "+meta["sender-client"])
print(Fore.GREEN+"[+] Content-Type: "+meta["content-type"])
print(Fore.GREEN+"[+] Date and Time: "+meta["dt"])
print(Fore.GREEN+"[+] Subject: "+meta["subject"]+"\n\n")
print(Style.RESET_ALL)
