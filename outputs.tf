output "vpc_id" {
  value = aws_vpc.main.id
}

output "uploads_bucket_name" {
  value = aws_s3_bucket.uploads.bucket
}