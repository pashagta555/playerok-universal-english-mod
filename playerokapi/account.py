from __future__ import annotations
from typing import *
from logging import getLogger
from typing import Literal
import json
import random
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
from .misc import PERSISTED_QUERIES


def get_account() -> Account | None:
    if hasattr(Account, "instance"):
        return getattr(Account, "instance")


class Account:
    """
    Class describing Playerok account data and methods.

    :param token: Account token.
    :type token: `str`

    :param user_agent: Browser user agent.
    :type user_agent: `str`

    :param proxy: IPV4 proxy in format: `user:pass@ip:port` or `ip:port`, _optional_.
    :type proxy: `str` or `None`

    :param requests_timeout: Request response timeout.
    :type requests_timeout: `int`

    :param request_max_retries: Maximum number of retry attempts for sending request if CloudFlare protection was detected.
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
        """ Account session token. """
        self.user_agent = user_agent
        """ Browser user agent. """
        self.requests_timeout = requests_timeout
        """ Request response timeout. """
        self.proxy = proxy
        """ Proxy. """
        self.__proxy_string = f"http://{self.proxy.replace('https://', '').replace('http://', '')}" if self.proxy else None
        """ Proxy string. """
        self.request_max_retries = request_max_retries
        """ Maximum number of retry attempts for sending request. """

        self.base_url = "https://playerok.com"
        """ Base URL for all requests. """

        self.id: str | None = None
        """ Account ID. \n\n_Filled on first use of get()_ """
        self.username: str | None = None
        """ Account username. \n\n_Filled on first use of get()_ """
        self.email: str | None = None
        """ Account email. \n\n_Filled on first use of get()_ """
        self.role: str | None = None
        """ Account role. \n\n_Filled on first use of get()_ """
        self.support_chat_id: str | None = None
        """ Support chat ID. \n\n_Filled on first use of get()_ """
        self.system_chat_id: str | None = None
        """ System chat ID. \n\n_Filled on first use of get()_ """
        self.unread_chats_counter: int | None = None
        """ Number of unread chats. \n\n_Filled on first use of get()_ """
        self.is_blocked: bool | None = None
        """ Whether account is blocked. \n\n_Filled on first use of get()_ """
        self.is_blocked_for: str | None = None
        """ Account block reason. \n\n_Filled on first use of get()_ """
        self.created_at: str | None = None
        """ Account creation date. \n\n_Filled on first use of get()_ """
        self.last_item_created_at: str | None = None
        """ Last item creation date. \n\n_Filled on first use of get()_ """
        self.has_frozen_balance: bool | None = None
        """ Whether account balance is frozen. \n\n_Filled on first use of get()_ """
        self.has_confirmed_phone_number: bool | None = None
        """ Whether phone number is confirmed. \n\n_Filled on first use of get()_ """
        self.can_publish_items: bool | None = None
        """ Whether can sell items. \n\n_Filled on first use of get()_ """
        self.profile: AccountProfile | None = None
        """ Account profile (not to be confused with user profile). \n\n_Filled on first use of get()_ """

        self.__cert_path = os.path.join(os.path.dirname(__file__), "cacert.pem")
        self.__tmp_cert_path = os.path.join(tempfile.gettempdir(), "cacert.pem")
        shutil.copyfile(self.__cert_path, self.__tmp_cert_path)

        self._refresh_clients()
        self.__logger = getLogger("playerokapi")

    def _refresh_clients(self):
        self.__tls_requests = tls_requests.Client(
            proxy=self.__proxy_string
        )
        self.__curl_session = curl_cffi.Session(
            impersonate="chrome",
            timeout=10,
            proxy=self.__proxy_string,
            verify=self.__tmp_cert_path
        )

    def request(self, method: Literal["get", "post"], url: str, headers: dict[str, str], 
                payload: dict[str, str] | None = None, files: dict | None = None) -> requests.Response:
        """
        Sends request to playerok.com server.

        :param method: Request method: post, get.
        :type method: `str`

        :param url: Request URL.
        :type url: `str`

        :param headers: Request headers.
        :type headers: `dict[str, str]`
        
        :param payload: Request payload.
        :type payload: `dict[str, str]` or `None`
        
        :param files: Request files.
        :type files: `dict` or `None`

        :return: Request response.
        :rtype: `requests.Response`
        """
        agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/118.0.2088.62 Chrome/118.0.5993.90 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:119.0) Gecko/20100101 Firefox/119.0",
            "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36 OPR/88.0.0.0",
            "Opera/9.80 (Windows NT 6.3; U; en) Presto/2.12.388 Version/12.16"
        ]
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
            "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
            "sec-ch-ua-arch": "\"x86\"",
            "sec-ch-ua-bitness": "\"64\"",
            "sec-ch-ua-full-version": "\"142.0.7444.162\"",
            "sec-ch-ua-full-version-list": "\"Chromium\";v=\"142.0.7444.162\", \"Google Chrome\";v=\"142.0.7444.162\", \"Not_A Brand\";v=\"99.0.0.0\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-ch-ua-platform-version": "\"19.0.0\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": self.user_agent if self.user_agent else random.choice(agents),
            "x-gql-op": "viewer",
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

        cloudflare_signatures = [
            "<title>Just a moment...</title>",
            "window._cf_chl_opt",
            "Enable JavaScript and cookies to continue",
            "Checking your browser before accessing",
            "cf-browser-verification",
            "Cloudflare Ray ID"
        ]
        for attempt in range(30):
            resp = make_req()
            if not any(sig in resp.text for sig in cloudflare_signatures):
                break
            self._refresh_clients()
            delay = min(120.0, 5.0 * (2 ** attempt)) 
            self.__logger.error(f"Cloudflare Detected, trying to send request again in {delay} seconds")
            time.sleep(delay)
        else:
            raise CloudflareDetectedException(resp)
        try:
            if "errors" in resp.json():
                for attempt in range(3):
                    resp = make_req()
                    exc = RequestError(resp)
                    if exc.error_code != 500:
                        break
                    delay = min(120.0, 2 ** attempt)
                    self.__logger.error(f"500 Error Code, trying to send request again in {delay} seconds")
                    time.sleep(delay)
                else:
                    raise exc
        except:
            pass
        if resp.status_code != 200:
           raise RequestFailedError(resp)
        return resp
    
    def get(self) -> Account:
        """
        Gets/updates account data.

        :return: Account object with updated data.
        :rtype: `playerokapi.account.Account`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "viewer",
            "query": "query viewer {\n  viewer {\n    ...Viewer\n    __typename\n  }\n}\n\nfragment Viewer on User {\n  id\n  username\n  email\n  role\n  hasFrozenBalance\n  supportChatId\n  systemChatId\n  unreadChatsCounter\n  isBlocked\n  isBlockedFor\n  createdAt\n  lastItemCreatedAt\n  hasConfirmedPhoneNumber\n  canPublishItems\n  profile {\n    id\n    avatarURL\n    testimonialCounter\n    __typename\n  }\n  __typename\n}",
            "query": "query viewer {\n  viewer {\n    ...Viewer\n    __typename\n  }\n}\n\nfragment Viewer on User {\n  id\n  username\n  email\n  role\n  hasFrozenBalance\n  supportChatId\n  systemChatId\n  unreadChatsCounter\n  isBlocked\n  isBlockedFor\n  createdAt\n  lastItemCreatedAt\n  hasConfirmedPhoneNumber\n  canPublishItems\n  profile {\n    id\n    avatarURL\n    testimonialCounter\n    __typename\n  }\n  __typename\n}",
            "variables": {}
        }
        r = self.request("post", f"{self.base_url}/graphql", headers, payload)
        rjson = r.json()
        data: dict = rjson["data"]["viewer"]
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
        
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "user",
            "variables": json.dumps({"username": self.username, "hasSupportAccess": False}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("user")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        data: dict = r["data"]["user"]
        if data.get("__typename") == "User": self.profile = account_profile(data)
        return self
    
    def get_user(self, id: str | None = None, username: str | None = None) -> types.UserProfile:
        """
        Gets user profile.\n
        Can be obtained by either of two parameters:

        :param id: User ID, _optional_.
        :type id: `str` or `None`

        :param username: User username, _optional_.
        :type username: `str` or `None`

        :return: User profile object.
        :rtype: `playerokapi.types.UserProfile`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "user",
            "variables": json.dumps({"id": id, "username": username, "hasSupportAccess": False}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("user")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        data: dict = r["data"]["user"]
        if data.get("__typename") == "UserFragment": profile = data
        elif data.get("__typename") == "User": profile = data.get("profile")
        else: profile = None
        return user_profile(profile)

    def get_deals(self, count: int = 24, statuses: list[ItemDealStatuses] | None = None, 
                  direction: ItemDealDirections | None = None, after_cursor: str = None) -> types.ItemDealList:
        """
        Gets account deals.

        :param count: Number of deals to get (no more than 24 per request).
        :type count: `int`

        :param statuses: Deal statuses to get, _optional_.
        :type statuses: `list[playerokapi.enums.ItemDealStatuses]` or `None`

        :param direction: Deal direction, _optional_.
        :type direction: `playerokapi.enums.ItemDealDirections` or `None`

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str`
        
        :return: Page of deals.
        :rtype: `playerokapi.types.ItemDealList`
        """
        str_statuses = [status.name for status in statuses] if statuses else None
        str_direction = direction.name if direction else None
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "deals",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"userId": self.id, "direction": str_direction, "status": str_statuses}, "showForbiddenImage": True}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("deals")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return item_deal_list(r["data"]["deals"])

    def get_deal(self, deal_id: str) -> types.ItemDeal:
        """
        Gets deal.

        :param deal_id: Deal ID.
        :type deal_id: `str`
        
        :return: Deal object.
        :rtype: `playerokapi.types.ItemDeal`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "deal",
            "variables": json.dumps({"id": deal_id, "hasSupportAccess": False, "showForbiddenImage": True}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("deal")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return item_deal(r["data"]["deal"])
    
    def update_deal(self, deal_id: str, new_status: ItemDealStatuses) -> types.ItemDeal:
        """
        Updates deal status
        (used to confirm, issue refund, etc.).

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
            "query": "mutation updateDeal($input: UpdateItemDealInput!) {\n  updateDeal(input: $input) {\n    ...RegularItemDeal\n    __typename\n  }\n}\n\nfragment RegularItemDeal on ItemDeal {\n  id\n  status\n  direction\n  statusExpirationDate\n  statusDescription\n  obtaining\n  hasProblem\n  reportProblemEnabled\n  completedBy {\n    ...MinimalUserFragment\n    __typename\n  }\n  props {\n    ...ItemDealProps\n    __typename\n  }\n  prevStatus\n  completedAt\n  createdAt\n  logs {\n    ...ItemLog\n    __typename\n  }\n  transaction {\n    ...ItemDealTransaction\n    __typename\n  }\n  user {\n    ...UserEdgeNode\n    __typename\n  }\n  chat {\n    ...RegularChatId\n    __typename\n  }\n  item {\n    ...PartialDealItem\n    __typename\n  }\n  testimonial {\n    ...RegularItemDealTestimonial\n    __typename\n  }\n  obtainingFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  commentFromBuyer\n  __typename\n}\n\nfragment MinimalUserFragment on UserFragment {\n  id\n  username\n  role\n  __typename\n}\n\nfragment ItemDealProps on ItemDealProps {\n  autoConfirmPeriod\n  __typename\n}\n\nfragment ItemLog on ItemLog {\n  id\n  event\n  createdAt\n  user {\n    ...UserEdgeNode\n    __typename\n  }\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment ItemDealTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  status\n  value\n  createdAt\n  paymentMethodId\n  statusExpirationDate\n  __typename\n}\n\nfragment RegularChatId on Chat {\n  id\n  __typename\n}\n\nfragment PartialDealItem on Item {\n  ...PartialDealMyItem\n  ...PartialDealForeignItem\n  __typename\n}\n\nfragment PartialDealMyItem on MyItem {\n  id\n  slug\n  priority\n  status\n  name\n  price\n  priorityPrice\n  rawPrice\n  statusExpirationDate\n  sellerType\n  approvalDate\n  createdAt\n  priorityPosition\n  viewsCounter\n  feeMultiplier\n  comment\n  attachments {\n    ...RegularFile\n    __typename\n  }\n  user {\n    ...UserEdgeNode\n    __typename\n  }\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  category {\n    ...MinimalGameCategory\n    __typename\n  }\n  dataFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  obtainingType {\n    ...MinimalGameCategoryObtainingType\n    __typename\n  }\n  __typename\n}\n\nfragment RegularFile on File {\n  id\n  url\n  filename\n  mime\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment MinimalGameCategory on GameCategory {\n  id\n  slug\n  name\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment MinimalGameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment PartialDealForeignItem on ForeignItem {\n  id\n  slug\n  priority\n  status\n  name\n  price\n  rawPrice\n  sellerType\n  approvalDate\n  priorityPosition\n  createdAt\n  viewsCounter\n  feeMultiplier\n  comment\n  attachments {\n    ...RegularFile\n    __typename\n  }\n  user {\n    ...UserEdgeNode\n    __typename\n  }\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  category {\n    ...MinimalGameCategory\n    __typename\n  }\n  dataFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  obtainingType {\n    ...MinimalGameCategoryObtainingType\n    __typename\n  }\n  __typename\n}\n\nfragment RegularItemDealTestimonial on Testimonial {\n  id\n  status\n  text\n  rating\n  createdAt\n  updatedAt\n  creator {\n    ...RegularUserFragment\n    __typename\n  }\n  moderator {\n    ...RegularUserFragment\n    __typename\n  }\n  user {\n    ...RegularUserFragment\n    __typename\n  }\n  __typename\n}"
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return item_deal(r["data"]["updateDeal"])

    def get_games(self, count: int = 24, type: GameTypes | None = None, 
                  after_cursor: str = None) -> types.GameList:
        """
        Gets all games and/or applications.

        :param count: Number of games to get (no more than 24 per request).
        :type count: `int`

        :param type: Type of games to get. If not specified, gets all at once, _optional_.
        :type type: `playerokapi.enums.GameTypes` or `None`

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str`
        
        :return: Page of games.
        :rtype: `playerokapi.types.GameList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "games",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"type": type.name} if type else {}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("games")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_list(r["data"]["games"])
    
    def get_game(self, id: str | None = None, slug: str | None = None) -> types.Game:
        """
        Gets game/application.\n
        Can be obtained by either of two parameters:

        :param id: Game/application ID, _optional_.
        :type id: `str` or `None`

        :param slug: Game/application page name, _optional_.
        :type slug: `str` or `None`
        
        :return: Game object.
        :rtype: `playerokapi.types.Game`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "GamePage",
            "variables": json.dumps({"id": id, "slug": slug}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("game")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game(r["data"]["game"])

    def get_game_category(self, id: str | None = None, game_id: str | None = None,
                          slug: str | None = None) -> types.GameCategory:
        """
        Gets game/application category.\n
        Can be obtained by `id` parameter or by combination of `game_id` and `slug` parameters

        :param id: Category ID, _optional_.
        :type id: `str` or `None`

        :param game_id: Category game ID (better to specify together with slug to find exact category), _optional_.
        :type game_id: `str` or `None`

        :param slug: Category page name, _optional_.
        :type slug: `str` or `None`
        
        :return: Game category object.
        :rtype: `playerokapi.types.GameCategory`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "GamePageCategory",
            "variables": json.dumps({"id": id, "gameId": game_id, "slug": slug}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("game_category")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category(r["data"]["gameCategory"])
    
    def get_game_category_agreements(self, game_category_id: str, user_id: str | None = None,
                                     count: int = 24, after_cursor: str | None = None) -> types.GameCategoryAgreementList:
        """
        Gets user agreements for selling items in category (if user has already accepted these agreements - list will be empty).

        :param game_category_id: Game category ID.
        :type game_category_id: `str`

        :param user_id: User ID whose agreements to get. If not specified, will get by your account ID, _optional_.
        :type user_id: `str` or `None`

        :param count: Number of agreements to get (no more than 24 per request).
        :type count: `int`
        
        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of agreements.
        :rtype: `playerokapi.types.GameCategoryAgreementList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryAgreements",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"gameCategoryId": game_category_id, "userId": user_id if user_id else self.id}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("game_category_agreements")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_agreement_list(r["data"]["gameCategoryAgreements"])
    
    def get_game_category_obtaining_types(self, game_category_id: str, count: int = 24,
                                          after_cursor: str | None = None) -> types.GameCategoryObtainingTypeList:
        """
        Gets item obtaining types (methods) in category.
        
        :param game_category_id: Game category ID.
        :type game_category_id: `str`

        :param count: Number of obtaining types to get (no more than 24 per request).
        :type count: `int`
        
        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of obtaining types.
        :rtype: `playerokapi.types.GameCategoryObtainingTypeList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryObtainingTypes",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"gameCategoryId": game_category_id}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("game_category_obtaining_types")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_obtaining_type_list(r["data"]["gameCategoryObtainingTypes"])
    
    def get_game_category_instructions(self, game_category_id: str, obtaining_type_id: str, count: int = 24,
                                       type: GameCategoryInstructionTypes | None = None, after_cursor: str | None = None) -> types.GameCategoryInstructionList:
        """
        Gets selling/buying instructions in category.
        
        :param game_category_id: Game category ID.
        :type game_category_id: `str`
        
        :param obtaining_type_id: Item obtaining type (method) ID.
        :type obtaining_type_id: `str`

        :param count: Number of instructions to get (no more than 24 per request).
        :type count: `int`
        
        :param type: Instruction type: for seller or for buyer, _optional_.
        :type type: `enums.GameCategoryInstructionTypes` or `None`

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of instructions.
        :rtype: `playerokapi.types.GameCategoryInstructionList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryInstructions",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"gameCategoryId": game_category_id, "obtainingTypeId": obtaining_type_id, "type": type.name if type else None}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("game_category_instructions")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_instruction_list(r["data"]["gameCategoryInstructions"])

    def get_game_category_data_fields(self, game_category_id: str, obtaining_type_id: str, count: int = 24,
                                      type: GameCategoryDataFieldTypes | None = None, after_cursor: str | None = None) -> types.GameCategoryDataFieldList:
        """
        Gets category data fields (which are sent after purchase).
        
        :param game_category_id: Game category ID.
        :type game_category_id: `str`
        
        :param obtaining_type_id: Item obtaining type (method) ID.
        :type obtaining_type_id: `str`

        :param count: Number of data fields to get (no more than 24 per request).
        :type count: `int`
        
        :param type: Data field type, _optional_.
        :type type: `enums.GameCategoryDataFieldTypes` or `None`

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of data fields.
        :rtype: `playerokapi.types.GameCategoryDataFieldList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "gameCategoryDataFields",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"gameCategoryId": game_category_id, "obtainingTypeId": obtaining_type_id, "type": type.name if type else None}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("game_category_data_fields")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return game_category_data_field_list(r["data"]["gameCategoryDataFields"])
    
    def get_chats(self, count: int = 24, type: ChatTypes | None = None,
                  status: ChatStatuses | None = None, after_cursor: str | None = None) -> types.ChatList:
        """
        Gets all account chats.

        :param count: Number of chats to get (no more than 24 per request).
        :type count: `int`

        :param type: Type of chats to get. If not specified, gets all at once, _optional_.
        :type type: `playerokapi.enums.ChatTypes` or `None`

        :param status: Status of chats to get. If not specified, gets any, _optional_.
        :type status: `playerokapi.enums.ChatStatuses` or `None`
        
        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of chats.
        :rtype: `playerokapi.types.ChatList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "chats",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"userId": self.id, "type": type.name if type else None, "status": status.name if status else None}, "hasSupportAccess": False}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("chats")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return chat_list(r["data"]["chats"])
    
    def get_chat(self, chat_id: str) -> types.Chat:
        """
        Gets chat.

        :param chat_id: Chat ID.
        :type chat_id: `str`
        
        :return: Chat object.
        :rtype: `playerokapi.types.Chat`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "chat",
            "variables": json.dumps({"id": chat_id, "hasSupportAccess": False}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("chat")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return chat(r["data"]["chat"])
    
    def get_chat_by_username(self, username: str) -> types.Chat | None:
        """
        Gets chat by interlocutor username.

        :param username: Interlocutor username.
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
    
    def get_chat_messages(self, chat_id: str, count: int = 24,
                          after_cursor: str | None = None) -> types.ChatMessageList:
        """
        Gets chat messages.

        :param chat_id: Chat ID.
        :type chat_id: `str`

        :param count: Number of messages to get (no more than 24 per request).
        :type count: `int`

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of messages.
        :rtype: `playerokapi.types.ChatMessageList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "chatMessages",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": {"chatId": chat_id}, "hasSupportAccess": False, "showForbiddenImage": True}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("chat_messages")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return chat_message_list(r["data"]["chatMessages"])

    def mark_chat_as_read(self, chat_id: str) -> types.Chat:
        """
        Marks chat as read (all messages).

        :param chat_id: Chat ID.
        :type chat_id: `str`

        :return: Chat object with updated data.
        :rtype: `playerokapi.types.Chat`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "markChatAsRead",
            "query": "mutation markChatAsRead($input: MarkChatAsReadInput!) {\n	markChatAsRead(input: $input) {\n		...RegularChat\n		__typename\n	}\n}\n\nfragment RegularChat on Chat {\n	id\n	type\n	unreadMessagesCounter\n	bookmarked\n	isTextingAllowed\n	owner {\n		...ChatParticipant\n		__typename\n	}\n	agent {\n		...ChatParticipant\n		__typename\n	}\n	participants {\n		...ChatParticipant\n		__typename\n	}\n	deals {\n		...ChatActiveItemDeal\n		__typename\n	}\n	status\n	startedAt\n	finishedAt\n	__typename\n}\n\nfragment ChatParticipant on UserFragment {\n	...RegularUserFragment\n	__typename\n}\n\nfragment RegularUserFragment on UserFragment {\n	id\n	username\n	role\n	avatarURL\n	isOnline\n	isBlocked\n	rating\n	testimonialCounter\n	createdAt\n	supportChatId\n	systemChatId\n	__typename\n}\n\nfragment ChatActiveItemDeal on ItemDealProfile {\n	id\n	direction\n	status\n	hasProblem\n	testimonial {\n		id\n		rating\n		__typename\n	}\n	item {\n		...ChatDealItemEdgeNode\n		__typename\n	}\n	user {\n		...RegularUserFragment\n		__typename\n	}\n	__typename\n}\n\nfragment ChatDealItemEdgeNode on ItemProfile {\n	...ChatDealMyItemEdgeNode\n	...ChatDealForeignItemEdgeNode\n	__typename\n}\n\nfragment ChatDealMyItemEdgeNode on MyItemProfile {\n	id\n	slug\n	priority\n	status\n	name\n	price\n	rawPrice\n	statusExpirationDate\n	sellerType\n	attachment {\n		...PartialFile\n		__typename\n	}\n	user {\n		...UserItemEdgeNode\n		__typename\n	}\n	approvalDate\n	createdAt\n	priorityPosition\n	feeMultiplier\n	__typename\n}\n\nfragment PartialFile on File {\n	id\n	url\n	__typename\n}\n\nfragment UserItemEdgeNode on UserFragment {\n	...UserEdgeNode\n	__typename\n}\n\nfragment UserEdgeNode on UserFragment {\n	...RegularUserFragment\n	__typename\n}\n\nfragment ChatDealForeignItemEdgeNode on ForeignItemProfile {\n	id\n	slug\n	priority\n	status\n	name\n	price\n	rawPrice\n	sellerType\n	attachment {\n		...PartialFile\n		__typename\n	}\n	user {\n		...UserItemEdgeNode\n		__typename\n	}\n	approvalDate\n	priorityPosition\n	createdAt\n	feeMultiplier\n	__typename\n}",
            "variables": {
                "input": {
                    "chatId": chat_id
                }
            }
        }
        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return chat(r["data"]["markChatAsRead"])
    
    def send_message(self, chat_id: str, text: str | None = None,
                     photo_file_path: str | None = None, mark_chat_as_read: bool = False) -> types.ChatMessage:
        """
        Sends message to chat.\n
        Can send text message `text` or photo `photo_file_path`.

        :param chat_id: Chat ID to send message to.
        :type chat_id: `str`

        :param text: Message text, _optional_.
        :type text: `str` or `None`

        :param photo_file_path: Path to photo file, _optional_.
        :type photo_file_path: `str` or `None`

        :param mark_chat_as_read: Mark chat as read before sending, _optional_.
        :type mark_chat_as_read: `bool`

        :return: Sent message object.
        :rtype: `playerokapi.types.ChatMessage`
        """
        if mark_chat_as_read:
            self.mark_chat_as_read(chat_id=chat_id)
        headers = {"accept": "*/*"}
        if photo_file_path: query = "mutation createChatMessage($input: CreateChatMessageInput!, $file: Upload, $showForbiddenImage: Boolean) {\n  createChatMessage(input: $input, file: $file) {\n    ...RegularChatMessage\n    __typename\n  }\n}\n\nfragment RegularChatMessage on ChatMessage {\n  id\n  text\n  createdAt\n  deletedAt\n  isRead\n  isSuspicious\n  isBulkMessaging\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  file {\n    ...PartialFile\n    __typename\n  }\n  user {\n    ...ChatMessageUserFields\n    __typename\n  }\n  deal {\n    ...ChatMessageItemDeal\n    __typename\n  }\n  item {\n    ...ItemEdgeNode\n    __typename\n  }\n  transaction {\n    ...RegularTransaction\n    __typename\n  }\n  moderator {\n    ...UserEdgeNode\n    __typename\n  }\n  eventByUser {\n    ...ChatMessageUserFields\n    __typename\n  }\n  eventToUser {\n    ...ChatMessageUserFields\n    __typename\n  }\n  isAutoResponse\n  event\n  buttons {\n    ...ChatMessageButton\n    __typename\n  }\n  images {\n    ...RegularFile\n    __typename\n  }\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment ChatMessageUserFields on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment ChatMessageItemDeal on ItemDeal {\n  id\n  direction\n  status\n  statusDescription\n  hasProblem\n  user {\n    ...ChatParticipant\n    __typename\n  }\n  testimonial {\n    ...ChatMessageDealTestimonial\n    __typename\n  }\n  item {\n    id\n    name\n    price\n    slug\n    rawPrice\n    sellerType\n    user {\n      ...ChatParticipant\n      __typename\n    }\n    category {\n      id\n      __typename\n    }\n    attachments(showForbiddenImage: $showForbiddenImage) {\n      ...PartialFile\n      __typename\n    }\n    isAttachmentsForbidden\n    comment\n    dataFields {\n      ...GameCategoryDataFieldWithValue\n      __typename\n    }\n    obtainingType {\n      ...GameCategoryObtainingType\n      __typename\n    }\n    __typename\n  }\n  obtainingFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  chat {\n    id\n    type\n    __typename\n  }\n  transaction {\n    id\n    statusExpirationDate\n    __typename\n  }\n  statusExpirationDate\n  commentFromBuyer\n  __typename\n}\n\nfragment ChatParticipant on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment ChatMessageDealTestimonial on Testimonial {\n  id\n  status\n  text\n  rating\n  createdAt\n  updatedAt\n  creator {\n    ...RegularUserFragment\n    __typename\n  }\n  moderator {\n    ...RegularUserFragment\n    __typename\n  }\n  user {\n    ...RegularUserFragment\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment GameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  agreements {\n    ...MinimalGameCategoryAgreement\n    __typename\n  }\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment MinimalGameCategoryAgreement on GameCategoryAgreement {\n  description\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment ItemEdgeNode on ItemProfile {\n  ...MyItemEdgeNode\n  ...ForeignItemEdgeNode\n  __typename\n}\n\nfragment MyItemEdgeNode on MyItemProfile {\n  id\n  slug\n  priority\n  status\n  name\n  price\n  rawPrice\n  statusExpirationDate\n  sellerType\n  attachment(showForbiddenImage: $showForbiddenImage) {\n    ...PartialFile\n    __typename\n  }\n  isAttachmentsForbidden\n  user {\n    ...UserItemEdgeNode\n    __typename\n  }\n  approvalDate\n  createdAt\n  priorityPosition\n  viewsCounter\n  feeMultiplier\n  __typename\n}\n\nfragment UserItemEdgeNode on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment ForeignItemEdgeNode on ForeignItemProfile {\n  id\n  slug\n  priority\n  status\n  name\n  price\n  rawPrice\n  sellerType\n  attachment(showForbiddenImage: $showForbiddenImage) {\n    ...PartialFile\n    __typename\n  }\n  isAttachmentsForbidden\n  user {\n    ...UserItemEdgeNode\n    __typename\n  }\n  approvalDate\n  priorityPosition\n  createdAt\n  viewsCounter\n  feeMultiplier\n  __typename\n}\n\nfragment RegularTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  provider {\n    ...RegularTransactionProvider\n    __typename\n  }\n  user {\n    ...RegularUserFragment\n    __typename\n  }\n  creator {\n    ...RegularUserFragment\n    __typename\n  }\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  fee\n  createdAt\n  props {\n    ...RegularTransactionProps\n    __typename\n  }\n  verifiedAt\n  verifiedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  completedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  paymentMethodId\n  completedAt\n  isSuspicious\n  spbBankName\n  __typename\n}\n\nfragment RegularTransactionProvider on TransactionProvider {\n  id\n  name\n  fee\n  minFeeAmount\n  description\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  paymentMethods {\n    ...TransactionPaymentMethod\n    __typename\n  }\n  __typename\n}\n\nfragment RegularTransactionProviderAccount on TransactionProviderAccount {\n  id\n  value\n  userId\n  __typename\n}\n\nfragment TransactionProviderPropsFragment on TransactionProviderPropsFragment {\n  requiredUserData {\n    ...TransactionProviderRequiredUserData\n    __typename\n  }\n  tooltip\n  __typename\n}\n\nfragment TransactionProviderRequiredUserData on TransactionProviderRequiredUserData {\n  email\n  phoneNumber\n  eripAccountNumber\n  __typename\n}\n\nfragment ProviderLimits on ProviderLimits {\n  incoming {\n    ...ProviderLimitRange\n    __typename\n  }\n  outgoing {\n    ...ProviderLimitRange\n    __typename\n  }\n  __typename\n}\n\nfragment ProviderLimitRange on ProviderLimitRange {\n  min\n  max\n  __typename\n}\n\nfragment TransactionPaymentMethod on TransactionPaymentMethod {\n  id\n  name\n  fee\n  providerId\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  __typename\n}\n\nfragment RegularTransactionProps on TransactionPropsFragment {\n  creatorId\n  dealId\n  paidFromPendingIncome\n  paymentURL\n  successURL\n  fee\n  paymentAccount {\n    id\n    value\n    __typename\n  }\n  paymentGateway\n  alreadySpent\n  exchangeRate\n  amountAfterConversionRub\n  amountAfterConversionUsdt\n  userData {\n    account\n    email\n    ipAddress\n    phoneNumber\n    __typename\n  }\n  __typename\n}\n\nfragment ChatMessageButton on ChatMessageButton {\n  type\n  url\n  text\n  __typename\n}\n\nfragment RegularFile on File {\n  id\n  url\n  filename\n  mime\n  __typename\n}"
        elif text: query = "mutation createChatMessage($input: CreateChatMessageInput!, $file: Upload) {\n  createChatMessage(input: $input, file: $file) {\n    ...RegularChatMessage\n    __typename\n  }\n}\n\nfragment RegularChatMessage on ChatMessage {\n  id\n  text\n  createdAt\n  deletedAt\n  isRead\n  isSuspicious\n  isBulkMessaging\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  file {\n    ...PartialFile\n    __typename\n  }\n  user {\n    ...ChatMessageUserFields\n    __typename\n  }\n  deal {\n    ...ChatMessageItemDeal\n    __typename\n  }\n  item {\n    ...ItemEdgeNode\n    __typename\n  }\n  transaction {\n    ...RegularTransaction\n    __typename\n  }\n  moderator {\n    ...UserEdgeNode\n    __typename\n  }\n  eventByUser {\n    ...ChatMessageUserFields\n    __typename\n  }\n  eventToUser {\n    ...ChatMessageUserFields\n    __typename\n  }\n  isAutoResponse\n  event\n  buttons {\n    ...ChatMessageButton\n    __typename\n  }\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment ChatMessageUserFields on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment ChatMessageItemDeal on ItemDeal {\n  id\n  direction\n  status\n  statusDescription\n  hasProblem\n  user {\n    ...ChatParticipant\n    __typename\n  }\n  testimonial {\n    ...ChatMessageDealTestimonial\n    __typename\n  }\n  item {\n    id\n    name\n    price\n    slug\n    rawPrice\n    sellerType\n    user {\n      ...ChatParticipant\n      __typename\n    }\n    category {\n      id\n      __typename\n    }\n    attachments {\n      ...PartialFile\n      __typename\n    }\n    comment\n    dataFields {\n      ...GameCategoryDataFieldWithValue\n      __typename\n    }\n    obtainingType {\n      ...GameCategoryObtainingType\n      __typename\n    }\n    __typename\n  }\n  obtainingFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  chat {\n    id\n    type\n    __typename\n  }\n  transaction {\n    id\n    statusExpirationDate\n    __typename\n  }\n  statusExpirationDate\n  commentFromBuyer\n  __typename\n}\n\nfragment ChatParticipant on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment ChatMessageDealTestimonial on Testimonial {\n  id\n  status\n  text\n  rating\n  createdAt\n  updatedAt\n  creator {\n    ...RegularUserFragment\n    __typename\n  }\n  moderator {\n    ...RegularUserFragment\n    __typename\n  }\n  user {\n    ...RegularUserFragment\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment GameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  agreements {\n    ...MinimalGameCategoryAgreement\n    __typename\n  }\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment MinimalGameCategoryAgreement on GameCategoryAgreement {\n  description\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment ItemEdgeNode on ItemProfile {\n  ...MyItemEdgeNode\n  ...ForeignItemEdgeNode\n  __typename\n}\n\nfragment MyItemEdgeNode on MyItemProfile {\n  id\n  slug\n  priority\n  status\n  name\n  price\n  rawPrice\n  statusExpirationDate\n  sellerType\n  attachment {\n    ...PartialFile\n    __typename\n  }\n  user {\n    ...UserItemEdgeNode\n    __typename\n  }\n  approvalDate\n  createdAt\n  priorityPosition\n  viewsCounter\n  feeMultiplier\n  __typename\n}\n\nfragment UserItemEdgeNode on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment ForeignItemEdgeNode on ForeignItemProfile {\n  id\n  slug\n  priority\n  status\n  name\n  price\n  rawPrice\n  sellerType\n  attachment {\n    ...PartialFile\n    __typename\n  }\n  user {\n    ...UserItemEdgeNode\n    __typename\n  }\n  approvalDate\n  priorityPosition\n  createdAt\n  viewsCounter\n  feeMultiplier\n  __typename\n}\n\nfragment RegularTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  provider {\n    ...RegularTransactionProvider\n    __typename\n  }\n  user {\n    ...RegularUserFragment\n    __typename\n  }\n  creator {\n    ...RegularUserFragment\n    __typename\n  }\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  fee\n  createdAt\n  props {\n    ...RegularTransactionProps\n    __typename\n  }\n  verifiedAt\n  verifiedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  completedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  paymentMethodId\n  completedAt\n  isSuspicious\n  __typename\n}\n\nfragment RegularTransactionProvider on TransactionProvider {\n  id\n  name\n  fee\n  minFeeAmount\n  description\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  paymentMethods {\n    ...TransactionPaymentMethod\n    __typename\n  }\n  __typename\n}\n\nfragment RegularTransactionProviderAccount on TransactionProviderAccount {\n  id\n  value\n  userId\n  __typename\n}\n\nfragment TransactionProviderPropsFragment on TransactionProviderPropsFragment {\n  requiredUserData {\n    ...TransactionProviderRequiredUserData\n    __typename\n  }\n  tooltip\n  __typename\n}\n\nfragment TransactionProviderRequiredUserData on TransactionProviderRequiredUserData {\n  email\n  phoneNumber\n  __typename\n}\n\nfragment ProviderLimits on ProviderLimits {\n  incoming {\n    ...ProviderLimitRange\n    __typename\n  }\n  outgoing {\n    ...ProviderLimitRange\n    __typename\n  }\n  __typename\n}\n\nfragment ProviderLimitRange on ProviderLimitRange {\n  min\n  max\n  __typename\n}\n\nfragment TransactionPaymentMethod on TransactionPaymentMethod {\n  id\n  name\n  fee\n  providerId\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  __typename\n}\n\nfragment RegularTransactionProps on TransactionPropsFragment {\n  creatorId\n  dealId\n  paidFromPendingIncome\n  paymentURL\n  successURL\n  fee\n  paymentAccount {\n    id\n    value\n    __typename\n  }\n  paymentGateway\n  alreadySpent\n  exchangeRate\n  amountAfterConversionRub\n  amountAfterConversionUsdt\n  __typename\n}\n\nfragment ChatMessageButton on ChatMessageButton {\n  type\n  url\n  text\n  __typename\n}"
        operations = {
            "operationName": "createChatMessage",
            "query": query,
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
        payload = operations if photo_file_path is None else {"operations": json.dumps(operations), "map": json.dumps(map)}
        r = self.request("post", f"{self.base_url}/graphql", headers, payload, files).json()
        return chat_message(r["data"]["createChatMessage"])

    def create_item(self, game_category_id: str, obtaining_type_id: str, name: str, price: int, 
                    description: str, options: list[GameCategoryOption], data_fields: list[GameCategoryDataField],
                    attachments: list[str]) -> types.Item:
        """
        Creates item (after creation goes to draft, not immediately put up for sale).

        :param game_category_id: Game category ID where item needs to be created.
        :type game_category_id: `str`

        :param obtaining_type_id: Item obtaining type ID.
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
            !!! Must fill fields with type `ITEM_DATA`, i.e., data specified when filling item information.
            Fields with type `OBTAINING_DATA` **should not be filled or passed**, as buyer will specify this data when ordering item.
        :type data_fields: `list[playerokapi.types.GameCategoryDataField]`

        :param attachments: Array of item attachment files. File paths are specified.
        :type attachments: `list[str]`

        :return: Created item object.
        :rtype: `playerokapi.types.Item`
        """
        payload_attributes = {option.field: option.value for option in options}
        payload_data_fields = [{"fieldId": field.id, "value": field.value} for field in data_fields]
        headers = {"accept": "*/*"}
        operations = {
            "operationName": "createItem",
            "query": "mutation createItem($input: CreateItemInput!, $attachments: [Upload!]!) {\n  createItem(input: $input, attachments: $attachments) {\n    ...RegularItem\n    __typename\n  }\n}\n\nfragment RegularItem on Item {\n  ...RegularMyItem\n  ...RegularForeignItem\n  __typename\n}\n\nfragment RegularMyItem on MyItem {\n  ...ItemFields\n  prevPrice\n  priority\n  sequence\n  priorityPrice\n  statusExpirationDate\n  comment\n  viewsCounter\n  statusDescription\n  editable\n  statusPayment {\n    ...StatusPaymentTransaction\n    __typename\n  }\n  moderator {\n    id\n    username\n    __typename\n  }\n  approvalDate\n  deletedAt\n  createdAt\n  updatedAt\n  mayBePublished\n  prevFeeMultiplier\n  sellerNotifiedAboutFeeChange\n  __typename\n}\n\nfragment ItemFields on Item {\n  id\n  slug\n  name\n  description\n  rawPrice\n  price\n  attributes\n  status\n  priorityPosition\n  sellerType\n  feeMultiplier\n  user {\n    ...ItemUser\n    __typename\n  }\n  buyer {\n    ...ItemUser\n    __typename\n  }\n  attachments {\n    ...PartialFile\n    __typename\n  }\n  category {\n    ...RegularGameCategory\n    __typename\n  }\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  comment\n  dataFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  obtainingType {\n    ...GameCategoryObtainingType\n    __typename\n  }\n  __typename\n}\n\nfragment ItemUser on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment RegularGameCategory on GameCategory {\n  id\n  slug\n  name\n  categoryId\n  gameId\n  obtaining\n  options {\n    ...RegularGameCategoryOption\n    __typename\n  }\n  props {\n    ...GameCategoryProps\n    __typename\n  }\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  useCustomObtaining\n  autoConfirmPeriod\n  autoModerationMode\n  agreements {\n    ...RegularGameCategoryAgreement\n    __typename\n  }\n  feeMultiplier\n  __typename\n}\n\nfragment RegularGameCategoryOption on GameCategoryOption {\n  id\n  group\n  label\n  type\n  field\n  value\n  valueRangeLimit {\n    min\n    max\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryProps on GameCategoryPropsObjectType {\n  minTestimonials\n  minTestimonialsForSeller\n  __typename\n}\n\nfragment RegularGameCategoryAgreement on GameCategoryAgreement {\n  description\n  gameCategoryId\n  gameCategoryObtainingTypeId\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment GameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  agreements {\n    ...MinimalGameCategoryAgreement\n    __typename\n  }\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment MinimalGameCategoryAgreement on GameCategoryAgreement {\n  description\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment StatusPaymentTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  props {\n    paymentURL\n    __typename\n  }\n  __typename\n}\n\nfragment RegularForeignItem on ForeignItem {\n  ...ItemFields\n  __typename\n}",
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
        i=0
        for att in attachments:
            i+=1
            map[str(i)] = [f"variables.attachments.{i-1}"]
            files[str(i)] = open(att, "rb")
        payload = {
            "operations": json.dumps(operations),
            "map": json.dumps(map)
        }

        r = self.request("post", f"{self.base_url}/graphql", headers, payload, files).json()
        return item(r["data"]["createItem"])
    
    def update_item(self, id: str, name: str | None = None, price: int | None = None, description: str | None = None, 
                    options: list[GameCategoryOption] | None = None, data_fields: list[GameCategoryDataField] | None = None, 
                    remove_attachments: list[str] | None = None, add_attachments: list[str] | None = None) -> types.Item:
        """
        Updates account item.

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
            !!! Must fill fields with type `ITEM_DATA`, i.e., data specified when filling item information.
            Fields with type `OBTAINING_DATA` **should not be filled or passed**, as buyer will specify this data when ordering item.
        :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

        :param remove_attachments: Array of item attachment file IDs to remove.
        :type remove_attachments: `list[str]` or `None`

        :param add_attachments: Array of item attachment files to add. File paths are specified.
        :type add_attachments: `list[str]` or `None`

        :return: Updated item object.
        :rtype: `playerokapi.types.Item`
        """
        payload_attributes = {option.field: option.value for option in options} if options is not None else None
        payload_data_fields = [{"fieldId": field.id, "value": field.value} for field in data_fields] if data_fields is not None else None
        headers = {"accept": "*/*"}
        operations = {
            "operationName": "updateItem",
            "query": "mutation updateItem($input: UpdateItemInput!, $addedAttachments: [Upload!]) {\n  updateItem(input: $input, addedAttachments: $addedAttachments) {\n    ...RegularItem\n    __typename\n  }\n}\n\nfragment RegularItem on Item {\n  ...RegularMyItem\n  ...RegularForeignItem\n  __typename\n}\n\nfragment RegularMyItem on MyItem {\n  ...ItemFields\n  prevPrice\n  priority\n  sequence\n  priorityPrice\n  statusExpirationDate\n  comment\n  viewsCounter\n  statusDescription\n  editable\n  statusPayment {\n    ...StatusPaymentTransaction\n    __typename\n  }\n  moderator {\n    id\n    username\n    __typename\n  }\n  approvalDate\n  deletedAt\n  createdAt\n  updatedAt\n  mayBePublished\n  prevFeeMultiplier\n  sellerNotifiedAboutFeeChange\n  __typename\n}\n\nfragment ItemFields on Item {\n  id\n  slug\n  name\n  description\n  rawPrice\n  price\n  attributes\n  status\n  priorityPosition\n  sellerType\n  feeMultiplier\n  user {\n    ...ItemUser\n    __typename\n  }\n  buyer {\n    ...ItemUser\n    __typename\n  }\n  attachments {\n    ...PartialFile\n    __typename\n  }\n  category {\n    ...RegularGameCategory\n    __typename\n  }\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  comment\n  dataFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  obtainingType {\n    ...GameCategoryObtainingType\n    __typename\n  }\n  __typename\n}\n\nfragment ItemUser on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment RegularGameCategory on GameCategory {\n  id\n  slug\n  name\n  categoryId\n  gameId\n  obtaining\n  options {\n    ...RegularGameCategoryOption\n    __typename\n  }\n  props {\n    ...GameCategoryProps\n    __typename\n  }\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  useCustomObtaining\n  autoConfirmPeriod\n  autoModerationMode\n  agreements {\n    ...RegularGameCategoryAgreement\n    __typename\n  }\n  feeMultiplier\n  __typename\n}\n\nfragment RegularGameCategoryOption on GameCategoryOption {\n  id\n  group\n  label\n  type\n  field\n  value\n  valueRangeLimit {\n    min\n    max\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryProps on GameCategoryPropsObjectType {\n  minTestimonials\n  minTestimonialsForSeller\n  __typename\n}\n\nfragment RegularGameCategoryAgreement on GameCategoryAgreement {\n  description\n  gameCategoryId\n  gameCategoryObtainingTypeId\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment GameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  agreements {\n    ...MinimalGameCategoryAgreement\n    __typename\n  }\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment MinimalGameCategoryAgreement on GameCategoryAgreement {\n  description\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment StatusPaymentTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  props {\n    paymentURL\n    __typename\n  }\n  __typename\n}\n\nfragment RegularForeignItem on ForeignItem {\n  ...ItemFields\n  __typename\n}",
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
            i=0
            for att in add_attachments:
                i+=1
                map[str(i)] = [f"variables.addedAttachments.{i-1}"]
                files[str(i)] = open(att, "rb")
        payload = {
            "operations": json.dumps(operations),
            "map": json.dumps(map)
        }
        r = self.request("post", f"{self.base_url}/graphql", headers, payload if files else operations, files if files else None).json()
        return item(r["data"]["updateItem"])

    def remove_item(self, id: str) -> bool:
        """
        Completely removes your account item.

        :param id: Item ID.
        :type id: `str`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "removeItem",
            "query": "mutation removeItem($id: UUID!) {\n  removeItem(id: $id) {\n    ...RegularItem\n    __typename\n  }\n}\n\nfragment RegularItem on Item {\n  ...RegularMyItem\n  ...RegularForeignItem\n  __typename\n}\n\nfragment RegularMyItem on MyItem {\n  ...ItemFields\n  prevPrice\n  priority\n  sequence\n  priorityPrice\n  statusExpirationDate\n  comment\n  viewsCounter\n  statusDescription\n  editable\n  statusPayment {\n    ...StatusPaymentTransaction\n    __typename\n  }\n  moderator {\n    id\n    username\n    __typename\n  }\n  approvalDate\n  deletedAt\n  createdAt\n  updatedAt\n  mayBePublished\n  prevFeeMultiplier\n  sellerNotifiedAboutFeeChange\n  __typename\n}\n\nfragment ItemFields on Item {\n  id\n  slug\n  name\n  description\n  rawPrice\n  price\n  attributes\n  status\n  priorityPosition\n  sellerType\n  feeMultiplier\n  user {\n    ...ItemUser\n    __typename\n  }\n  buyer {\n    ...ItemUser\n    __typename\n  }\n  attachments {\n    ...PartialFile\n    __typename\n  }\n  category {\n    ...RegularGameCategory\n    __typename\n  }\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  comment\n  dataFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  obtainingType {\n    ...GameCategoryObtainingType\n    __typename\n  }\n  __typename\n}\n\nfragment ItemUser on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment RegularGameCategory on GameCategory {\n  id\n  slug\n  name\n  categoryId\n  gameId\n  obtaining\n  options {\n    ...RegularGameCategoryOption\n    __typename\n  }\n  props {\n    ...GameCategoryProps\n    __typename\n  }\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  useCustomObtaining\n  autoConfirmPeriod\n  autoModerationMode\n  agreements {\n    ...RegularGameCategoryAgreement\n    __typename\n  }\n  feeMultiplier\n  __typename\n}\n\nfragment RegularGameCategoryOption on GameCategoryOption {\n  id\n  group\n  label\n  type\n  field\n  value\n  valueRangeLimit {\n    min\n    max\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryProps on GameCategoryPropsObjectType {\n  minTestimonials\n  minTestimonialsForSeller\n  __typename\n}\n\nfragment RegularGameCategoryAgreement on GameCategoryAgreement {\n  description\n  gameCategoryId\n  gameCategoryObtainingTypeId\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment GameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  agreements {\n    ...MinimalGameCategoryAgreement\n    __typename\n  }\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment MinimalGameCategoryAgreement on GameCategoryAgreement {\n  description\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment StatusPaymentTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  props {\n    paymentURL\n    __typename\n  }\n  __typename\n}\n\nfragment RegularForeignItem on ForeignItem {\n  ...ItemFields\n  __typename\n}",
            "variables": {
                "id": id,
            }
        }
        self.request("post", f"{self.base_url}/graphql", headers, payload)
        return True
    
    def publish_item(self, item_id: str, priority_status_id: str, 
                     transaction_provider_id: TransactionProviderIds = TransactionProviderIds.LOCAL) -> types.Item:
        """
        Publishes item for sale.

        :param item_id: Item ID.
        :type item_id: `str`

        :param priority_status_id: Item priority status ID under which to publish it for sale.
        :type priority_status_id: `str`

        :param transaction_provider_id: Transaction provider ID.
        :type transaction_provider_id: `playerokapi.enums.TransactionProviderIds`

        :return: Published item object.
        :rtype: `playerokapi.types.Item`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "publishItem",
            "query": "mutation publishItem($input: PublishItemInput!) {\n  publishItem(input: $input) {\n    ...RegularItem\n    __typename\n  }\n}\n\nfragment RegularItem on Item {\n  ...RegularMyItem\n  ...RegularForeignItem\n  __typename\n}\n\nfragment RegularMyItem on MyItem {\n  ...ItemFields\n  prevPrice\n  priority\n  sequence\n  priorityPrice\n  statusExpirationDate\n  comment\n  viewsCounter\n  statusDescription\n  editable\n  statusPayment {\n    ...StatusPaymentTransaction\n    __typename\n  }\n  moderator {\n    id\n    username\n    __typename\n  }\n  approvalDate\n  deletedAt\n  createdAt\n  updatedAt\n  mayBePublished\n  prevFeeMultiplier\n  sellerNotifiedAboutFeeChange\n  __typename\n}\n\nfragment ItemFields on Item {\n  id\n  slug\n  name\n  description\n  rawPrice\n  price\n  attributes\n  status\n  priorityPosition\n  sellerType\n  feeMultiplier\n  user {\n    ...ItemUser\n    __typename\n  }\n  buyer {\n    ...ItemUser\n    __typename\n  }\n  attachments {\n    ...PartialFile\n    __typename\n  }\n  category {\n    ...RegularGameCategory\n    __typename\n  }\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  comment\n  dataFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  obtainingType {\n    ...GameCategoryObtainingType\n    __typename\n  }\n  __typename\n}\n\nfragment ItemUser on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment RegularGameCategory on GameCategory {\n  id\n  slug\n  name\n  categoryId\n  gameId\n  obtaining\n  options {\n    ...RegularGameCategoryOption\n    __typename\n  }\n  props {\n    ...GameCategoryProps\n    __typename\n  }\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  useCustomObtaining\n  autoConfirmPeriod\n  autoModerationMode\n  agreements {\n    ...RegularGameCategoryAgreement\n    __typename\n  }\n  feeMultiplier\n  __typename\n}\n\nfragment RegularGameCategoryOption on GameCategoryOption {\n  id\n  group\n  label\n  type\n  field\n  value\n  valueRangeLimit {\n    min\n    max\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryProps on GameCategoryPropsObjectType {\n  minTestimonials\n  minTestimonialsForSeller\n  __typename\n}\n\nfragment RegularGameCategoryAgreement on GameCategoryAgreement {\n  description\n  gameCategoryId\n  gameCategoryObtainingTypeId\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment GameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  agreements {\n    ...MinimalGameCategoryAgreement\n    __typename\n  }\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment MinimalGameCategoryAgreement on GameCategoryAgreement {\n  description\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment StatusPaymentTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  props {\n    paymentURL\n    __typename\n  }\n  __typename\n}\n\nfragment RegularForeignItem on ForeignItem {\n  ...ItemFields\n  __typename\n}",
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

    def get_items(self, game_id: str | None = None, category_id: str | None = None, count: int = 24,
                  status: ItemStatuses = ItemStatuses.APPROVED, after_cursor: str | None = None) -> types.ItemProfileList:
        """
        Gets game/application items.\n
        Can be obtained by either of two parameters: `game_id`, `category_id`.

        :param game_id: Game/application ID, _optional_.
        :type game_id: `str` or `None`

        :param category_id: Game/application category ID, _optional_.
        :type category_id: `str` or `None`

        :param count: Number of items to get (no more than 24 per request).
        :type count: `int`

        :param status: Type of items to get: active or sold. Default is active.
        :type status: `playerokapi.enums.ItemStatuses`

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of item profiles.
        :rtype: `playerokapi.types.ItemProfileList`
        """
        headers = {"accept": "*/*"}
        filter = {"gameId": game_id, "status": [status.name] if status else None} if not category_id else {"gameCategoryId": category_id, "status": [status.name] if status else None}
        payload = {
            "operationName": "items",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "filter": filter}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("items")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return item_profile_list(r["data"]["items"])

    def get_item(self, id: str | None = None, slug: str | None = None) -> types.MyItem | types.Item | types.ItemProfile:
        """
        Gets item (product).\n
        Can be obtained by either of two parameters:

        :param id: Item ID, _optional_.
        :type id: `str` or `None`

        :param slug: Item page name, _optional_.
        :type slug: `str` or `None`
        
        :return: Item object.
        :rtype: `playerokapi.types.MyItem` or `playerokapi.types.Item` or `playerokapi.types.ItemProfile`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "item",
            "variables": json.dumps({"id": id, "slug": slug, "hasSupportAccess": False, "showForbiddenImage": True}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("item")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        data: dict = r["data"]["item"]
        if data["__typename"] == "MyItem": _item = my_item(data)
        elif data["__typename"] == "ItemProfile": _item = item_profile(data)
        elif data["__typename"] in ["Item", "ForeignItem"]: _item = item(data)
        else: _item = None
        return _item

    def get_item_priority_statuses(self, item_id: str, item_price: str) -> list[types.ItemPriorityStatus]:
        """
        Gets priority statuses for item.

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
            "variables": json.dumps({"itemId": item_id, "price": int(item_price)}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("item_priority_statuses")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return [item_priority_status(status) for status in r["data"]["itemPriorityStatuses"]]

    def increase_item_priority_status(self, item_id: str, priority_status_id: str, payment_method_id: TransactionPaymentMethodIds | None = None, 
                                      transaction_provider_id: TransactionProviderIds = TransactionProviderIds.LOCAL) -> types.Item:
        """
        Increases item priority status.

        :param item_id: Item ID.
        :type item_id: `str`

        :param priority_status_id: Priority status ID to change to.
        :type priority_status_id: `int` or `str`

        :param payment_method_id: Payment method, _optional_.
        :type payment_method_id: `playerokapi.enums.TransactionPaymentMethodIds` or `None`

        :param transaction_provider_id: Transaction provider ID (LOCAL - from site wallet balance).
        :type transaction_provider_id: `playerokapi.enums.TransactionProviderIds`
        
        :return: Updated item object.
        :rtype: `playerokapi.types.Item`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "increaseItemPriorityStatus",
            "query": "mutation increaseItemPriorityStatus($input: PublishItemInput!) {\n  increaseItemPriorityStatus(input: $input) {\n    ...RegularItem\n    __typename\n  }\n}\n\nfragment RegularItem on Item {\n  ...RegularMyItem\n  ...RegularForeignItem\n  __typename\n}\n\nfragment RegularMyItem on MyItem {\n  ...ItemFields\n  prevPrice\n  priority\n  sequence\n  priorityPrice\n  statusExpirationDate\n  comment\n  viewsCounter\n  statusDescription\n  editable\n  statusPayment {\n    ...StatusPaymentTransaction\n    __typename\n  }\n  moderator {\n    id\n    username\n    __typename\n  }\n  approvalDate\n  deletedAt\n  createdAt\n  updatedAt\n  mayBePublished\n  prevFeeMultiplier\n  sellerNotifiedAboutFeeChange\n  __typename\n}\n\nfragment ItemFields on Item {\n  id\n  slug\n  name\n  description\n  rawPrice\n  price\n  attributes\n  status\n  priorityPosition\n  sellerType\n  feeMultiplier\n  user {\n    ...ItemUser\n    __typename\n  }\n  buyer {\n    ...ItemUser\n    __typename\n  }\n  attachments {\n    ...PartialFile\n    __typename\n  }\n  category {\n    ...RegularGameCategory\n    __typename\n  }\n  game {\n    ...RegularGameProfile\n    __typename\n  }\n  comment\n  dataFields {\n    ...GameCategoryDataFieldWithValue\n    __typename\n  }\n  obtainingType {\n    ...GameCategoryObtainingType\n    __typename\n  }\n  __typename\n}\n\nfragment ItemUser on UserFragment {\n  ...UserEdgeNode\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment PartialFile on File {\n  id\n  url\n  __typename\n}\n\nfragment RegularGameCategory on GameCategory {\n  id\n  slug\n  name\n  categoryId\n  gameId\n  obtaining\n  options {\n    ...RegularGameCategoryOption\n    __typename\n  }\n  props {\n    ...GameCategoryProps\n    __typename\n  }\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  useCustomObtaining\n  autoConfirmPeriod\n  autoModerationMode\n  agreements {\n    ...RegularGameCategoryAgreement\n    __typename\n  }\n  feeMultiplier\n  __typename\n}\n\nfragment RegularGameCategoryOption on GameCategoryOption {\n  id\n  group\n  label\n  type\n  field\n  value\n  valueRangeLimit {\n    min\n    max\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryProps on GameCategoryPropsObjectType {\n  minTestimonials\n  minTestimonialsForSeller\n  __typename\n}\n\nfragment RegularGameCategoryAgreement on GameCategoryAgreement {\n  description\n  gameCategoryId\n  gameCategoryObtainingTypeId\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment RegularGameProfile on GameProfile {\n  id\n  name\n  type\n  slug\n  logo {\n    ...PartialFile\n    __typename\n  }\n  __typename\n}\n\nfragment GameCategoryDataFieldWithValue on GameCategoryDataFieldWithValue {\n  id\n  label\n  type\n  inputType\n  copyable\n  hidden\n  required\n  value\n  __typename\n}\n\nfragment GameCategoryObtainingType on GameCategoryObtainingType {\n  id\n  name\n  description\n  gameCategoryId\n  noCommentFromBuyer\n  instructionForBuyer\n  instructionForSeller\n  sequence\n  feeMultiplier\n  agreements {\n    ...MinimalGameCategoryAgreement\n    __typename\n  }\n  props {\n    minTestimonialsForSeller\n    __typename\n  }\n  __typename\n}\n\nfragment MinimalGameCategoryAgreement on GameCategoryAgreement {\n  description\n  iconType\n  id\n  sequence\n  __typename\n}\n\nfragment StatusPaymentTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  props {\n    paymentURL\n    __typename\n  }\n  __typename\n}\n\nfragment RegularForeignItem on ForeignItem {\n  ...ItemFields\n  __typename\n}",
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

    def get_transaction_providers(self, direction: TransactionProviderDirections = TransactionProviderDirections.IN) -> list[types.TransactionProvider]:
        """
        Gets all transaction providers.

        :param direction: Transaction direction (deposit/withdrawal).
        :type direction: `playerokapi.enums.TransactionProviderDirections`
        
        :return: List of transaction providers.
        :rtype: `list` of `playerokapi.types.TransactionProvider`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "transactionProviders",
            "variables": json.dumps({"filter": {"direction": direction.name if direction else None}}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("transaction_providers")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return [transaction_provider(provider) for provider in r["data"]["transactionProviders"]]

    def get_transactions(self, count: int = 24, operation: TransactionOperations | None = None, min_value: int | None = None,
                         max_value: int | None = None, provider_id: TransactionProviderIds | None = None, status: TransactionStatuses | None = None,
                         after_cursor: str | None = None) -> TransactionList:
        """
        Gets all account transactions.

        :param count: Number of transactions to get (no more than 24 per request).
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

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of transactions.
        :rtype: `playerokapi.types.TransactionList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "transactions",
            "variables": {"pagination": {"first": count, "after": after_cursor}, "filter": {"userId": self.id}, "hasSupportAccess": False},
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("transactions")}}, ensure_ascii=False)
        }
        if operation: payload["variables"]["filter"]["operation"] = [operation.name]
        if min_value or max_value:
            payload["variables"]["filter"]["value"] = {}
            if min_value: payload["variables"]["filter"]["value"]["min"] = str(min_value)
            if max_value: payload["variables"]["filter"]["value"]["max"] = str(max_value)
        if provider_id: payload["variables"]["filter"]["providerId"] = [provider_id.name]
        if status: payload["variables"]["filter"]["status"] = [status.name]
        payload["variables"] = json.dumps(payload["variables"], ensure_ascii=False),
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return transaction_list(r["data"]["transactions"])
    
    def get_sbp_bank_members(self) -> list[SBPBankMember]:
        """
        Gets all SBP bank members.

        :return: List of SBP bank members.
        :rtype: `list` of `playerokapi.types.SBPBankMember`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "SbpBankMembers",
            "variables": json.dumps({}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("sbp_bank_members")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return [sbp_bank_member(member) for member in r["data"]["sbpBankMembers"]]
    
    def get_verified_cards(self, count: int = 24, after_cursor: str | None = None,
                           direction: SortDirections = SortDirections.ASC) -> types.UserBankCardList:
        """
        Gets verified account cards.

        :param count: Number of bank cards to get (no more than 24 per request).
        :type count: `int`

        :param after_cursor: Cursor to start parsing from (if not provided - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`

        :param direction: Bank card sort type.
        :type direction: `playerokapi.enums.SortDirections`
        
        :return: Page of user bank cards.
        :rtype: `playerokapi.types.UserBankCardList`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "verifiedCards",
            "variables": json.dumps({"pagination": {"first": count, "after": after_cursor}, "sort": {"direction": direction.name}, "field": "createdAt"}, ensure_ascii=False),
            "extensions": json.dumps({"persistedQuery": {"version": 1, "sha256Hash": PERSISTED_QUERIES.get("verified_cards")}}, ensure_ascii=False)
        }
        r = self.request("get", f"{self.base_url}/graphql", headers, payload).json()
        return user_bank_card_list(r["data"]["verifiedCards"])
    
    def delete_card(self, card_id: str) -> bool:
        """
        Deletes card from saved in account.

        :param card_id: Bank card ID.
        :type card_id: `str`
        
        :return: True if card was deleted, otherwise False
        :rtype: `bool`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "deleteCard",
            "query": "mutation deleteCard($input: DeleteCardInput!) {\n  deleteCard(input: $input)\n}",
            "variables": {
                "input": {
                    "cardId": card_id
                }
            }
        }
        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return r["data"]["deleteCard"]
    
    def request_withdrawal(self, provider: TransactionProviderIds, account: str, value: int,
                           payment_method_id: TransactionPaymentMethodIds | None = None,
                           sbp_bank_member_id: str | None = None) -> types.Transaction:
        """
        Sends withdrawal request from account balance.

        :param provider: Transaction provider.
        :type provider: `playerokapi.enums.TransactionProviderIds`

        :param account: Added card ID or phone number if provider is SBP, to perform withdrawal to.
        :type account: `str`

        :param value: Withdrawal amount.
        :type value: `int`

        :param payment_method_id: Payment method ID, _optional_.
        :type payment_method_id: `playerokapi.enums.TransactionPaymentMethodIds` or `None`

        :param sbp_bank_member_id: SBP bank member ID (only if SBP provider is specified), _optional_.
        :type sbp_bank_member_id: `str` or `None`
        
        :return: Withdrawal transaction object.
        :rtype: `playerokapi.types.Transaction`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "requestWithdrawal",
            "query": "mutation requestWithdrawal($input: CreateWithdrawalTransactionInput!) {\n  requestWithdrawal(input: $input) {\n    ...RegularTransaction\n    __typename\n  }\n}\n\nfragment RegularTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  provider {\n    ...RegularTransactionProvider\n    __typename\n  }\n  user {\n    ...RegularUserFragment\n    __typename\n  }\n  creator {\n    ...RegularUserFragment\n    __typename\n  }\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  fee\n  createdAt\n  props {\n    ...RegularTransactionProps\n    __typename\n  }\n  verifiedAt\n  verifiedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  completedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  paymentMethodId\n  completedAt\n  isSuspicious\n  spbBankName\n  __typename\n}\n\nfragment RegularTransactionProvider on TransactionProvider {\n  id\n  name\n  fee\n  minFeeAmount\n  description\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  paymentMethods {\n    ...TransactionPaymentMethod\n    __typename\n  }\n  __typename\n}\n\nfragment RegularTransactionProviderAccount on TransactionProviderAccount {\n  id\n  value\n  userId\n  providerId\n  paymentMethodId\n  __typename\n}\n\nfragment TransactionProviderPropsFragment on TransactionProviderPropsFragment {\n  requiredUserData {\n    ...TransactionProviderRequiredUserData\n    __typename\n  }\n  tooltip\n  __typename\n}\n\nfragment TransactionProviderRequiredUserData on TransactionProviderRequiredUserData {\n  email\n  phoneNumber\n  eripAccountNumber\n  __typename\n}\n\nfragment ProviderLimits on ProviderLimits {\n  incoming {\n    ...ProviderLimitRange\n    __typename\n  }\n  outgoing {\n    ...ProviderLimitRange\n    __typename\n  }\n  __typename\n}\n\nfragment ProviderLimitRange on ProviderLimitRange {\n  min\n  max\n  __typename\n}\n\nfragment TransactionPaymentMethod on TransactionPaymentMethod {\n  id\n  name\n  fee\n  providerId\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment RegularTransactionProps on TransactionPropsFragment {\n  creatorId\n  dealId\n  paidFromPendingIncome\n  paymentURL\n  successURL\n  fee\n  paymentAccount {\n    id\n    value\n    __typename\n  }\n  paymentGateway\n  alreadySpent\n  exchangeRate\n  amountAfterConversionRub\n  amountAfterConversionUsdt\n  userData {\n    account\n    email\n    ipAddress\n    phoneNumber\n    __typename\n  }\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}",
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
    
    def remove_transaction(self, transaction_id: str) -> types.Transaction:
        """
        Removes transaction (e.g., can cancel withdrawal).

        :param transaction_id: Transaction ID.
        :type transaction_id: `str`
        
        :return: Cancelled transaction object.
        :rtype: `playerokapi.types.Transaction`
        """
        headers = {"accept": "*/*"}
        payload = {
            "operationName": "removeTransaction",
            "query": "mutation removeTransaction($id: UUID!) {\n  removeTransaction(id: $id) {\n    ...RegularTransaction\n    __typename\n  }\n}\n\nfragment RegularTransaction on Transaction {\n  id\n  operation\n  direction\n  providerId\n  provider {\n    ...RegularTransactionProvider\n    __typename\n  }\n  user {\n    ...RegularUserFragment\n    __typename\n  }\n  creator {\n    ...RegularUserFragment\n    __typename\n  }\n  status\n  statusDescription\n  statusExpirationDate\n  value\n  fee\n  createdAt\n  props {\n    ...RegularTransactionProps\n    __typename\n  }\n  verifiedAt\n  verifiedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  completedBy {\n    ...UserEdgeNode\n    __typename\n  }\n  paymentMethodId\n  completedAt\n  isSuspicious\n  spbBankName\n  __typename\n}\n\nfragment RegularTransactionProvider on TransactionProvider {\n  id\n  name\n  fee\n  minFeeAmount\n  description\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  paymentMethods {\n    ...TransactionPaymentMethod\n    __typename\n  }\n  __typename\n}\n\nfragment RegularTransactionProviderAccount on TransactionProviderAccount {\n  id\n  value\n  userId\n  providerId\n  paymentMethodId\n  __typename\n}\n\nfragment TransactionProviderPropsFragment on TransactionProviderPropsFragment {\n  requiredUserData {\n    ...TransactionProviderRequiredUserData\n    __typename\n  }\n  tooltip\n  __typename\n}\n\nfragment TransactionProviderRequiredUserData on TransactionProviderRequiredUserData {\n  email\n  phoneNumber\n  eripAccountNumber\n  __typename\n}\n\nfragment ProviderLimits on ProviderLimits {\n  incoming {\n    ...ProviderLimitRange\n    __typename\n  }\n  outgoing {\n    ...ProviderLimitRange\n    __typename\n  }\n  __typename\n}\n\nfragment ProviderLimitRange on ProviderLimitRange {\n  min\n  max\n  __typename\n}\n\nfragment TransactionPaymentMethod on TransactionPaymentMethod {\n  id\n  name\n  fee\n  providerId\n  account {\n    ...RegularTransactionProviderAccount\n    __typename\n  }\n  props {\n    ...TransactionProviderPropsFragment\n    __typename\n  }\n  limits {\n    ...ProviderLimits\n    __typename\n  }\n  __typename\n}\n\nfragment RegularUserFragment on UserFragment {\n  id\n  username\n  role\n  avatarURL\n  isOnline\n  isBlocked\n  rating\n  testimonialCounter\n  createdAt\n  supportChatId\n  systemChatId\n  __typename\n}\n\nfragment RegularTransactionProps on TransactionPropsFragment {\n  creatorId\n  dealId\n  paidFromPendingIncome\n  paymentURL\n  successURL\n  fee\n  paymentAccount {\n    id\n    value\n    __typename\n  }\n  paymentGateway\n  alreadySpent\n  exchangeRate\n  amountAfterConversionRub\n  amountAfterConversionUsdt\n  userData {\n    account\n    email\n    ipAddress\n    phoneNumber\n    __typename\n  }\n  __typename\n}\n\nfragment UserEdgeNode on UserFragment {\n  ...RegularUserFragment\n  __typename\n}",
            "variables": {
                "id": transaction_id
            }
        }
        r = self.request("post", f"{self.base_url}/graphql", headers, payload).json()
        return transaction(r["data"]["removeTransaction"])