import os
import yaml
import json
import joblib
from chicken_disease_classifier import logger
from box.exceptions import BoxValueError 
from box import Box, ConfigBox
from pathlib import Path
from typing import Any
import base64
from ensure import ensure_annotations
#import logging

# Setting up logging configuration
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger("chicken_disease_classifier")

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents in a ConfigBox for dot notation access.
    
    Args:
        path_to_yaml (Path): Path to the YAML file to read.
    
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox.
    
    Raises:
        ValueError: If the YAML file is empty.
        Exception: For other exceptions that might occur.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if isinstance(content, dict):
                return ConfigBox(content)
            else:
                raise ValueError(f"YAML file at {path_to_yaml} is empty or contains non-dictionary content")

    except BoxValueError:
        raise ValueError("YAML file is improperly structured.")
    except Exception as e:
        raise ValueError(f"An error occurred while reading {path_to_yaml}: {str(e)}")

@ensure_annotations
def create_directories(paths_to_directories: list, verbose: bool = True):
    """Creates directories from a list of paths.
    
    Args:
        paths_to_directories (list): List of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in paths_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> Box:
    """Loads JSON data from a file.
    
    Args:
        path (Path): Path to the JSON file.
    
    Returns:
        Box: Data loaded from JSON file as a Box for dot notation access.
    """
    with open(path, "r") as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data in binary format.
    
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the output binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file.
    
    Args:
        path (Path): Path to the binary file.
    
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes.
    
    Args:
        path (Path): Path of the file.
    
    Returns:
        str: Size of the file in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

def decode_image(imgstring: str, fileName: str):
    """Decodes a base64 encoded image to a file.
    
    Args:
        imgstring (str): Base64 encoded string of the image.
        fileName (str): File name to save the decoded image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)

def encode_image_into_base64(image_path: Path) -> bytes:
    """Encodes an image file into a base64 string.
    
    Args:
        image_path (Path): Path to the image file.
    
    Returns:
        bytes: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read())
