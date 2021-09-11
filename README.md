# fastapi-docker-example

# Build
- export DEBUG='True'
- docker-compose build

# Run
- docker-compose up -d

# Down
- docker-compose down -d

# Remove all images
docker rmi $(docker image ls -q)

## Remove docker image <none>
docker rmi $(docker image ls -f 'dangling=true' -q)
