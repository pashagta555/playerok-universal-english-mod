import os
import requests
import zipfile
import io
import shutil
from colorama import Fore
from logging import getLogger

from __init__ import VERSION, SKIP_UPDATES
from core.utils import restart


REPO = "pashagta555/playerok-universal-english-mod"
logger = getLogger(f"universal.updater")


def check_for_updates():
    """
    Checks the GitHub project for new updates.
    If a new release is available - downloads and installs the update.
    """
    try:
        response = requests.get(f"https://api.github.com/repos/{REPO}/releases")
        if response.status_code != 200:
            raise Exception(f"GitHub API request error: {response.status_code}")
        releases = response.json()
        latest_release = releases[0]
        versions = [release["tag_name"] for release in releases]
        if VERSION not in versions:
            logger.info(f"Your version {Fore.LIGHTWHITE_EX}{VERSION} {Fore.WHITE}is not in the repository releases. Latest version: {Fore.LIGHTWHITE_EX}{latest_release['tag_name']}")
            return
        elif VERSION == latest_release["tag_name"]:
            logger.info(f"You have the latest version installed: {Fore.LIGHTWHITE_EX}{VERSION}")
            return
        logger.info(f"{Fore.YELLOW}New version available: {Fore.LIGHTWHITE_EX}{latest_release['tag_name']}")
        if SKIP_UPDATES:
            logger.info(f"Skipping update installation. If you want to automatically download updates, change the value "
                        f"{Fore.LIGHTWHITE_EX}SKIP_UPDATES{Fore.WHITE} to {Fore.YELLOW}False {Fore.WHITE}in the initialization file {Fore.LIGHTWHITE_EX}(__init__.py)")
            return
        logger.info(f"Downloading update: {Fore.LIGHTWHITE_EX}{latest_release['html_url']}")
        bytes = download_update(latest_release)
        if bytes:
            if install_update(latest_release, bytes):
                logger.info(f"{Fore.YELLOW}Update {Fore.LIGHTWHITE_EX}{latest_release['tag_name']} {Fore.YELLOW}was successfully installed.")
                restart()
    except Exception as e:
        logger.error(f"{Fore.LIGHTRED_EX}An error occurred while checking for updates: {Fore.WHITE}{e}")


def download_update(release_info: dict) -> bytes:
    """
    Gets update files.

    :param release_info: GitHub release information.
    :type release_info: `dict`

    :return: File contents.
    :rtype: `bytes`
    """
    try:
        logger.info(f"Loading update {release_info['tag_name']}...")
        zip_url = release_info['zipball_url']
        zip_response = requests.get(zip_url)
        if zip_response.status_code != 200:
            raise Exception(f"Error occurred while downloading update archive: {zip_response.status_code}")
        return zip_response.content
    except Exception as e:
        logger.error(f"{Fore.LIGHTRED_EX}An error occurred while downloading the update: {Fore.WHITE}{e}")
        return False


def install_update(release_info: dict, content: bytes) -> bool:
    """
    Installs update files into the current project.

    :param release_info: GitHub release information.
    :type release_info: `dict`

    :param content: File contents.
    :type content: `bytes`
    """
    temp_dir = ".temp_update"
    try:
        logger.info(f"Installing update {release_info['tag_name']}...")
        with zipfile.ZipFile(io.BytesIO(content), 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            archive_root = None
            for item in os.listdir(temp_dir):
                if os.path.isdir(os.path.join(temp_dir, item)):
                    archive_root = os.path.join(temp_dir, item)
                    break
            if not archive_root:
                raise Exception("No root folder in archive!")
            for root, _, files in os.walk(archive_root):
                for file in files:
                    src = os.path.join(root, file)
                    dst = os.path.join('.', os.path.relpath(src, archive_root))
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(src, dst)
            return True
    except Exception as e:
        logger.error(f"{Fore.LIGHTRED_EX}An error occurred while installing the update: {Fore.WHITE}{e}")
        return False
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
