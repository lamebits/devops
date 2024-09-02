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