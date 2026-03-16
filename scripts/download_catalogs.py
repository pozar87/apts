import logging
import os
import sys

# Ensure project root is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apts.cache import download_all_data

# Set up basic logging to see progress
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    Manually triggers the download of all required astronomical catalogs and data files.
    This script is useful for setting up an environment before running tests or when
    automatic downloads fail due to network restrictions.
    """
    logger.info("Starting download of astronomical data files...")
    try:
        download_all_data()
        logger.info("All data files downloaded successfully.")

        # Verify specific directories
        if os.path.exists("data/hip_main.dat"):
            logger.info("Verified: Hipparcos catalog (data/hip_main.dat) is present.")
        else:
            logger.warning("Hipparcos catalog download may have failed or was skipped.")

    except Exception as e:
        logger.error(f"An error occurred during download: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
