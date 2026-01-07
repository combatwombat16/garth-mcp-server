import os
from functools import wraps

import garth


def requires_garth_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = kwargs.get("garth_token")
        if token:
            garth.client.loads(token)
        else:
            email = os.getenv("GARMIN_EMAIL")
            password = os.getenv("GARMIN_PASSWORD")
            if email and password:
                # Only login if not already authenticated with OAuth1
                if not garth.client.oauth1_token:
                    try:
                        garth.login(email, password)
                    except Exception as e:
                        return f"Authentication failed: {str(e)}"
            else:
                return (
                    "Authentication required. Either provide 'garth_token' as a tool argument "
                    "or set 'GARMIN_EMAIL' and 'GARMIN_PASSWORD' environment variables."
                )
        return func(*args, **kwargs)

    return wrapper
