import os
import requests
import zipfile
import io
import shutil
from colorama import Fore
from logging import getLogger
from packaging.version import Version

from __init__ import VERSION, SKIP_UPDATES
from core.utils import restart


REPO = "pashagta555/playerok-universal-english-mod"
logger = getLogger("universal.updater")


def get_releases():
    response = requests.get(f"https://api.github.com/repos/{REPO}/releases", timeout=5)
    response.raise_for_status()
    if response.status_code != 200:
        raise Exception(f"Error request To GitHub API: {response.status_code}")
    return response.json()


def get_latest_release(releases):
    latest = None
    latest_rel = None
    for rel in releases:
        tag_name = rel["tag_name"]
        if latest is None:
            latest = Version(tag_name)
            latest_rel = rel
        if Version(tag_name) > latest:
            latest = Version(tag_name)
            latest_rel = rel
    return latest_rel


def download_update(release_info: dict) -> bytes:
    zip_url = release_info['zipball_url']
    zip_response = requests.get(zip_url)
    if zip_response.status_code != 200:
        raise Exception(f"Error at downloading archive updates: {zip_response.status_code}")
    return zip_response.content


def install_update(release_info: dict, content: bytes) -> bool:
    temp_dir = ".temp_update"
    try:
        with zipfile.ZipFile(io.BytesIO(content), 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            archive_root = None
            for item in os.listdir(temp_dir):
                if os.path.isdir(os.path.join(temp_dir, item)):
                    archive_root = os.path.join(temp_dir, item)
                    break
            if not archive_root:
                raise Exception("IN archive No root folders!")
            for root, _, files in os.walk(archive_root):
                for file in files:
                    src = os.path.join(root, file)
                    dst = os.path.join('.', os.path.relpath(src, archive_root))
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy2(src, dst)
            return True
    finally:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)


def check_for_updates():
    try:
        releases = get_releases()
        latest_release = get_latest_release(releases)
        versions = [release["tag_name"] for release in releases]
        
        if VERSION not in versions:
            logger.info(f"yours versions {Fore.LIGHTWHITE_EX}{VERSION} {Fore.WHITE}There is not V releases repository. Last version: {Fore.LIGHTWHITE_EX}{latest_release['tag_name']}")
            return
        elif Version(VERSION) == Version(latest_release["tag_name"]):
            logger.info(f"U you installed last version: {Fore.LIGHTWHITE_EX}{VERSION}")
            return
        elif Version(VERSION) < Version(latest_release["tag_name"]):
            logger.info(f"{Fore.YELLOW}Available new version: {Fore.LIGHTWHITE_EX}{latest_release['tag_name']}")
            if SKIP_UPDATES:
                logger.info(
                    f"I'm skipping installation updates. If You want automatically download updates, change meaning "
                    f"{Fore.LIGHTWHITE_EX}SKIP_UPDATES{Fore.WHITE} on {Fore.YELLOW}False {Fore.WHITE}V file initialization {Fore.LIGHTWHITE_EX}(__init__.py)"
                )
                return
            
            logger.info(f"Loading update {latest_release['tag_name']}...")
            bytes = download_update(latest_release)
            if not bytes:
                return
            logger.info(f"Installing update {latest_release['tag_name']}...")
            if install_update(latest_release, bytes):
                logger.info(f"{Fore.YELLOW}Update {Fore.LIGHTWHITE_EX}{latest_release['tag_name']} {Fore.YELLOW}was successfully installed.")
                restart()
    except Exception as e:
        logger.error(f"{Fore.LIGHTRED_EX}Error at update: {Fore.WHITE}{e}")
