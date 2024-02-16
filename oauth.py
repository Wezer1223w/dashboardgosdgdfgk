import requests


class Oauth:
    client_id = "1136958256753938472"
    client_secret = "EQ5lqwNzlOK4Ub2j4TwCPXOoHDq5gl0n"
    redirect_uri = "http://127.0.0.1:5000/login"
    scope = "identify+email+guilds+guilds.join"
    discord_login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"

    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Oauth.redirect_uri,
            "scope": Oauth.scope
        }
        access_token = requests.post(url = Oauth.discord_token_url, data = payload).json()
        return access_token.get("access_token")
    
    @staticmethod
    def get_user_json(access_token):
        url = f"{Oauth.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}

        user_object = requests.get(url = url, headers = headers).json()
        return user_object
