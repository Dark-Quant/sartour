from uuid import uuid4
import os

def upload_video_to(instance, filename):
    upload_to = 'video/'
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join(upload_to, filename)

def upload_photo_to(instance, filename):
    upload_to = 'photo/'
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join(upload_to, filename)