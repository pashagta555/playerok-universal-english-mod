from __future__ import annotations
from typing import *
from logging import getLogger
from typing import Literal
import json
import time
import os
import tempfile
import shutil

import tls_requests
import curl_cffi

from . import types
from .exceptions import *
from .parser import *
from .enums import *
from .misc import (
    PERSISTED_QUERIES, 
    QUERIES
)


def get_account() -> Account | None:
    if hasattr(Account, "instance"):
        return getattr(Account, "instance")


class Account:
    """
    Class that describes the data and methods of a Playerok account.

    :param token: Account token.
    :type token: `str`

    :param user_agent: Browser user agent.
    :type user_agent: `str`

    :param proxy: IPv4 proxy in the format: `user:pass@ip:port` or `ip:port`, _optional_.
    :type proxy: `str` or `None`

    :param requests_timeout: Timeout for waiting on request responses.
    :type requests_timeout: `int`

    :param request_max_retries: Maximum number of retry attempts if CloudFlare protection is detected.
    :type request_max_retries: `int`
    """
    def __new__(cls, *args, **kwargs) -> Account:
        if not hasattr(cls, "instance"):
            cls.instance = super(Account, cls).__new__(cls)
        return getattr(cls, "instance")

    def __init__(
            self, 
            token: str, 
            user_agent: str = "", 
            proxy: str = None, 
            requests_timeout: int = 15,
            request_max_retries: int = 5,
            **kwargs
        ):
        self.token = token
        """Account session token."""
        self.user_agent = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        """Browser user agent."""
        self.requests_timeout = requests_timeout
        """Timeout for waiting on request responses."""
        self.proxy = proxy
        """Proxy."""
        self.__proxy_string = f"http://{self.proxy.replace('https://', '').replace('http://', '')}" if self.proxy else None
        """Proxy string."""
        self.request_max_retries = request_max_retries
        """Maximum number of retry attempts when sending a request."""

        self.base_url = "https://playerok.com"
        """Base URL for all requests."""

        self.id: str | None = None
        """Account ID. \n\n_Filled in on the first use of get()_"""
        self.username: str | None = None
        """Account username. \n\n_Filled in on the first use of get()_"""
        self.email: str | None = None
        """Account email. \n\n_Filled in on the first use of get()_"""
        self.role: str | None = None
        """Account role. \n\n_Filled in on the first use of get()_"""
        self.support_chat_id: str | None = None
        """Support chat ID. \n\n_Filled in on the first use of get()_"""
        self.system_chat_id: str | None = None
        """System chat ID. \n\n_Filled in on the first use of get()_"""
        self.unread_chats_counter: int | None = None
        """Number of unread chats. \n\n_Filled in on the first use of get()_"""
        self.is_blocked: bool | None = None
        """Whether the account is blocked. \n\n_Filled in on the first use of get()_"""
        self.is_blocked_for: str | None = None
        """Reason for blocking the account. \n\n_Filled in on the first use of get()_"""
        self.created_at: str | None = None
        """Account creation date. \n\n_Filled in on the first use of get()_"""
        self.last_item_created_at: str | None = None
        """Creation date of the last item. \n\n_Filled in on the first use of get()_"""
        self.has_frozen_balance: bool | None = None
        """Whether the account balance is frozen. \n\n_Filled in on the first use of get()_"""
        self.has_confirmed_phone_number: bool | None = None
        """Whether the phone number is confirmed. \n\n_Filled in on the first use of get()_"""
        self.can_publish_items: bool | None = None
        """Whether the account can publish items. \n\n_Filled in on the first use of get()_"""
        self.profile: AccountProfile | None = None
        """Account profile (not to be confused with the user profile). \n\n_Filled in on the first use of get()_"""

        self._cert_path = os.path.join(os.path.dirname(__file__), "cacert.pem")
        self._tmp_cert_path = os.path.join(tempfile.gettempdir(), "cacert.pem")
        shutil.copyfile(self._cert_path, self._tmp_cert_path)

        self._refresh_clients()
        self.logger = getLogger("playerokapi")

    def _refresh_clients(self):
        self.__tls_requests = tls_requests.Client(
            proxy=self.__proxy_string
        )
        self.__curl_session = curl_cffi.Session(
            impersonate="chrome",
            timeout=10,
            proxy=self.__proxy_string,
            verify=self._tmp_cert_path
        )

    def request(
        self, 
        method: Literal["get", "post"], 
        url: str, 
        headers: dict[str, str], 
        payload: dict[str, str] | None = None, 
        files: dict | None = None
    ) -> requests.Response:
        """
        Sends a request to the playerok.com server.

        :param method: HTTP method: post, get.
        :type method: `str`

        :param url: Request URL.
        :type url: `str`

        :param headers: Request headers.
        :type headers: `dict[str, str]`
        
        :param payload: Request payload.
        :type payload: `dict[str, str]` or `None`
        
        :param files: Request files.
        :type files: `dict` or `None`

        :return: Response object from requests.
        :rtype: `requests.Response`
        """
        try: x_gql_op = payload.get("operationName", "viewer")
        except: x_gql_op = "viewer"
        _headers = {
            "accept": "*/*",
            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "access-control-allow-headers": "sentry-trace, baggage",
            "apollo-require-preflight": "true",
            "apollographql-client-name": "web",
            "content-type": "application/json",
            "cookie": f"token={self.token}",
            "origin": "https://playerok.com",
            "priority": "u=1, i",
            "referer": "https://playerok.com/",
            "sec-ch-ua": "\"Chromium\";v=\"144\", \"Google Chrome\";v=\"144\", \"Not_A Brand\";v=\"99\"",
            "sec-ch-ua-arch": "\"x86\"",
            "sec-ch-ua-bitness": "\"64\"",
            "sec-ch-ua-full-version": "\"144.0.7559.110\"",
            "sec-ch-ua-full-version-list": "Not(A:Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"144.0.7559.110\", \"Google Chrome\";v=\"144.0.7559.110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-ch-ua-platform-version": "\"19.0.0\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": self.user_agent,
            "x-gql-op": x_gql_op,
            "x-gql-path": "/",
            "x-timezone-offset": "-240"
        }
        headers = {k: v for k, v in _headers.items() if k not in headers.keys()}
                
        def make_req():
            if method == "get":
                r = self.__curl_session.get(
                    url=url, 
                    params=payload, 
                    headers=headers, 
                    timeout=self.requests_timeout
                )
            elif method == "post":
                if files:
                    r = self.__tls_requests.post(
                        url=url, 
                        json=payload if not files else None, 
                        data=payload if files else None, 
                        headers=headers, 
                        files=files, 
                        timeout=self.requests_timeout
                    )
                else:
                    r = self.__curl_session.post(
                        url=url, 
                        json=payload,
                        headers=headers, 
                        timeout=self.requests_timeout
                    )
            return r

        cf_sigs = [
            "<title>Just a moment...</title>",
            "window._cf_chl_opt",
            "Enable JavaScript and cookies to continue",
            "Checking your browser before accessing",
            "cf-browser-verification",
            "Cloudflare Ray ID"
        ]
        
        for attempt in range(30):
            resp = make_req()
            if not any(sig in resp.text for sig in cf_sigs):
                break
            self._refresh_clients()
            delay = min(120.0, 5.0 * (2 ** attempt)) 
            self.logger.warning(f"Cloudflare detected, retrying request in {delay} seconds")
            time.sleep(delay)
        else:
            raise CloudflareDetectedException(resp)
        
        try: 
            json = resp.json()
            if "errors" in json:
                raise RequestError(resp)
        except: 
            pass

        if resp.status_code != 200:
           raise RequestFailedError(resp)
        
        return resp
    
    def get(self) -> Account:
        """
        Retrieves/updates account data.

        :return: Account object with updated data.
        :rtype: `playerokapi.account.Account`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "viewer",
            "query": QUERIES.get("viewer"),
            "variables": {}
        }
        
        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        data: dict = r["data"]["viewer"]
        if data is None:
            raise UnauthorizedError()
        
        self.id = data.get("id")
        self.username = data.get("username")
        self.email = data.get("email")
        self.role = data.get("role")
        self.has_frozen_balance = data.get("hasFrozenBalance")
        self.support_chat_id = data.get("supportChatId")
        self.system_chat_id = data.get("systemChatId")
        self.unread_chats_counter = data.get("unreadChatsCounter")
        self.is_blocked = data.get("isBlocked")
        self.is_blocked_for = data.get("isBlockedFor")
        self.created_at = data.get("createdAt")
        self.last_item_created_at = data.get("lastItemCreatedAt")
        self.has_confirmed_phone_number = data.get("hasConfirmedPhoneNumber")
        self.can_publish_items = data.get("canPublishItems")
        self.unread_chats_counter = data.get("unreadChatsCounter")
        
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "user",
            "variables": json.dumps({
                "username": self.username, 
                "hasSupportAccess": False
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("user")
                }
            })
        }
        
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        data: dict = r["data"]["user"]
        if data.get("__typename") == "User": self.profile = account_profile(data)
        return self
    
    def get_user(
        self, 
        id: str | None = None, 
        username: str | None = None
    ) -> types.UserProfile:
        """
        Retrieves a user profile.\n
        Can be obtained by either of the two parameters:

        :param id: User ID, _optional_.
        :type id: `str` or `None`

        :param username: Username, _optional_.
        :type username: `str` or `None`

        :return: User profile object.
        :rtype: `playerokapi.types.UserProfile`
        """
        if not any([id, username]):
            raise TypeError("None of the required arguments were provided: id, username")
        
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "user",
            "variables": json.dumps({
                "id": id, 
                "username": username, 
                "hasSupportAccess": False
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("user")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        data: dict = r["data"]["user"]
        if data.get("__typename") == "UserFragment": profile = data
        elif data.get("__typename") == "User": profile = data.get("profile")
        else: profile = None
        
        return user_profile(profile)

    def get_deals(
        self, 
        count: int = 24, 
        statuses: list[ItemDealStatuses] | None = None, 
        direction: ItemDealDirections | None = None, 
        after_cursor: str = None
    ) -> types.ItemDealList:
        """
        Retrieves deals for the account.

        :param count: Number of deals to retrieve (no more than 24 per request).
        :type count: `int`

        :param statuses: Deal statuses to retrieve, _optional_.
        :type statuses: `list[playerokapi.enums.ItemDealsStatuses]` or `None`

        :param direction: Direction of deals, _optional_.
        :type direction: `playerokapi.enums.ItemDealsDirections` or `None`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str`
        
        :return: Page of deals.
        :rtype: `playerokapi.types.ItemDealList`
        """
        str_statuses = [status.name for status in statuses] if statuses else None
        str_direction = direction.name if direction else None
        
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "deals",
            "variables": json.dumps({
                "pagination": {
                    "first": count, 
                    "after": after_cursor
                }, 
                "filter": {
                    "userId": self.id, 
                    "direction": str_direction, 
                    "status": str_statuses
                }, 
                "showForbiddenImage": True
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("deals")
                }
            })
        }
        
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return item_deal_list(r["data"]["deals"])

    def get_deal(
        self, 
        deal_id: str
    ) -> types.ItemDeal:
        """
        Retrieves a deal.

        :param deal_id: Deal ID.
        :type deal_id: `str`
        
        :return: Deal object.
        :rtype: `playerokapi.types.ItemDeal`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "deal",
            "variables": json.dumps({
                "id": deal_id,
                "hasSupportAccess": False,
                "showForbiddenImage": True
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("deal")
                }
            })
        } 
        
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return item_deal(r["data"]["deal"])
    
    def update_deal(
        self, 
        deal_id: str, 
        new_status: ItemDealStatuses
    ) -> types.ItemDeal:
        """
        Updates the status of a deal
        (used to confirm, refund, etc.).

        :param deal_id: Deal ID.
        :type deal_id: `str`

        :param new_status: New deal status.
        :type new_status: `playerokapi.enums.ItemDealStatuses`
        
        :return: Updated deal object.
        :rtype: `playerokapi.types.ItemDeal`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "updateDeal",
            "variables": {
                "input": {
                    "id": deal_id,
                    "status": new_status.name
                }
            },
            "query": QUERIES.get("updateDeal")
        }
        
        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return item_deal(r["data"]["updateDeal"])

    def get_games(
        self, 
        count: int = 24, 
        type: GameTypes | None = None, 
        after_cursor: str = None
    ) -> types.GameList:
        """
        Retrieves all games and/or applications.

        :param count: Number of games to retrieve (no more than 24 per request).
        :type count: `int`

        :param type: Type of games to retrieve. If not specified, all types are returned, _optional_.
        :type type: `playerokapi.enums.GameTypes` or `None`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str`
        
        :return: Page of games.
        :rtype: `playerokapi.types.GameList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "games",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": {
                    "type": type.name if type else None
                }
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("games")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_list(r["data"]["games"])
    
    def get_game(
        self, 
        id: str | None = None, 
        slug: str | None = None
    ) -> types.Game:
        """
        Retrieves a game/application.\n
        Can be obtained by either of the two parameters:

        :param id: Game/application ID, _optional_.
        :type id: `str` or `None`

        :param slug: Game/application page slug, _optional_.
        :type slug: `str` or `None`
        
        :return: Game object.
        :rtype: `playerokapi.types.Game`
        """
        if not any([id, slug]):
            raise TypeError("None of the required arguments were provided: id, slug")
        
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "GamePage",
            "variables": json.dumps({
                "id": id,
                "slug": slug
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("GamePage")
                }
            })
        }
        
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game(r["data"]["game"])

    def get_game_category(
        self, 
        id: str | None = None, 
        game_id: str | None = None,
        slug: str | None = None
    ) -> types.GameCategory:
        """
        Retrieves a game/application category.\n
        Can be obtained by the `id` parameter or by the combination of `game_id` and `slug`.

        :param id: Category ID, _optional_.
        :type id: `str` or `None`

        :param game_id: Game ID for the category (preferably used together with slug to find the exact category), _optional_.
        :type game_id: `str` or `None`

        :param slug: Category page slug, _optional_.
        :type slug: `str` or `None`
        
        :return: Game category object.
        :rtype: `playerokapi.types.GameCategory`
        """
        if not id and not all([game_id, slug]):
            if not id and (game_id or slug):
                raise TypeError("The argument pair game_id, slug was provided incompletely")
            raise TypeError("None of the required arguments were provided: id, game_id, slug")

        headers = {"accept": "*/*"}
        payload = {
            "operationName": "GamePageCategory",
            "variables": json.dumps({
                "id": id,
                "gameId": game_id,
                "slug": slug
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("GamePageCategory")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category(r["data"]["gameCategory"])
    
    def get_game_category_agreements(
        self, 
        game_category_id: str, 
        user_id: str | None = None,
        count: int = 24, 
        after_cursor: str | None = None
    ) -> types.GameCategoryAgreementList:
        """
        Retrieves user agreements for selling items in a category (if the user has already accepted these agreements, the list will be empty).

        :param game_category_id: Game category ID.
        :type game_category_id: `str`

        :param user_id: User ID whose agreements should be retrieved. If not specified, the current account ID is used, _optional_.
        :type user_id: `str` or `None`

        :param count: Number of agreements to retrieve (no more than 24 per request).
        :type count: `int`
        
        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of agreements.
        :rtype: `playerokapi.types.GameCategoryAgreementList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryAgreements",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": {
                    "gameCategoryId": game_category_id,
                    "userId": user_id if user_id else self.id
                }
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("gameCategoryAgreements")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_agreement_list(r["data"]["gameCategoryAgreements"])
    
    def get_game_category_obtaining_types(
        self, 
        game_category_id: str, 
        count: int = 24,
        after_cursor: str | None = None
    ) -> types.GameCategoryObtainingTypeList:
        """
        Retrieves the types (methods) of obtaining an item in a category.
        
        :param game_category_id: Game category ID.
        :type game_category_id: `str`

        :param count: Number of entries to retrieve (no more than 24 per request).
        :type count: `int`
        
        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of obtaining types.
        :rtype: `playerokapi.types.GameCategoryAgreementList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryObtainingTypes",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": {
                    "gameCategoryId": game_category_id
                }
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("gameCategoryObtainingTypes")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_obtaining_type_list(r["data"]["gameCategoryObtainingTypes"])
    
    def get_game_category_instructions(
        self, 
        game_category_id: str, 
        obtaining_type_id: str, 
        count: int = 24,
        type: GameCategoryInstructionTypes | None = None, 
        after_cursor: str | None = None
    ) -> types.GameCategoryInstructionList:
        """
        Retrieves instructions for selling/buying in a category.
        
        :param game_category_id: Game category ID.
        :type game_category_id: `str`
        
        :param obtaining_type_id: ID of the type (method) of obtaining the item.
        :type obtaining_type_id: `str`

        :param count: Number of instructions to retrieve (no more than 24 per request).
        :type count: `int`
        
        :param type: Type of instruction: for seller or buyer, _optional_.
        :type type: `enums.GameCategoryInstructionTypes` or `None`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of instructions.
        :rtype: `playerokapi.types.GameCategoryInstructionList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryInstructions",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": {
                    "gameCategoryId": game_category_id,
                    "obtainingTypeId": obtaining_type_id,
                    "type": type.name if type else None
                }
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("gameCategoryInstructions")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_instruction_list(r["data"]["gameCategoryInstructions"])

    def get_game_category_data_fields(
        self, 
        game_category_id: str, 
        obtaining_type_id: str, 
        count: int = 24,
        type: GameCategoryDataFieldTypes | None = None, 
        after_cursor: str | None = None
    ) -> types.GameCategoryDataFieldList:
        """
        Retrieves data fields of a category (which are sent after purchase).
        
        :param game_category_id: Game category ID.
        :type game_category_id: `str`
        
        :param obtaining_type_id: ID of the type (method) of obtaining the item.
        :type obtaining_type_id: `str`

        :param count: Number of fields to retrieve (no more than 24 per request).
        :type count: `int`
        
        :param type: Type of data fields, _optional_.
        :type type: `enums.GameCategoryDataFieldTypes` or `None`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of data fields.
        :rtype: `playerokapi.types.GameCategoryDataFieldList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryDataFields",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": {
                    "gameCategoryId": game_category_id,
                    "obtainingTypeId": obtaining_type_id,
                    "type": type.name if type else None
                }
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("gameCategoryDataFields")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_data_field_list(r["data"]["gameCategoryDataFields"])
    
    def get_chats(
        self, 
        count: int = 24, 
        type: ChatTypes | None = None,
        status: ChatStatuses | None = None, 
        after_cursor: str | None = None
    ) -> types.ChatList:
        """
        Retrieves all chats for the account.

        :param count: Number of chats to retrieve (no more than 24 per request).
        :type count: `int`

        :param type: Type of chats to retrieve. If not specified, all types are returned, _optional_.
        :type type: `playerokapi.enums.ChatTypes` or `None`

        :param status: Status of chats to retrieve. If not specified, any status is allowed, _optional_.
        :type status: `playerokapi.enums.ChatStatuses` or `None`
        
        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of chats.
        :rtype: `playerokapi.types.ChatList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "userChats",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": {
                    "userId": self.id,
                    "type": type.name if type else None,
                    "status": status.name if status else None
                },
                "hasSupportAccess": False
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("userChats")
                }
            })
        }
        
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return chat_list(r["data"]["chats"])
    
    def get_chat(
        self, 
        chat_id: str
    ) -> types.Chat:
        """
        Retrieves a chat.

        :param chat_id: Chat ID.
        :type chat_id: `str`
        
        :return: Chat object.
        :rtype: `playerokapi.types.Chat`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "chat",
            "variables": json.dumps({
                "id": chat_id,
                "hasSupportAccess": False
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("chat")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return chat(r["data"]["chat"])
    
    def get_chat_by_username(
        self, 
        username: str
    ) -> types.Chat | None:
        """
        Retrieves a chat by the interlocutor's username.

        :param username: Interlocutor's username.
        :type username: `str`

        :return: Chat object.
        :rtype: `playerokapi.types.Chat` or `None`
        """
        next_cursor = None
        while True:
            chats = self.get_chats(count=24, after_cursor=next_cursor)
            for chat in chats.chats:
                if any(user for user in chat.users if user.username.lower() == username.lower()):
                    return chat
            if not chats.page_info.has_next_page:
                break
            next_cursor = chats.page_info.end_cursor
    
    def get_chat_messages(
        self, 
        chat_id: str, 
        count: int = 24,
        after_cursor: str | None = None
    ) -> types.ChatMessageList:
        """
        Retrieves chat messages.

        :param chat_id: Chat ID.
        :type chat_id: `str`

        :param count: Number of messages to retrieve (no more than 24 per request).
        :type count: `int`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of messages.
        :rtype: `playerokapi.types.ChatMessageList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "chatMessages",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": {
                    "chatId": chat_id
                },
                "hasSupportAccess": False,
                "showForbiddenImage": True
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("chatMessages")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return chat_message_list(r["data"]["chatMessages"])

    def mark_chat_as_read(
        self, 
        chat_id: str
    ) -> types.Chat:
        """
        Marks a chat as read (all messages).

        :param chat_id: Chat ID.
        :type chat_id: `str`

        :return: Chat object with updated data.
        :rtype: `playerokapi.types.Chat`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "markChatAsRead",
            "query": QUERIES.get("markChatAsRead"),
            "variables": {
                "input": {
                    "chatId": chat_id
                }
            }
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return chat(r["data"]["markChatAsRead"])
    
    def send_message(
        self, 
        chat_id: str, 
        text: str | None = None,
        photo_file_path: str | None = None, 
        mark_chat_as_read: bool = False
    ) -> types.ChatMessage:
        """
        Sends a message to a chat.\n
        You can send either a text message (`text`) or a photo (`photo_file_path`).

        :param chat_id: ID of the chat to send the message to.
        :type chat_id: `str`

        :param text: Message text, _optional_.
        :type text: `str` or `None`

        :param photo_file_path: Path to the photo file, _optional_.
        :type photo_file_path: `str` or `None`

        :param mark_chat_as_read: Whether to mark the chat as read before sending, _optional_.
        :type mark_chat_as_read: `bool`

        :return: Sent message object.
        :rtype: `playerokapi.types.ChatMessage`
        """
        if not any([text, photo_file_path]):
            raise TypeError("None of the required arguments were provided: text, photo_file_path")
        
        if mark_chat_as_read:
            self.mark_chat_as_read(chat_id=chat_id)
        headers = {"accept": "*/*"}
        operations = {
            "operationName": "createChatMessage",
            "query": QUERIES.get("createChatMessageWithFile") if photo_file_path else QUERIES.get("createChatMessage"),
            "variables": {
                "input": {
                    "chatId": chat_id
                }
            }
        }
        if photo_file_path:
            operations["variables"]["file"] = None
        elif text:
            operations["variables"]["input"]["text"] = text
        
        files = {"1": open(photo_file_path, "rb")} if photo_file_path else None
        map = {"1":["variables.file"]} if photo_file_path else None
        payload = operations if not files else {"operations": json.dumps(operations), "map": json.dumps(map)}
        
        r = self.request("post", f"{self.base_url}/graphql", headers, payload, files).json()
        return chat_message(r["data"]["createChatMessage"])
 
    def create_item(
        self, 
        game_category_id: str, 
        obtaining_type_id: str, 
        name: str, 
        price: int, 
        description: str, 
        options: list[GameCategoryOption], 
        data_fields: list[GameCategoryDataField],
        attachments: list[str]
    ) -> types.Item:
        """
        Creates an item (after creation it is placed in drafts, not immediately listed for sale).

        :param game_category_id: ID of the game category in which the item should be created.
        :type game_category_id: `str`

        :param obtaining_type_id: ID of the method of obtaining the item.
        :type obtaining_type_id: `str`

        :param name: Item name.
        :type name: `str`

        :param price: Item price.
        :type price: `int` or `str`

        :param description: Item description.
        :type description: `str`

        :param options: Array of **selected** item options (attributes).
        :type options: `list[playerokapi.types.GameCategoryOption]`

        :param data_fields: Array of item data fields. \n
            !!! Fields with type `ITEM_DATA` must be filled in; these are the data specified when filling in item information.
            Fields with type `OBTAINING_DATA` **must not be filled or passed**, as this data is provided by the buyer when placing the order.
        :type data_fields: `list[playerokapi.types.GameCategoryDataField]`

        :param attachments: Array of attachment files for the item. These are paths to files.
        :type attachments: `list[str]`

        :return: Created item object.
        :rtype: `playerokapi.types.Item`
        """
        payload_attributes = {option.field: option.value for option in options}
        payload_data_fields = [{"fieldId": field.id, "value": field.value} for field in data_fields]
        
        headers = {"accept": "*/*"}
        operations = {
            "operationName": "createItem",
            "query": QUERIES.get("createItem"),
            "variables": {
                "input": {
                    "gameCategoryId": game_category_id,
                    "obtainingTypeId": obtaining_type_id,
                    "name": name,
                    "price": int(price),
                    "description": description,
                    "attributes": payload_attributes,
                    "dataFields": payload_data_fields
                },
                "attachments": [None] * len(attachments)
            }
        }
        
        map = {}
        files = {}
        
        for i, att in enumerate(attachments, start=1):
            map[str(i)] = [f"variables.attachments.{i-1}"]
            files[str(i)] = open(att, "rb")
        
        payload = {
            "operations": json.dumps(operations),
            "map": json.dumps(map)
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload, files).json()
        return item(r["data"]["createItem"])
    
    def update_item(
        self, 
        id: str, 
        name: str | None = None, 
        price: int | None = None, 
        description: str | None = None, 
        options: list[GameCategoryOption] | None = None, 
        data_fields: list[GameCategoryDataField] | None = None, 
        remove_attachments: list[str] | None = None, 
        add_attachments: list[str] | None = None
    ) -> types.Item:
        """
        Updates an item of the account.

        :param id: Item ID.
        :type id: `str`

        :param name: Item name.
        :type name: `str` or `None`

        :param price: Item price.
        :type price: `int` or `str` or `None`

        :param description: Item description.
        :type description: `str` or `None`

        :param options: Array of **selected** item options (attributes).
        :type options: `list[playerokapi.types.GameCategoryOption]` or `None`

        :param data_fields: Array of item data fields. \n
            !!! Fields with type `ITEM_DATA` must be filled in; these are the data specified when filling in item information.
            Fields with type `OBTAINING_DATA` **must not be filled or passed**, as this data is provided by the buyer when placing the order.
        :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

        :param remove_attachments: Array of IDs of item attachment files to remove.
        :type remove_attachments: `list[str]` or `None`

        :param add_attachments: Array of attachment files to add to the item. These are paths to files.
        :type add_attachments: `list[str]` or `None`

        :return: Updated item object.
        :rtype: `playerokapi.types.Item`
        """
        payload_attributes = {option.field: option.value for option in options} if options is not None else None
        payload_data_fields = [{"fieldId": field.id, "value": field.value} for field in data_fields] if data_fields is not None else None
        
        headers = {"accept": "*/*"}
        operations = {
            "operationName": "updateItem",
            "query": QUERIES.get("updateItem"),
            "variables": {
                "input": {
                    "id": id
                },
                "addedAttachments": [None] * len(add_attachments) if add_attachments else None
            }
        }
        if name: operations["variables"]["input"]["name"] = name
        if price: operations["variables"]["input"]["price"] = int(price)
        if description: operations["variables"]["input"]["description"] = description
        if options: operations["variables"]["input"]["attributes"] = payload_attributes
        if data_fields: operations["variables"]["input"]["dataFields"] = payload_data_fields
        if remove_attachments: operations["variables"]["input"]["removedAttachments"] = remove_attachments

        map = {}
        files = {}
        
        if add_attachments:
            for i, att in enumerate(add_attachments, start=1):
                map[str(i)] = [f"variables.addedAttachments.{i-1}"]
                files[str(i)] = open(att, "rb")
        
        payload = {
            "operations": json.dumps(operations),
            "map": json.dumps(map)
        }
        
        r = self.request("post", f"{self.base_url}/graphql", headers, payload if files else operations, files if files else None).json()
        return item(r["data"]["updateItem"])

    def remove_item(
        self, 
        id: str
    ) -> bool:
        """
        Completely removes an item from your account.

        :param id: Item ID.
        :type id: `str`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "removeItem",
            "query": QUERIES.get("removeItem"),
            "variables": {
                "id": id,
            }
        }
        
        self.request("post", f"{self.base_url}/graphql", headers, payload)
        return True
    
    def publish_item(
        self, 
        item_id: str, 
        priority_status_id: str, 
        transaction_provider_id: TransactionProviderIds = TransactionProviderIds.LOCAL
    ) -> types.Item:
        """
        Publishes an item for sale.

        :param item_id: Item ID.
        :type item_id: `str`

        :param priority_status_id: ID of the priority status under which the item should be listed for sale.
        :type priority_status_id: `str`

        :param transaction_provider_id: ID of the transaction provider.
        :type transaction_provider_id: `playerokapi.types.TransactionProviderIds`

        :return: Published item object.
        :rtype: `playerokapi.types.Item`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "publishItem",
            "query": QUERIES.get("publishItem"),
            "variables": {
                "input": {
                    "transactionProviderId": transaction_provider_id.name,
                    "priorityStatuses": [priority_status_id],
                    "itemId": item_id
                }
            }
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return item(r["data"]["publishItem"])

    def get_items(
        self, 
        game_id: str | None = None, 
        category_id: str | None = None, 
        count: int = 24,
        status: ItemStatuses = ItemStatuses.APPROVED, 
        after_cursor: str | None = None
    ) -> types.ItemProfileList:
        """
        Retrieves the items of a game/application.\n
        Can be obtained by either of the two parameters: `game_id`, `category_id`.

        :param game_id: Game/application ID, _optional_.
        :type game_id: `str` or `None`

        :param category_id: Game/application category ID, _optional_.
        :type category_id: `str` or `None`

        :param count: Number of items to retrieve (no more than 24 per request).
        :type count: `int`

        :param status: Type of items to retrieve: active or sold. Active by default.
        :type status: `playerokapi.enums.ItemStatuses`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of item profiles.
        :rtype: `playerokapi.types.ItemProfileList`
        """
        if not any([game_id, category_id]):
            raise TypeError("None of the required arguments were provided: game_id, category_id")
        
        headers = {"accept": "*/*"}
        filter = {"gameId": game_id, "status": [status.name] if status else None} if not category_id else {"gameCategoryId": category_id, "status": [status.name] if status else None}
        payload = {
            "operationName": "items",
            "variables": json.dumps({
                "pagination": {
                    "first": count,
                    "after": after_cursor
                },
                "filter": filter
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("items")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return item_profile_list(r["data"]["items"])

    def get_item(
        self, 
        id: str | None = None, 
        slug: str | None = None
    ) -> types.MyItem | types.Item | types.ItemProfile:
        """
        Retrieves an item (product).\n
        Can be obtained by either of the two parameters:

        :param id: Item ID, _optional_.
        :type id: `str` or `None`

        :param slug: Item page slug, _optional_.
        :type slug: `str` or `None`
        
        :return: Item object.
        :rtype: `playerokapi.types.MyItem` or `playerokapi.types.Item` or `playerokapi.types.ItemProfile`
        """
        if not any([id, slug]):
            raise TypeError("None of the required arguments were provided: id, slug")
        
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "item",
            "variables": json.dumps({
                "id": id,
                "slug": slug,
                "hasSupportAccess": False,
                "showForbiddenImage": True
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("item")
                }
            })
        }
        
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        data: dict = r["data"]["item"]
        if data["__typename"] == "MyItem": _item = my_item(data)
        elif data["__typename"] == "ItemProfile": _item = item_profile(data)
        elif data["__typename"] in ["Item", "ForeignItem"]: _item = item(data)
        else: _item = None
        return _item

    def get_item_priority_statuses(
        self, 
        item_id: str, 
        item_price: str
    ) -> list[types.ItemPriorityStatus]:
        """
        Retrieves priority statuses for an item.

        :param item_id: Item ID.
        :type item_id: `str`

        :param item_price: Item price.
        :type item_price: `int` or `str`
        
        :return: Array of item priority statuses.
        :rtype: `list[playerokapi.types.ItemPriorityStatus]`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "itemPriorityStatuses",
            "variables": json.dumps({
                "itemId": item_id,
                "price": int(item_price)
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": PERSISTED_QUERIES.get("itemPriorityStatuses")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return [item_priority_status(status) for status in r["data"]["itemPriorityStatuses"]]

    def increase_item_priority_status(
        self, 
        item_id: str, 
        priority_status_id: str, 
        payment_method_id: TransactionPaymentMethodIds | None = None, 
        transaction_provider_id: TransactionProviderIds = TransactionProviderIds.LOCAL
    ) -> types.Item:
        """
        Increases the priority status of an item.

        :param item_id: Item ID.
        :type item_id: `str`

        :param priority_status_id: ID of the priority status to change to.
        :type priority_status_id: `int` or `str`

        :param payment_method_id: Payment method, _optional_.
        :type payment_method_id: `playerokapi.enums.TransactionPaymentMethodIds` or `None`

        :param transaction_provider_id: ID of the transaction provider (LOCAL - from the wallet balance on the site).
        :type transaction_provider_id: `playerokapi.enums.TransactionProviderIds`
        
        :return: Updated item object.
        :rtype: `playerokapi.types.Item`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "increaseItemPriorityStatus",
            "query": QUERIES.get("increaseItemPriorityStatus"),
            "variables": {
                "input": {
                    "itemId": item_id,
                    "priorityStatuses": [priority_status_id],
                    "transactionProviderData": {
                        "paymentMethodId": payment_method_id.name if payment_method_id else None
                    },
                    "transactionProviderId": transaction_provider_id.name
                }
            }
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return item(r["data"]["increaseItemPriorityStatus"])

    def get_transaction_providers(
        self, 
        direction: TransactionProviderDirections = TransactionProviderDirections.IN
    ) -> list[types.TransactionProvider]:
        """
        Retrieves all transaction providers.

        :param direction: Direction of transactions (deposit/withdrawal).
        :type direction: `playerokapi.enums.TransactionProviderDirections`
        
        :return: List of transaction providers.
        :rtype: `list` of `playerokapi.types.TransactionProvider`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "transactionProviders",
            "variables": json.dumps({
                "filter": {
                    "direction": direction.name if direction else None
                }
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("transactionProviders")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return [transaction_provider(provider) for provider in r["data"]["transactionProviders"]]

    def get_transactions(
        self, 
        count: int = 24, 
        operation: TransactionOperations | None = None, 
        min_value: int | None = None,
        max_value: int | None = None, 
        provider_id: TransactionProviderIds | None = None, 
        status: TransactionStatuses | None = None,
        after_cursor: str | None = None
    ) -> TransactionList:
        """
        Retrieves all transactions of the account.

        :param count: Number of transactions to retrieve (no more than 24 per request).
        :type count: `int`

        :param operation: Transaction operation, _optional_.
        :type operation: `playerokapi.enums.TransactionOperations` or `None`

        :param min_value: Minimum transaction amount, _optional_.
        :type min_value: `int` or `None`

        :param max_value: Maximum transaction amount, _optional_.
        :type max_value: `int` or `None`

        :param provider_id: Transaction provider ID, _optional_.
        :type provider_id: `playerokapi.enums.TransactionProviderIds` or `None`

        :param status: Transaction status, _optional_.
        :type status: `playerokapi.enums.TransactionStatuses` or `None`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of transactions.
        :rtype: `playerokapi.types.TransactionList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "transactions",
            "variables": {
                "pagination": {
                    "first": count, 
                    "after": after_cursor
                }, 
                "filter": {
                    "userId": self.id
                }, 
                "hasSupportAccess": False
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("transactions")
                }
            }
        }
        
        if operation: payload["variables"]["filter"]["operation"] = [operation.name]
        if min_value or max_value:
            payload["variables"]["filter"]["value"] = {}
            if min_value: payload["variables"]["filter"]["value"]["min"] = str(min_value)
            if max_value: payload["variables"]["filter"]["value"]["max"] = str(max_value)
        if provider_id: payload["variables"]["filter"]["providerId"] = [provider_id.name]
        if status: payload["variables"]["filter"]["status"] = [status.name]

        payload["variables"] = json.dumps(payload["variables"])
        payload["extensions"] = json.dumps(payload["extensions"])
        
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return transaction_list(r["data"]["transactions"])
    
    def get_sbp_bank_members(self) -> list[SBPBankMember]:
        """
        Retrieves all SBP bank members.

        :return: List of SBP bank members.
        :rtype: `list` of `playerokapi.types.SBPBankMember`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "SbpBankMembers",
            "variables": {},
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("SbpBankMembers")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return [sbp_bank_member(member) for member in r["data"]["sbpBankMembers"]]
    
    def get_verified_cards(
        self, 
        count: int = 24, 
        after_cursor: str | None = None,
        direction: SortDirections = SortDirections.ASC
    ) -> types.UserBankCardList:
        """
        Retrieves the verified cards of the account.

        :param count: Number of bank cards to retrieve (no more than 24 per request).
        :type count: `int`

        :param after_cursor: Cursor from which parsing starts (if not set - starts from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`

        :param direction: Sort direction for bank cards.
        :type direction: `playerokapi.enums.SortDirections`
        
        :return: Page of user bank cards.
        :rtype: `playerokapi.types.UserBankCardList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "verifiedCards",
            "variables": json.dumps({
                "pagination": {
                    "first": count, 
                    "after": after_cursor
                }, 
                "sort": {
                    "direction": direction.name
                }, 
                "field": "createdAt"
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("verifiedCards")
                }
            })
        }

        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return user_bank_card_list(r["data"]["verifiedCards"])
    
    def delete_card(
        self, 
        card_id: str
    ) -> bool:
        """
        Deletes a card from those saved in the account.

        :param card_id: Bank card ID.
        :type card_id: `str`
        
        :return: True if the card was deleted, otherwise False.
        :rtype: `bool`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "deleteCard",
            "query": QUERIES.get("deleteCard"),
            "variables": {
                "input": {
                    "cardId": card_id
                }
            }
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return r["data"]["deleteCard"]
    
    def request_withdrawal(
        self, 
        provider: TransactionProviderIds, 
        account: str, 
        value: int,
        payment_method_id: TransactionPaymentMethodIds | None = None,
        sbp_bank_member_id: str | None = None
    ) -> types.Transaction:
        """
        Creates a request to withdraw funds from the account balance.

        :param provider: Transaction provider.
        :type provider: `playerokapi.enums.TransactionProviderIds`

        :param account: ID of the added card (or phone number if the provider is SBP) to which the withdrawal should be made.
        :type account: `str`

        :param value: Withdrawal amount.
        :type value: `int`

        :param payment_method_id: Payment method ID, _optional_.
        :type payment_method_id: `playerokapi.enums.TransactionPaymentMethodIds` or `None`

        :param sbp_bank_member_id: SBP bank member ID (only if the SBP provider is specified), _optional_.
        :type sbp_bank_member_id: `str` or `None`
        
        :return: Withdrawal transaction object.
        :rtype: `playerokapi.types.Transaction`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "requestWithdrawal",
            "query": QUERIES.get("requestWithdrawal"),
            "variables": {
                "input": {
                    "provider": provider.name,
                    "account": account,
                    "value": value,
                    "providerData": {
                        "paymentMethodId": payment_method_id.name if payment_method_id else None,
                        "sbpBankMemberId": sbp_bank_member_id if sbp_bank_member_id else None
                    }
                }
            }
        }
        
        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return transaction(r["data"]["requestWithdrawal"])
    
    def remove_transaction(
        self, 
        transaction_id: str
    ) -> types.Transaction:
        """
        Deletes a transaction (for example, you can cancel a withdrawal).

        :param transaction_id: Transaction ID.
        :type transaction_id: `str`
        
        :return: Cancelled transaction object.
        :rtype: `playerokapi.types.Transaction`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "removeTransaction",
            "query": QUERIES.get("removeTransaction"),
            "variables": {
                "id": transaction_id
            }
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return transaction(r["data"]["removeTransaction"])