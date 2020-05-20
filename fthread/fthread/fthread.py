
from urllib.request import urlopen
import os
import time
from pathlib import Path
from time import process_time 
import shutil
import concurrent.futures
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage



FLAGS = ['aa','ac','ae','af','ag','aj','al','am','an','ao','aq','ar','as','at','au','av','ax',
    'ba','bb','bc','bd','be','bf','bg','bh','bk','bl','bm','bn','bo','bp','bq','br','bt','bu','bv','bx','by',
    'ca','cb','cc','cd','ce','cf','cg','ch','ci','cj','ck','cm','cn','co','cr','cs','ct','cu','cv','cy',
    'da','dj','do','dr','dx',
    'ec','ee','eg','ei','ek','en','er','es','et','ez',
    'fi','fj','fk','fm','fo','fp','fr','fs',
    'ga','gb','gg','gh','gi','gj','gk','gl','gm','gq','gr','gt','gv','gy',
    'ha','hk','hm','ho','hr','hu',
    'ic','id','im','in','io','ip','ir','is','it','iv','iz',
    'ja','je','jm','jn','jo',
    'ke','kg','kn','kr','ks','kt','ku','kv','kz',
    'la','le','lg','lh','li','lo','ls','lt','lu','ly',
    'ma','mc','md','mg','mx',
    'nc','ne','nf','ng','nh','ni','nl','no','np','nr','ns','nu','nz',
    'od',
    'pa','pc','pe','pk','pl','pm','po','pp','pu',
    'qa',
    'ri','rm','rn','ro','rp','rq','rs','rw',
    'sa','sb','sc','se','sf','sg','sh','si','sk','sl','sm','sn','so','sp','st','su','sv','sw','sx','sy','sz',
    'tb','td','th','ti','tk','tl','tn','to','tp','ts','tt','tu','tv','tw','tx','tz',
    'ug','uk','um','up','us','uv','uy','uz',
    'vc','ve','vi','vm','vq','vt',
    'wa','wf','wq','ws','wz',
    'ym',
    'za','zi']

picture_page = "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/"
path = os.getcwd() + "/flags"

#create a directory in path directory to place dowloaded flags
def make_dir():
    global path

    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)           
        os.makedirs(path)

#function to take arg and find flag on website
def processfun(l):
    placeholder = ["xx", "-lgflag.gif"]
    placeholder[0] = l
    endurl = ''.join(placeholder)
    finalpage = picture_page + endurl
    page1 = urlopen(finalpage)
    my_picture = page1.read()
    global path
    savename = path + "/" + endurl
    fout = open(savename, "wb")
    fout.write(my_picture)
    fout.close()


def main():
    make_dir()
    
    #timers for process time and overall time
    start = time.time()
    t1_start = process_time()  
    #using concurrent.futures.Threadpoolexecutor to map flags and run through function
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for prime in executor.map(processfun, FLAGS):
            pass

    

    t1_stop = process_time() 
    end = time.time()
    total_size = 0
    global path
    start_path = path
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path,f)
            total_size += os.path.getsize(fp)

    newpath = os.getcwd()
    filename = newpath + "/fthread.txt"
    if os.path.exists(filename):
        os.remove(filename)

    #Write information to file and close file
    fo = open(filename, 'w')
    fo.write("Number of bytes: " + str(total_size) + "\n")
    fo.write("Execution time: " + str(end - start) + "\n")
    fo.write("CPU time: " + str(t1_stop - t1_start) + "\n")
    fo.close()
    
    #Build email specifics
    mail_content = "Here you go, Professor Durney! This is Dallin Bise if my email does not indicate that."
    The mail addresses and password
    sender_address = 'dbise17@gmail.com'
    sender_pass = '***************'
    receiver_address = 'bdurney1@gmail.com'

    #Set up smtp session, sign in and send email
    message = MIMEMultipart()

    message['From'] = sender_address

    message['To'] = receiver_address

    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line

    The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    Create SMTP session for sending the mail

    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port

    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password

    file = os.getcwd() + "/flags/" + "us-lgflag.gif"
    fp = open(file, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    message.attach(img)

    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)

    session.quit()

    print('Mail Sent')

if __name__ == '__main__':
    main()