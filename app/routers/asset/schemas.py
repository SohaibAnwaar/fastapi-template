from dataclasses import Field
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

import uuid



class AreaBase(BaseModel):
    name: str
    site_id: int
    # enterprise_id: int is passed from User jwt token information

    class Config:
        orm_mode = True



class RespArea(AreaBase):
    id: int
    created_at: datetime
    last_modified_at: datetime
    enterprise_id: int

    class Config:
        orm_mode = True

class ReqArea(AreaBase):
    id: int