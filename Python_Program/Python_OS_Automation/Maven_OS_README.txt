1. Create EC2 instance named "buildserver".
2. Login ssh -i "key.pem" ubuntu@ip
3. sudo apt update
4. sudo apt install openjdk-11-jdk -y
5. sudo apt install maven -y
6. wget https://archive.apache.org/dist/maven/maven-3/3.9.3/binaries/apache-maven-3.9.3-bin.tar.gz
7. tar xzvf apache-maven-3.9.3-bin.tar.gz
8. sudo mv apache-maven-3.9.3 /opt/
9. /opt/apache-maven-3.9.3/bin/mvn -version
10. git clone https://github.com/devopshydclub/vprofile-project.git
11. cd vprofile-project
12. mvn validate
13. mvn test
14. mvn clean install - now able to see vprofile-v2.war file in target folder
15. ls /home/ubuntu/.m2/repository/
16. mvn install
17. rm -rf /home/ubuntu/.m2/repository/
18. mvn clean
19. /opt/apache-maven-3.9.3/bin/mvn install
20. vim pom.xml -> v2 to v3 -> :wq
21. mvn clean install
22. ls target/ -> show vprofile-v3.war (artifact)

For AWS CloudShell

1. Open AWS CloudShell
2. cat /opt/os-release
3. sudo yum search jdk
4. sudo yum install java-1.8.0-openjdk
5. sudo  yum install maven -y
6. git clone https://github.com/devopshydclub/vprofile-project.git
7. aws s3 ls
8. aws s3 mb s3://maven-arts
9. aws s3 cp target/vprofile-v2.war s3://maven-arts
