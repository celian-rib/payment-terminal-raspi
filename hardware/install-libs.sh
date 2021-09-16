if [ ! -d ./src/libs ]; then
	mkdir ./src/libs
	cd ./src/libs
	git clone https://github.com/HubCityLabs/py532lib.git
	
else
	echo "Libs already installed locally"
fi
