cd backend

echo "----- [ STARTING BACKEND APPLICATION ] -----"
echo "[ OK ] -- Build backend image"
docker run -p 5000:5000 -v $(pwd)/db:/usr/src/app/db -d backend
echo "[ OK ] -- Start backend container"
docker run -p 5000:5000 -v $(pwd)/db:/usr/src/app/db -d backend
echo "[ OK ] -- Backend started"

cd ../hardware

echo "----- [ STARTING HARDWARE APPLICATION ] -----"
echo "[ SKIP ] -- No suitable application yet"