
How to create EFS?

1. Create Intances in AWS.
2. Go to Security Group:
	a. create new security group.
	b. Edit inbound rule
		select Type "NFS" -> and created security group for key
3. Go To Amazon EFS:
	a. create EFS by customize
	b. change security group which are created for img.
	b. assign EFS to Access Point.
4. Install amazon-efs-utils package:
	a. Go to git bash
	b. ssh -i "key.pem" ec2.user@ip
	c. sudo -i
	d. cd /var/www/html/images
	e. mkdir /tmp/img-backup
	f. mv /var/www/html/images/* /tmp/img-backup/
	g. Install following command:
		$ sudo yum -y install git rpm-build make rust cargo openssl-devel
		$ git clone https://github.com/aws/efs-utils
		$ cd efs-utils
		$ make rpm
		$ sudo yum -y install build/amazon-efs-utils*rpm	
	h. edit fstab file
		a. vi /etc/fstab add below line
		file-system-id:/ efs-mount-point efs _netdev,noresvport,tls,iam,accesspoint=access-point-id 0 0
		Note: Using Access Point or IAM user
	i. sudo mount -fav
		Succefully mount checked by df -h then /var/www/html/images are mounted.
		
		
	