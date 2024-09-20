Re-Architectiure of webapp on AWS Cloud[PAAS, SAAS]

1. Login to AWS account.
2. Create key pair for beanstalk instance login.
	Name : vprofile-beans-key
3. Create security group for backend services (elasticcache, RDS and RabbitMQ).
	a. Security Group for backend i.e. vprofile-backend-sg -> Alltraffic -> itself vprofile-backend-sg
	b. Security group for mysql : vprofile-mysql-sg -> SSH->22->MyIP
4. Create:
	1. Amazon RDS:

	    1. Subnet groups:
		1. Create Subnet Group i.e. vprofile-rds-sub-group.
		2. Select all availability zones.
		3. Select all subnets.
	    2. Parameter groups:
		1. Create Parameter group i.e. vprofile-rds-para-grp.
		2. Select Engine Type:MySQL Community.
		3. Parameter group family: mysql8.0.
	    3. Create Database:
		1. Select database Mysql.
		2. Engine Version : MySQL 8.0.35
		3. Select Dev/Test Template
		4. Single DB instance Availability and durability
		5. DB instance identifier : vprofile-rds-mysql
		6. Credential setting: Username:admin and Self managed - Auto generate password.
		7. Instance configuration: Burstable classes - db.t3.micro
		8. enable include previous generation classes toggle.
		9. Storage: General Purpose SSD(gp2)-20
		10.Select DB subnet group : vprofile-rds-sub-group
		11. Cancel default Existing VPC security group
		12. Database Options: Initial database name-accounts, DB parameter group-vprofile-rds-para-grp
		13. Select all log exports.
		14. create it.	
		username : admin	
		password: zbtn1zMSABsTlPpzTkFf
		EndPoint : vprofile-rds-mysql.cfayc08ayp1k.us-east-1.rds.amazonaws.com
			
	2. Amazon Elastic Cache:

	     1. Subnet groups:
		1. Create Subnet Group i.e. vprofile-memcached-sub-group.
		2. Select all availability zones.
		3. create it.
	     2. Parameter Group:
		1. Create parameter group name vprofile-memcached-para-grp
		2. Family : memcached1.6
		3. create it.
	     3. Memcached Cluster:
		1. Enable Design your own cache.
		2. Enable Standard create
		3. Enable AWS Cloud
		4. Given cluster info : vprofile-elasticache-svc
		5. Engine version : 1.6.22
		6. PortNo : 11211
		7. Parameter group : vprofile-memcached-para-grp
		8. Node Type: cache.t2.micro
		9. Select subnet group : vprofile-memcached-sub-group
		10. Security -> click on Manage -> Select security group(vprofile-backend-sg)
		EndPoint : memcached.active.host=vprofile-elasticache-svc.ywenkg.cfg.use1.cache.amazonaws.com
	3. Amazon Rabbit MQ:

		1. Open Amazon MQ
		2. Select Rabbit MQ
		3. Enable single instance broker
		4. Broker name :vprofile-rmq
		5. Broker Instance Type : mq.t3.micro
		6. Username: rabbitmq Password: Rabbitmq@123
		7. Netwrok and Security: Private Access
		8. Select security group : vprofile-backend-sg.
		Endpoint : b-d07e2c9e-e534-4fd6-8bda-4953ed984a10.mq.us-east-1.amazonaws.com
5. Launch EC2 instance for DB initializing:
	1. Launch Instance name mysql-client
	2. OS :Ubuntu 22
	3. Key Pair : vprofile-beans-key
	4. Select security group : vprofile-mysql-sg
	5. Add vprofile-mysql-sg (3306portno) on vprofile-backend-sg security group.
	6. Go to git bash login ssh -i "key.pem" ubuntu@ip -> sudo -i
	7. sudo apt update && sudo apt install mysql-client -y
	8. mysql -h <RDS EndPoint> -u <username> -p<password> accounts
	9. git clone https://github.com/hkcoder/vprofile-project.git
	10. cd vprofile-project
	11. ls src/main/resources/db_backup.sql
	12. mysql -h <RDS EndPoint> -u <username> -p<password> accounts < src/main/resources/db_backup.sql
	13. show tables;
	14. Copy Amazon MQ endpoint
		b-d07e2c9e-e534-4fd6-8bda-4953ed984a10.mq.us-east-1.amazonaws.com
	15. Copy ElastiCache EndPoint
		vprofile-elasticache-svc.ywenkg.cfg.use1.cache.amazonaws.com

