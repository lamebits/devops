resource "aws_vpc" "terraform-vpc" {
  cidr_block           = "10.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"
  tags = {
    Name = "vprofile"
  }
}

resource "aws_subnet" "terraform-pub-1" {
  vpc_id                  = aws_vpc.terraform-vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.ZONE1
  tags = {
    Name = "terraform-pub-1"
  }
}

resource "aws_subnet" "terraform-pub-2" {
  vpc_id                  = aws_vpc.terraform-vpc.id
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.ZONE2
  tags = {
    Name = "terraform-pub-2"
  }
}


resource "aws_subnet" "terraform-pub-3" {
  vpc_id                  = aws_vpc.terraform-vpc.id
  cidr_block              = "10.0.3.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.ZONE3
  tags = {
    Name = "terraform-pub-3"
  }
}

resource "aws_subnet" "terraform-priv-4" {
  vpc_id                  = aws_vpc.terraform-vpc.id
  cidr_block              = "10.0.4.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.ZONE1
  tags = {
    Name = "terraform-priv-1"
  }
}

resource "aws_subnet" "terraform-priv-5" {
  vpc_id                  = aws_vpc.terraform-vpc.id
  cidr_block              = "10.0.5.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.ZONE2
  tags = {
    Name = "terraform-priv-2"
  }
}


resource "aws_subnet" "terraform-priv-6" {
  vpc_id                  = aws_vpc.terraform-vpc.id
  cidr_block              = "10.0.6.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = var.ZONE3
  tags = {
    Name = "terraform-priv-3"
  }
}

resource "aws_internet_gateway" "terraform-IGW" {
  vpc_id = aws_vpc.terraform-vpc.id
  tags = {
    Name = "terraform-IGW"
  }
}

resource "aws_route_table" "terraform-RT" {
  vpc_id = aws_vpc.terraform-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.terraform-IGW.id
  }
  tags = {
    Name = "terraform-RT"
  }
}

resource "aws_route_table_association" "terraform-pub-1-a" {
  subnet_id      = aws_subnet.terraform-pub-1.id
  route_table_id = aws_route_table.terraform-RT.id
}

resource "aws_route_table_association" "terraform-pub-2-a" {
  subnet_id      = aws_subnet.terraform-pub-2.id
  route_table_id = aws_route_table.terraform-RT.id
}

resource "aws_route_table_association" "terraform-pub-3-a" {
  subnet_id      = aws_subnet.terraform-pub-3.id
  route_table_id = aws_route_table.terraform-RT.id
}

