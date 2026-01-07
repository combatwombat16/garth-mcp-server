import os
import garth
from ..app import server

@server.tool()
def generate_garth_token(
    email: str | None = None, password: str | None = None
) -> str:
    """
    Generate a GARTH_TOKEN string using Garmin credentials.
    If email and password are provided, they will be used.
    Otherwise, it will fall back to GARMIN_EMAIL and GARMIN_PASSWORD environment variables.
    The resulting token can be used as the 'garth_token' argument in other tools.
    """
    email = email or os.getenv("GARMIN_EMAIL")
    password = password or os.getenv("GARMIN_PASSWORD")
    
    if not email or not password:
        return (
            "Credentials missing. Please provide email and password as arguments "
            "or set GARMIN_EMAIL and GARMIN_PASSWORD environment variables."
        )
        
    try:
        garth.login(email, password)
        return garth.client.dumps()
    except Exception as e:
        return f"Failed to generate token: {str(e)}"
