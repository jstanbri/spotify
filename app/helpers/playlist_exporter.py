import json
import logging
from helpers.logs_mod import setup_logger

# Set up logger for this module
logger = setup_logger(__name__)

class PlaylistExporter:
    """
    A class to handle exporting playlist data to a file.
    """

    def __init__(self):
        logger.debug("PlaylistExporter initialized.")

    def export_to_json(self, tracks, filename):
        """
        Exports a list of tracks to a JSON file.
        
        Args:
            tracks (list): A list of track dictionaries to export.
            filename (str): The name of the file to save the data to.

        Returns:
            bool: True if the export was successful, False otherwise.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(tracks, f, indent=2)
            logger.info(f"Successfully exported playlist to {filename}")
            return True
        except IOError as e:
            logger.error(f"Failed to write file {filename}: {e}")
            return False
