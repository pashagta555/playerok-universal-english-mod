from __future__ import annotations 
from typing import *
from logging import getLogger 
from typing import Literal 
import json 
import time 
import os 
import tempfile 
import shutil 
import uuid 

import tls_requests 
import curl_cffi 

from .import types 
from .exceptions import *
from .parser import *
from .enums import *
from .misc import (
PERSISTED_QUERIES ,
QUERIES 
)


logger =getLogger ("playerokapi")


def get_account ()->Account |None :
    if hasattr (Account ,"instance"):
        return getattr (Account ,"instance")


class Account :
    "Class describing data and methods of Playerok account.

:param token: Account token.
:type token: str

:param user_agent: User-agent browser.
:type user_agent: str

:param proxy: IPV4 proxy in the format: `user:pass@ip:port` or `ip:port`, optionally.
:type proxy: str or None

:param requests_timeout: Timeout waiting for responses to queries.
:type requests_timeout: int

:param request_max_retries: Maximum number of repeated attempts to send a request if CloudFlare protection is detected.
:type request_max_retries: int"
    def __new__ (cls ,*args ,**kwargs )->Account :
        if not hasattr (cls ,"instance"):
            cls .instance =super (Account ,cls ).__new__ (cls )
        return getattr (cls ,"instance")

    def __init__ (
    self ,
    token :str ,
    user_agent :str ="",
    proxy :str =None ,
    requests_timeout :int =15 ,
    request_max_retries :int =5 ,
    **kwargs 
    ):
        self .token =token 
        "Account session token."
        self .user_agent =user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        "Browser user agent."
        self .requests_timeout =requests_timeout 
        "Timeout waiting for answers to requests."
        self .proxy =proxy 
        "Proxy."
        self .__proxy_string =f"http://{self .proxy .replace ('https://','').replace ('http://','')}"if self .proxy else None 
        "Proxy line."
        self .request_max_retries =request_max_retries 
        "Maximum number of repeated attempts to send the request."

        self .base_url ="https://playerok.com"
        "Basic URL for all requests."

        self .id :str |None =None 
        "Account ID.\n\n_Filled in when using get() for the first time._"
        self .username :str |None =None 
        "Account nickname.
            
 Заполняется при первом использовании get()."
        self .email :str |None =None 
        "Email account. _

 Заполняется при первом использовании get()._"
        self .role :str |None =None 
        "Account role.
 
_Filled in when first using get()._"
        self .support_chat_id :str |None =None 
        "Chat support ID. 

Filled in when using get() for the first time."
        self .system_chat_id :str |None =None 
        "System chat ID."
        self .unread_chats_counter :int |None =None 
        "The number of unread chats."
        self .is_blocked :bool |None =None 
        "Is the account blocked.\n\n_Filling in when first using get()._"
        self .is_blocked_for :str |None =None 
        "Reason for account blocking. 

 Заполняется при первом использовании get()"
        self .created_at :str |None =None 
        "Date of account creation.\n\n_Filled in upon first use of get()._"
        self .last_item_created_at :str |None =None 
        "Creation date of the last subject.

_This field is filled in when the get() method is used for the first time._"
        self .has_frozen_balance :bool |None =None 
        "Frozen is the account balance."
        self .has_confirmed_phone_number :bool |None =None 
        "Is the phone number confirmed.\"
        self .can_publish_items :bool |None =None 
        "Can sell items."
        self .profile :AccountProfile |None =None 
        "Profile account (not to be confused with user profile). 

 Заполняется при первом использовании get()"

        self ._cert_path =os .path .join (os .path .dirname (__file__ ),"cacert.pem")
        self ._tmp_cert_path =os .path .join (tempfile .gettempdir (),"cacert.pem")
        shutil .copyfile (self ._cert_path ,self ._tmp_cert_path )

        self ._refresh_clients ()

    def _refresh_clients (self ):
        self .__tls_requests =tls_requests .Client (
        proxy =self .__proxy_string 
        )
        self .__curl_session =curl_cffi .Session (
        impersonate ="chrome",
        timeout =10 ,
        proxy =self .__proxy_string ,
        verify =self ._tmp_cert_path 
        )

        # under testing...
    """def refresh_ddg(self):
        
        #import easyocr
        print(1)
        import CaptchaCracker as cc

        from selenium import webdriver
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By

        print(2)
        driver = webdriver.Chrome()
        driver.get("https://playerok.com")
        wait = WebDriverWait(driver, 30)

        print(3)
        iframe = wait.until(
            EC.presence_of_element_located((By.ID, "ddg-iframe"))
        )
        print(4)
        input()
        
        driver.switch_to.frame(iframe)

        st_nums = [
            int(name.replace("captcha", "").replace(".png", "")) 
             for name in os.listdir("playerokapi/captchas") 
             if name.startswith("captcha")
        ]
        st_num = max(st_nums) + 1 if st_nums else 1
        print("st_num:", st_num) #ddg-captcha__checkbox
        
        for i in range(st_num, 1000):
            print(i)
            captcha = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ddg-modal__captcha-image"))
            )

            print("captcha:", captcha)
            captcha.screenshot(f"playerokapi/captchas/captcha{i}.png")

            btn = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ddg-modal__refresh"))
            )
            btn.click()
            time.sleep(3)
        
        #result = reader.readtext("captcha.png")
        #input(result)
        cookies = driver.get_cookies()

        ddg_cookies = {}
        for c in cookies:
            if c["name"].startswith("__ddg"):
                ddg_cookies[c["name"]] = c["value"]

        input(ddg_cookies)

        driver.quit()"""

    def request (
    self ,
    method :Literal ["get","post"],
    url :str ,
    headers :dict [str ,str ],
    payload :dict [str ,str ]|None =None ,
    files :dict |None =None ,
    pass_304 :bool =True 
    )->requests .Response :
        "Sends a request to the playerok.com server.

