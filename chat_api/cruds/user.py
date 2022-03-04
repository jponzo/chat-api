import logging
from sqlalchemy.orm import Session
from chat_api.models.user import UserModel
from chat_api.schemas.user import UserCreateSchema

logger = logging.getLogger(__name__)


class UserCrud():

    def create(db: Session, user: UserCreateSchema):
        logger.info(user)
        new_user = UserModel(name=user.name, email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_by_id(db: Session, user_id: int):
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        return user

    def list(db: Session):
        users = db.query(UserModel).all()
        return users

    def login(db: Session, user_email, user_password):
        user = db.query(UserModel).filter(UserModel.email == user_email).filter(UserModel.password == user_password).one_or_none()
        return user
