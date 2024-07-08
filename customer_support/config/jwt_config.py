from datetime import timedelta

SIMPLE_JWT_CONFIG = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "USER_ID_FIELD" : "user_id",
}