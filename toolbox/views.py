from django.shortcuts import render, HttpResponse
from django.conf import settings

from weasyprint import HTML

import boto3, os, logging


logger = logging.getLogger(__name__)

def upload_s3(bucket_name, bucket_sub_dir, output_dir, filename, content_type):

        full_path = "{}/{}".format(output_dir, filename)

        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )

        data = open(full_path, 'rb')

        result = s3.put_object(Key = "{}/{}".format(bucket_sub_dir, filename) , Body = data, Bucket = bucket_name, ContentType = content_type, ACL = 'public-read')

        if 'ResponseMetadata' in result and result['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False

def pdf_generator(request):
    url = request.GET.get('url', None)
    file_name = request.GET.get('file_name', None)

    output_dir = "/tmp"
    bucket_name = 'leantech-cl'
    bucket_sub_dir = "pdf-generator"
    full_output = "{}/{}".format(output_dir, file_name)
    success = False

    try:
        if os.path.exists(full_output):
            os.remove(full_output)

        HTML(url).write_pdf(full_output)

        if upload_s3(bucket_name, bucket_sub_dir, output_dir, file_name, "application/pdf"):
            success = True

        if os.path.exists(full_output):
            os.remove(full_output)

        if success:
            return HttpResponse(content = "https://s3.amazonaws.com/{}/{}/{}".format(bucket_name, bucket_sub_dir, file_name), status = 200)
        else:
            return HttpResponse(content = "Error generando PDF", status = 404)

    except Exception as e:
        logger.critical(str(e))
        return HttpResponse(status = 404)