resource "aws_key_pair" "terraform-key" {
  key_name   = "terraforn-key"
  public_key = file("terraforn-key.pub")
}

resource "aws_instance" "terraform-instance-3" {
  ami                    = var.AMIS[var.REGION]
  instance_type          = "t2.micro"
  availability_zone      = var.ZONE1
  key_name               = aws_key_pair.terraform-key.key_name
  subnet_id              = "subnet-04f4a6c983d898458"
  vpc_security_group_ids = ["sg-0bea8de1c2994c9f7"]
  tags = {
    Name = "Terraform-Instance-3"
  }

  provisioner "file" {
    source      = "web.sh"
    destination = "/tmp/web.sh"
  }
  provisioner "remote-exec" {
    inline = [
      "chmod u+x /tmp/web,sh",
      "sudo /tmp/web.sh"
    ]
  }
  connection {
	typr        = "ssh"
    user        = var.USER
    private_key = file("terraforn-key")
    host        = self.public_ip
  }
}