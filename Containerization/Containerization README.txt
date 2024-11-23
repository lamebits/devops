VProfile Containerization

1.  Understand requirement of the vprofile project

MySQL (Database SVC)        => 8.0.33
Memcache (DB Caching SVC)   => 1.6
RabbitMQ (Broker/Queue SVC) => 4.0
JDK                         => JDK 21
MAVEN                       => Maven 3.9.9
Tomcat (Application SVC)    => 10, jdk21
Nginx (Web SVC)             => 1.27

Tags:

mysql:8.0.33
memcache:latest
rabbitmq:latest
maven:3.9.9-eclipse-temurin-21-jammy
tomcat:10-jdk21
nginx:latest

2. Open git bash and go to below path
C:\Users\meena\vagrant-vms\devops\Containerization\vprofile-project-containers\vagrant\windowsAndMacIntel

3. Run command : vagrant up
4. Install docker engine in VM
https://docs.docker.com/engine/install/ubuntu/

4.1 # Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

4.2 # Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

4.3 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
4.4 usermod -aG docker vagrant // vagrant user also run the docker command

5. Create three repository vprofileapp, vprofiledb, vprofileweb in docker hub.

6. create structure in directory
Docker-files
    -> app
         -> Dockerfile
    -> db
         -> Dockerfile
    -> web
         -> Dockerfile

6.1 app -> Dockerfile
FROM maven:3.9.9-eclipse-temurin-21-jammy AS build_image
RUN apt-get update && apt-get install -y curl
RUN curl -I https://github.com
RUN git clone https://github.com/hkhcoder/vprofile-project.git
RUN cd vprofile-project && git checkout containers && mvn install

FROM tomcat:10-jdk21
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=build_image vprofile-project/target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
CMD ["catalina.sh", "run"]

6.2 db -> Dockerfile
FROM mysql:8.0
LABEL ProjectName="vprofile"
LABEL Username="Meenal"

ENV MYSQL_ROOT_PASSWORD="vprodbpass"
ENV MYSQL_DATABASE="accounts"

ADD db_backup.sql /docker-entrypoint-initdb.d/db_backup.sql

6.3 web -> Dockerfile

nginvproapp.conf  is in same directory

FROM nginx:1.27
LABEL ProjectName="vprofile"
LABEL Username="Meenal"

RUN rm -rf /etc/nginx/conf.d/default.conf
ADD nginvproapp.conf /etc/nginx/conf.d/vproapp.conf

7. Create docker-compose.yml file
services:
  vprodb:
    build:
      context: ./Docker-files/db
    image: meenalmate/vprofiledb
    container_name: vprodb
    ports: 
      - "3306:3306"
    volumes:
      - vprodbdata:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=vprodbpass

  vprocache01:
    image: memcached
    container_name: vprocache01
    ports: 
      - "11211:11211"

  vpromq01:
    image: rabbitmq
    container_name: vpromq01
    ports: 
      - "15672:15672"
    environment: 
      - RABBITMQ_DEFAULT_PASS = guest
      - RABBITMQ_DEFAULT_USER = guest

  vproapp:
    build:
      context: ./Docker-files/app
    image: meenalmate/vprofileapp
    container_name: vproapp
    ports: 
      - "8080:8080"
    volumes:
      - vproappdata:/usr/local/tomcat/webapps

  vproweb:
    build:
      context: ./Docker-files/web
    image: meenalmate/vprofileweb
    container_name: vproweb
    ports: 
      - "80:80"

volumes:
  vprodbdata: {}
  vproappdata: {}



8. Build and Run
8.1 login vagrant
8.2  cd /vagrant/ 
8.3 docker compose build
8.4 docker compose up -d
	- docker compose down : for deleting containers
8.5 check url by ip address
	-> ip addr show
8.6 Login to docker hub
	-> docker login
8.7 Push the docker images in dockerhub
	-> docker push <imagename>
8.8 Cleanup
	-> docker compose down
	-> docker volume rm <volumename>
	0r
	-> docker system prune -a // it will remove containers, images, caches etc.




