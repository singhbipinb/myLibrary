import os
from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(basedir, '.env'))



class Config(object):
    MONGO_URI = os.environ.get("MONGO_URI")
