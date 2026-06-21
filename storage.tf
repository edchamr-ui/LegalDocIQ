resource "aws_s3_bucket" "uploads" {
  bucket = "${var.project_name}-uploads"

  tags = {
    Name = "${var.project_name}-uploads"
  }
}

resource "aws_s3_bucket" "processed" {
  bucket = "${var.project_name}-processed"

  tags = {
    Name = "${var.project_name}-processed"
  }
}