from chat_api.db.mongodb import get_db_client
import logging


logger = logging.getLogger(__name__)


class UserCrud():

    async def create(user):
        client = await get_db_client()
        db = client.users
        new_user = await db["users"].insert_one(user)
        created_user = await db["users"].find_one({"_id": new_user.inserted_id})
        return created_user

    async def get(email):
        client = await get_db_client()
        db = client.users
        message = await db["users"].find_one({"email": email})
        return message

    async def list():
        client = await get_db_client()
        db = client.users
        users = await db["users"].find().to_list(1000)
        return users
