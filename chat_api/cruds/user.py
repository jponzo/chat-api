import logging
from sqlalchemy.orm import Session
from chat_api.models.user import UserModel
from chat_api.schemas.user import UserSchema, UserCreateSchema

logger = logging.getLogger(__name__)


class UserCrud():

    def create(db: Session, user: UserCreateSchema):
        logger.info(user)
        new_user = UserModel(name=user.name, email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_user_by_id(db: Session, user_id: int):
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        return user

    def get_users_by_recipient(db: Session, recipient_id: int, ):
        users = db.query(UserModel).filter(UserModel.recipient == recipient_id).first()
        return users

    def list(db: Session):
        users = db.query(UserModel).all()
        return users

    def login(db: Session, user_email, user_password):
        user = db.query(UserModel).filter(UserModel.email == user_email).filter(UserModel.password == user_password).one_or_none()
        return user
