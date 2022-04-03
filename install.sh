echo "Building WikiApp Image..."
docker build -t wiki-app:1.0 .
echo "Running docker-compose..."
docker-compose up