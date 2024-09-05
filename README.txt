AWS Lift and Shift Application Website

1. Purchase DomainName
2. Register on AWS certificate Manager
	a. Copy CNAME and CVALUE and Add into domainname hosting website.
	b. Check Status : issued.
3. Create security group[vprofile-ELB-sg].
	HTTP : Anywhere
	HTTPS : Anywhere
4. Create another security group[vprofile-app-sg]
	Allow traffic only from vprofile-ELB-sg 8080 portno.
	Custom TCP -> 22 -> MyIP
	custom TCP -> 8080 -> MyIP
5. Create another security group[vprofile-backend-sg]
	Select MySQL-Aurora -> 3306 -> vprofile-app-sg
	Select Custom TCP -> 11211 -> vprofile-app-sg
	Select Custom TCP -> 5672 -> vprofile-app-sg
	Select Custom TCP -> 22 -> MyIP
	Select All traffic -> vprofile-backend-sg(itself) -> vprofile-app-sg
6. Create Key-Pair[vprofile-prod-key].
7. Clone the git project "https://github.com/devopshydclub/vprofile-project.git"
8. go to aws-liftAndShift branch.
9. Create instances 
	a. vprofile-db01(mysql) : Amazon Linux Service -> vprofile-backend-sg -> Add script into advance setting
		#!/bin/bash
		DATABASE_PASS='admin123'
		sudo yum update -y
		sudo yum install epel-release -y
		sudo yum install git zip unzip -y
		sudo yum install mariadb-server -y


		# starting & enabling mariadb-server
		sudo systemctl start mariadb
		sudo systemctl enable mariadb
		cd /tmp/
		git clone -b main https://github.com/hkhcoder/vprofile-project.git
		#restore the dump file for the application
		sudo mysqladmin -u root password "$DATABASE_PASS"
		sudo mysql -u root -p"$DATABASE_PASS" -e "UPDATE mysql.user SET Password=PASSWORD('$DATABASE_PASS') WHERE User='root'"
		sudo mysql -u root -p"$DATABASE_PASS" -e "DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1')"
		sudo mysql -u root -p"$DATABASE_PASS" -e "DELETE FROM mysql.user WHERE User=''"
		sudo mysql -u root -p"$DATABASE_PASS" -e "DELETE FROM mysql.db WHERE Db='test' OR Db='test\_%'"
		sudo mysql -u root -p"$DATABASE_PASS" -e "FLUSH PRIVILEGES"
		sudo mysql -u root -p"$DATABASE_PASS" -e "create database accounts"
		sudo mysql -u root -p"$DATABASE_PASS" -e "grant all privileges on accounts.* TO 'admin'@'localhost' identified by 'admin123'"
		sudo mysql -u root -p"$DATABASE_PASS" -e "grant all privileges on accounts.* TO 'admin'@'%' identified by 'admin123'"
		sudo mysql -u root -p"$DATABASE_PASS" accounts < /tmp/vprofile-project/src/main/resources/db_backup.sql
		sudo mysql -u root -p"$DATABASE_PASS" -e "FLUSH PRIVILEGES"

		# Restart mariadb-server
		sudo systemctl restart mariadb


		#starting the firewall and allowing the mariadb to access from port no. 3306
		sudo systemctl start firewalld
		sudo systemctl enable firewalld
		sudo firewall-cmd --get-active-zones
		sudo firewall-cmd --zone=public --add-port=3306/tcp --permanent
		sudo firewall-cmd --reload
		sudo systemctl restart mariadb

	b. vprofile-mc01	: Amazon Linux Service -> vprofile-backend-sg -> Add script into advance setting

		#!/bin/bash
		sudo dnf install epel-release -y
		sudo dnf install memcached -y
		sudo systemctl start memcached
		sudo systemctl enable memcached
		sudo systemctl status memcached
		sed -i 's/127.0.0.1/0.0.0.0/g' /etc/sysconfig/memcached
		sudo systemctl restart memcached
		firewall-cmd --add-port=11211/tcp
		firewall-cmd --runtime-to-permanent
		firewall-cmd --add-port=11111/udp
		firewall-cmd --runtime-to-permanent
		sudo memcached -p 11211 -U 11111 -u memcached -d

	c. vprofile-rmq01	: Amazon Linux Service -> vprofile-backend-sg -> Add script into advance setting

		#!/bin/bash
		## primary RabbitMQ signing key
		rpm --import 'https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc'
		## modern Erlang repository
		rpm --import 'https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key'
		## RabbitMQ server repository
		rpm --import 'https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key'
		curl -o /etc/yum.repos.d/rabbitmq.repo https://raw.githubusercontent.com/hkhcoder/vprofile-project/aws-LiftAndShift/al2023rmq.repo
		dnf update -y
		## install these dependencies from standard OS repositories
		dnf install socat logrotate -y
		## install RabbitMQ and zero dependency Erlang
		dnf install -y erlang rabbitmq-server
		systemctl enable rabbitmq-server
		systemctl start rabbitmq-server
		sudo sh -c 'echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config'
		sudo rabbitmqctl add_user test test
		sudo rabbitmqctl set_user_tags test administrator
		sudo systemctl restart rabbitmq-server

	Note: Facing issue to running RabbitMQ so created new intances without provisioning and run above command manually in git bash.
		
	d. vprofile-app01	: Ubuntu Service 22 SSD Volumn -> vprofile-app-sg -> Add script into advance setting
		
		#!/bin/bash
		sudo apt update
		sudo apt upgrade -y
		sudo apt install openjdk-11-jdk -y
		sudo apt install tomcat9 tomcat9-admin tomcat9-docs tomcat9-common git -y

		
