ZOHO_CLIENT_ID = "1000.POVC3GU43D87VB27CFW8MT3G6XPY9E"
ZOHO_CLIENT_SECRET = "e6a543299168c79f8831c43d5abb923e4d4e914c25"
ZOHO_CLIENT_AU = "6f79515f4abed869e77de769b84b85439a876ffdb2"


def get_auth_url():
    URI = "https://accounts.zoho.com.au/"

    ACCESS = "ZohoBooks.fullaccess.all"

    STATE = "testing"

    REDIRECT_URL = "http://localhost:8000/items/zoho/jwt"

    URL = f"{URI}/oauth/v2/auth?scope={ACCESS}&client_id={ZOHO_CLIENT_ID}&state={STATE}&response_type=code&redirect_uri={REDIRECT_URL}&access_type=offline"
    return URL
