from ast import operator
from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint, Enum, func, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .databasecon import Base
import enum
from sqlalchemy.dialects.postgresql import UUID
import uuid

class site(Base):
    __tablename__ = "site"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    last_modified_at = Column(DateTime(
        timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())



class Area(Base):
    __tablename__ = "area"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    last_modified_at = Column(DateTime(
        timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    site_id = Column(Integer, ForeignKey("site.id"), nullable=False)
    site = relationship("Site", back_populates='areas')

    lines = relationship("Line", back_populates='area')

