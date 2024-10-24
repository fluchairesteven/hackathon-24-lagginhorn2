docker rm neo4j
docker run \
    -it \
    --name neo4j \
    -v /srv/neo4j/data:/data \
    -v /srv/neo4j/upload:/tmp/data \
    --restart always \
    --publish=7474:7474 --publish=7687:7687 \
    neo4j:latest \
    /bin/bash

