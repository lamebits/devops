variable "REGION" {
  default = "us-east-1"
}
variable "ZONE1" {
  default = "us-east-1a"
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
