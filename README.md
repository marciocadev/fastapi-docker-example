# fastapi-docker-example

# Build
- export DEBUG='True'
- docker-compose build

# Run
- docker-compose up -d


## Remove docker image <none>
docker rmi $(docker images -f 'dangling=true' -q)