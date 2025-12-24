"""
Save and Load functionality for game progress
"""
import os
import pickle
import json
from datetime import datetime

SAVE_DIR = "saves"
SAVE_FILE = os.path.join(SAVE_DIR, "game_save.pkl")
SAVE_FILE_JSON = os.path.join(SAVE_DIR, "game_save.json")


def ensure_save_directory():
    """Create save directory if it doesn't exist"""
    try:
        if not os.path.exists(SAVE_DIR):
            os.makedirs(SAVE_DIR)
        return True
    except Exception as e:
        print(f"Error creating save directory: {e}")
        return False


def save_game(game_info, mario_state, viewport_x):
    """
    Save game progress to file
    
    Args:
        game_info: Dictionary containing game state information
        mario_state: Dictionary containing Mario's state
        viewport_x: Camera position
    
    Returns:
        bool: True if save successful, False otherwise
    """
    try:
        if not ensure_save_directory():
            return False
        
        save_data = {
            'game_info': game_info.copy(),
            'mario_state': mario_state,
            'viewport_x': viewport_x,
            'timestamp': datetime.now().isoformat()
        }
        
        # Save using pickle for Python objects
        with open(SAVE_FILE, 'wb') as f:
            pickle.dump(save_data, f)
        
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False


def load_game():
    """
    Load game progress from file
    
    Returns:
        tuple: (game_info, mario_state, viewport_x) or (None, None, None) if load fails
    """
    try:
        if not os.path.exists(SAVE_FILE):
            return None, None, None
        
        with open(SAVE_FILE, 'rb') as f:
            save_data = pickle.load(f)
        
        return (save_data.get('game_info'),
                save_data.get('mario_state'),
                save_data.get('viewport_x', 0))
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None, None


def save_exists():
    """Check if a save file exists"""
    return os.path.exists(SAVE_FILE)

