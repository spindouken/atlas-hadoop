# atlas-hadoop

- HADOOP DOCKER SET-UP ENVIRONMENT BY INCLUDING:
    - Include xml files, start-up scripts in project local directory, and Dockerfile in project directory  (core-site.xml, hdfs-site.xml, hue.ini, mapred-site.xml, yarn-site.xml, ssh-config.sh, start-all.sh)
    - build docker image from Dockerfile using:
    
    ```python
    docker build -t hadoop3-dev .
    ```
    
    - Assuming the image creation went well, run a container for the hadoop dev environment using:
    
    ```bash
    sudo docker run  -v "$(pwd)":/scripts --hostname=hadoop3 -p 8088:8088 -p 9870:9870 -p 9864:9864 -p 19888:19888 -p 8042:8042 -p 8888:8888 --name hadoop3-dev -d hadoop3-dev
    ```
    
    This command mounts the current directory to `/scripts` in the container, and names the container `hadoop3-dev'
    
    To access the shell of your `hadoop3-dev` container:
    ```bash
    docker exec -it python-mongo-dev /bin/bash
    ```
