function proxy_on() {
	export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com,*.lufthansa.com,*.dlh.de"
	
	local username="U815496"
	local password="skeletor"
	local server="57.20.4.150"
	local port="8080"	
    local pre="$username:$password@"

	export http_proxy="http://$pre$server:$port/"
	export https_proxy=$http_proxy
	export ftp_proxy=$http_proxy
	export rsync_proxy=$http_proxy
	export HTTP_PROXY=$http_proxy
	export HTTPS_PROXY=$http_proxy
	export FTP_PROXY=$http_proxy
	export RSYNC_PROXY=$http_proxy
}

function proxy_off(){
	unset http_proxy
	unset https_proxy
	unset ftp_proxy
	unset rsync_proxy
	unset HTTP_PROXY
	unset HTTPS_PROXY
	unset FTP_PROXY
	unset RSYNC_PROXY
    unset no_proxy
	echo -e "Proxy environment variables removed."
}

