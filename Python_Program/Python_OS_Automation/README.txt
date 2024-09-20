1. Create vagrant file:
	vagrant init
2. Edit Vagrant file
	
Vagrant.configure("2") do |config|
 
   config.vm.define "scriptbox" do |scriptbox|
  	scriptbox.vm.box = "ubuntu/bionic64"
	scriptbox.vm.hostname = "scriptbox"
	scriptbox.vm.network "private_network", ip: "192.168.10.2"
   end
   config.vm.define "web01" do |web01|
  	web01.vm.box = "centos/7"
	web01.vm.hostname = "web01"
	web01.vm.network "private_network", ip: "192.168.10.3"
	web01.vm.provider "virtualbox" do |vb|
		vb.memory = "1024"
		vb.cpus = 2
	end
   end
   config.vm.define "web02" do |web02|
  	web02.vm.box = "centos/7"
	web02.vm.hostname = "web02"
	web02.vm.network "private_network", ip: "192.168.10.4"
	
   end

end
3. vagrant up
4. vagrant ssh scriptbox
5. sudo -i
6. mkdir /opt/pyscripts
7. cd /opt/pyscripts
8. mkdir ostasks
9. python3
10. import os
11. os.system("ls") //Linux command write in ""
12. touch /tmp/textfile.txt //create file
13. vim check-script.py
	#!/usr/bin/python3
	import os
	path = "/tmp/textfile.txt"
	if os.path.isdir(path):
    		print("It is a directory")
	elif os.path.isfile(path):
    		print("It is a file")
	else:
    		print("file or dir does not exists")
14. ls -l /usr/bin/python3
15. chmod +x check-script.py
16. ./check-script.py
17. vim ostasks.py
18. 	#!/usr/bin/python3
	import os
	userlist = ["alpha","beta","gamma"]

	for user in userlist:
    		exitcode = os.system("id {}".format(user)) //write linux command in ""
    		if exitcode != 0:
        		print("{} user doesnot exist".format(user))
        		os.system("useradd {}".format(user))
    		else:
        		print()
        	print("{} user already exist".formar(user))

	
	#Add group
	exitcode = os.system("grep science /etc/group")
	if exitcode != 0:
    		print("Group Science does not exist.. Adding it")
    		os.system("groupadd Science")
	else:
    		print("Group Science already exist.")
    		print()

	#Adding User in Science Group
	for user in userlist:
    		print("Adding user {} in Science group".format(user))
    		print()
    		os.system("usermod G Science {}".format(user))

	# Adding Directory
	if os.path.isdir("/opt/science_dir"):
    		print("Directory already exist, skipping it")
	else:
    		os.mkdir("/opt/science_dir")

	# Assigning Ownership and Permission to directory

	os.system("chown :Science /opt/science_dir")
	os.system("chmod 770 /opt/science_dir")


19. chmod +x ostask.py
20. ./ostasks.py
21. ls -ld /opt/science_dir

	
