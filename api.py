import requests
from settings import config


CREATE_URL = "https://mvsep.com/api/separation/create"
GET_URL = "https://mvsep.com/api/separation/get"

output_format = config.common.output_format
is_demo = config.common.is_demo
token = config.secert.token