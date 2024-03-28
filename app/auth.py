from models import User

from starlette.authentication import (
    AuthCredentials, AuthenticationBackend, AuthenticationError
)
import base64
import binascii

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            return

        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        if user := await User.find_one(User.username == username):
            return AuthCredentials(["authenticated"]), user
        else:
            raise AuthenticationError('Invalid basic auth credentials')
        