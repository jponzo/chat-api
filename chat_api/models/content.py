from chat_api.db.sql import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ContentModel(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    text = Column(String)
    url = Column(String)
    height = Column(String)
    width = Column(String)
    source = Column(String)