:param method: Request method: post, get.
:type method: str

:param url: Request URL.
:type url: str

:param headers: Request headers.
:type headers: dict[str, str]

:param payload: Request payload.
:type payload: dict[str, str] or None

:param files: Files to be sent in the request.
:type files: dict or None

:return: Response of the request.
:rtype: requests.Response"
        try :x_gql_op =payload .get ("operationName","viewer")
        except :x_gql_op ="viewer"
        _headers ={
        "accept":"*/*",
        "accept-language":"ru,en;q=0.9",
        "access-control-allow-headers":"sentry-trace, baggage",
        "apollo-require-preflight":"true",
        "apollographql-client-name":"web",
        "content-type":"application/json",
        "cookie":f"token={self .token }",
        "origin":"https://playerok.com",
        "priority":"u=1, i",
        "referer":"https://playerok.com/",
        "sec-ch-ua":'"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        "sec-ch-ua-arch":'"x86"',
        "sec-ch-ua-bitness":'"64"',
        "sec-ch-ua-full-version":'"146.0.7680.180"',
        "sec-ch-ua-full-version-list":'"Chromium";v="146.0.7680.180", "Not-A.Brand";v="24.0.0.0", "Google Chrome";v="146.0.7680.180"',
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-model":'""',
        "sec-ch-ua-platform":'"Windows"',
        "sec-ch-ua-platform-version":"\"19.0.0\"",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":self .user_agent ,
        "x-gql-op":x_gql_op ,
        "x-gql-path":"/",
        "x-timezone-offset":"-240",
        "x-apollo-operation-name":x_gql_op 
        }
        headers ={k :v for k ,v in _headers .items ()if k not in headers .keys ()}

        def make_req ():
            err =""

            for _ in range (3 ):
                try :
                    if method =="get":
                        r =self .__curl_session .get (
                        url =url ,
                        params =payload ,
                        headers =headers ,
                        timeout =self .requests_timeout 
                        )
                    elif method =="post":
                        if files :
                            r =self .__tls_requests .post (
                            url =url ,
                            json =payload if not files else None ,
                            data =payload if files else None ,
                            headers =headers ,
                            files =files ,
                            timeout =self .requests_timeout 
                            )
                        else :
                            r =self .__curl_session .post (
                            url =url ,
                            json =payload ,
                            headers =headers ,
                            timeout =self .requests_timeout 
                            )
                    return r 
                except Exception as e :
                    err =str (e )
                    logger .debug (f"Ошибка при отправке запроса: {e }")
                    logger .debug (f"Отправляю запрос повторно...")

            raise RequestSendingError (url ,err )

        cf_sigs =[
        "<title>Just a moment...</title>",
        "window._cf_chl_opt",
        "Enable JavaScript and cookies to continue",
        "Checking your browser before accessing",
        "cf-browser-verification",
        "Cloudflare Ray ID"
        ]

        for attempt in range (30 ):
            resp =make_req ()
            if not any (sig in resp .text for sig in cf_sigs ):
                break 

            self ._refresh_clients ()
            delay =min (120.0 ,5.0 *(2 **attempt ))
            logger .warning (f"Cloudflare Detected, пробую отправить запрос снова через {delay } секунд")

            time .sleep (delay )
        else :
            raise CloudflareDetectedException (resp )

        json ={}
        try :json =resp .json ()
        except :pass 

        if "errors"in json :
            raise RequestPlayerokError (resp )

        if resp .status_code !=200 and not (resp .status_code ==304 and pass_304 ):
           raise RequestFailedError (resp )

        return resp 

    def get (self )->Account :
        "Gets/updates account data.

