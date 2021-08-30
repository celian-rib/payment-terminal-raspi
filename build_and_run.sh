#/bin/bash

red=`tput setaf 1`
green=`tput setaf 2`
cyan=`tput setaf 6`
yellow=`tput setaf 3`
reset=`tput sgr0`

error () {
    echo
    echo
    echo "${red}[[[ ERROR ]]]${reset}"
    exit
}

success () {
    echo
    echo "${green}$1${reset}"
}

title () {
    echo
    echo "${cyan}[ $1 ]${reset}"
}

step () {
    echo
    echo "${yellow}$1${reset}"
    $2 || error
}


title "Starting backend application"

if test "$(docker ps | wc -l)" -gt 1 ;then
    step "Killing existing container" "docker rm $(docker stop $(docker ps -a -q --filter ancestor=backend --format="{{.ID}}"))"
else
    success "No container running found"
fi

step "Build backend image" "docker image build -t backend ./backend"

step "Run backend container" "docker run -p 5000:5000 -v $(pwd)/backend/db:/usr/src/app/db -d backend"

step "All running containers" "docker ps"

success "APPLICATION STARTED"