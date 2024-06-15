import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))


class Urls:
    # we do a little wrapping
    HOME_PAGE: str = os.environ.get("HOME_PAGE_URL")


