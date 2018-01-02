#! /bin/bash
lat=$(whereami |sed 's/,/ /g'|awk '{print $1}')
lon=$(whereami |sed 's/,/ /g'|awk '{print $2}')
ENABLE_BIAS_T=0
rtl_biast -d 0 -b $ENABLE_BIAS_T
dump1090 --interactive --net --lat $lat --lon $lon --modeac --mlat --write-json $data_home
