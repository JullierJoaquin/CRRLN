from fastapi_users import BaseUserManager, IntegerIDMixin
from backend.users.schemas import User

SECRET = "SUPER-SECRET-KEY"  # Reemplazar por un valor seguro, idealmente desde .env

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    user_db_model = User
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
