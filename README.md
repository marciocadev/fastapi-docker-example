# fastapi-docker-example

## Remove docker image <none>
docker rmi $(docker images -f 'dangling=true' -q)