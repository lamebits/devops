terraform {
  backend "s3" {
    bucket = "terraform-state-27"
    key    = "terraform/backend_exercise6"
    region = "us-east-1"
  }
}