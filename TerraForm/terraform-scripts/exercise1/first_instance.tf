provider "aws" {
  region = "us-east-1"
}
resource "aws_instance" "intro" {
  ami                    = "ami-08c40ec9ead489470"
  instance_type          = "t2.micro"
  availability_zone      = "us-east-1a"
  key_name               = "terraform-key"
  subnet_id = "subnet-0acc8671fcec3f17f"
  vpc_security_group_ids = ["sg-050f4ca27745db418"]
  tags = {
    Name = "TerraForm-Instance"
    Project = "Dove"
  }
}