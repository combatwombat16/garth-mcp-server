import garth
from ..app import server
from ..auth import requires_garth_session

@server.tool()
@requires_garth_session
def user_profile(garth_token: str | None = None) -> str | garth.UserProfile:
    """
    Get user profile information using Garth's UserProfile data class.
    """
    return garth.UserProfile.get()


@server.tool()
@requires_garth_session
def user_settings(garth_token: str | None = None) -> str | garth.UserSettings:
    """
    Get user settings using Garth's UserSettings data class.
    """
    return garth.UserSettings.get()