6. Create IAM Roles:
	a. Create Role : AWS service -> EC2
	b. Select permission: AWSElasticBeanstalkWebTier,AdministratorAccess-AWSElasticBeanstalk,AWSElasticBeanstalkCustomPlatformforEC2Role,AWSElasticBeanstalkRoleSNS
	C. Give name to role i.e. vprofile-bean-role
	d. delete aws-elasticbeanstalk-service-role if visible.

7. Create Elastic Beanstalk Environment
	a. enable web server environment and application name it as "vprofile-app" and evn name as "Vprofile-app-prod"
	b. domain name : vprofileapp09
	c. platform : Tomcat
	d. Tomcat 8.5 with corretto 11
	e. custom configuration
	f. service access:
		a. enable create and use new service role
		b. aws-elasticbeanstalk-service-role
		c. EC2 key pair : vprofile-beans-key
		d. EC2 instance prodile : vprofile-bean-role
	g. VPC : 
		a. select default vpc
		b. checked mark on Activated Public IP Address
		c. enable all subnets
		d. Tag Name:vproapp
	h. Instance:
		a. Select Load balance in envornment type and min or max
		b. instance type : t2/t3 micro.
		c. Application Deployement : Rolling : 50
		d. submit and wait to Health check OK
7. Open Amazon S3:
	a. Check elasticbeanstack bucket created.
	b. go to permission and enable ACL and in Object Ownership enable Bucket owner preferred.
	c. Come back to Amazon ElasticBeanstalk
		a. go to configuration
		b. Instance traffic and scaling
		c. Edit Processes
			a. path : /login
			b. enable session stickiness
			c. save
		d. Edit Listeners
			a. Add Listener Port: 443
	`		b. Listener protocol : HTTPS
			c. SSL Certificate
			d. save
			e. Health status : severe
			d. Copy domain name : vprofileapp09.us-east-1.elasticbeanstalk.com
			e. as min instance set to 2 , EC2 launch two instances automatically
		e. EC2 Instance:
			a. go to EC2 instance select any one instance 
			b. select security -> security group -> security group id
			c. Paste that security group instance id into vprofile-backend-sg security group with all traffic.
			d. Add rule: 3306,11211&5672 -> select Instance security group it
			e. save

9. Build and Deploy Artifact 
	a.Download sourcecode from github repository "https://github.com/hkhcoder/vprofile-project.git"
	b.Open application.properties file from src->main->resource folder.
	c. Paste RDS endpoint replace of db01  in jdbc.url.
	d. modify RDS username,endpoint and password in the application.properties file.
	e. copy memcache endpoint "vprofile-elasticache-svc.ywenkg.cfg.use1.cache.amazonaws.com" and paste itinto file "memcached.active.host=vprofile-elasticache-svc.ywenkg.cfg.use1.cache.amazonaws.com"
	f. copy rabbitmq Endpoint "amqps://b-d07e2c9e-e534-4fd6-8bda-4953ed984a10.mq.us-east-1.amazonaws.com:5671" and paste it rabbitmq.address=b-d07e2c9e-e534-4fd6-8bda-4953ed984a10.mq.us-east-1.amazonaws.com and change port number 5672 to 5671 as per AWS port and also provide username(rabbitmq) and password(Rabbitmq@123)
	g. save the file.
	h. open git bash from the file is exist.
		a. mvn --version check
		b. mvn install - created target/vprofile-v2.war(our artifact)
		c. Go to Amazon ElasticBean
			a. Go to upload and deploy -> select the vprofile-v2.war file and deploy it.
	i. open godaddy wesite
		a. add rule -> CNAME->vprofile-> paste Elasticbean domain.
	j. Check url "https://vprofile.awsdevops.xyz" in browser. 

10. Amazon CloudFront: Content Delivery Network
	a. Disturbute over the network.
	b. Create it and select Origin Domain of Elatic Load Balancer
	c. Legacy cache setting ALL(Headers,Query strings and Cookies)
	d. Enable Do not enable security protections.
	e. Add alternate domain name "vprofile.awsdevops.xyz" and select SSL Certificate and select TLSv1 security policy
	f. Create Distribution.
	g. Copy Distibution domain name "https://d2c3zv47vwb25p.cloudfront.net"
	h. Add a Record in Godaddy as CNAME->vprofile->d2c3zv47vwb25p.cloudfront.net
	i. wait CloudFront Distribution Status Enabled and not showing Deploying.

11. Validate
	a. open url "https://vprofile.awsdevops.xyz"
	b. inspect and go to console
	c. check via: ---(CloudFront)
	
