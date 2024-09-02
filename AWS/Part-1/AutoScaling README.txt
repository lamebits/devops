Auto Scaling Group

1. Create Target Group.
2. Create Load Balancer assign target group.
3. Create AMI and Instance.
4. Create Auto Scaling
	a. Name it
	b. Select launch template
	c. select zones
	d. with load balancer
	e. select target group
	f. select health check condition 
	g. configure group size and scaling policies:
		desired instance = 2
		Min instance = 1
		Max instance = 8
	h. Select Target scaling policy
	i. Add notification
	j. Add tag
	k. Save
Note: 
1. it will create instance dynamically through launch template.
2. if you want to change any condition like
create new launch template and assign to auto scaling group for changes.