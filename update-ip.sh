#!/bin/sh
ipNew=$(curl -s ip.skittel.de)
name=$(cat "$1")
currentdate=date+"%d.%m.%y" 

update_ip_and_git() {
	echo $ipNew > $1
	git add ip-raspberry-pi-3
	git commit ip-raspberry-pi-3 -m"ip update from - $currentdate"
	git push ip-raspberry-pi-3
}

if [ -z "$name" ]
then
	update_ip_and_git $1
elif [[ "$ipNew" != *"$name"* ]]
then
	update_ip_and_git $1
else
	echo "nichts ende"
fi
