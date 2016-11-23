#!/bin/sh

link_dir="$(dirname $(readlink -f $0))/link"


function link_recursive() {
	local source_dir="$1"
	for source in $source_dir/*; do
		if [ -d "$source" ]; then
			link_recursive "$source"
		else
			link_file "$source"
		fi
	done
}

function link_file() {
	local source_file="$1"
	echo $source_file
	target_file=$(echo "${source_file#$linkDir}" | sed "s/home/home\/$USER/")
	echo $target_file
}


link_recursive "$link_dir"
