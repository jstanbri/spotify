import logging
from helpers.logs_mod import setup_logger

# Set up logger for this module
logger = setup_logger(__name__)

class PlaylistConverter:
    """
    A class to convert and format playlist data from one service to another.
    """

    def __init__(self):
        logger.debug("PlaylistConverter initialized.")

    def convert_spotify_tracks(self, spotify_tracks):
        """
        Converts Spotify track data into a simplified format for a new platform.
        
        Args:
            spotify_tracks (dict): The dictionary containing track information from Spotipy.

        Returns:
            list: A list of dictionaries, each representing a track with a simplified structure.
                  Returns None if the input is invalid.
        """
        if not spotify_tracks or 'items' not in spotify_tracks:
            logger.error("Invalid Spotify tracks data provided for conversion.")
            return None
        
        converted_tracks = []
        for item in spotify_tracks['items']:
            track = item['track']
            if not track:
                continue

            # Check if there are artists before attempting to access the first one
            artist_name = track['artists'][0]['name'] if track['artists'] else 'Unknown Artist'

            converted_tracks.append({
                'title': track['name'],
                'artist': artist_name,
                'album': track['album']['name'],
                'is_local': track['is_local'],
                # We can add more data here if needed for the target platform
            })
        
        logger.info(f"Successfully converted {len(converted_tracks)} tracks.")
        return converted_tracks
