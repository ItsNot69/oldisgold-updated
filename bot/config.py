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
        "ACCEPT_MESSAGE", "Hello {m.from_user.mention}!\nYour Request To Join Was Approved") 
