Master username : admin
Master Password : xpWV2aCqiZok0pW1PtqZ
End Point : vprofile-mysql-rds.cfayc08ayp1k.us-east-1.rds.amazonaws.com
mysql -h vprofile-mysql-rds.cfayc08ayp1k.us-east-1.rds.amazonaws.com -u admin -pxpWV2aCqiZok0pW1PtqZ

############# Amazon RDS[Relational Database Service] ############

1. Create Amazon RDS : configure setting like security group vprofile-mysql-sg and other setting.
2. Create EC2 Instance : Create instance and security groyp mysql-client-sq.
3. Go to security group of RDS [vprofile-mysql-sg] and add instance security group[mysql-client-sq] and also add Private IP of instance having Type Mysql-Aurora.
4. Go to git bash login and check:
	a. ssh -i "key.pem" ubuntu@ip
	b. sudo -i :root login
	c. apt update
	d. apt install mysql-client -y
	e. mysql -h <EndPoint> -u <username> -p<password>
5. Mysql successfully login.
