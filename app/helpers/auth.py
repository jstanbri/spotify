# auth.py
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from helpers.logs_mod import setup_logger

logger = setup_logger(__name__)

class SpotifyAuth:
    """
    Class to authenticate with Spotify using OAuth.
    """
    
    def __init__(self):
        """
        Initializes the SpotifyAuth instance and sets up the authentication manager.
        """
        logger.debug("Initializing Spotify authentication.")
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
            scope="user-library-read"
        ))
        logger.info("Spotify authentication manager created.")

    def get_sp_instance(self):
        """
        Returns the authenticated Spotipy instance.
        """
        return self.sp

    def get_current_user(self):
        """
        Returns the currently authenticated user's profile information.
        """
        try:
            logger.debug("Attempting to fetch the current user profile.")
            user_info = self.sp.current_user()
            logger.info("Successfully fetched current user profile.")
            return user_info
        except Exception as e:
            logger.error(f"An error occurred while fetching user profile: {e}")
            return None
