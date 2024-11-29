resource "aws_instance" "intro" {
  ami                    = var.AMIS[var.REGION]
  instance_type          = "t2.micro"
  availability_zone      = var.ZONE1
  key_name               = "terraform-key"
  subnet_id              = "subnet-04f4a6c983d898458"
  vpc_security_group_ids = ["sg-0bea8de1c2994c9f7"]
  tags = {
    Name = "Terraform-instance-2"
  }
}