10. Check vprofile-db01 instance[mysql/mariadb]
	a. Login to gitbash using vprofile-prod-key
	b. sudo -i
	c. check mariadb running status using "systemctl status mariadb" -> mysql -u admin -padmin123 accounts
		If not works : 
			* cat /etc/os-release
			* yum search mariadb
			* wget https://raw.githubusercontent.com/hkhcoder/vprofile-project/aws-LiftAndShift/userdata/mysql.sh
			  /bin/bash mysql.sh
	d. mysql -u <username> -p<password> tablename
		mysql -u admin -padmin@123 accounts
11. Check all instance in gitbash one by one:
	a. Login to gitbash using vprofile-prod-key
	b. sudo -i
	c. check memcached running status using "systemctl status memcached,rabbitmq-server,memcached,tomcat9" or ss -tunlp | grep portno(11211)
12. Go to Amazon Route S3
	a. Create hosted zone [vprofile.in]
	b. Select Private hosted zone.
	c. Select region and VPC ID.
	d. create record for db01[mysql], mc01[memcached] and rmq01[rabbitmq]
	e. name record and paste private IP of all backend instances.
13. Open VSCode from vprofile project.
	a. In Search typed cntrl+Shift+p and search Select Default profile-> Git Bash
	b. View->Terminal
	c. Edit application.properties file
		c.a. change database name whcih defined in Amazon Route 53 like db01.vprofile.in,mc01.vprofile.in,rmqo1.vprofile.in
	d. In Termial 
		1. ls : pom.xml
		2. check mvn, java &aws CLI : mvn --version and aws commands
		3. mvn install : create target folder
14. Create IAM user:
	a. username ->Attach policies directly -> AmazonS3FullAccess -> Create User
	b. click on user -> Security credential -> generate Access key and download it.
	c. in VSCode terminal:
		1. create s3 bucket : aws s3 mb s3://awsdevops-vpro-arts
		2. copy artifacts into bucket : aws s3 cp target/vprofile-v2.war s3://awsdevops-vpro-arts/
		3. Able to see the bucket in amazon cloud.
15. Create Roles and IAM
	1. Go to IAM -> AWS Service -> EC2 -> AmazonS3FullAccess Permission -> Name it and create.
	2. Assign IAM Roles to Ec2 instance[vprofile-app01] -> Select instance->Action->Security->Modify IAM->Select.
16. Open Git bash and login tomcat using ssh -i ".pem" ubuntu@ip -> sudo -i
	1. apt update
	2. apt install awscli -y
	3. aws s3 ls
	4. aws s3 cp s3://awsdevops-vpro-arts/vprofile-v2.war /tmp/
	5. systemctl stop tomcat9
	6. rm -rf /var/lib/tomcat9/webapps/ROOT
	7. cp /tmp/vprofile-v2.war /var/lib/tomcat9/webapps/ROOT.war
	8. systemctl start tomcat9
	9. ls /var/lib/tomcat9/webapps/
	10. cat /var/lib/tomcat9/webapps/ROOT/WEB-INF/classes/application.properties
17. Create Target group for load balancer
	a. Create target group name as vprofile-app-tg.
	b. port:8080
	c. Select instance vprofile-app01
18. Create Load Balancer:
	a. Select Application Load Balancer.
	b. Load Balancer Name :vprofile-app-elb
	c. Select all regions.
	d. Select security group which is specially created for load balancer i.e. vprofile-ELB-sg
	e. Select target group in Listerner section for both Http & https(required certificate)
	f. Select certificate *.awsdevops.xyz for https[443]
	g. Copy DNS info of Load balancer.
19. Go to Godaddy website and register your DNS
	a. CNAME -> projectname(vprofileapp) -> DNS ->Save
	b. copy DNS into browser to check app status.
20. Check url as http://vprofileapp.awsdevops.xyz on browser.
	a. login usign admin_vp credential.
21. Do Autoscaling Group:
	a. Create AMI:
		- Select instance -> Actions -> Image and Template -> Create Image i.e vprofile-app-image
		- Wait status of AMI available.
	b. Create Launch Template:
		a. Name it as vprofile-app-tmp
		b. Select Application OS image we have created AMI i.e. vprofile-app-image
		c. Select key pair i.e vprofile-prod-key
		d. Select security group i.e vprofile-app-sg
		e. In Advance details:Select IAM instance profile -> awsdevops-vprofile.
	c. Go to AutoScaling Group:
		a. Name i.e. vprofile-app-asg
		b. Select launch template i.e. vprofile-app-tmp
		c. Select all zones.
		d. Select Attached to an existing load balancer
		e. Select target group i.e. vprofile-app-tg
		f. Turn on "Turn on Elastic Load Balancing health checks"
		g. Enable "Target tracking scaling policy"
		h. Add Notification (created for billing alarm i.e MonitoringTeam)
			a. go to billing and enable check marks "Invoice delivery preference" & "Alert prefrences."
			b. go to CloudWatch -> Alarms -> All Alarms -> Billing -> Total Estimated charge -> in alarm -> name alarm -> provide Billing Name -> create Alarm.
22. Validate the URL:
	https://vprofileapp.awsdevops.xyz 
	