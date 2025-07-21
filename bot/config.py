import os
from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    API_ID = int(os.environ.get("API_ID", "28726816"))
    API_HASH = os.environ.get("API_HASH", "45edf74203ecf6ff14b394a9e47dca34")
    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN", "6059695462:AAHHGQk0mQj-Q06Yt7_8yoiBejI-HwCN90k")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5521380948"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
    CHAT_ID = [int(x) for x in os.environ.get(
        "CHAT_ID", "-1001654163482").split()]
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQGMcpgAhs3f_tWmduO-MhKsI-_BVDHw2ltF9syKe1Fqm_ON8WtRQwPXS992oTthM8mLwOJMG_HY_FjLbAsLbGoXEDRv7RGaeeH8enr5RLlezvoNQQSi6Pb8ZBw4vxyqWOgYS9xb_i8ITU4cE_6UdjJ5bGL--uHoR22iVQsFPPY7rg529IFAKc6Fprm9ddC2MoH3N3inkauh8OUwq5DOOi38DXQFvfMc30tGJzTxtLL7_E0HrolQl9sxn1AIqzp2uYq-F1NYNm0EBHnSW07bhsAtVe0C1CUPh39k2SwUSaIne-8mca1YRGXfvOmCUa6-wK5zSsLXcHeZ6RgkHQx9uS2S0gXESQAAAAHgKGfnAA")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://Rohit33:Rohit11@cluster0.i7dsnm5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "Telegram")


class Script(object):
    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message")
    ACCEPT_MESSAGE = os.environ.get(
        "ACCEPT_MESSAGE", "🙈𝗠𝗼𝗺 𝗦𝗼𝗻 𝗩𝗶𝗗𝗲𝗢😍\nhttps://t.me/+8RxKRwvb9PI3OWQ0\n\n😍𝐃𝐄𝐒𝐈 𝐁𝐇𝐀𝐁𝐇𝐈 𝐋𝐄𝐀𝐊𝐄𝐃 𝐌𝐌𝐒😍\nhttps://t.me/+UjRcYFYlqLYyYzM0\n\n😍𝐈𝐍𝐒𝐓𝐀 𝐕𝐈𝐑𝐀𝐋 𝐋𝐄𝐀𝐊𝐄𝐃 𝐌𝐌𝐒😍\nhttps://t.me/+Qd9aKKzkYSlkNmI0\n\n🥲🫣𝘾𝙤𝙪𝙨𝙞𝙣 𝙎𝙞𝙨𝙩𝙚𝙧 𝙈𝙢𝙨🫣🥲\nhttps://t.me/+R_Xul2mZrqpjN2Qx\n\n𝐈𝐧𝐬𝐓𝐚 𝐕𝐢𝐑𝐚𝐋 𝐕𝐢𝐃𝐞𝐨'𝐒🙈\nhttps://t.me/+KvegAY6RBd80ZWNi\n\n😱𝐎𝐲𝐎 𝐫𝟎𝟎𝐦 𝐋𝐞𝐚𝐤𝐞𝐝 𝐕𝐢𝐝𝐞𝐨😱\nhttps://t.me/addlist/8osqFXryv1g2ZWU0\n\n😱😜🔞𝘽𝙝𝙖𝙗𝙝𝙞 𝙡𝙤𝙫𝙚𝙧𝙨 😘😈😱\nhttps://t.me/+rbrEEvfGg2plYjQ6\n𝘾𝙡𝙞𝙘𝙠 𝙁𝙤𝙧 𝙎𝙥𝙚𝙘𝙞𝙖𝙡 𝘾𝙝𝙖𝙣𝙣𝙚𝙡𝙨 👉 /start") 
