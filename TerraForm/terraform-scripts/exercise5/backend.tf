terraform{
	backend "s3"{
		bucket = "terraform-state-25"
		key = "terraform/backend"
		region = "us-east-1"
	}
}