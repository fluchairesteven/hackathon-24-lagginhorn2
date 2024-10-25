
echo neo4j-admin database load --overwrite-destination=true --from-path=/tmp/data/ democrasci

docker exec -it neo4j /bin/bash

exit

docker run \
    -it \
    -v /srv/neo4j/data:/data \
    -v /srv/neo4j/upload:/tmp/data \
    neo4j:latest \
    /bin/bash

