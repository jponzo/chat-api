from chat_api.db.mongodb import get_db_client
import logging
from bson import ObjectId


logger = logging.getLogger(__name__)


class MessageCrud():

    async def create(message):
        client = await get_db_client()
        db = client.messages
        new_message = await db["messages"].insert_one(message)
        created_message = await db["messages"].find_one({"_id": new_message.inserted_id})
        return created_message

    async def get(id):
        client = await get_db_client()
        db = client.messages
        message = await db["messages"].find_one({"_id": id})
        return message

    async def get_by_recipient(recipient_id, message_start_id, limit):
        client = await get_db_client()
        db = client.messages
        messages = await db["messages"].find({"recipient_id": recipient_id, "_id": {"$gt": ObjectId(message_start_id)}}).to_list(limit)
        return messages

    async def list():
        client = await get_db_client()
        db = client.messages
        messages = await db["messages"].find().to_list(1000)
        return messages
