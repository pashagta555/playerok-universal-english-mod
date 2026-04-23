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


logger =getLogger ('playerokapi')


def get_account ()->Account |None :
    if hasattr (Account ,'instance'):
        return getattr (Account ,'instance')


class Account :
    'A class that describes Playerok account data and methods.\n\n    :param token: Account token.\n    :type token: `str` or `None`\n\n    :param ddg5: Cookie to bypass DDoS-Guard protection (full name: `__ddg5_`).\n                \n **Note:** This Cookie "dies" every time:\n                \n - IP changes\n                \n - User-Agent / TLS fingerprint changes\n                \n - the server updated the keys/algorithm\n                \n For the API to work, this Cookie must be taken from the Cookie data of the account whose token you specified, and requests must come from the same IP address under which you logged in to Playerok.\n                \n If it is invalid, requests will throw a `BotCheckDetectedException` exception.\n    :type ddg5: `str`\n\n    :param user_agent: Browser user agent.\n    :type user_agent: `str` or `None`\n\n    :param cookies: Cookie data of the authorized account. You can specify `token`, `ddg5`, `user_agent` instead of parameters.\n    :type cookies: `str` or `dict[str, str]` or `None`\n\n    :param proxy: IPV4 proxy in the format: `user:pass@ip:port` or `ip:port`, _optional_.\n    :type proxy: `str` or `None`\n\n    :param requests_timeout: Timeout for waiting for responses to requests.\n    :type requests_timeout: `int`'
    def __new__ (cls ,*args ,**kwargs )->Account :
        if not hasattr (cls ,'instance'):
            cls .instance =super (Account ,cls ).__new__ (cls )
        return getattr (cls ,'instance')

    def __init__ (
    self ,
    token :str =None ,
    ddg5 :str ='',
    user_agent :str ='',
    cookies :str |dict [str ,str ]=None ,
    proxy :str =None ,
    requests_timeout :int =15 ,
    **kwargs 
    ):
        if not any ((token ,cookies )):
            raise TypeError ('One of the required arguments must be specified: token or cookies')

        self .token =token 
        'Account session token.'

        self .ddg5 =ddg5 
        'Cookie to bypass DDoS-Guard protection.'

        self .user_agent =user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
        'Browser user agent.'

        self .cookies =cookies 
        'Authorized account cookies.'

        if isinstance (cookies ,str ):
            self .cookies ={
            c .split ('=')[0 ].strip ():c .split ('=')[1 ].strip ()for c 
            in cookies .split (';')if c .strip ()and '='in c 
            }

        if not self .cookies :
            self .cookies ={
            'token':self .token ,
            '__ddg5_':self .ddg5 
            }

        self .requests_timeout =requests_timeout 
        'Timeout waiting for responses to requests.'

        self .proxy =proxy 
        'Proxy.'

        self .__proxy_string =f"http://{self .proxy .replace ('https://','').replace ('http://','')}"if self .proxy else None 
        'Proxy string.'

        self .base_url ='https://playerok.com'
        'Base URL for all requests.'

        self .id :str |None =None 
        'Account ID. \n\n_Filled in when get() is used for the first time_'
        self .username :str |None =None 
        'Account nickname. \n\n_Filled in when get() is used for the first time_'
        self .email :str |None =None 
        'Account email. \n\n_Filled in when get() is used for the first time_'
        self .role :str |None =None 
        'Account role. \n\n_Filled in when get() is used for the first time_'
        self .support_chat_id :str |None =None 
        'Support chat ID. \n\n_Filled in when get() is used for the first time_'
        self .system_chat_id :str |None =None 
        'System chat ID. \n\n_Filled in when get() is used for the first time_'
        self .unread_chats_counter :int |None =None 
        'Number of unread chats. \n\n_Filled in when get() is used for the first time_'
        self .is_blocked :bool |None =None 
        'Is the account blocked? \n\n_Filled in when get() is used for the first time_'
        self .is_blocked_for :str |None =None 
        'Reason for account blocking. \n\n_Filled in when get() is used for the first time_'
        self .created_at :str |None =None 
        'Account creation date. \n\n_Filled in when get() is used for the first time_'
        self .last_item_created_at :str |None =None 
        'Date of last item creation. \n\n_Filled in when get() is used for the first time_'
        self .has_frozen_balance :bool |None =None 
        'Is your account balance frozen? \n\n_Filled in when get() is used for the first time_'
        self .has_confirmed_phone_number :bool |None =None 
        'Is the phone number verified? \n\n_Filled in when get() is used for the first time_'
        self .can_publish_items :bool |None =None 
        'Can sell items? \n\n_Filled in when get() is used for the first time_'
        self .profile :AccountProfile |None =None 
        'Account profile (not to be confused with user profile). \n\n_Filled in when get() is used for the first time_'

        self ._is_initiated =False 
        'Whether the account has been initialized.'

        self ._cert_path =os .path .join (os .path .dirname (__file__ ),'cacert.pem')
        self ._tmp_cert_path =os .path .join (tempfile .gettempdir (),'cacert.pem')
        shutil .copyfile (self ._cert_path ,self ._tmp_cert_path )

        self ._refresh_clients ()

    def _refresh_clients (self ):
        self .__tls_requests =tls_requests .Client (
        proxy =self .__proxy_string 
        )
        self .__curl_session =curl_cffi .Session (
        impersonate ='chrome',
        timeout =self .requests_timeout ,
        proxy =self .__proxy_string ,
        verify =self ._tmp_cert_path 
        )

    def request (
    self ,
    method :Literal ['get','post'],
    url :str ,
    headers :dict [str ,str ],
    payload :dict [str ,str ]|None =None ,
    files :dict |None =None ,
    pass_304 :bool =True 
    )->requests .Response :
        'Sends a request to the playerok.com server.\n\n        :param method: Request method: post, get.\n        :type method: `str`\n\n        :param url: Request URL.\n        :type url: `str`\n\n        :param headers: Request headers.\n        :type headers: `dict[str, str]`\n        \n        :param payload: Payload of the request.\n        :type payload: `dict[str, str]` or `None`\n        \n        :param files: Request files.\n        :type files: `dict` or `None`\n\n        :return: Response from requests.\n        :rtype: `requests.Response`'
        try :x_gql_op =payload .get ('operationName','viewer')
        except :x_gql_op ='viewer'
        _headers ={
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'access-control-allow-headers':'sentry-trace, baggage',
        'apollo-require-preflight':'true',
        'apollographql-client-name':'web',
        'content-type':'application/json',
        'cookie':'; '.join ([f"{k }={v }"for k ,v in self .cookies .items ()]),
        'priority':'u=1, i',
        'origin':'https://playerok.com',
        'referer':'https://playerok.com/',
        'sec-ch-ua':'"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-arch':'"x86"',
        'sec-ch-ua-bitness':'"64"',
        'sec-ch-ua-full-version':'"146.0.7680.180"',
        'sec-ch-ua-full-version-list':'"Chromium";v="146.0.7680.180", "Not-A.Brand";v="24.0.0.0", "Google Chrome";v="146.0.7680.180"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-model':'""',
        'sec-ch-ua-platform':'"Windows"',
        'sec-ch-ua-platform-version':'"19.0.0"',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        'user-agent':self .user_agent ,
        'x-gql-op':x_gql_op ,
        'x-gql-path':'/',
        'x-timezone-offset':'-240',
        'x-apollo-operation-name':x_gql_op 
        }
        headers ={k :v for k ,v in _headers .items ()if k not in headers .keys ()}

        def make_req ():
            err =''

            for _ in range (3 ):
                try :
                    if method =='get':
                        r =self .__curl_session .get (
                        url =url ,
                        params =payload ,
                        headers =headers ,
                        timeout =self .requests_timeout 
                        )
                    elif method =='post':
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

        sigs =[
        '<title>Just a moment...</title>',
        'window._cf_chl_opt',
        'Enable JavaScript and cookies to continue',
        'Checking your browser before accessing',
        'cf-browser-verification',
        'Cloudflare Ray ID'
        ]

        resp =make_req ()
        if any (sig in resp .text for sig in sigs ):
            raise BotCheckDetectedException ()

        cookie_headers ={
        v .split ('=')[0 ]:v .split ('=')[1 ].split (';')[0 ]
        for k ,v in resp .headers .multi_items ()if k .lower ()=='set-cookie'
        }
        for k ,v in cookie_headers .items ():
            self .cookies [k ]=v 

        json ={}
        try :json =resp .json ()
        except :pass 

        if 'errors'in json :
            raise RequestPlayerokError (resp )

        if resp .status_code !=200 and not (resp .status_code ==304 and pass_304 ):
           raise RequestFailedError (resp )

        return resp 

    def get (self )->Account :
        'Retrieves/updates account information.\n\n        :return: Account object with updated data.\n        :rtype: `playerokapi.account.Account`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'viewer',
        'query':QUERIES .get ('viewer'),
        'variables':{}
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ['data']['viewer']
        if data is None :
            raise UnauthorizedError ()

        self .id =data .get ('id')
        self .username =data .get ('username')
        self .email =data .get ('email')
        self .role =data .get ('role')
        self .has_frozen_balance =data .get ('hasFrozenBalance')
        self .support_chat_id =data .get ('supportChatId')
        self .system_chat_id =data .get ('systemChatId')
        self .unread_chats_counter =data .get ('unreadChatsCounter')
        self .is_blocked =data .get ('isBlocked')
        self .is_blocked_for =data .get ('isBlockedFor')
        self .created_at =data .get ('createdAt')
        self .last_item_created_at =data .get ('lastItemCreatedAt')
        self .has_confirmed_phone_number =data .get ('hasConfirmedPhoneNumber')
        self .can_publish_items =data .get ('canPublishItems')
        self .unread_chats_counter =data .get ('unreadChatsCounter')
        self ._is_initiated =True 

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'user',
        'variables':json .dumps ({
        'username':self .username ,
        'hasSupportAccess':False 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('user')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ['data']['user']

        if data .get ('__typename')=='User':
            self .profile =account_profile (data )

        return self 

    def get_user (
    self ,
    id :str |None =None ,
    username :str |None =None 
    )->types .UserProfile :
        "Gets the user's profile.\n\n        Can be obtained using any of two parameters:\n\n        :param id: User ID, _optional_.\n        :type id: `str` or `None`\n\n        :param username: User nickname, _optional_.\n        :type username: `str` or `None`\n\n        :return: User profile object.\n        :rtype: `playerokapi.types.UserProfile`"
        if not any ((id ,username )):
            raise TypeError ('None of the required arguments were passed: id, username')

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'user',
        'variables':json .dumps ({
        'id':id ,
        'username':username ,
        'hasSupportAccess':False 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('user')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ['data']['user']
        if data .get ('__typename')=='UserFragment':profile =data 
        elif data .get ('__typename')=='User':profile =data .get ('profile')
        else :profile =None 

        return user_profile (profile )

    def get_deals (
    self ,
    count :int =24 ,
    statuses :list [ItemDealStatuses ]|None =None ,
    direction :ItemDealDirections |None =None ,
    after_cursor :str =None 
    )->types .ItemDealList :
        'Receives the deal of the account.\n\n        :param count: Number of transactions to receive (no more than 24 per request).\n        :type count: `int`\n\n        :param statuses: Statuses of transactions that need to be received, _optional_.\n        :type statuses: `list[playerokapi.enums.ItemDealsStatuses]` or `None`\n\n        :param direction: Direction of trades, _optional_.\n        :type direction: `playerokapi.enums.ItemDealsDirections` or `None`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str`\n        \n        :return: Deals page.\n        :rtype: `playerokapi.types.ItemDealList`'
        if not self ._is_initiated :
            raise NotInitiatedError ()

        str_statuses =[status .name for status in statuses ]if statuses else None 
        str_direction =direction .name if direction else None 

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'deals',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'userId':self .id ,
        'direction':str_direction ,
        'status':str_statuses 
        },
        'showForbiddenImage':True 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('deals')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_deal_list (r ['data']['deals'])

    def get_deal (
    self ,
    deal_id :str 
    )->types .ItemDeal :
        'Get a deal.\n\n        :param deal_id: The ID of the deal.\n        :type deal_id: `str`\n        \n        :return: Object deal.\n        :rtype: `playerokapi.types.ItemDeal`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'deal',
        'variables':json .dumps ({
        'id':deal_id ,
        'hasSupportAccess':False ,
        'showForbiddenImage':True 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('deal')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_deal (r ['data']['deal'])

    def update_deal (
    self ,
    deal_id :str ,
    new_status :ItemDealStatuses 
    )->types .ItemDeal :
        'Updates the Status of the deal\n        (used to confirm, issue a return, etc.).\n\n        :param deal_id: ID deal.\n        :type deal_id: `str`\n\n        :param new_status: New Status of the deal.\n        :type new_status: `playerokapi.enums.ItemDealStatuses`\n        \n        :return: Updated deal object.\n        :rtype: `playerokapi.types.ItemDeal`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'updateDeal',
        'variables':{
        'input':{
        'id':deal_id ,
        'status':new_status .name 
        }
        },
        'query':QUERIES .get ('updateDeal')
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_deal (r ['data']['updateDeal'])

    def get_games (
    self ,
    count :int =24 ,
    type :GameTypes |None =None ,
    after_cursor :str =None 
    )->types .GameList :
        'Retrieves all games and/or applications.\n\n        :param count: Number of games to receive (no more than 24 per request).\n        :type count: `int`\n\n        :param type: Type of games to receive. Not specified by default, which means they will be all at once, _optional_.\n        :type type: `playerokapi.enums.GameTypes` or `None`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str`\n        \n        :return: Games page.\n        :rtype: `playerokapi.types.GameList`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'games',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'type':type .name if type else None 
        }
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('games')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_list (r ['data']['games'])

    def get_game (
    self ,
    id :str |None =None ,
    slug :str |None =None 
    )->types .Game :
        'Gets the game/application.\n\n        Can be obtained using any of two parameters:\n\n        :param id: Game/application ID, _optional_.\n        :type id: `str` or `None`\n\n        :param slug: Game/application page name, _optional_.\n        :type slug: `str` or `None`\n        \n        :return: Game object.\n        :rtype: `playerokapi.types.Game`'
        if not any ((id ,slug )):
            raise TypeError ('None of the required arguments were passed: id, slug')

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'GamePage',
        'variables':json .dumps ({
        'id':id ,
        'slug':slug 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('GamePage')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return game (r ['data']['game'])

    def get_game_category (
    self ,
    id :str |None =None ,
    game_id :str |None =None ,
    slug :str |None =None 
    )->types .GameCategory :
        'Gets the game/application category.\n\n        Can be obtained by the `id` parameter or by a combination of the `game_id` and `slug` parameters\n\n        :param id: Category ID, _optional_.\n        :type id: `str` or `None`\n\n        :param game_id: Category game ID (it’s better to specify it in conjunction with slug to find the exact category), _optional_.\n        :type game_id: `str` or `None`\n\n        :param slug: Category page name, _optional_.\n        :type slug: `str` or `None`\n        \n        :return: Game category object.\n        :rtype: `playerokapi.types.GameCategory`'
        if not id and not all ((game_id ,slug )):
            if not id and (game_id or slug ):
                raise TypeError ('A bunch of game_id, slug arguments were not fully passed')
            raise TypeError ('None of the required arguments were passed: id, game_id, slug')

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'GamePageCategory',
        'variables':json .dumps ({
        'id':id ,
        'gameId':game_id ,
        'slug':slug 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('GamePageCategory')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category (r ['data']['gameCategory'])

    def get_game_category_agreements (
    self ,
    game_category_id :str ,
    user_id :str |None =None ,
    count :int =24 ,
    after_cursor :str |None =None 
    )->types .GameCategoryAgreementList :
        "Retrieves the user's agreements for the sale of items in the category (if the user has already accepted these agreements, the list will be empty).\n\n        :param game_category_id: Game category ID.\n        :type game_category_id: `str`\n\n        :param user_id: ID of the user whose agreements should be obtained. If not specified, it will be received by your account ID, _optional_.\n        :type user_id: `str` or `None`\n\n        :param count: Number of agreements to be received (no more than 24 per request).\n        :type count: `int`\n        \n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Agreements page.\n        :rtype: `playerokapi.types.GameCategoryAgreementList`"
        if not user_id and not self ._is_initiated :
            raise NotInitiatedError ()

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'gameCategoryAgreements',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'gameCategoryId':game_category_id ,
        'userId':user_id if user_id else self .id 
        }
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('gameCategoryAgreements')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_agreement_list (r ['data']['gameCategoryAgreements'])

    def get_game_category_obtaining_types (
    self ,
    game_category_id :str ,
    count :int =24 ,
    after_cursor :str |None =None 
    )->types .GameCategoryObtainingTypeList :
        'Gets the types (methods) of obtaining an item in a category.\n        \n        :param game_category_id: Game category ID.\n        :type game_category_id: `str`\n\n        :param count: Number of agreements to be received (no more than 24 per request).\n        :type count: `int`\n        \n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Agreements page.\n        :rtype: `playerokapi.types.GameCategoryAgreementList`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'gameCategoryObtainingTypes',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'gameCategoryId':game_category_id 
        }
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('gameCategoryObtainingTypes')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_obtaining_type_list (r ['data']['gameCategoryObtainingTypes'])

    def get_game_category_instructions (
    self ,
    game_category_id :str ,
    obtaining_type_id :str ,
    count :int =24 ,
    type :GameCategoryInstructionTypes |None =None ,
    after_cursor :str |None =None 
    )->types .GameCategoryInstructionList :
        'Receives instructions for selling/buying in a category.\n        \n        :param game_category_id: Game category ID.\n        :type game_category_id: `str`\n        \n        :param obtaining_type_id: ID of the type (method) of obtaining the item.\n        :type obtaining_type_id: `str`\n\n        :param count: Number of instructions to receive (no more than 24 per request).\n        :type count: `int`\n        \n        :param type: Instruction type: for the seller or for the buyer, _optional_.\n        :type type: `enums.GameCategoryInstructionTypes` or `None`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Instructions page.\n        :rtype: `playerokapi.types.GameCategoryInstructionList`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'gameCategoryInstructions',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'gameCategoryId':game_category_id ,
        'obtainingTypeId':obtaining_type_id ,
        'type':type .name if type else None 
        }
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('gameCategoryInstructions')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_instruction_list (r ['data']['gameCategoryInstructions'])

    def get_game_category_data_fields (
    self ,
    game_category_id :str ,
    obtaining_type_id :str ,
    count :int =24 ,
    type :GameCategoryDataFieldTypes |None =None ,
    after_cursor :str |None =None 
    )->types .GameCategoryDataFieldList :
        'Gets the category data fields (which are sent after purchase).\n        \n        :param game_category_id: Game category ID.\n        :type game_category_id: `str`\n        \n        :param obtaining_type_id: ID of the type (method) of obtaining the item.\n        :type obtaining_type_id: `str`\n\n        :param count: Number of instructions to receive (no more than 24 per request).\n        :type count: `int`\n        \n        :param type: Type of data fields, _optional_.\n        :type type: `enums.GameCategoryDataFieldTypes` or `None`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Page of data fields.\n        :rtype: `playerokapi.types.GameCategoryDataFieldList`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'gameCategoryDataFields',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'gameCategoryId':game_category_id ,
        'obtainingTypeId':obtaining_type_id ,
        'type':type .name if type else None 
        }
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('gameCategoryDataFields')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return game_category_data_field_list (r ['data']['gameCategoryDataFields'])

    def get_chats (
    self ,
    count :int =24 ,
    type :ChatTypes |None =None ,
    status :ChatStatuses |None =None ,
    after_cursor :str |None =None 
    )->types .ChatList :
        'Retrieves all chats of the account.\n\n        :param count: Number of chats to receive (no more than 24 per request).\n        :type count: `int`\n\n        :param type: Type of chats to receive. Not specified by default, which means they will be all at once, _optional_.\n        :type type: `playerokapi.enums.ChatTypes` or `None`\n\n        :param status: Status of the chats to receive. Not specified by default, which means there will be any, _optional_.\n        :type status: `playerokapi.enums.ChatStatuses` or `None`\n        \n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Chats page.\n        :rtype: `playerokapi.types.ChatList`'
        if not self ._is_initiated :
            raise NotInitiatedError ()

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'userChats',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'userId':self .id ,
        'type':type .name if type else None ,
        'status':status .name if status else None 
        },
        'hasSupportAccess':False 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('userChats')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat_list (r ['data']['chats'])

    def get_chat (
    self ,
    chat_id :str 
    )->types .Chat :
        'Receives chat.\n\n        :param chat_id: Chat ID.\n        :type chat_id: `str`\n        \n        :return: Chat object.\n        :rtype: `playerokapi.types.Chat`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'chat',
        'variables':json .dumps ({
        'id':chat_id ,
        'hasSupportAccess':False 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('chat')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat (r ['data']['chat'])

    def get_chat_by_username (
    self ,
    username :str 
    )->types .Chat |None :
        'Receives a chat by the nickname of the interlocutor.\n\n        :param username: Nickname of the interlocutor.\n        :type username: `str`\n\n        :return: Chat object.\n        :rtype: `playerokapi.types.Chat` or `None`'
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
        'Receives chat messages.\n\n        :param chat_id: Chat ID.\n        :type chat_id: `str`\n\n        :param count: Number of messages to receive (no more than 24 per request).\n        :type count: `int`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Messages page.\n        :rtype: `playerokapi.types.ChatMessageList`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'chatMessages',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'chatId':chat_id 
        },
        'hasSupportAccess':False ,
        'showForbiddenImage':True 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('chatMessages')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat_message_list (r ['data']['chatMessages'])

    def mark_chat_as_read (
    self ,
    chat_id :str 
    )->types .Chat :
        'Marks the chat as read (all messages).\n\n        :param chat_id: Chat ID.\n        :type chat_id: `str`\n\n        :return: Chat object with updated data.\n        :rtype: `playerokapi.types.Chat`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'markChatAsRead',
        'query':QUERIES .get ('markChatAsRead'),
        'variables':{
        'input':{
        'chatId':chat_id 
        }
        }
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat (r ['data']['markChatAsRead'])

    def upload_chat_image_into_temporary_store (
    self ,
    photo_file_path :str ,
    chat_id :str 
    )->types .Chat :
        'Uploads the chat image to temporary storage\n        (before sending a message with the image).\n\n        :param chat_id: Chat ID.\n        :type chat_id: `str`\n\n        :return: Chat object with updated data.\n        :rtype: `playerokapi.types.Chat`'
        headers ={'accept':'*/*'}
        operations ={
        'operationName':'uploadChatImageIntoTemporaryStore',
        'query':QUERIES .get ('uploadChatImageIntoTemporaryStore'),
        'variables':{
        'file':None ,
        'input':{
        'chatId':chat_id ,
        'clientAttachmentId':str (uuid .uuid4 ())
        }
        }
        }

        files ={'1':open (photo_file_path ,'rb')}
        map ={'1':['variables.file']}if photo_file_path else None 
        payload ={
        'operations':json .dumps (operations ),
        'map':json .dumps (map )
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ,files ).json ()
        return temporary_attachment_upload_output (r ['data']['uploadChatImageIntoTemporaryStore'])

    def send_message (
    self ,
    chat_id :str ,
    text :str |None =None ,
    photo_file_paths :list [str ]=[],
    mark_chat_as_read :bool =False 
    )->types .ChatMessage :
        'Sends a message to the chat.\n\n        You can send a text message `text` or a photo `photo_file_path`.\n\n        :param chat_id: ID of the chat to which the message should be sent.\n        :type chat_id: `str`\n\n        :param text: Message text, _optional_.\n        :type text: `str` or `None`\n\n        :param photo_file_paths: Array of paths to photo files, _optional_.\n        :type photo_file_paths: `list` of `str`\n\n        :param mark_chat_as_read: Mark the chat as read before sending, _optional_.\n        :type mark_chat_as_read: `bool`\n\n        :return: Message object sent.\n        :rtype: `playerokapi.types.ChatMessage`'
        if not any ((text ,photo_file_paths )):
            raise TypeError ('None of the required arguments were passed: text, photo_file_paths')

        if mark_chat_as_read :
            self .mark_chat_as_read (chat_id =chat_id )

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'createChatMessage',
        'query':QUERIES .get ('createChatMessage'),
        'variables':{
        'input':{
        'chatId':chat_id ,
        'imagesIds':[],
        'text':text or ''
        }
        }
        }

        for file_path in photo_file_paths :
            image =self .upload_chat_image_into_temporary_store (file_path ,chat_id )
            if image :
                payload ['variables']['input']['imagesIds'].append (image .id )

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return chat_message (r ['data']['createChatMessage'])

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
        'Creates an Item (after creation, it is placed in the draft, and not immediately put up for sale).\n\n        :param game_category_id: ID of the category of the game in which the Item needs to be created.\n        :type game_category_id: `str`\n\n        :param obtaining_type_id: ID of the type of obtaining the item.\n        :type obtaining_type_id: `str`\n\n        :param name: Name of the item.\n        :type name: `str`\n\n        :param price: The price of the item.\n        :type price: `int` or `str`\n\n        :param description: Description of the item.\n        :type description: `str`\n\n        :param options: An array of **selected** options (attributes) of the item.\n        :type options: `list[playerokapi.types.GameCategoryOption]`\n\n        :param data_fields: An array of fields with item data. \n\n            !!! Data with the field type `ITEM_DATA` must be filled in, that is, the data that is specified when filling out information about the product.\n            Fields with the `OBTAINING_DATA` type **do not need to be filled in and passed**, since this data will be indicated by the Buyer himself when registering the item.\n        :type data_fields: `list[playerokapi.types.GameCategoryDataField]`\n\n        :param attachments: An array of item attachment files. The paths to the files are indicated.\n        :type attachments: `list[str]`\n\n        :return: The object of the created item.\n        :rtype: `playerokapi.types.Item`'
        payload_attributes ={option .field :option .value for option in options }
        payload_data_fields =[{'fieldId':field .id ,'value':field .value }for field in data_fields ]

        headers ={'accept':'*/*'}
        operations ={
        'operationName':'createItem',
        'query':QUERIES .get ('createItem'),
        'variables':{
        'input':{
        'gameCategoryId':game_category_id ,
        'obtainingTypeId':obtaining_type_id ,
        'name':name ,
        'price':int (price ),
        'description':description ,
        'attributes':payload_attributes ,
        'dataFields':payload_data_fields 
        },
        'attachments':[None ]*len (attachments )
        }
        }

        map ={}
        files ={}

        for i ,att in enumerate (attachments ,start =1 ):
            map [str (i )]=[f"variables.attachments.{i -1 }"]
            files [str (i )]=open (att ,'rb')

        payload ={
        'operations':json .dumps (operations ),
        'map':json .dumps (map )
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ,files ).json ()
        return item (r ['data']['createItem'])

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
        'Updates the Item of the account.\n\n        :param id: Item ID.\n        :type id: `str`\n\n        :param name: Name of the item.\n        :type name: `str` or `None`\n\n        :param price: The price of the item.\n        :type price: `int` or `str` or `None`\n\n        :param description: Description of the item.\n        :type description: `str` or `None`\n\n        :param options: An array of **selected** options (attributes) of the item.\n        :type options: `list[playerokapi.types.GameCategoryOption]` or `None`\n\n        :param data_fields: An array of fields with item data. \n\n            !!! Data with the field type `ITEM_DATA` must be filled in, that is, the data that is specified when filling out information about the product.\n            Fields with the `OBTAINING_DATA` type **do not need to be filled in and passed**, since this data will be indicated by the Buyer himself when registering the item.\n        :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`\n\n        :param remove_attachments: An array of item attachment file IDs to remove.\n        :type remove_attachments: `list[str]` or `None`\n\n        :param add_attachments: An array of item attachment files to add. The paths to the files are indicated.\n        :type add_attachments: `list[str]` or `None`\n\n        :return: Object of the updated item.\n        :rtype: `playerokapi.types.Item`'
        payload_attributes ={option .field :option .value for option in options }if options is not None else None 
        payload_data_fields =[{'fieldId':field .id ,'value':field .value }for field in data_fields ]if data_fields is not None else None 

        headers ={'accept':'*/*'}
        operations ={
        'operationName':'updateItem',
        'query':QUERIES .get ('updateItem'),
        'variables':{
        'input':{
        'id':id 
        },
        'addedAttachments':[None ]*len (add_attachments )if add_attachments else None 
        }
        }
        if name :operations ['variables']['input']['name']=name 
        if price :operations ['variables']['input']['price']=int (price )
        if description :operations ['variables']['input']['description']=description 
        if options :operations ['variables']['input']['attributes']=payload_attributes 
        if data_fields :operations ['variables']['input']['dataFields']=payload_data_fields 
        if remove_attachments :operations ['variables']['input']['removedAttachments']=remove_attachments 

        map ={}
        files ={}

        if add_attachments :
            for i ,att in enumerate (add_attachments ,start =1 ):
                map [str (i )]=[f"variables.addedAttachments.{i -1 }"]
                files [str (i )]=open (att ,'rb')

        payload ={
        'operations':json .dumps (operations ),
        'map':json .dumps (map )
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload if files else operations ,files if files else None ).json ()
        return item (r ['data']['updateItem'])

    def remove_item (
    self ,
    id :str 
    )->bool :
        'Completely deletes the Item from your account.\n\n        :param id: Item ID.\n        :type id: `str`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'removeItem',
        'query':QUERIES .get ('removeItem'),
        'variables':{
        'id':id ,
        }
        }

        self .request ('post',f"{self .base_url }/graphql",headers ,payload )
        return True 

    def publish_item (
    self ,
    item_id :str ,
    priority_status_id :str ,
    transaction_provider_id :TransactionProviderIds =TransactionProviderIds .LOCAL 
    )->types .Item :
        'Puts an Item up for sale.\n\n        :param item_id: Item ID.\n        :type item_id: `str`\n\n        :param priority_status_id: ID of the priority status of the item under which it should be put up for sale.\n        :type priority_status_id: `str`\n\n        :param transaction_provider_id: ID of the transaction provider.\n        :type transaction_provider_id: `playerokapi.types.TransactionProviderIds`\n\n        :return: Object of the published item.\n        :rtype: `playerokapi.types.Item`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'publishItem',
        'query':QUERIES .get ('publishItem'),
        'variables':{
        'input':{
        'transactionProviderId':transaction_provider_id .name ,
        'priorityStatuses':[priority_status_id ],
        'itemId':item_id 
        }
        }
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return item (r ['data']['publishItem'])

    def get_items (
    self ,
    game_id :str |None =None ,
    category_id :str |None =None ,
    count :int =24 ,
    status :ItemStatuses =ItemStatuses .APPROVED ,
    after_cursor :str |None =None 
    )->types .ItemProfileList :
        'Receives game/application items.\n\n        Can be obtained by any of two parameters: `game_id`, `category_id`.\n\n        :param game_id: Game/application ID, _optional_.\n        :type game_id: `str` or `None`\n\n        :param category_id: Game/application category ID, _optional_.\n        :type category_id: `str` or `None`\n\n        :param count: Number of items to receive (no more than 24 per request).\n        :type count: `int`\n\n        :param status: Type of items to receive: active or sold. Active by default.\n        :type status: `playerokapi.enums.ItemStatuses`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Item profile page.\n        :rtype: `playerokapi.types.ItemProfileList`'
        if not any ((game_id ,category_id )):
            raise TypeError ('None of the required arguments were passed: game_id, category_id')

        headers ={'accept':'*/*'}
        filter ={'gameId':game_id ,'status':[status .name ]if status else None }if not category_id else {'gameCategoryId':category_id ,'status':[status .name ]if status else None }
        payload ={
        'operationName':'items',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':filter 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('items')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return item_profile_list (r ['data']['items'])

    def get_item (
    self ,
    id :str |None =None ,
    slug :str |None =None 
    )->types .MyItem |types .Item |types .ItemProfile :
        'Gets Item.\n\n        Can be obtained using any of two parameters:\n\n        :param id: Item ID, _optional_.\n        :type id: `str` or `None`\n\n        :param slug: Item page name, _optional_.\n        :type slug: `str` or `None`\n        \n        :return: Item object.\n        :rtype: `playerokapi.types.MyItem` or `playerokapi.types.Item` or `playerokapi.types.ItemProfile`'
        if not any ((id ,slug )):
            raise TypeError ('None of the required arguments were passed: id, slug')

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'item',
        'variables':json .dumps ({
        'id':id ,
        'slug':slug ,
        'hasSupportAccess':False ,
        'showForbiddenImage':True 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('item')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        data :dict =r ['data']['item']
        if data ['__typename']=='MyItem':_item =my_item (data )
        elif data ['__typename']=='ItemProfile':_item =item_profile (data )
        elif data ['__typename']in ['Item','ForeignItem']:_item =item (data )
        else :_item =None 
        return _item 

    def get_item_priority_statuses (
    self ,
    item_id :str ,
    item_price :int |str 
    )->list [types .ItemPriorityStatus ]:
        'Gets the priority statuses for an item.\n\n        :param item_id: Item ID.\n        :type item_id: `str`\n\n        :param item_price: The price of the item.\n        :type item_price: `int` or `str`\n        \n        :return: An array of item priority statuses.\n        :rtype: `list[playerokapi.types.ItemPriorityStatus]`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'itemPriorityStatuses',
        'variables':json .dumps ({
        'itemId':item_id ,
        'price':int (item_price )
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('itemPriorityStatuses')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return [item_priority_status (status )for status in r ['data']['itemPriorityStatuses']]

    def increase_item_priority_status (
    self ,
    item_id :str ,
    priority_status_id :str ,
    payment_method_id :TransactionPaymentMethodIds |None =None ,
    transaction_provider_id :TransactionProviderIds =TransactionProviderIds .LOCAL 
    )->types .Item :
        'Increases the Status of the priority of an item.\n\n        :param item_id: Item ID.\n        :type item_id: `str`\n\n        :param priority_status_id: ID of the priority status to change to.\n        :type priority_status_id: `int` or `str`\n\n        :param payment_method_id: Payment method, _optional_.\n        :type payment_method_id: `playerokapi.enums.TransactionPaymentMethodIds` or `None`\n\n        :param transaction_provider_id: ID of the transaction provider (LOCAL - from the wallet balance on the website).\n        :type transaction_provider_id: `playerokapi.enums.TransactionProviderIds`\n        \n        :return: Object of the updated item.\n        :rtype: `playerokapi.types.Item`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'increaseItemPriorityStatus',
        'query':QUERIES .get ('increaseItemPriorityStatus'),
        'variables':{
        'input':{
        'itemId':item_id ,
        'priorityStatuses':[priority_status_id ],
        'transactionProviderData':{
        'paymentMethodId':payment_method_id .name if payment_method_id else None 
        },
        'transactionProviderId':transaction_provider_id .name 
        }
        }
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return item (r ['data']['increaseItemPriorityStatus'])

    def get_transaction_providers (
    self ,
    direction :TransactionProviderDirections =TransactionProviderDirections .IN 
    )->list [types .TransactionProvider ]:
        'Gets all transaction providers.\n\n        :param direction: Transaction direction (deposit/withdrawal).\n        :type direction: `playerokapi.enums.TransactionProviderDirections`\n        \n        :return: The list of providers is transactional.\n        :rtype: `list` of `playerokapi.types.TransactionProvider`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'transactionProviders',
        'variables':json .dumps ({
        'filter':{
        'direction':direction .name if direction else None 
        }
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('transactionProviders')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return [transaction_provider (provider )for provider in r ['data']['transactionProviders']]

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
        'Retrieves all account transactions.\n\n        :param count: Number of transactions to receive (no more than 24 per request).\n        :type count: `int`\n\n        :param operation: Transaction operation, _optional_.\n        :type operation: `playerokapi.enums.TransactionOperations` or `None`\n\n        :param min_value: Minimum Price of the transaction, _optional_.\n        :type min_value: `int` or `None`\n\n        :param max_value: Maximum Transaction Price, _optional_.\n        :type max_value: `int` or `None`\n\n        :param provider_id: Transaction provider ID, _optional_.\n        :type provider_id: `playerokapi.enums.TransactionProviderIds` or `None`\n\n        :param status: Status of the transaction, _optional_.\n        :type status: `playerokapi.enums.TransactionStatuses` or `None`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Transactions page.\n        :rtype: `playerokapi.types.TransactionList`'
        if not self ._is_initiated :
            raise NotInitiatedError ()

        headers ={'accept':'*/*'}
        payload ={
        'operationName':'transactions',
        'variables':{
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':{
        'userId':self .id 
        },
        'hasSupportAccess':False 
        },
        'extensions':{
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('transactions')
        }
        }
        }

        if operation :payload ['variables']['filter']['operation']=[operation .name ]
        if min_value or max_value :
            payload ['variables']['filter']['value']={}
            if min_value :payload ['variables']['filter']['value']['min']=str (min_value )
            if max_value :payload ['variables']['filter']['value']['max']=str (max_value )
        if provider_id :payload ['variables']['filter']['providerId']=[provider_id .name ]
        if status :payload ['variables']['filter']['status']=[status .name ]

        payload ['variables']=json .dumps (payload ['variables'])
        payload ['extensions']=json .dumps (payload ['extensions'])

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return transaction_list (r ['data']['transactions'])

    def get_sbp_bank_members (self )->list [SBPBankMember ]:
        'Receives all members of the SBP bank.\n\n        :return: Transaction provider object.\n        :rtype: `list` of `playerokapi.types.SBPBankMember`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'SbpBankMembers',
        'variables':{},
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('SbpBankMembers')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return [sbp_bank_member (member )for member in r ['data']['sbpBankMembers']]

    def get_verified_cards (
    self ,
    count :int =24 ,
    after_cursor :str |None =None ,
    direction :SortDirections =SortDirections .ASC 
    )->types .UserBankCardList :
        "Receives verified account cards.\n\n        :param count: Number of bank cards to receive (no more than 24 per request).\n        :type count: `int`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n\n        :param direction: Bank card sorting type.\n        :type direction: `playerokapi.enums.SortDirections`\n        \n        :return: Page of the user's bank cards.\n        :rtype: `playerokapi.types.UserBankCardList`"
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'verifiedCards',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'sort':{
        'direction':direction .name 
        },
        'field':'createdAt'
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('verifiedCards')
        }
        })
        }

        r =self .request ('get',f"{self .base_url }/graphql",headers ,payload ).json ()
        return user_bank_card_list (r ['data']['verifiedCards'])

    def delete_card (
    self ,
    card_id :str 
    )->bool :
        'Removes a card from those saved in your account.\n\n        :param card_id: Bank card ID.\n        :type card_id: `str`\n        \n        :return: True if the card was deleted, otherwise False\n        :rtype: `bool`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'deleteCard',
        'query':QUERIES .get ('deleteCard'),
        'variables':{
        'input':{
        'cardId':card_id 
        }
        }
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return r ['data']['deleteCard']

    def request_withdrawal (
    self ,
    provider :TransactionProviderIds ,
    account :str ,
    value :int ,
    payment_method_id :TransactionPaymentMethodIds |None =None ,
    sbp_bank_member_id :str |None =None 
    )->types .Transaction :
        'Creates a request to withdraw funds from your account balance.\n\n        :param provider: Transaction provider.\n        :type provider: `playerokapi.enums.TransactionProviderIds`\n\n        :param account: ID of the added card (or phone number, if the SBP provider) to which you want to make a withdrawal.\n        :type account: `str`\n\n        :param value: Price of the output.\n        :type value: `int`\n\n        :param payment_method_id: Payment method ID, _optional_.\n        :type payment_method_id: `playerokapi.enums.TransactionPaymentMethodIds` or `None`\n\n        :param sbp_bank_member_id: SBP bank member ID (only if the SBP provider is specified), _optional_.\n        :type sbp_bank_member_id: `str` or `None`\n        \n        :return: Output transaction object.\n        :rtype: `playerokapi.types.Transaction`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'requestWithdrawal',
        'query':QUERIES .get ('requestWithdrawal'),
        'variables':{
        'input':{
        'provider':provider .name ,
        'account':account ,
        'value':value ,
        'providerData':{
        'paymentMethodId':payment_method_id .name if payment_method_id else None ,
        'sbpBankMemberId':sbp_bank_member_id if sbp_bank_member_id else None 
        }
        }
        }
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return transaction (r ['data']['requestWithdrawal'])

    def remove_transaction (
    self ,
    transaction_id :str 
    )->types .Transaction :
        'Deletes a transaction (for example, you can cancel the withdrawal).\n\n        :param transaction_id: Transaction ID.\n        :type transaction_id: `str`\n        \n        :return: Object of the canceled transaction.\n        :rtype: `playerokapi.types.Transaction`'
        headers ={'accept':'*/*'}
        payload ={
        'operationName':'removeTransaction',
        'query':QUERIES .get ('removeTransaction'),
        'variables':{
        'id':transaction_id 
        }
        }

        r =self .request ('post',f"{self .base_url }/graphql",headers ,payload ).json ()
        return transaction (r ['data']['removeTransaction'])