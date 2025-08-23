# spotify

James' Spotify API work

## Overview

This project is a Python application that interacts with the Spotify API to manage and analyze playlists. It allows users to create, modify, and delete playlists, as well as retrieve information about tracks and artists.

Start here: [spotify developer dashboard](https://developer.spotify.com/dashboard/applications)

### Features

- Login and Authentication
- Playlist Creation and Modification
- Track and Artist Information Retrieval

TODO: Implement output to YouTube music playlist

## Environment Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/spotify.git
   cd spotify
   ```

2. I use Python 3.11.6, create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
    ```

4. You will need to set up your Spotify Developer credentials. Create a `.env` file in the root directory and add the following:

   ```bash
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=your_redirect_uri
   ``` For obvious reasons, keep these in the .gitignore file.

5. Run the application:

   ```bash
   python app/app.py
   ```  
