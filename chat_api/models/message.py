from chat_api.db.sql import Base
from sqlalchemy import Column, Integer, ForeignKey
from chat_api.models.content import ContentModel
from sqlalchemy.orm import relationship


class MessageModel(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(Integer, ForeignKey("users.id"))
    sender = Column(Integer, ForeignKey("users.id"))
    content_id = Column(Integer, ForeignKey("contents.id"))
    content = relationship(ContentModel)
