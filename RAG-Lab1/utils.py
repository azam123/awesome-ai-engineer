"""
utils.py

Common utility functions.

Author: Mohammad Azam Shaikh
"""

import os
import logging
from pathlib import Path

from config import config


# ---------------------------------------------------
# Logging
# ---------------------------------------------------

def configure_logging():

    Path(config.LOG_DIRECTORY).mkdir(exist_ok=True)

    logging.basicConfig(

        level=config.LOG_LEVEL,

        format="%(asctime)s | %(levelname)s | %(message)s",

        handlers=[

            logging.FileHandler(
                os.path.join(
                    config.LOG_DIRECTORY,
                    config.LOG_FILE
                )
            ),

            logging.StreamHandler()
        ]
    )


# ---------------------------------------------------
# Create Project Directories
# ---------------------------------------------------

def create_directories():

    folders = [

        config.UPLOAD_DIRECTORY,

        config.LOG_DIRECTORY,

        config.CHROMA_DB_DIRECTORY

    ]

    for folder in folders:

        Path(folder).mkdir(

            parents=True,

            exist_ok=True
        )


# ---------------------------------------------------
# Validate PDF
# ---------------------------------------------------

def validate_pdf(file_path):

    if file_path is None:

        return False

    extension = os.path.splitext(file_path)[1].lower()

    if extension not in config.ALLOWED_FILE_TYPES:

        return False

    return True


# ---------------------------------------------------
# File Size
# ---------------------------------------------------

def file_size_mb(file_path):

    return round(

        os.path.getsize(file_path)

        / (1024 * 1024),

        2

    )


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

def system_status():

    return {

        "Embedding Model":

            config.EMBEDDING_MODEL,

        "GPT Model":

            config.GPT_MODEL,

        "Vector DB":

            config.CHROMA_DB_DIRECTORY,

        "Chunk Size":

            config.CHUNK_SIZE,

        "Chunk Overlap":

            config.CHUNK_OVERLAP,

        "Top K":

            config.TOP_K_RESULTS

    }
