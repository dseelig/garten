#!/bin/sh
ipNew=$(curl -s ip.skittel.de)
name=$(cat "$1")

update_ip_and_git() {
	echo $ipNew > $1
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
