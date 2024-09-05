1. Create instance in AWS
2. Create volumn and attached to instance
3. Copy public ip of instance from AWS
3. Type command in git hub
	a. ssh -i "key.pem" ecr-user@ip
	b. sudo -i : switch to root user
	c. Run following commands
		
		yum install httpd wget unzip -y
		systemctl start httpd
		systemctl enable httpd
		cd /tmp
		wget https://www.tooplate.com/zip-templates/2119_gymso_fitness.zip
		unzip -o 2119_gymso_fitness.zip
		cp -r 2119_gymso_fitness/* /var/www/html/
		systemctl restart httpd
		systemctl status httpd
	d. fdisk -l : check disk partitions.
	e. df -h : show partitions
	f. fdisk /dev/xvdf
		a. type m
		b. type n : add new partition
		c. type p : print the partition
		d. type w : write table to disk and exit
	g. mkfs click tab button 2 times
		it will show all mkfs files
	h. select one of the mkfs file i.e. mkfs.ext4
	i. mkfs.ext4 /dev/xvdf1
	j. ls /var/www/html/images/
	k. mkdir /tmp/images-backups
	l. mv /var/www/html/images/* /tmp/images-backups/
	m. mount /dev/xvdf1 /var/www/html/images/
	n. df -h
		but this mount it not permanent to make it permenant do it
		a. vi /etc/fstab
			/dev/xvdf1	/var/www/html/images	ext4	defaults 	0 0
	o. mount -a
	p. mv /tmp/images-backups/* /var/www/html/images/
	q. systemctl restart httpd
	r. systemctl status httpd
	s. check the ip on browser for verification if not showing images do it
	t. vi /etc/selinux/config
		selinux = disabled -> :wq(Save)
	u. reboot and check it again. 

------------------------SNAPSHOT[Backup and Recovery]-------------------------------------

1. Stop all services
2. umount the partitions. 
3. Detach Volumn from instance.
4. Create new volumn from corrupted SNAPSHOT.
5. Attached new volumn to instance.
6. mount it if not.
7. df -h : check mount status
8. check the path for recovery of data : ls /var/www/html/images