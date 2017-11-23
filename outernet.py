import os, sys,time
import subprocess
from daemonize import Daemonize
import os, shutil,stat
from tzlocal import get_localzone
import configparser


confpath = "/etc/outernet/settings.conf"

def get_config(path):
    """
    Returns the config object
    """

    config = configparser.ConfigParser()
    config.read(path)
    return config

def biast_enable(e):

    return e

print "#####'reading config'#####"
ebiast=get_config(confpath)['Settings']['enable_biast']
freq= get_config(confpath)['Settings']['freq']
srate=get_config(confpath)['Settings']['symbol_rate']
ufreq=get_config(confpath)['Settings']['uncertainty_freq']




if ebiast == 1:
    print "INFO: bias_t is enable"
else:
    print "INFO: bias_t is disable"
tz = get_localzone()

print "INFO: cache path "+ "/var/spool/ondd"
print "INFO: downloads path " + "/srv/downloads"
print "INFO: your location "+ str(tz)
print "##########################"
CMD="/usr/local/bin/sdr100 -f " + freq + " -r " +srate+" -u "+ufreq+" -s 1 -b 0.2 -w"
print "start command: ",CMD
p=subprocess.Popen(CMD, shell=True, bufsize=256, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

for line in p.stdout:
    print(">>> " + str(line.rstrip()))
    p.stdout.flush()


def erptool():
    proc = subprocess.Popen (CMD, shell=False, stdout=subprocess.PIPE)
    out = proc.communicate()[0]
    print(out),
erptool()

#def main():
#    while True:
#        log=open('/var/log/outernet-demod',"a")
#        proc = subprocess.Popen("sdr100", shell=True)
#        log.write(proc.stderr)
#        time.sleep(5)



#if __name__ == '__main__':
#        myname=os.path.basename(sys.argv[0])
#        print myname
#        pidfile='/tmp/%s' % myname       # any name
#        daemon = Daemonize(app=myname,pid=pidfile, action=main)
#        Daemonize()
#        print pidfile
#        daemon.start()
