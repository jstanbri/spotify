from dotenv import load_dotenv
import os
import logging
import json

from helpers.logs_mod import setup_logger
from helpers.auth import SpotifyAuth
from helpers.spotify_client import SpotifyClient
from helpers.playlist_converter import PlaylistConverter
from helpers.playlist_exporter import PlaylistExporter

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

    # Replace with a real playlist ID you want to convert
    playlist_id = '5fvxnQRYyQ7wXgqEVcmQdk'  
    
    # Use the SpotifyClient to get the playlist tracks
    spotify_tracks = spotify_client.get_playlist_tracks(playlist_id)
    
    if spotify_tracks:
        logger.info("Spotify playlist tracks fetched successfully.")
        
        # Initialize the PlaylistConverter and Exporter
        converter = PlaylistConverter()
        exporter = PlaylistExporter()
        
        # Convert the Spotify tracks to a simplified format
        converted_tracks = converter.convert_spotify_tracks(spotify_tracks)
        
        if converted_tracks:
            logger.info("Successfully converted tracks to a new format.")
            
            # Export the converted tracks to a JSON file
            export_filename = "youtube_music_playlist.json"
            if exporter.export_to_json(converted_tracks, export_filename):
                logger.info(f"Playlist exported successfully! You can find the file at: {export_filename}")
                print(f"\nYour YouTube Music playlist is ready to be imported. Look for the file '{export_filename}' in your project directory.")
            else:
                logger.error("Failed to export the playlist to a file.")
        else:
            logger.error("Failed to convert tracks.")
    else:
        logger.error("Failed to retrieve Spotify playlist tracks.")

if __name__ == "__main__":
    main()
