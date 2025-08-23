# app.py
from dotenv import load_dotenv
import os
import logging
import json

from helpers.logs_mod import setup_logger
from helpers.auth import SpotifyAuth
from helpers.spotify_client import SpotifyClient

# Load environment variables from the .env file.
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Set up the logger for this module
logger = setup_logger(__name__)

def main():
    logger.info("Starting the application...")
    
    # Authenticate with Spotify
    spotify_auth = SpotifyAuth()
    
    # Get the authenticated Spotipy instance
    sp_instance = spotify_auth.get_sp_instance()
    
    # Use the authenticated instance to create the SpotifyClient
    spotify_client = SpotifyClient(sp_instance)

    # Example: get the current user's profile
    user_info = spotify_auth.get_current_user()
    if user_info:
        logger.info(f"Successfully authenticated as: {user_info['display_name']}")
    else:
        logger.error("Authentication failed. Please check your credentials.")
        return

    # Example: Replace with a real playlist ID
    playlist_id = '5fvxnQRYyQ7wXgqEVcmQdk'  # ThisIsSodaBlonde
    
    # Use the SpotifyClient to get the playlist tracks
    playlist_tracks = spotify_client.get_playlist_tracks(playlist_id)
    
    if playlist_tracks:
        logger.info("Playlist tracks fetched successfully.")
        # Pretty print the JSON for a clear output
        print(json.dumps(playlist_tracks, indent=2))
    else:
        logger.error("Failed to retrieve playlist tracks.")

if __name__ == "__main__":
    main()



