#/bin/bash

red=`tput setaf 1`
green=`tput setaf 2`
cyan=`tput setaf 6`
yellow=`tput setaf 3`
reset=`tput sgr0`

ARG=$1

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

kill-existing-container () {
    if test "$(docker ps | wc -l)" -gt 1 ;then
        step "Killing existing container" "docker rm $(docker stop $(docker ps -a -q --filter ancestor=backend --format="{{.ID}}"))"
    else
        success "No container running found"
    fi
}

if ! test $1; then
    title "Mode selection"
    echo
    echo "${yellow}- Build only      [b]${reset}"
    echo "${cyan}- Build and Run   [r]${reset}"
    echo "${green}- Run last builds [l]${reset}"

    read mode
else
    mode="$1"
fi

kill-existing-container

title "Starting backend application"

if test "$mode" = "b" || test "$mode" = "r"; then
    step "Build backend image" "docker image build -t backend ./backend"
fi

if ! test "$mode" = "b"; then
    step "Run backend container" "docker run -p 5000:5000 -v $(pwd)/backend/db:/usr/src/app/db -d backend"
fi

step "All running containers" "docker ps"

success "APPLICATION STARTED"