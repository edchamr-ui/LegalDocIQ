resource "aws_secretsmanager_secret" "anthropic_api_key" {
  name = "${var.project_name}/anthropic-api-key"
}

resource "aws_secretsmanager_secret_version" "anthropic_api_key_value" {
  secret_id = aws_secretsmanager_secret.anthropic_api_key.id

  secret_string = jsonencode({
    ANTHROPIC_API_KEY = "your-real-claude-api-key-here"
  })
}

