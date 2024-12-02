resource "aws_key_pair" "terraform-key" {
  key_name   = "terraforn-key"
  public_key = file(var.PUB_KEY)
}

resource "aws_instance" "terraform-instance-4" {
  ami                    = var.AMIS[var.REGION]
  instance_type          = "t2.micro"
  availability_zone      = var.ZONE1
  key_name               = aws_key_pair.terraform-key.key_name
  subnet_id              = aws_subnet.terraform-pub-1.id
  vpc_security_group_ids = [aws_security_group.terraform_stack_sg.id]
  tags = {
    Name = "Terraform-Instance-4"
  }
}

resource "aws_ebs_volume" "vol_4_terraform" {
  availability_zone = var.ZONE1
  size              = 3
  tags = {
    Name = "extr-vol-4-terraform"
  }
}

resource "aws_volume_attachment" "atch_vol_terraform" {
  device_name = "/dev/xvdh"
  volume_id   = aws_ebs_volume.vol_4_terraform.id
  instance_id = aws_instance.terraform-instance-4.id
}

output "PublicIP" {
  value = aws_instance.terraform-instance-4.public_ip
}

output "PrivateIP" {
  value = aws_instance.terraform-instance-4.private_ip
}