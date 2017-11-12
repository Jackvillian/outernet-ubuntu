import os, shutil,stat
from tzlocal import get_localzone
import configparser
from crontab import CronTab

def create_config(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "FREQ", "")
    config.set("Settings", "SYMBOL_RATE", "4200")
    config.set("Settings", "ENABLE_BIAST", "0")
    config.set("Settings", "UNCERTAINTY_FREQ", "4000")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)






tz = get_localzone()
print "OUTERNET BY SDR-RTL ON LINUX MACHINE\n          INSTALL START\n####################################"
envfile=open('.env','w')
envfile.write('export LD_LIBRARY_PATH="/usr/local/sdr.d/starsdr-rtlsdr/"\n')
print "Location setting by your timezone:\r"
loc=str(tz).split(os.sep)
print tz
if loc[0]=="Europe" or loc[0]=="Africa":
    frec=1546.25
elif loc[0] == "America":
    frec=1539.8725
elif loc[0] == "Asia" or "Australia" :
    frec=1545.9525
print "configure location settings, tuner set f=", frec,"MHZ"



if __name__ == "__main__":
    path = "etc/outernet/settings.conf"
    update_setting(path,"Settings","FREQ",str(frec))



print "\nCOPY BINARIES:"
PEFIX_DIR_PATH = "/usr/local/"

LIST_DIRS=['bin/','sdr.d/','share/outernet/']
BIN_LIST=['ondd-2.2.0','rtl_biast','sdr100-1.0.4']
CACHE_PATH="/var/spool/ondd"
DOWNLOADS_PATH="/var/downloads"
for dir in LIST_DIRS:
    try:
        if os.path.isdir(PEFIX_DIR_PATH+dir):
            shutil.rmtree(PEFIX_DIR_PATH+dir)
        os.makedirs(PEFIX_DIR_PATH+dir)
        print PEFIX_DIR_PATH+dir
    except:
        print PEFIX_DIR_PATH + dir+"\n"
        print "alredy exist or permission denied!\n"

shutil.copytree('sdr.d/starsdr-mirics', PEFIX_DIR_PATH+"sdr.d/starsdr-mirics")
shutil.copytree('sdr.d/starsdr-rtlsdr', PEFIX_DIR_PATH+"sdr.d/starsdr-rtlsdr")
shutil.copytree('etc/outernet/', '/etc/outernet/')
for bins in BIN_LIST:
    shutil.copy('bin/'+bins, PEFIX_DIR_PATH + 'bin/'+bins)
    st = os.stat(PEFIX_DIR_PATH + 'bin/'+bins)
    os.chmod(PEFIX_DIR_PATH + 'bin/'+bins, st.st_mode | stat.S_IEXEC)


print "\nCREATE RECEIVED DATA DIRS:"
print CACHE_PATH
print DOWNLOADS_PATH
if os.path.isdir(CACHE_PATH):
    shutil.rmtree(CACHE_PATH)
    os.makedirs(CACHE_PATH)
if os.path.isdir(DOWNLOADS_PATH):
    shutil.rmtree(DOWNLOADS_PATH)
    os.makedirs(DOWNLOADS_PATH)



