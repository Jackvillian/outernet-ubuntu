#! /bin/bash
home=$(pwd)
apt-get install -y rsync git vim nano cmake gr-osmosdr libusb-1.0-0-dev ntp build-essential pkg-config
git clone https://github.com/Jackvillian/rtl_biast.git /usr/local/share/bias-t
mkdir -p /usr/local/share/bias-t/build
cd /usr/local/share/bias-t/build && cmake .. && make && make install
cp /usr/local/share/bias-t/build/src/rtl_biast /usr/local/bin/
cp -r $home/bin/* /usr/local/bin/
cp -r $home/lib/lib* /usr/lib
ln -s /usr/local/bin/ondd-2.2.0 /usr/local/bin/ondd
ln -s /usr/local/bin/sdr100-1.0.4 /usr/local/bin/sdr100
mkdir -p /etc/sdr_outernet
git clone https://github.com/Jackvillian/dump1090.git /usr/local/share/dump1090
cd /usr/local/share/dump1090/ && make
cp /usr/local/share/dump1090/dump1090 /usr/local/bin/
cp $home/outernet-run.sh /etc/sdr_outernet/outernet-run
ln -s  /etc/sdr_outernet/outernet-run /usr/local/bin/outernet-run
chmod 777 /usr/local/bin/outernet-run
echo "blacklist dvb_usb_rtl28xxu" >> /etc/modprobe.d/blacklist.conf
