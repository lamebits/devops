variable "REGION" {
  default = "us-east-1"
}
variable "ZONE1" {
  default = "us-east-1a"
}
variable "ZONE2" {
  default = "us-east-1b"
}
variable "ZONE3" {
  default = "us-east-1c"
}
variable "USER" {
  default = "ec2-user"
}
variable "AMIS" {
  type = map(any)
  default = {
    us-east-1 = "ami-08c40ec9ead489470"
    us-east-2 = "ami-0a9f08a6603f3338e"
  }
}
variable "PUB_KEY" {
  default = "terraforn-key.pub"
}
variable "PRIV_KEY" {
  default = "terraforn-key"
}
variable "MYIP" {
  default = "192.168.56.1/32"
}
