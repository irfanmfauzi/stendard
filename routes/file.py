from fastapi import APIRouter, UploadFile
from utils import save_file

file = APIRouter(prefix='/api/file')


@file.post('')
async def upload_file(file: UploadFile):
    await save_file(file.filename, await file.read())
    return {'file_name': file.filename}