:return: Account object with updated data.
:rtype: `playerokapi.account.Account`"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"viewer",
        "query":QUERIES .get ("viewer"),
        "variables":{}
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ["data"]["viewer"]
        if data is None :
            raise UnauthorizedError ()

        self .id =data .get ("id")
        self .username =data .get ("username")
        self .email =data .get ("email")
        self .role =data .get ("role")
        self .has_frozen_balance =data .get ("hasFrozenBalance")
        self .support_chat_id =data .get ("supportChatId")
        self .system_chat_id =data .get ("systemChatId")
        self .unread_chats_counter =data .get ("unreadChatsCounter")
        self .is_blocked =data .get ("isBlocked")
        self .is_blocked_for =data .get ("isBlockedFor")
        self .created_at =data .get ("createdAt")
        self .last_item_created_at =data .get ("lastItemCreatedAt")
        self .has_confirmed_phone_number =data .get ("hasConfirmedPhoneNumber")
        self .can_publish_items =data .get ("canPublishItems")
        self .unread_chats_counter =data .get ("unreadChatsCounter")

        headers ={"accept":"*/*"}
        payload ={
        "operationName":"user",
        "variables":json .dumps ({
        "username":self .username ,
        "hasSupportAccess":False 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("user")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ["data"]["user"]

        if data .get ("__typename")=="User":
            self .profile =account_profile (data )

        return self 

    def get_user (
    self ,
    id :str |None =None ,
    username :str |None =None 
    )->types .UserProfile :
        "Gets user profile.

It is possible to get by any of two parameters:

    :param id: ID of the user, _optional_.
    :type id: `str` or `None`

    :param username: Username of the user, _optional_.
    :type username: `str` or `None`

    :return: User profile object.
    :rtype: `playerokapi.types.UserProfile`"
        if not any ((id ,username )):
            raise TypeError ("No mandatory arguments were passed: id, username")

        headers ={"accept":"*/*"}
        payload ={
        "operationName":"user",
        "variables":json .dumps ({
        "id":id ,
        "username":username ,
        "hasSupportAccess":False 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("user")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ["data"]["user"]
        if data .get ("__typename")=="UserFragment":profile =data 
        elif data .get ("__typename")=="User":profile =data .get ("profile")
        else :profile =None 

        return user_profile (profile )

    def get_deals (
    self ,
    count :int =24 ,
    statuses :list [ItemDealStatuses ]|None =None ,
    direction :ItemDealDirections |None =None ,
    after_cursor :str =None 
    )->types .ItemDealList :
        "Gets account deals.

:param count: Number of deals to get (not more than 24 in one request).
:type count: `int`

:param statuses: Deal statuses to retrieve, _optional_.
:type statuses: `list[playerokapi.enums.ItemDealsStatuses]` or `None`

:param direction: Direction of deals, _optional_.
:type direction: `playerokapi.enums.ItemDealsDirections` or `None`

:param after_cursor: Cursor from which parsing will start (if none - searches from the beginning of the page), _optional_.
:type after_cursor: `str`
        
:return: Deal page.
:rtype: `playerokapi.types.ItemDealList`"
        str_statuses =[status .name for status in statuses ]if statuses else None 
        str_direction =direction .name if direction else None 

        headers ={"accept":"*/*"}
        payload ={
        "operationName":"deals",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "userId":self .id ,
        "direction":str_direction ,
        "status":str_statuses 
        },
        "showForbiddenImage":True 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("deals")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_deal_list (r ["data"]["deals"])

    def get_deal (
    self ,
    deal_id :str 
    )->types .ItemDeal :
        "Gets a deal.

    :param deal_id: ID of the deal.
    :type deal_id: str
    
    :return: Deal object.
    :rtype: playerokapi.types.ItemDeal"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"deal",
        "variables":json .dumps ({
        "id":deal_id ,
        "hasSupportAccess":False ,
        "showForbiddenImage":True 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("deal")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_deal (r ["data"]["deal"])

    def update_deal (
    self ,
    deal_id :str ,
    new_status :ItemDealStatuses 
    )->types .ItemDeal :
        "Updates the deal status
(param deal_id: ID of the deal.
:type deal_id: str)

:param new_status: New deal status.
:type new_status: playerokapi.enums.ItemDealStatuses
        
:return: Object with updated deal.
:rtype: playerokapi.types.ItemDeal"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"updateDeal",
        "variables":{
        "input":{
        "id":deal_id ,
        "status":new_status .name 
        }
        },
        "query":QUERIES .get ("updateDeal")
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_deal (r ["data"]["updateDeal"])

    def get_games (
    self ,
    count :int =24 ,
    type :GameTypes |None =None ,
    after_cursor :str =None 
    )->types .GameList :
        "Gets all games or/applications.

:param count: The number of games that need to be obtained (not more than 24 per request).
:type count: int

:param type: The type of games that need to be retrieved. By default, it is not specified, so all will be received, optionally.
:type type: playerokapi.enums.GameTypes or None

:param after_cursor: The cursor from which parsing will begin (if none - searches from the beginning of the page), optionally.
:type after_cursor: str
        
:return: Game page.
:rtype: playerokapi.types.GameList"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"games",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "type":type .name if type else None 
        }
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("games")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_list (r ["data"]["games"])

    def get_game (
    self ,
    id :str |None =None ,
    slug :str |None =None 
    )->types .Game :
        "Gets the game/app.
Can be obtained by any of two parameters:

:param id: ID of the game/app, _optional_.
:type id: `str` or `None`

:param slug: Name of the page of the game/app, _optional_.
:type slug: `str` or `None`
        
:return: Game object.
:rtype: `playerokapi.types.Game`"
        if not any ((id ,slug )):
            raise TypeError ("No mandatory arguments were passed: id, slug")

        headers ={"accept":"*/*"}
        payload ={
        "operationName":"GamePage",
        "variables":json .dumps ({
        "id":id ,
        "slug":slug 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("GamePage")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return game (r ["data"]["game"])

    def get_game_category (
    self ,
    id :str |None =None ,
    game_id :str |None =None ,
    slug :str |None =None 
    )->types .GameCategory :
        "Gets the category of a game/app.
Can get parameters `id`, or link parameters `game_id` and `slug`

:param id: ID category, optional.
:type id: `str` or `None`

:param game_id: ID game category (better to specify with slug to find exact category), optional.
:type game_id: `str` or `None`

:param slug: Name of the page category, optional.
:type slug: `str` or `None`
        
:return: Game category object.
:rtype: `playerokapi.types.GameCategory`"
        if not id and not all ((game_id ,slug )):
            if not id and (game_id or slug ):
                raise TypeError ("The missing argument link for game_id and slug was passed incompletely.")
            raise TypeError ("There was not passed any of the mandatory arguments: id, game_id, slug")

        headers ={"accept":"*/*"}
        payload ={
        "operationName":"GamePageCategory",
        "variables":json .dumps ({
        "id":id ,
        "gameId":game_id ,
        "slug":slug 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("GamePageCategory")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category (r ["data"]["gameCategory"])

    def get_game_category_agreements (
    self ,
    game_category_id :str ,
    user_id :str |None =None ,
    count :int =24 ,
    after_cursor :str |None =None 
    )->types .GameCategoryAgreementList :
        "Gets user agreements for selling items in a category (if the user has already accepted these agreements - the list will be empty).

:param game_category_id: ID of the game category.
:type game_category_id: `str`

:param user_id: User ID whose agreements need to be obtained. If not specified, will retrieve by your account ID, _optional_.
:type user_id: `str` or `None`

:param count: The number of agreements that need to be obtained (no more than 24 per request).
:type count: `int`
        
:param after_cursor: The cursor from which parsing will start (if not specified - searches from the beginning of the page), _optional_.
:type after_cursor: `str` or `None`
        
:return: Agreement page.
:rtype: `playerokapi.types.GameCategoryAgreementList`"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"gameCategoryAgreements",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "gameCategoryId":game_category_id ,
        "userId":user_id if user_id else self .id 
        }
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("gameCategoryAgreements")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_agreement_list (r ["data"]["gameCategoryAgreements"])

    def get_game_category_obtaining_types (
    self ,
    game_category_id :str ,
    count :int =24 ,
    after_cursor :str |None =None 
    )->types .GameCategoryObtainingTypeList :
        "Gets types (ways) of obtaining an item in a category.

:param game_category_id: ID of the game category.
:type game_category_id: str

:param count: Number of agreements that need to be obtained (not more than 24 for one request).
:type count: int
        
:param after_cursor: Cursor from which parsing will start (if not specified, searches from the beginning of the page), optionally.
:type after_cursor: str or None
        
:return: Agreement page.
:rtype: playerokapi.types.GameCategoryAgreementList"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"gameCategoryObtainingTypes",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "gameCategoryId":game_category_id 
        }
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("gameCategoryObtainingTypes")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_obtaining_type_list (r ["data"]["gameCategoryObtainingTypes"])

    def get_game_category_instructions (
    self ,
    game_category_id :str ,
    obtaining_type_id :str ,
    count :int =24 ,
    type :GameCategoryInstructionTypes |None =None ,
    after_cursor :str |None =None 
    )->types .GameCategoryInstructionList :
        "Gets instructions for sale/purchase in the category.

:param game_category_id: ID of the game category.
:type game_category_id: str

:param obtaining_type_id: ID of the type (way) of obtaining an item.
:type obtaining_type_id: str

:param count: The number of instructions to get (no more than 24 per request).
:type count: int

:param type: Instruction type: for seller or for buyer, optionally.
:type type: enums.GameCategoryInstructionTypes or None

:param after_cursor: Cursor from which parsing will start (if none - looks for the beginning of the page), optionally.
:type after_cursor: str or None

:return: Instruction page.
:rtype: playerokapi.types.GameCategoryInstructionList"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"gameCategoryInstructions",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "gameCategoryId":game_category_id ,
        "obtainingTypeId":obtaining_type_id ,
        "type":type .name if type else None 
        }
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("gameCategoryInstructions")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_instruction_list (r ["data"]["gameCategoryInstructions"])

    def get_game_category_data_fields (
    self ,
    game_category_id :str ,
    obtaining_type_id :str ,
    count :int =24 ,
    type :GameCategoryDataFieldTypes |None =None ,
    after_cursor :str |None =None 
    )->types .GameCategoryDataFieldList :
        "Gets fields with category data (sent after purchase).

:param game_category_id: ID of the game category.
:type game_category_id: str

:param obtaining_type_id: ID of the type (way) of receiving an item.
:type obtaining_type_id: str

:param count: The number of instructions to retrieve (not more than 24 per request).
:type count: int

:param type: Optional. Type of fields with data, _enums.GameCategoryDataFieldTypes_ or None.

:param after_cursor: Cursor from which parsing will start (if not provided - starts from the beginning of the page), optional.
:type after_cursor: str or None

:return: Page of fields with data.
:rtype: playerokapi.types.GameCategoryDataFieldList"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"gameCategoryDataFields",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "gameCategoryId":game_category_id ,
        "obtainingTypeId":obtaining_type_id ,
        "type":type .name if type else None 
        }
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("gameCategoryDataFields")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_data_field_list (r ["data"]["gameCategoryDataFields"])

    def get_chats (
    self ,
    count :int =24 ,
    type :ChatTypes |None =None ,
    status :ChatStatuses |None =None ,
    after_cursor :str |None =None 
    )->types .ChatList :
        "Gets all chats of the account.

:param count: Number of chats to get (not more than 24 per request).
:type count: int

:param type: Type of chats to get. Default is not specified, so all will be retrieved optionally.
:type type: playerokapi.enums.ChatTypes or None

:param status: Status of chats to get. Default is not specified, so any will be retrieved optionally.
:type status: playerokapi.enums.ChatStatuses or None
        
:param after_cursor: Cursor from which parsing will start (if none - search from the beginning of the page), optionally.
:type after_cursor: str or None
        
:return: Chat list page.
:rtype: playerokapi.types.ChatList"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"userChats",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "userId":self .id ,
        "type":type .name if type else None ,
        "status":status .name if status else None 
        },
        "hasSupportAccess":False 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("userChats")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat_list (r ["data"]["chats"])

    def get_chat (
    self ,
    chat_id :str 
    )->types .Chat :
        "Gets a chat.

    :param chat_id: Chat ID.
    :type chat_id: str
    
    :return: Chat object.
    :rtype: playerokapi.types.Chat"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"chat",
        "variables":json .dumps ({
        "id":chat_id ,
        "hasSupportAccess":False 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("chat")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat (r ["data"]["chat"])

    def get_chat_by_username (
    self ,
    username :str 
    )->types .Chat |None :
        "Gets a chat by the nickname of the interlocutor.

    :param username: Nickname of the interlocutor.
    :type username: str

    :return: Chat object.
    :rtype: playerokapi.types.Chat or None"
        next_cursor =None 
        while True :
            chats =self .get_chats (count =24 ,after_cursor =next_cursor )
            for chat in chats .chats :
                if any (user for user in chat .users if user .username .lower ()==username .lower ()):
                    return chat 
            if not chats .page_info .has_next_page :
                break 
            next_cursor =chats .page_info .end_cursor 

    def get_chat_messages (
    self ,
    chat_id :str ,
    count :int =24 ,
    after_cursor :str |None =None 
    )->types .ChatMessageList :
        "Gets chat messages.

:param chat_id: ID of the chat.
:type chat_id: str

:param count: The number of messages to retrieve (not more than 24 per request).
:type count: int

:param after_cursor: The cursor from which parsing will start (if none - searches from the beginning of the page), optionally.
:type after_cursor: str or None
        
:return: Message page.
:rtype: playerokapi.types.ChatMessageList"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"chatMessages",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "chatId":chat_id 
        },
        "hasSupportAccess":False ,
        "showForbiddenImage":True 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("chatMessages")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat_message_list (r ["data"]["chatMessages"])

    def mark_chat_as_read (
    self ,
    chat_id :str 
    )->types .Chat :
        "Marks the chat as read (all messages).

    :param chat_id: ID of the chat.
    :type chat_id: str

    :return: Chat object with updated data.
    :rtype: playerokapi.types.Chat"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"markChatAsRead",
        "query":QUERIES .get ("markChatAsRead"),
        "variables":{
        "input":{
        "chatId":chat_id 
        }
        }
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat (r ["data"]["markChatAsRead"])

    def upload_chat_image_into_temporary_store (
    self ,
    photo_file_path :str ,
    chat_id :str 
    )->types .Chat :
        "Translates to:

Uploads the chat image to a temporary storage
(param chat_id: ID of the chat. type chat_id: str)

:return: A chat object with updated data.
:rtype: playerokapi.types.Chat"
        headers ={"accept":"*/*"}
        operations ={
        "operationName":"uploadChatImageIntoTemporaryStore",
        "query":QUERIES .get ("uploadChatImageIntoTemporaryStore"),
        "variables":{
        "file":None ,
        "input":{
        "chatId":chat_id ,
        "clientAttachmentId":str (uuid .uuid4 ())
        }
        }
        }

        files ={"1":open (photo_file_path ,"rb")}
        map ={"1":["variables.file"]}if photo_file_path else None 
        payload ={
        "operations":json .dumps (operations ),
        "map":json .dumps (map )
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ,files ).json ()
        return temporary_attachment_upload_output (r ["data"]["uploadChatImageIntoTemporaryStore"])

    def send_message (
    self ,
    chat_id :str ,
    text :str |None =None ,
    photo_file_paths :list [str ]=[],
    mark_chat_as_read :bool =False 
    )->types .ChatMessage :
        "Sends a message to the chat.

Can send a text message `text` or a photo `photo_file_path`.

:param chat_id: Chat ID to which the message should be sent.
:type chat_id: `str`

:param text: The text of the message, _optional_.
:type text: `str` or `None`

:param photo_file_paths: Array of file paths to photos, _optional_.
:type photo_file_paths: `list` of `str`

:param mark_chat_as_read: Mark the chat as read before sending, _optional_.
:type mark_chat_as_read: `bool`

:return: The sent message object.
:rtype: `playerokapi.types.ChatMessage`"
        if not any ((text ,photo_file_paths )):
            raise TypeError ("No required arguments were passed: text, photo_file_paths")

        if mark_chat_as_read :
            self .mark_chat_as_read (chat_id =chat_id )

        headers ={"accept":"*/*"}
        payload ={
        "operationName":"createChatMessage",
        "query":QUERIES .get ("createChatMessage"),
        "variables":{
        "input":{
        "chatId":chat_id ,
        "imagesIds":[],
        "text":text or ""
        }
        }
        }

        for file_path in photo_file_paths :
            image =self .upload_chat_image_into_temporary_store (file_path ,chat_id )
            if image :
                payload ["variables"]["input"]["imagesIds"].append (image .id )

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat_message (r ["data"]["createChatMessage"])

    def create_item (
    self ,
    game_category_id :str ,
    obtaining_type_id :str ,
    name :str ,
    price :int ,
    description :str ,
    options :list [GameCategoryOption ],
    data_fields :list [GameCategoryDataField ],
    attachments :list [str ]
    )->types .Item :
        "Creates an item (after creation, it is placed in a draft and not immediately put up for sale).

:param game_category_id: ID of the game category in which the item must be created.
:type game_category_id: str

:param obtaining_type_id: ID of the type of obtaining the item.
:type obtaining_type_id: str

:param name: Name of the item.
:type name: str

:param price: Price of the item.
:type price: int or str

:param description: Description of the item.
:type description: str

:param options: Array of selected options (attributes) of the item.
:type options: list[playerokapi.types.GameCategoryOption]

:param data_fields: Array of fields with item data. 
    !!! Must be filled in with data of type `ITEM_DATA`, i.e., those that are specified when filling in information about a product.
    Fields of type `OBTAINING_DATA` **must not be filled or passed**, as these data will be indicated by the buyer when purchasing the item.
:type data_fields: list[playerokapi.types.GameCategoryDataField]

:param attachments: Array of file attachments to the item. Paths to files are specified.
:type attachments: list[str]

:return: Object of the created item.
:rtype: playerokapi.types.Item"
        payload_attributes ={option .field :option .value for option in options }
        payload_data_fields =[{"fieldId":field .id ,"value":field .value }for field in data_fields ]

        headers ={"accept":"*/*"}
        operations ={
        "operationName":"createItem",
        "query":QUERIES .get ("createItem"),
        "variables":{
        "input":{
        "gameCategoryId":game_category_id ,
        "obtainingTypeId":obtaining_type_id ,
        "name":name ,
        "price":int (price ),
        "description":description ,
        "attributes":payload_attributes ,
        "dataFields":payload_data_fields 
        },
        "attachments":[None ]*len (attachments )
        }
        }

        map ={}
        files ={}

        for i ,att in enumerate (attachments ,start =1 ):
            map [str (i )]=[f"variables.attachments.{i -1 }"]
            files [str (i )]=open (att ,"rb")

        payload ={
        "operations":json .dumps (operations ),
        "map":json .dumps (map )
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ,files ).json ()
        return item (r ["data"]["createItem"])

    def update_item (
    self ,
    id :str ,
    name :str |None =None ,
    price :int |None =None ,
    description :str |None =None ,
    options :list [GameCategoryOption ]|None =None ,
    data_fields :list [GameCategoryDataField ]|None =None ,
    remove_attachments :list [str ]|None =None ,
    add_attachments :list [str ]|None =None 
    )->types .Item :
        "Updates the item account.

    :param id: ID of the item.
    :type id: `str`

    :param name: The name of the item.
    :type name: `str` or `None`

    :param price: The price of the item.
    :type price: `int` or `str` or `None`

    :param description: Description of the item.
    :type description: `str` or `None`

    :param options: Array of selected options (attributes) of the item.
    :type options: `list[playerokapi.types.GameCategoryOption]` or `None`

    :param data_fields: Array of fields with item data. 
        !!! Data fields should be filled in with "ITEM_DATA" field type, i.e., the data that is specified when filling information about the product.
        Fields with "OBTAINING_DATA" **do not need to be filled** and passed, as these data will indicate the buyer himself when ordering the item.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param remove_attachments: Array of IDs of file attachments of the item that need to be deleted.
    :type remove_attachments: `list[str]` or `None`

    :param add_attachments: Array of file attachments of the item that need to be added. The paths to the files are specified.
    :type add_attachments: `list[str]` or `None`

    :return: Object of updated item.
    :rtype: `playerokapi.types.Item`"
        payload_attributes ={option .field :option .value for option in options }if options is not None else None 
        payload_data_fields =[{"fieldId":field .id ,"value":field .value }for field in data_fields ]if data_fields is not None else None 

        headers ={"accept":"*/*"}
        operations ={
        "operationName":"updateItem",
        "query":QUERIES .get ("updateItem"),
        "variables":{
        "input":{
        "id":id 
        },
        "addedAttachments":[None ]*len (add_attachments )if add_attachments else None 
        }
        }
        if name :operations ["variables"]["input"]["name"]=name 
        if price :operations ["variables"]["input"]["price"]=int (price )
        if description :operations ["variables"]["input"]["description"]=description 
        if options :operations ["variables"]["input"]["attributes"]=payload_attributes 
        if data_fields :operations ["variables"]["input"]["dataFields"]=payload_data_fields 
        if remove_attachments :operations ["variables"]["input"]["removedAttachments"]=remove_attachments 

        map ={}
        files ={}

        if add_attachments :
            for i ,att in enumerate (add_attachments ,start =1 ):
                map [str (i )]=[f"variables.addedAttachments.{i -1 }"]
                files [str (i )]=open (att ,"rb")

        payload ={
        "operations":json .dumps (operations ),
        "map":json .dumps (map )
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload if files else operations ,files if files else None ).json ()
        return item (r ["data"]["updateItem"])

    def remove_item (
    self ,
    id :str 
    )->bool :
        "Completely deletes the item from your account.

    :param id: ID of the item.
    :type id: str"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"removeItem",
        "query":QUERIES .get ("removeItem"),
        "variables":{
        "id":id ,
        }
        }

        self .request ("post",f"{self .base_url }/graphql",headers ,payload )
        return True 

    def publish_item (
    self ,
    item_id :str ,
    priority_status_id :str ,
    transaction_provider_id :TransactionProviderIds =TransactionProviderIds .LOCAL 
    )->types .Item :
        "Lists an item for sale.

:param item_id: ID of the item.
:type item_id: str

:param priority_status_id: ID of the priority status of the item, under which it should be listed for sale.
:type priority_status_id: str

:param transaction_provider_id: ID of the transaction provider.
:type transaction_provider_id: playerokapi.types.TransactionProviderIds

:return: Published item object.
:rtype: playerokapi.types.Item"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"publishItem",
        "query":QUERIES .get ("publishItem"),
        "variables":{
        "input":{
        "transactionProviderId":transaction_provider_id .name ,
        "priorityStatuses":[priority_status_id ],
        "itemId":item_id 
        }
        }
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return item (r ["data"]["publishItem"])

    def get_items (
    self ,
    game_id :str |None =None ,
    category_id :str |None =None ,
    count :int =24 ,
    status :ItemStatuses =ItemStatuses .APPROVED ,
    after_cursor :str |None =None 
    )->types .ItemProfileList :
        "Gets game/application items.
Can be obtained by any of the two parameters: `game_id`, `category_id`.

:param game_id: Game/application ID, optionally.
:type game_id: `str` or `None`

:param category_id: Category ID of the game/application, optionally.
:type category_id: `str` or `None`

:param count: The number of items to get (not more than 24 per request).
:type count: `int`

:param status: Type of items to retrieve: active or sold. Default is active.
:type status: `playerokapi.enums.ItemStatuses`

:param after_cursor: Cursor from which parsing will start (if not specified, it will search from the beginning of the page), optionally.
:type after_cursor: `str` or `None`
        
:return: Item profile list page.
:rtype: `playerokapi.types.ItemProfileList`"
        if not any ((game_id ,category_id )):
            raise TypeError ("No required arguments were passed: game_id, category_id")

        headers ={"accept":"*/*"}
        filter ={"gameId":game_id ,"status":[status .name ]if status else None }if not category_id else {"gameCategoryId":category_id ,"status":[status .name ]if status else None }
        payload ={
        "operationName":"items",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":filter 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("items")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_profile_list (r ["data"]["items"])

    def get_item (
    self ,
    id :str |None =None ,
    slug :str |None =None 
    )->types .MyItem |types .Item |types .ItemProfile :
        "Gets the item (product).

Can be obtained by any of two parameters:

:param id: ID of the item, optionally.
:type id: str or None

:param slug: Name of the item page, optionally.
:type slug: str or None

:return: Item object.
:rtype: playerokapi.types.MyItem or playerokapi.types.Item or playerokapi.types.ItemProfile"
        if not any ((id ,slug )):
            raise TypeError ("No required arguments were passed: id, slug")

        headers ={"accept":"*/*"}
        payload ={
        "operationName":"item",
        "variables":json .dumps ({
        "id":id ,
        "slug":slug ,
        "hasSupportAccess":False ,
        "showForbiddenImage":True 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("item")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ["data"]["item"]
        if data ["__typename"]=="MyItem":_item =my_item (data )
        elif data ["__typename"]=="ItemProfile":_item =item_profile (data )
        elif data ["__typename"]in ["Item","ForeignItem"]:_item =item (data )
        else :_item =None 
        return _item 

    def get_item_priority_statuses (
    self ,
    item_id :str ,
    item_price :int |str 
    )->list [types .ItemPriorityStatus ]:
        "Gets statuses of priorities for the item.

:param item_id: ID of the item.
:type item_id: `str`

:param item_price: Price of the item.
:type item_price: `int` or `str`
        
:return: Array of statuses of priority of the item.
:rtype: `list[playerokapi.types.ItemPriorityStatus]`"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"itemPriorityStatuses",
        "variables":json .dumps ({
        "itemId":item_id ,
        "price":int (item_price )
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("itemPriorityStatuses")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return [item_priority_status (status )for status in r ["data"]["itemPriorityStatuses"]]

    def increase_item_priority_status (
    self ,
    item_id :str ,
    priority_status_id :str ,
    payment_method_id :TransactionPaymentMethodIds |None =None ,
    transaction_provider_id :TransactionProviderIds =TransactionProviderIds .LOCAL 
    )->types .Item :
        "Raises priority status of the item.

:param item_id: ID of the item.
:type item_id: str

:param priority_status_id: ID of the priority status to change to.
:type priority_status_id: int or str

:param payment_method_id: Payment method, optionally.
:type payment_method_id: playerokapi.enums.TransactionPaymentMethodIds or None

:param transaction_provider_id: ID of the transaction provider (LOCAL - from site wallet balance).
:type transaction_provider_id: playerokapi.enums.TransactionProviderIds
        
:return: Object of updated item.
:rtype: playerokapi.types.Item"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"increaseItemPriorityStatus",
        "query":QUERIES .get ("increaseItemPriorityStatus"),
        "variables":{
        "input":{
        "itemId":item_id ,
        "priorityStatuses":[priority_status_id ],
        "transactionProviderData":{
        "paymentMethodId":payment_method_id .name if payment_method_id else None 
        },
        "transactionProviderId":transaction_provider_id .name 
        }
        }
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return item (r ["data"]["increaseItemPriorityStatus"])

    def get_transaction_providers (
    self ,
    direction :TransactionProviderDirections =TransactionProviderDirections .IN 
    )->list [types .TransactionProvider ]:
        "Gets all transaction providers.

:param direction: Transaction direction (replenishment/withdrawal).
:type direction: playerokapi.enums.TransactionProviderDirections

:return: List of transaction providers.
:rtype: list of playerokapi.types.TransactionProvider"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"transactionProviders",
        "variables":json .dumps ({
        "filter":{
        "direction":direction .name if direction else None 
        }
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("transactionProviders")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return [transaction_provider (provider )for provider in r ["data"]["transactionProviders"]]

    def get_transactions (
    self ,
    count :int =24 ,
    operation :TransactionOperations |None =None ,
    min_value :int |None =None ,
    max_value :int |None =None ,
    provider_id :TransactionProviderIds |None =None ,
    status :TransactionStatuses |None =None ,
    after_cursor :str |None =None 
    )->TransactionList :
        "Gets all account transactions.

:param count: Number of transactions to retrieve (not more than 24 per request).
:type count: int

:param operation: Transaction operation, optionally.
:type operation: playerokapi.enums.TransactionOperations or None

:param min_value: Minimum transaction value, optionally.
:type min_value: int or None

:param max_value: Maximum transaction value, optionally.
:type max_value: int or None

:param provider_id: Transaction provider ID, optionally.
:type provider_id: playerokapi.enums.TransactionProviderIds or None

:param status: Transaction status, optionally.
:type status: playerokapi.enums.TransactionStatuses or None

:param after_cursor: Cursor from which parsing will start (if not provided - starts from the beginning of the page), optionally.
:type after_cursor: str or None
        
:return: Transaction page.
:rtype: playerokapi.types.TransactionList"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"transactions",
        "variables":{
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":{
        "userId":self .id 
        },
        "hasSupportAccess":False 
        },
        "extensions":{
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("transactions")
        }
        }
        }

        if operation :payload ["variables"]["filter"]["operation"]=[operation .name ]
        if min_value or max_value :
            payload ["variables"]["filter"]["value"]={}
            if min_value :payload ["variables"]["filter"]["value"]["min"]=str (min_value )
            if max_value :payload ["variables"]["filter"]["value"]["max"]=str (max_value )
        if provider_id :payload ["variables"]["filter"]["providerId"]=[provider_id .name ]
        if status :payload ["variables"]["filter"]["status"]=[status .name ]

        payload ["variables"]=json .dumps (payload ["variables"])
        payload ["extensions"]=json .dumps (payload ["extensions"])

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return transaction_list (r ["data"]["transactions"])

    def get_sbp_bank_members (self )->list [SBPBankMember ]:
        "Gets all bank members of SBP.

:return: Transaction provider object.
:rtype: `list` of `playerokapi.types.SBPBankMember`"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"SbpBankMembers",
        "variables":{},
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("SbpBankMembers")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return [sbp_bank_member (member )for member in r ["data"]["sbpBankMembers"]]

    def get_verified_cards (
    self ,
    count :int =24 ,
    after_cursor :str |None =None ,
    direction :SortDirections =SortDirections .ASC 
    )->types .UserBankCardList :
        "Gets verified account maps.

    :param count: Number of bank cards to receive (not more than 24 in one request).
    :type count: `int`

    :param after_cursor: Cursor from which parsing will start (if not provided - searches from the beginning of the page), _optional_.
    :type after_cursor: `str` or `None`

    :param direction: Bank card sorting type.
    :type direction: `playerokapi.enums.SortDirections`
    
    :return: User bank card list page.
    :rtype: `playerokapi.types.UserBankCardList`"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"verifiedCards",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "sort":{
        "direction":direction .name 
        },
        "field":"createdAt"
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("verifiedCards")
        }
        })
        }

        r =self .request ("get",f"{self .base_url }/graphql",headers ,payload ).json ()
        return user_bank_card_list (r ["data"]["verifiedCards"])

    def delete_card (
    self ,
    card_id :str 
    )->bool :
        "Deletes the map from saved in account.

:param card_id: ID bank card.
:type card_id: str
        
:return: True if the card was deleted, otherwise False
:rtype: bool"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"deleteCard",
        "query":QUERIES .get ("deleteCard"),
        "variables":{
        "input":{
        "cardId":card_id 
        }
        }
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return r ["data"]["deleteCard"]

    def request_withdrawal (
    self ,
    provider :TransactionProviderIds ,
    account :str ,
    value :int ,
    payment_method_id :TransactionPaymentMethodIds |None =None ,
    sbp_bank_member_id :str |None =None 
    )->types .Transaction :
        "Creates a request to output funds from the account balance.

:param provider: Transaction provider.
:type provider: playerokapi.enums.TransactionProviderIds

:param account: ID of an added card (or phone number if the SBP provider), on which the withdrawal should be made.
:type account: str

:param value: Withdrawal amount.
:type value: int

:param payment_method_id: ID of a payment method, optional.
:type payment_method_id: playerokapi.enums.TransactionPaymentMethodIds or None

:param sbp_bank_member_id: ID of an SBP bank member (only if the SBP provider is specified), optional.
:type sbp_bank_member_id: str or None
        
:return: Transaction output object.
:rtype: playerokapi.types.Transaction"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"requestWithdrawal",
        "query":QUERIES .get ("requestWithdrawal"),
        "variables":{
        "input":{
        "provider":provider .name ,
        "account":account ,
        "value":value ,
        "providerData":{
        "paymentMethodId":payment_method_id .name if payment_method_id else None ,
        "sbpBankMemberId":sbp_bank_member_id if sbp_bank_member_id else None 
        }
        }
        }
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return transaction (r ["data"]["requestWithdrawal"])

    def remove_transaction (
    self ,
    transaction_id :str 
    )->types .Transaction :
        "Deletes a transaction (for example, you can cancel an output).

:param transaction_id: ID of the transaction.
:type transaction_id: str
        
:return: The cancelled transaction object.
:rtype: playerokapi.types.Transaction"
        headers ={"accept":"*/*"}
        payload ={
        "operationName":"removeTransaction",
        "query":QUERIES .get ("removeTransaction"),
        "variables":{
        "id":transaction_id 
        }
        }

        r =self .request ("post",f"{self .base_url }/graphql",headers ,payload ).json ()
        return transaction (r ["data"]["removeTransaction"])