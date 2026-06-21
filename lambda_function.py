import json
import boto3
import urllib.parse
import time

s3_client = boto3.client("s3")
textract_client = boto3.client("textract")
secrets_client = boto3.client("secretsmanager")


def get_anthropic_api_key():
    response = secrets_client.get_secret_value(
        SecretId="legaldociq/anthropic-api-key"
    )

    secret_string = response["SecretString"]

    secret_data = json.loads(secret_string)

    return secret_data["ANTHROPIC_API_KEY"]


def wait_for_textract_job(job_id):
    while True:
        response = textract_client.get_document_text_detection(
            JobId=job_id
        )

        status = response["JobStatus"]

        print(f"Textract job status: {status}")

        if status == "SUCCEEDED":
            return

        if status == "FAILED":
            raise Exception("Textract job failed")

        time.sleep(5)


def get_textract_text(job_id):
    lines = []
    next_token = None

    while True:
        if next_token:
            response = textract_client.get_document_text_detection(
                JobId=job_id,
                NextToken=next_token
            )
        else:
            response = textract_client.get_document_text_detection(
                JobId=job_id
            )

        for block in response["Blocks"]:
            if block["BlockType"] == "LINE":
                lines.append(block["Text"])

        next_token = response.get("NextToken")

        if not next_token:
            break

    return "\n".join(lines)


def lambda_handler(event, context):

    print("Event received:")
    print(json.dumps(event, indent=2))

    api_key = get_anthropic_api_key()
    print("Claude API key loaded from Secrets Manager:", bool(api_key))

    for record in event["Records"]:

        s3_event = json.loads(record["body"])

        for s3_record in s3_event["Records"]:

            bucket_name = s3_record["s3"]["bucket"]["name"]

            object_key = s3_record["s3"]["object"]["key"]
            object_key = urllib.parse.unquote_plus(object_key)

            file_name = object_key.split("/")[-1]
            local_file_path = f"/tmp/{file_name}"

            print(f"Bucket name: {bucket_name}")
            print(f"Object key: {object_key}")
            print(f"Local file path: {local_file_path}")

            s3_client.download_file(
                bucket_name,
                object_key,
                local_file_path
            )

            print("File downloaded successfully")

            textract_start_response = textract_client.start_document_text_detection(
                DocumentLocation={
                    "S3Object": {
                        "Bucket": bucket_name,
                        "Name": object_key
                    }
                }
            )

            job_id = textract_start_response["JobId"]

            print(f"Started Textract job: {job_id}")

            wait_for_textract_job(job_id)

            document_text = get_textract_text(job_id)

            print("Extracted document text:")
            print(document_text)

    return {
        "statusCode": 200,
        "body": json.dumps("Document downloaded and text extracted successfully")
    }