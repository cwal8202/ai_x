import os
from dotenv import load_dotenv
from decouple import config

# 방법 1
load_dotenv(".env") # ".env"는 load_dotenv() 안될떄 입력하는 경우 많음
client_id = os.getenv('CLIENT_ID')
print('방법1: ', client_id)

# 방법 2
client_id = config('CLIENT_ID')
print('방법2: ', client_id)