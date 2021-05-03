"""
    1. Create bucket at aws S3
    2. Get credentials:
        2.1 ACCESS_KEY_ID
        2.2 SECRET_KEY
    3. Check how to use the credentials via CLI or python script
    4. Return from the function the URL of the current saved logo
"""

from PipelineSystem import PipelineSystem
from pipelines import pipelines
import boto3
from botocore.exceptions import NoCredentialsError
import uuid
import os
import sys
from creds import ACCESS_KEY_ID, SECRET_ACCESS_KEY


def upload_to_aws(local_file, bucket, prefix=''):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=SECRET_ACCESS_KEY)

    try:
        file_name = prefix + str(uuid.uuid4()) + ".png"
        s3.upload_file(local_file, bucket, 'logos/' + file_name)

        return file_name
    except FileNotFoundError:
        return False
    except NoCredentialsError:
        return False


def main():
    # init
    p_system = PipelineSystem(None, pipelines)

    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = ''
    if command == 'set_active':
        to_set = sys.argv[2]
        p_system.set_active_pipeline(to_set)
    elif command == 'get_active':
        print(p_system.get_active_pipeline(True))
        sys.stdout.flush()
    elif command == 'sync':
        for index in range(len(p_system.pipelines)):
            print(str(index) + ':' + p_system.pipelines[index].model + ':' + p_system.pipelines[index].text)
    else:
        active_pipeline = p_system.get_active_pipeline()
        if not active_pipeline:
            print("Theres no active pipeline")
            sys.stdout.flush()
        if len(sys.argv) > 2:
            active_pipeline.set_text(sys.argv[2])
        if len(sys.argv) > 3:
            active_pipeline.set_model(sys.argv[3])

        image = active_pipeline.activate()
        upload_result = upload_to_aws(image, 'deep-logo-image')
        os.remove(image)
        if upload_result:
            print("Upload Successful")
            print(upload_result)
            sys.stdout.flush()
        else:
            print("Something went wrong")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
