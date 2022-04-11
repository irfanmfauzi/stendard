import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import BaseModel


class File(BaseModel):
    __tablename__ = 'files'

    id: Column(Integer, primary_key=True)
    file_name: Column(String)
    created_at: Column(DateTime, default=datetime.now())


class FileCommit(BaseModel):
    uuid: Column(String, primary_key=True, default=uuid.uuid3())
    file_id: Column(Integer, ForeignKey('files.id'))
    created_at: Column(DateTime, default=datetime.now())
