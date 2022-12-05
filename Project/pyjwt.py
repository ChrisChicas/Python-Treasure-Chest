from flask import request
from . import _config
import jwt

def token_check():
    if 'tokens' in request.headers:
        token = request.headers['tokens']
        data = jwt.decode(token, _config.secret_key, algorithms=["HS256"])
    else:
        data = None
    
    return data