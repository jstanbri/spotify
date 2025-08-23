import spotipy
from helpers.logs_mod import setup_logger

# Get a logger instance for this module
logger = setup_logger(__name__)

class SpotifyClient:
    """
    A class for interacting with the Spotify API to retrieve data.
    """
    
    def __init__(self, sp_instance: spotipy.Spotify):
        """
        Initializes the SpotifyClient with an authenticated Spotipy instance.
        
        Args:
            sp_instance (spotipy.Spotify): An authenticated Spotipy object.
        """
        self.sp = sp_instance
        logger.debug("SpotifyClient initialized with authenticated instance.")

    def get_playlist_tracks(self, playlist_id):
        """
        Retrieves all tracks from a given playlist.
        
        Args:
            playlist_id (str): The Spotify ID of the playlist.
            
        Returns:
            list: A list of track objects, or None if an error occurs.
        """
        try:
            logger.info(f"Attempting to fetch tracks for playlist ID: {playlist_id}")
            # Fetch the items from the playlist
            tracks = self.sp.playlist_items(playlist_id)
            if tracks is not None and 'items' in tracks:
                logger.info(f"Successfully fetched {len(tracks['items'])} tracks.")
            else:
                logger.warning("No tracks found or unexpected response structure.")
            return tracks
        except Exception as e:
            logger.error(f"An error occurred while fetching playlist tracks: {e}")
            return None
