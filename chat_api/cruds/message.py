import logging
from sqlalchemy.orm import Session
from chat_api.models.message import MessageModel
from chat_api.models.content import ContentModel
from chat_api.schemas.message import MessageSchema, ContentSchema

logger = logging.getLogger(__name__)


class MessageCrud():

    def create(db: Session, message: MessageSchema):
        new_content_dict = message.content.dict()
        new_content = ContentModel(**new_content_dict,)
        db.add(new_content)
        db.commit()
        db.refresh(new_content)

        new_message = MessageModel(recipient=message.recipient,
                                   sender=message.sender,
                                   content_id=new_content.id
                                   )
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message

    def get_message_by_id(db: Session, message_id: int):
        message = db.query(MessageModel).filter(MessageModel.id == message_id).first()
        return message

    def get_messages_by_recipient(db: Session, recipient_id: int, message_start_id: int, limit: int = 100):
        return db.query(MessageModel).filter(MessageModel.recipient == recipient_id).filter(MessageModel.id >= message_start_id).limit(limit).all()
