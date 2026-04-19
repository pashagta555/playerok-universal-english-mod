from __future__ import annotations 
from typing import *
import json 

from .import parser 
from .enums import *
from .misc import PERSISTED_QUERIES 


class FileObject :
    "The File Object.

    :param id: ID file.
    :type id: `str`

    :param url: URL file.
    :type url: `str`

    :param filename: Name file.
    :type filename: `str` or `None`

    :param mime: Mime file.
    :type mime: `str` or `None`"

    def __init__ (self ,id :str ,url :str ,
    filename :str |None ,mime :str |None ):
        self .id :str =id 
        "File ID."
        self .url :str =url 
        "File URL."
        self .filename :str |None =filename 
        "File name."
        self .mime :str |None =mime 
        "File name."


class AccountBalance :
    "Account balance subclass.

:param id: ID of the balance.
:type id: str

:param value: The balance amount.
:type value: int

:param frozen: The frozen balance amount.
:type frozen: int

:param available: The available balance amount.
:type available: int

:param withdrawable: The balance amount available for withdrawal.
:type withdrawable: int

:param pending_income: Pending income.
:type pending_income: int"

    def __init__ (self ,id :str ,value :int ,frozen :int ,available :int ,
    withdrawable :int ,pending_income :int ):
        self .id :str =id 
        "Balance ID."
        self .value :int =value 
        "General balance sum."
        self .frozen :int =frozen 
        "Frozen balance sum."
        self .available :int =available 
        "Available balance sum."
        self .withdrawable :int =withdrawable 
        "Available withdrawal balance sum."
        self .pending_income :int =pending_income 
        "Expected income."


class AccountIncomingDealsStats :
    "Account statistics subclass describing incoming trades.

:param total: Total outgoing deals.
:type total: int

:param finished: Completed outgoing deals.
:type finished: int"

    def __init__ (self ,total :int ,finished :int ):
        self .total :int =total 
        "All outgoing transactions."
        self .finished :int =finished 
        "Number of completed outgoing deals."


class AccountOutgoingDealsStats :
    "Account outgoing transaction statistics subclass.

:param total: Total outgoing transactions.
:type total: int

:param finished: Finished outgoing transactions.
:type finished: int"

    def __init__ (self ,total :int ,finished :int ):
        self .total =total 
        "All outgoing deals."
        self .finished =finished 
        "Number of completed outgoing deals."


class AccountDealsStats :
    "Account subclass describing account deal statistics.

:param incoming: Incoming deals.
:type incoming: playerokapi.types.AccountIncomingDealsStats

:param outgoing: Outgoing deals.
:type outgoing: playerokapi.types.AccountOutgoingDealsStats"

    def __init__ (self ,incoming :AccountIncomingDealsStats ,outgoing :AccountOutgoingDealsStats ):
        self .incoming :AccountIncomingDealsStats =incoming 
        "Incoming deals."
        self .outgoing :AccountOutgoingDealsStats =outgoing 
        "Outgoing transactions."


class AccountItemsStats :
    "Class describing the statistics of account items.

:param total: All items.
:type total: int

:param finished: Finished items.
:type finished: int"

    def __init__ (self ,total :int ,finished :int ):
        self .total :int =total 
        "All subjects."
        self .finished :int =finished 
        "Number of completed subjects."


class AccountStats :
    "Account class describing account statistics.

:param items: Statistics of items.
:type items: playerokapi.types.AccountItemsStats

:param deals: Statistics of deals.
:type deals: playerokapi.types.AccountDealsStats"

    def __init__ (self ,items :AccountItemsStats ,deals :AccountDealsStats ):
        self .items :AccountItemsStats =items 
        "Statistics subjects."
        self .deals :AccountDealsStats =deals 
        "Statistics of deals."


class AccountProfile :
    "Account profile class.

:param id: ID account.
:type id: `str`

:param username: Account nickname.
:type username: `str`

:param email: Account email.
:type email: `str`

:param balance: Account balance object.
:type balance: `playerokapi.types.AccountBalance`

:param stats: Account statistics.
:type stats: `str`

:param role: Account role.
:type role: `playerokapi.enums.UserTypes`

:param avatar_url: Account avatar URL.
:type avatar_url: `str`

:param is_online: Is account online now.
:type is_online: `bool`

:param is_blocked: Is account blocked.
:type is_blocked: `bool`

:param is_blocked_for: Reason for blocking.
:type is_blocked_for: `str`

:param is_verified: Is account verified.
:type is_verified: `bool`

:param rating: Account rating (0-5).
:type rating: `int`

:param reviews_count: Number of reviews on the account.
:type reviews_count: `int`

:param created_at: Date when account was created.
:type created_at: `str`

:param support_chat_id: ID of support chat.
:type support_chat_id: `str`

:param system_chat_id: ID of system chat.
:type system_chat_id: `str`

:param has_frozen_balance: Is balance frozen on the account.
:type has_frozen_balance: `bool`

:param has_enabled_notifications: Are notifications enabled on the account.
:type has_enabled_notifications: `bool`

:param unread_chats_counter: Number of unread chats (or None).
:type unread_chats_counter: `int` or `None`"

    def __init__ (self ,id :str ,username :str ,email :str ,balance :AccountBalance ,stats :AccountStats ,role :UserTypes ,avatar_url :str ,is_online :bool ,is_blocked :bool ,
    is_blocked_for :str ,is_verified :bool ,rating :int ,reviews_count :int ,created_at :str ,support_chat_id :str ,system_chat_id :str ,
    has_frozen_balance :bool ,has_enabled_notifications :bool ,unread_chats_counter :int |None ):
        self .id :str =id 
        "Account ID."
        self .username :str =username 
        "Account nickname."
        self .email :str =email 
        "Account email."
        self .balance :AccountBalance =balance 
        "Account balance object."
        self .stats :AccountStats =stats 
        "Account statistics."
        self .role :UserTypes =role 
        "Account role."
        self .avatar_url :str =avatar_url 
        "URL avatar account."
        self .is_online :bool =is_online 
        "Is the account online now."
        self .is_blocked :bool =is_blocked 
        "Is the account blocked."
        self .is_blocked_for :str =is_blocked_for 
        "Reason for account blocking."
        self .is_verified :bool =is_verified 
        "Is the account verified."
        self .rating :int =rating 
        "Account rating (0-5)."
        self .reviews_count :int =reviews_count 
        "Number of reviews on the account."
        self .created_at :str =created_at 
        "Date of account creation."
        self .support_chat_id :str =support_chat_id 
        "Account Support Chat ID."
        self .system_chat_id :str =system_chat_id 
        "System chat account ID."
        self .has_frozen_balance :bool =has_frozen_balance 
        "Is the balance frozen on the account."
        self .has_enabled_notifications :bool =has_enabled_notifications 
        "Notifications are enabled on the account."
        self .unread_chats_counter :bool |None =unread_chats_counter 
        "Unread Messages Quantity."


class UserProfile :
    "Class describing a user profile.

:param id: User ID.
:type id: str

:param username: User nickname.
:type username: str

:param role: User role.
:type role: playerokapi.enums.UserTypes

:param avatar_url: User avatar URL.
:type avatar_url: str

:param is_online: Is the user online?
:type is_online: bool

:param is_blocked: Is the user blocked?
:type is_blocked: bool

:param rating: User rating (0-5).
:type rating: int

:param reviews_count: Number of user reviews.
:type reviews_count: int

:param support_chat_id: Support chat ID.
:type support_chat_id: str or None

:param system_chat_id: System chat ID.
:type system_chat_id: str or None

:param created_at: User account creation date.
:type created_at: str"

    def __init__ (self ,id :str ,username :str ,role :UserTypes ,avatar_url :str ,is_online :bool ,is_blocked :bool ,
    rating :int ,reviews_count :int ,support_chat_id :str ,system_chat_id :str |None ,created_at :str |None ):
        self .id :str =id 
        "User ID."
        self .username :str =username 
        "User nickname."
        self .role :UserTypes =role 
        "User role."
        self .avatar_url :str =avatar_url 
        "Profile URL."
        self .is_online :bool =is_online 
        "Is the user online now."
        self .is_blocked :bool =is_blocked 
        "Is the user blocked."
        self .rating :int =rating 
        "User rating (0-5)."
        self .reviews_count :int =reviews_count 
        "Number of user reviews."
        self .support_chat_id :str |None =support_chat_id 
        "Chat support ID."
        self .system_chat_id :str |None =system_chat_id 
        "System chat ID."
        self .created_at :str =created_at 
        "Date of account creation for the user."


    def get_items (
    self ,
    count :int =24 ,
    game_id :str |None =None ,
    category_id :str |None =None ,
    statuses :list [ItemStatuses ]|None =None ,
    after_cursor :str |None =None 
    )->ItemProfileList :
        "Gets user items.

:param count: The number of items to get (not more than 24 per request), optionally.
:type count: int
        
:param game_id: ID of the game/application whose items are needed, optionally.
:type game_id: str or None

:param category_id: ID of the category of games/applications whose items are needed, optionally.
:type category_id: str or None

:param status: An array of item types to get. Some statuses can only be obtained if they are in your account profile. If not specified, gets all possible immediately.
:type status: list[playerokapi.enums.ItemStatuses]

:param after_cursor: The cursor from which parsing will start (if none - searches from the beginning of the page), optionally.
:type after_cursor: str or None
        
:return: Item profile page.
:rtype: PlayerokAPI.types.ItemProfileList"
        from .account import get_account 
        account =get_account ()

        headers ={
        "Accept":"*/*",
        "Content-Type":"application/json",
        "Origin":account .base_url 
        }
        filter ={
        "userId":self .id ,
        "status":[status .name for status in statuses ]if statuses else None 
        }
        if game_id :filter ["gameId"]=game_id 
        elif category_id :filter ["gameCategoryId"]=category_id 

        payload ={
        "operationName":"items",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":filter ,
        "showForbiddenImage":False 
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("items")
        }
        })
        }

        r =account .request ("get",f"{account .base_url }/graphql",headers ,payload ).json ()
        return parser .item_profile_list (r ["data"]["items"])

    def get_reviews (
    self ,
    count :int =24 ,
    status :ReviewStatuses =ReviewStatuses .APPROVED ,
    comment_required :bool =False ,
    rating :int |None =None ,
    game_id :str |None =None ,
    category_id :str |None =None ,
    min_item_price :int |None =None ,
    max_item_price :int |None =None ,
    sort_direction :SortDirections =SortDirections .DESC ,
    sort_field :str ="createdAt",
    after_cursor :str |None =None 
    )->ReviewList :
        "Get user reviews.

:param count: Number of reviews to get (not more than 24 per request), optionally.
:type count: int

:param status: Type of reviews to get.
:type status: playerokapi.enums.ReviewStatuses

:param comment_required: Is a comment required in the review, optionally.
:type comment_required: bool

:param rating: Review rating (1-5), optionally.
:type rating: int or None

:param game_id: Game ID for reviews, optionally.
:type game_id: str or None

:param category_id: Category ID for reviews, optionally.
:type category_id: str or None

:param min_item_price: Minimum price of an item review, optionally.
:type min_item_price: bool or None

:param max_item_price: Maximum price of an item review, optionally.
:type max_item_price: bool or None

:param sort_direction: Sort direction type.
:type sort_direction: playerokapi.enums.SortDirections

:param sort_field: Field to sort by (default is createdAt - date), optionally.
:type sort_field: str

:param after_cursor: Cursor from which parsing will start (if none, starts from the beginning of the page), optionally.
:type after_cursor: str or None

:return: Review page.
:rtype: PlayerokAPI.types.ReviewList"
        from .account import get_account 
        account =get_account ()

        headers ={
        "Accept":"*/*",
        "Content-Type":"application/json",
        "Origin":account .base_url ,
        }

        filters ={"userId":self .id ,"status":[status .name ]if status else None }
        if comment_required is not None :
            filters ["hasComment"]=comment_required 
        if game_id is not None :
            filters ["gameId"]=game_id 
        if category_id is not None :
            filters ["categoryId"]=category_id 
        if rating is not None :
            filters ["rating"]=rating 
        if min_item_price is not None or max_item_price is not None :
            item_price ={}
            if min_item_price is not None :
                item_price ["min"]=min_item_price 
            if max_item_price is not None :
                item_price ["max"]=max_item_price 
            filters ["itemPrice"]=item_price 
        payload ={
        "operationName":"testimonials",
        "variables":json .dumps ({
        "pagination":{
        "first":count ,
        "after":after_cursor 
        },
        "filter":filters ,
        "sort":{
        "direction":sort_direction .name if sort_direction else None ,
        "field":sort_field 
        }
        }),
        "extensions":json .dumps ({
        "persistedQuery":{
        "version":1 ,
        "sha256Hash":PERSISTED_QUERIES .get ("testimonials")
        }
        })
        }

        r =account .request ("get",f"{account .base_url }/graphql",headers ,payload ).json ()
        return parser .review_list (r ["data"]["testimonials"])


class Event :
#TODO: Create an event class

    def __init__ (self ):
        pass 


class ItemDeal :
    "Object deal with item.

:param id: ID deal.
:type id: `str`

:param status: Status of the deal.
:type status: `playerokapi.enums.ItemDealStatuses`

:param status_expiration_date: Date of expiration of the status.
:type status_expiration_date: `str` or `None`

:param status_description: Description of the deal status.
:type status_description: `str` or `None`

:param direction: Direction of the deal (purchase/sale).
:type direction: `playerokapi.enums.ItemDealDirections`

:param obtaining: Obtaining of the deal.
:type obtaining: `str` or `None`

:param has_problem: Is there a problem with the deal?
:type has_problem: `bool`

:param report_problem_enabled: Is reporting a problem enabled?
:type report_problem_enabled: `bool` or `None`

:param completed_user: Profile of the user who confirmed the deal.
:type completed_user: `playerokapi.types.UserProfile` or `None`

:param props: Deal attributes.
:type props: `str` or `None`

:param previous_status: Previous status.
:type previous_status: `playerokapi.enums.ItemDealStatuses` or `None`

:param completed_at: Date of deal confirmation.
:type completed_at: `str` or `None`

:param created_at: Date of deal creation.
:type created_at: `str` or `None`

:param logs: Deal logs.
:type logs: `list[playerokapi.types.ItemLog]` or `None`

:param transaction: Transaction of the deal.
:type transaction: `playerokapi.types.Transaction` or `None`

:param user: Profile of the user who made the deal.
:type user: `playerokapi.types.UserProfile`

:param chat: Chat of the deal (only its ID is passed).
:type chat: `playerokapi.types.Chat` or `None`

:param item: Item of the deal.
:type item: `playerokapi.types.Item`

:param review: Review for the deal.
:type review: `playerokapi.types.Review` or `None`

:param obtaining_fields: Obtained fields.
:type obtaining_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

:param comment_from_buyer: Comment from buyer.
:type comment_from_buyer: `str` or `None`"

    def __init__ (self ,id :str ,status :ItemDealStatuses ,status_expiration_date :str |None ,status_description :str |None ,
    direction :ItemDealDirections ,obtaining :str |None ,has_problem :bool ,report_problem_enabled :bool |None ,
    completed_user :UserProfile |None ,props :str |None ,previous_status :ItemDealStatuses |None ,
    completed_at :str ,created_at :str ,logs :list [ItemLog ]|None ,transaction :Transaction |None ,
    user :UserProfile ,chat :Chat |None ,item :Item ,review :Review |None ,obtaining_fields :list [GameCategoryDataField ]|None ,
    comment_from_buyer :str |None ):
        self .id :str =id 
        "Deal ID."
        self .status :ItemDealStatuses =status 
        "Deal status."
        self .status_expiration_date :str |None =status_expiration_date 
        "Expiration date of the status."
        self .status_description :str |None =status_description 
        "Transaction status description."
        self .direction :ItemDealDirections =direction 
        "Direction of deal (purchase/sale)."
        self .obtaining :str |None =obtaining 
        "Deal acquisition."
        self .has_problem :bool =has_problem 
        "Is there an issue with the deal."
        self .report_problem_enabled :bool |None =report_problem_enabled 
        "Is the appeal of the problem included."
        self .completed_user :UserProfile |None =completed_user 
        "User profile confirming the deal."
        self .props :str |None =props 
        "Transaction details."
        self .previous_status :ItemDealStatuses |None =previous_status 
        "Previous status."
        self .completed_at :str |None =completed_at 
        "Date of deal confirmation."
        self .created_at :str |None =created_at 
        "Date of deal creation."
        self .logs :list [ItemLog ]|None =logs 
        "Deal logs."
        self .transaction :Transaction |None =transaction 
        "Transaction of the deal."
        self .user :UserProfile =user 
        "User profile of the person who made a deal."
        self .chat :Chat |None =chat 
        "Chat deal (transfers only its ID)."
        self .item :Item =item 
        "Transaction subject."
        self .review :Review |None =review 
        "Review of the deal."
        self .obtaining_fields :list [GameCategoryDataField ]|None =obtaining_fields 
        "Received fields."
        self .comment_from_buyer :str |None =comment_from_buyer 
        "Customer comment."


class ItemDealPageInfo :
    "Class describing information about a deals page.

:param start_cursor: Cursor of the beginning of the page.
:type start_cursor: str

:param end_cursor: Cursor of the end of the page.
:type end_cursor: str

:param has_previous_page: Does it have the previous page.
:type has_previous_page: bool

:param has_next_page: Does it have the next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse cursor end of page."
        self .has_previous_page :bool =has_previous_page 
        "Does have previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the following one."


class ItemDealList :
    "Class describing a reviews page.

:param deals: Deals of the page.
:type deals: list[playerokapi.types.ItemDeal]

:param page_info: Information about the page.
:type page_info: playerokapi.types.ItemDealPageInfo

:param total_count: Total number of deals.
:type total_count: int"

    def __init__ (self ,deals :list [ItemDeal ],page_info :ItemDealPageInfo ,
    total_count :int ):
        self .deals :list [ItemDeal ]=deals 
        "Deals pages."
        self .page_info :ItemDealPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All deals."


class GameCategoryAgreement :
    "Customer Agreement subclass describing buyer agreements.

:param id: ID of the agreement.
:type id: str

:param description: Description of the agreement.
:type description: str

:param icontype: Type of the agreement icon.
:type icontype: playerokapi.enums.GameCategoryAgreementIconTypes

:param sequence: Sequence of the agreement.
:type sequence: str"

    def __init__ (self ,id :str ,description :str ,
    icontype :GameCategoryAgreementIconTypes ,sequence :int ):
        self .id :str =id 
        "Agreement ID."
        self .description :str =description 
        "Description agreement."
        self .icontype :GameCategoryAgreementIconTypes =icontype 
        "Icon type agreement."
        self .sequence :str =sequence 
        "Sequence of Agreement."


class GameCategoryAgreementPageInfo :
    "Customer Agreement Page Information Class, describing information about a page.

:param start_cursor: Cursor of the beginning of the page.
:type start_cursor: str

:param end_cursor: Cursor of the end of the page.
:type end_cursor: str

:param has_previous_page: Whether there is a previous page.
:type has_previous_page: bool

:param has_next_page: Whether there is a next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse pointer of the end of the page."
        self .has_previous_page :bool =has_previous_page 
        "Has a previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the following one."


class GameCategoryAgreementList :
    "Class describing a page of agreements.

:param agreements: Agreements of the page.
:type agreements: list[playerokapi.types.GameCategoryAgreement]

:param page_info: Information about the page.
:type page_info: playerokapi.types.GameCategoryAgreementPageInfo

:param total_count: Total agreements.
:type total_count: int"

    def __init__ (self ,agreements :list [GameCategoryAgreement ],page_info :GameCategoryAgreementPageInfo ,
    total_count :int ):
        self .agreements :list [GameCategoryAgreement ]=agreements 
        "Page agreements."
        self .page_info :GameCategoryAgreementPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All agreements."


class GameCategoryObtainingType :
    "Class describing the type (way) of obtaining an object in a category.

:param id: ID way.
:type id: str

:param name: Name way.
:type name: str

:param description: Description way.
:type description: str

:param game_category_id: ID category game way.
:type game_category_id: str

:param no_comment_from_buyer: Without comment from buyer?
:type no_comment_from_buyer: bool

:param instruction_for_buyer: Instruction for buyer.
:type instruction_for_buyer: str

:param instruction_for_seller: Instruction for seller.
:type instruction_for_seller: str

:param sequence: Sequence way.
:type sequence: int

:param fee_multiplier: Fee multiplier.
:type fee_multiplier: float

:param agreements: Agreements buyer on buying/seller on selling.
:type agreements: list[playerokapi.types.GameCategoryAgreement]

:param props: Properties category.
:type props: playerokapi.types.GameCategoryProps"

    def __init__ (self ,id :str ,name :str ,description :str ,game_category_id :str ,no_comment_from_buyer :bool ,
    instruction_for_buyer :str |None ,instruction_for_seller :str |None ,sequence :int ,fee_multiplier :float ,
    agreements :list [GameCategoryAgreement ],props :GameCategoryProps ):
        self .id :str =id 
        "Method ID."
        self .name :str =name 
        "Method name."
        self .description :str =description 
        "Description method."
        self .game_category_id :str =game_category_id 
        "Game category by method."
        self .no_comment_from_buyer :bool =no_comment_from_buyer 
        "Without customer comment?"
        self .instruction_for_buyer :str |None =instruction_for_buyer 
        "Instruction for buyer."
        self .instruction_for_seller :str |None =instruction_for_seller 
        "Instructions for the seller."
        self .sequence :int =sequence 
        "Sequence of method."
        self .fee_multiplier :float =fee_multiplier 
        "Commission multiplier."
        self .agreements :list [GameCategoryAgreement ]=agreements 
        "Customer's agreement on purchase/seller's agreement on sale."
        self .props :GameCategoryProps =props 
        "Category proportions."


class GameCategoryObtainingTypePageInfo :
    "Information about a page type (way) to obtain an object in a category, subclass.

:param start_cursor: Cursor of the beginning of the page.
:type start_cursor: str

:param end_cursor: End cursor of the page.
:type end_cursor: str

:param has_previous_page: Whether there is a previous page.
:type has_previous_page: bool

:param has_next_page: Whether there is a next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Mouse pointer started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Does it have a previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the next one."


class GameCategoryObtainingTypeList :
    "Class describing a page of types (ways) of getting an object in a category.

:param obtaining_types: Ways of the page.
:type obtaining_types: list[playerokapi.types.GameCategoryObtainingType]

:param page_info: Information about the page.
:type page_info: playerokapi.types.GameCategoryObtainingTypePageInfo

:param total_count: Total ways.
:type total_count: int"

    def __init__ (self ,obtaining_types :list [GameCategoryObtainingType ],page_info :GameCategoryObtainingTypePageInfo ,
    total_count :int ):
        self .obtaining_types :list [GameCategoryObtainingType ]=obtaining_types 
        "Agreement page."
        self .page_info :GameCategoryAgreementPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "There is Only One Way."


class GameCategoryDataField :
    "Field describing the data fields of an object in a category (sent after purchase).

:param id: ID of the field with data.
:type id: str

:param label: Label-name of the field.
:type label: str

:param type: Type of the field with data.
:type type: playerokapi.enums.GameCategoryDataFieldTypes

:param input_type: Type of the value entered in the field.
:type input_type: playerokapi.enums.GameCategoryDataFieldInputTypes

:param copyable: Is it allowed to copy the value from the field?
:type copyable: bool

:param hidden: Are the data in the field hidden?
:type hidden: bool

:param required: Is this field mandatory?
:type required: bool

:param value: The value of the data in the field.
:type value: str or None"

    def __init__ (self ,id :str ,label :str ,type :GameCategoryDataFieldTypes ,
    input_type :GameCategoryDataFieldInputTypes ,copyable :bool ,
    hidden :bool ,required :bool ,value :str |None ):
        self .id :str =id 
        "Field with data identification."
        self .label :str =label 
        "Field title inscription."
        self .type :GameCategoryDataFieldTypes =type 
        "Field type with data."
        self .input_type :GameCategoryDataFieldInputTypes =input_type 
        "Field input type."
        self .copyable :bool =copyable 
        "Is copying the value from the field allowed."
        self .hidden :bool =hidden 
        "Are data hidden in the field."
        self .required :bool =required 
        "Is this field required?"
        self .value :str |None =value 
        "Value of data in the field."


class GameCategoryDataFieldPageInfo :
    "Class describing information about a page of fields with subject data.

:param start_cursor: Cursor of the start page.
:type start_cursor: str

:param end_cursor: Cursor of the end page.
:type end_cursor: str

:param has_previous_page: Has previous page.
:type has_previous_page: bool

:param has_next_page: Has next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Does it have a previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the next one."


class GameCategoryDataFieldList :
    "Class describing a page of fields with subject data.

:param data_fields: Fields with subject data in category on the page.
:type data_fields: list[playerokapi.types.GameCategoryDataField]

:param page_info: Information about the page.
:type page_info: playerokapi.types.GameCategoryDataFieldPageInfo

:param total_count: Total number of fields with data.
:type total_count: int"

    def __init__ (self ,data_fields :list [GameCategoryDataField ],
    page_info :GameCategoryDataFieldPageInfo ,total_count :int ):
        self .data_fields :list [GameCategoryDataField ]=data_fields 
        "Field data subject category page."
        self .page_info :GameCategoryDataFieldPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All fields with data."


class GameCategoryProps :
    "Class describing the proportions of the category.

:param min_reviews: Minimum number of reviews.
:type min_reviews: int

:param min_reviews_for_seller: Minimum number of reviews for seller.
:type min_reviews_for_seller: int"

    def __init__ (self ,min_reviews :int ,min_reviews_for_seller :int ):
        self .min_reviews :int =min_reviews 
        "Minimum number of reviews."
        self .min_reviews_for_seller :int =min_reviews_for_seller 
        "Minimum number of reviews for the seller."


class GameCategoryOption :
    "Option describing category option.

:param id: ID option.
:type id: str

:param group: Group option.
:type group: str

:param label: Option name-label.
:type label: str

:param type: Option type.
:type type: playerokapi.enums.GameCategoryOptionTypes

:param field: Field name (for payload request to site).
:type field: str

:param value: Value field (for payload request to site).
:type value: str

:param value_range_limit: Range limit by value.
:type value_range_limit: int or None"

    def __init__ (self ,id :str ,group :str ,label :str ,type :GameCategoryOptionTypes ,
    field :str ,value :str ,value_range_limit :int |None ):
        self .id :str =id 
        "Options ID."
        self .group :str =group 
        "Group of options."
        self .label :str =label 
        "Sign-title option."
        self .type :GameCategoryOptionTypes =type 
        "Type option."
        self .field :str =field 
        "Field name (for payload request on site)."
        self .value :str =value 
        "The value of the field (for a payload request on a website)."
        self .value_range_limit :int |None =value_range_limit 
        "Value range limit."


class GameCategoryInstruction :
    "Class describing information about a page instruction for sale/purchase in category.

:param id: ID of the instruction.
:type id: str

:param text: Text of the instruction.
:type text: str"

    def __init__ (self ,id :str ,text :str ):
        self .id :str =id 
        "Instructions."
        self .text :str =text 
        "Instruction Text.

Translation Engine Output:

Text instructions."


class GameCategoryInstructionPageInfo :
    "Class describing an instruction for buying/selling in a category.

:param start_cursor: Cursor of the beginning page.
:type start_cursor: str

:param end_cursor: Cursor of the end page.
:type end_cursor: str

:param has_previous_page: Has previous page.
:type has_previous_page: bool

:param has_next_page: Has next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Cursor started the page."
        self .end_cursor :str =end_cursor 
        "Cursor of the end page."
        self .has_previous_page :bool =has_previous_page 
        "Does it have the previous page."
        self .has_next_page :bool =has_next_page 
        "Does it have the next page."


class GameCategoryInstructionList :
    "Class, describing a page of instructions for sale/purchase in a category.

:param instructions: Instructions on the page.
:type instructions: list[playerokapi.types.GameCategoryInstruction]

:param page_info: Information about the page.
:type page_info: playerokapi.types.GameCategoryInstructionPageInfo

:param total_count: Total number of instructions.
:type total_count: int"

    def __init__ (self ,instructions :list [GameCategoryInstruction ],page_info :GameCategoryInstructionPageInfo ,
    total_count :int ):
        self .instructions :list [GameCategoryInstruction ]=instructions 
        "Page agreements."
        self .page_info :GameCategoryInstructionPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All instructions."


class GameCategory :
    "Object category of game/application.

:param id: ID category.
:type id: `str`

:param slug: Name page category.
:type slug: `str`

:param name: Category name.
:type name: `str`

:param category_id: ID parent category.
:type category_id: `str` or `None`

:param game_id: ID game category.
:type game_id: `str` or `None`

:param obtaining: Type getting.
:type obtaining: `str` or `None` or `None`

:param options: Options category.
:type options: `list[playerokapi.types.GameCategoryOption]` or `None`

:param props: Properties category.
:type props: `playerokapi.types.GameCategoryProps` or `None`

:param no_comment_from_buyer: Without comment from buyer?
:type no_comment_from_buyer: `bool` or `None`

:param instruction_for_buyer: Instruction for buyer.
:type instruction_for_buyer: `str` or `None`

:param instruction_for_seller: Instruction for seller.
:type instruction_for_seller: `str` or `None`

:param use_custom_obtaining: Used custom getting?
:type use_custom_obtaining: `bool`

:param auto_confirm_period: Period automatic confirmation deal category.
:type auto_confirm_period: `playerokapi.enums.GameCategoryAutoConfirmPeriods` or `None`

:param auto_moderation_mode: Is automatic moderation enabled?
:type auto_moderation_mode: `bool` or `None`

:param agreements: Buyer agreements.
:type agreements: `list[playerokapi.types.GameCategoryAgreement]` or `None`

:param fee_multiplier: Commission multiplier.
:type fee_multiplier: `float` or `None`"

    def __init__ (self ,id :str ,slug :str ,name :str ,category_id :str |None ,game_id :str |None ,
    obtaining :str |None ,options :list [GameCategoryOption ]|None ,props :GameCategoryProps |None ,
    no_comment_from_buyer :bool |None ,instruction_for_buyer :str |None ,instruction_for_seller :str |None ,
    use_custom_obtaining :bool ,auto_confirm_period :GameCategoryAutoConfirmPeriods |None ,
    auto_moderation_mode :bool |None ,agreements :list [GameCategoryAgreement ]|None ,fee_multiplier :float |None ):
        self .id :str =id 
        "Category ID."
        self .slug :str =slug 
        "Page name category."
        self .name :str =name 
        "Category Name."
        self .category_id :str |None =category_id 
        "Parent category ID."
        self .game_id :str |None =game_id 
        "Game categories ID."
        self .obtaining :str |None =obtaining 
        "Type of receipt."
        self .options :list [GameCategoryOption ]|None =options 
        "Category options."
        self .props :str |None =props 
        "Category proportions."
        self .no_comment_from_buyer :bool |None =no_comment_from_buyer 
        "Without customer comment?"
        self .instruction_for_buyer :str |None =instruction_for_buyer 
        "Instruction for Purchaser."
        self .instruction_for_seller :str |None =instruction_for_seller 
        "Instruction for seller."
        self .use_custom_obtaining :bool =use_custom_obtaining 
        "Is custom retrieval used."
        self .auto_confirm_period :GameCategoryAutoConfirmPeriods |None =auto_confirm_period 
        "Period of auto-affirmation of this category deal."
        self .auto_moderation_mode :bool |None =auto_moderation_mode 
        "Is automatic moderation enabled."
        self .agreements :list [GameCategoryAgreement ]|None =agreements 
        "Customer Agreements."
        self .fee_multiplier :float |None =fee_multiplier 
        "Commission multiplier."


class Game :
    "Game/Application Object.

:param id: Game/Application ID.
:type id: str

:param slug: Game/Application Page Name.
:type slug: str

:param name: Game/Application Name.
:type name: str

:param type: Type: game or application.
:type type: playerokapi.enums.GameTypes

:param logo: Game/Application Logo.
:type logo: playerokapi.types.FileObject

:param banner: Game/Application Banner.
:type banner: FileObject

:param categories: List of Game/Application Categories.
:type categories: list[playerokapi.types.GameCategory]

:param created_at: Creation Date.
:type created_at: str"

    def __init__ (self ,id :str ,slug :str ,name :str ,type :GameTypes ,
    logo :FileObject ,banner :FileObject ,categories :list [GameCategory ],
    created_at :str ):
        self .id :str =id 
        "Game/app ID."
        self .slug :str =slug 
        "Game/application page name."
        self .name :str =name 
        "Game/application name."
        self .type :GameTypes =type 
        "Type: game or application."
        self .logo :FileObject =logo 
        "Game/app logo."
        self .banner :FileObject =banner 
        "Game/application banner."
        self .categories :list [GameCategory ]=categories 
        "List of game/app categories."
        self .created_at :str =created_at 
        "Creation date."


class GameProfile :
    "Game/Application Profile.

:param id: Game/Application ID.
:type id: str

:param slug: Game/Application page name.
:type slug: str

:param name: Game/Application name.
:type name: str

:param type: Type: game or application.
:type type: playerokapi.types.GameTypes

:param logo: Game/Application logo.
:type logo: playerokapi.types.FileObject"

    def __init__ (self ,id :str ,slug :str ,name :str ,
    type :GameTypes ,logo :FileObject ):
        self .id :str =id 
        "Game/app ID."
        self .slug :str =slug 
        "Game/Application page name."
        self .name :str =name 
        "Game/Application Name."
        self .type :GameTypes =id 
        "Type: game or application."
        self .logo :FileObject =logo 
        "Game/app logo."


class GamePageInfo :
    "Page class describing information about game pages.

:param start_cursor: Start cursor of the page.
:type start_cursor: str

:param end_cursor: End cursor of the page.
:type end_cursor: str

:param has_previous_page: Whether there is a previous page.
:type has_previous_page: bool

:param has_next_page: Whether there is a next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Mouse cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Has previous page."
        self .has_next_page :bool =has_next_page 
        "Has the next page."


class GameList :
    "Class, describing a games page.

:param games: Games/apps of the page.
:type games: list[playerokapi.types.Game]

:param page_info: Information about the page.
:type page_info: playerokapi.types.ChatPageInfo

:param total_count: Total number of games.
:type total_count: int"

    def __init__ (self ,games :list [Game ],page_info :GamePageInfo ,
    total_count :int ):
        self .games :list [Game ]=games 
        "Games/Applications page."
        self .page_info :ChatPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All Games."


class ItemPriorityStatusPriceRange :
    "Price range, describing an item suitable for a certain priority status.

:param min: Minimum price of the item.
:type min: int

:param max: Maximum price of the item.
:type max: int"

    def __init__ (self ,min :int ,max :str ):
        self .min :int =min 
        "Minimum price of the item (in rubles)."
        self .max :int =max 
        "Maximum price of the item (in rubles)."


class ItemPriorityStatus :
    "Class describing the status priority of an item.

:param id: ID of the status priority.
:type id: `str`

:param price: Price of the status (in rubles).
:type price: `int`

:param name: Name of the status.
:type name: `str`

:param type: Type of the status.
:type type: `playerokapi.enums.PriorityTypes`

:param period: Duration of the status (in days).
:type period: `str`

:param price_range: Price range of the item status.
:type price_range: `playerokapi.types.ItemPriorityStatusPriceRange`"

    def __init__ (self ,id :str ,price :int ,name :str ,type :PriorityTypes ,
    period :int ,price_range :ItemPriorityStatusPriceRange ):
        self .id :str =id 
        "Status Priority ID."
        self .price :int =price 
        "Price of status (in rubles)."
        self .name :str =name 
        "Status name."
        self .type :PriorityTypes =type 
        "Status type."
        self .period :int =period 
        "Duration of the status (in days)."
        self .price_range :ItemPriorityStatusPriceRange =price_range 
        "Price range of the item status."


class ItemLog :
    "Event describing the log of an action with an item.

:param id: Log ID.
:type id: str
    
:param event: Log event.
:type event: playerokapi.enums.ItemLogEvents
    
:param created_at: Date of log creation.
:type created_at: str
    
:param user: Profile of the user who performed the log.
:type user: playerokapi.types.UserProfile"

    def __init__ (self ,id :str ,event :ItemLogEvents ,created_at :str ,
    user :UserProfile ):
        self .id :str =id 
        "Log ID."
        self .event :ItemLogEvents =event 
        "Event log."
        self .created_at :str =created_at 
        "Creation date of the log."
        self .user :UserProfile =user 
        "User profile, having logged in."


class Item :
    "Object subject.

:param id: ID subject.
:type id: `str`

:param name: Name subject.
:type name: `str`

:param description: Description subject.
:type description: `str`

:param status: Status subject.
:type status: `playerokapi.enums.ItemStatuses`

:param obtaining_type: Way of getting.
:type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

:param price: Price subject.
:type price: `int`

:param raw_price: Price without discount consideration.
:type raw_price: `int`

:param priority_position: Priority position.
:type priority_position: `int`

:param attachments: Attached files.
:type attachments: `list[playerokapi.types.FileObject]`

:param attributes: Subject attributes.
:type attributes: `dict`

:param category: Game category subject belongs to.
:type category: `playerokapi.types.GameCategory`

:param comment: Subject comment.
:type comment: `str` or `None`

:param data_fields: Data fields of the subject.
:type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

:param fee_multiplier: Commission multiplier.
:type fee_multiplier: `float`

:param game: Game profile the subject belongs to.
:type game: `playerokapi.types.GameProfile`

:param seller_type: Type of the seller.
"type seller_type: `playerokapi.enums.UserTypes`

:param slug: Page name of the subject.
:type slug: `str`

:param user: Seller profile.
:type user: `playerokapi.types.UserProfile`"

    def __init__ (self ,id :str ,slug :str ,name :str ,description :str ,obtaining_type :GameCategoryObtainingType |None ,price :int ,raw_price :int ,priority_position :int ,
    attachments :list [FileObject ],attributes :dict ,category :GameCategory ,comment :str |None ,data_fields :list [GameCategoryDataField ]|None ,
    fee_multiplier :float ,game :GameProfile ,seller_type :UserTypes ,status :ItemStatuses ,user :UserProfile ):
        self .id :str =id 
        "Object ID."
        self .slug :str =slug 
        "Page name subject."
        self .name :str =name 
        "Subject title."
        self .description :str =description 
        "Description of the subject."
        self .obtaining_type :GameCategoryObtainingType |None =obtaining_type 
        "Method of acquisition."
        self .price :int =price 
        "Item price."
        self .raw_price :int =raw_price 
        "Price without discount consideration."
        self .priority_position :int =priority_position 
        "Priority position."
        self .attachments :list [FileObject ]=attachments 
        "Files-application."
        self .attributes :dict =attributes 
        "Attributes of the subject."
        self .category :GameCategory =category 
        "Game category of the object."
        self .comment :str |None =comment 
        "Commentary on the subject."
        self .data_fields :list [GameCategoryDataField ]|None =data_fields 
        "Data subject fields."
        self .fee_multiplier :float =fee_multiplier 
        "Commission multiplier."
        self .game :GameProfile =game 
        "Game subject profile."
        self .seller_type :UserTypes =seller_type 
        "Seller Type."
        self .slug :str =slug 
        "Page name subject."
        self .status :ItemStatuses =status 
        "Subject Status."
        self .user :UserProfile =user 
        "Seller's Profile."


class MyItem :
    "Object of its subject.

:param id: ID of the subject.
:type id: str

:param slug: Name of the subject page.
:type slug: str

:param name: Name of the subject.
:type name: str

:param description: Description of the subject.
:type description: str

:param status: Status of the subject.
:type status: playerokapi.enums.ItemStatuses

:param obtaining_type: Way to obtain.
:type obtaining_type: playerokapi.types.GameCategoryObtainingType or None

:param price: Price of the subject.
:type price: int

:param prev_price: Previous price.
:type prev_price: int

:param raw_price: Price without discount consideration.
:type raw_price: int

:param priority_position: Priority position.
:type priority_position: int

:param attachments: Attachment files.
:type attachments: list[playerokapi.types.FileObject]

:param attributes: Subject attributes.
:type attributes: dict

:param category: Game category of the subject.
:type category: playerokapi.types.GameCategory

:param comment: Comment about the subject.
:type comment: str or None

:param data_fields: Data fields of the subject.
:type data_fields: list[playerokapi.types.GameCategoryDataField] or None

:param fee_multiplier: Commission multiplier.
:type fee_multiplier: float

:param prev_fee_multiplier: Previous commission multiplier.
:type prev_fee_multiplier: float

:param seller_notified_about_fee_change: Whether the seller is notified about the fee change.
:type seller_notified_about_fee_change: bool

:param game: Game profile of the subject.
:type game: playerokapi.types.GameProfile

\param seller_type: Type of seller.
:type seller_type: playerokapi.enums.UserTypes

\param user: Seller profile.
:type user: playerokapi.types.UserProfile

\param buyer: Buyer profile.
:type user: playerokapi.types.UserProfile

\param priority: Priority status of the subject.
:type priority: playerokapi.types.PriorityTypes

\param priority_price: Price of the priority status.
:type priority_price: int

\param sequence: Position of the subject in the table of users' goods.
:type sequence: int or None

\param status_expiration_date: Expiration date of the priority status.
:type status_expiration_date: str or None

\param status_description: Description of the priority status.
:type status_description: str or None

\param status_payment: Payment status (transaction) of the subject.
:type status_payment: playerokapi.types.Transaction or None

\param views_counter: Number of views of the subject.
:type views_counter: int

\param is_editable: Whether the goods can be edited.
:type is_editable: bool

\param approval_date: Date of publication of the subject.
:type approval_date: str or None

\param deleted_at: Date of deletion of the subject.
:type deleted_at: str or None

\param updated_at: Date of last update of the subject.
:type updated_at: str or None

\param created_at: Date of creation of the subject.
:type created_at: str or None"

    def __init__ (self ,id :str ,slug :str ,name :str ,description :str ,obtaining_type :GameCategoryObtainingType |None ,price :int ,raw_price :int ,priority_position :int ,
    attachments :list [FileObject ],attributes :dict ,buyer :UserProfile ,category :GameCategory ,comment :str |None ,
    data_fields :list [GameCategoryDataField ]|None ,fee_multiplier :float ,game :GameProfile ,seller_type :UserTypes ,status :ItemStatuses ,
    user :UserProfile ,prev_price :int ,prev_fee_multiplier :float ,seller_notified_about_fee_change :bool ,
    priority :PriorityTypes ,priority_price :int ,sequence :int |None ,status_expiration_date :str |None ,status_description :str |None ,
    status_payment :Transaction |None ,views_counter :int ,is_editable :bool ,approval_date :str |None ,deleted_at :str |None ,
    updated_at :str |None ,created_at :str |None ):
        self .id :str =id 
        "Item ID."
        self .slug :str =slug 
        "Page name subject."
        self .name :str =name 
        "Subject Name."
        self .status :ItemStatuses =status 
        "Subject status."
        self .description :str =description 
        "Description of the subject."
        self .obtaining_type :GameCategoryObtainingType |None =obtaining_type 
        "Method of obtaining."
        self .price :int =price 
        "Item price."
        self .prev_price :int =prev_price 
        "Previous price."
        self .raw_price :int =raw_price 
        "Price without discount consideration."
        self .priority_position :int =priority_position 
        "Priority position."
        self .attachments :list [FileObject ]=attachments 
        "Files-applications."
        self .attributes :dict =attributes 
        "Attributes of the object."
        self .category :GameCategory =category 
        "Game category of the subject."
        self .comment :str |None =comment 
        "Commentary subject."
        self .data_fields :list [GameCategoryDataField ]|None =data_fields 
        "Subject data fields."
        self .fee_multiplier :float =fee_multiplier 
        "Commission multiplier."
        self .prev_fee_multiplier :float =prev_fee_multiplier 
        "Previous commission multiplier."
        self .seller_notified_about_fee_change :bool =seller_notified_about_fee_change 
        "Is the seller aware of the commission change."
        self .game :GameProfile =game 
        "Game object profile."
        self .seller_type :UserTypes =seller_type 
        "Seller type."
        self .user :UserProfile =user 
        "Seller's Profile."
        self .buyer :UserProfile =buyer 
        "Customer profile for the item (if sold)."
        self .priority :PriorityTypes =priority 
        "Status of the subject priority."
        self .priority_price :int =priority_price 
        "Prices of priority status."
        self .sequence :int |None =sequence 
        "Position of the subject in the table of users' goods."
        self .status_expiration_date :str |None =status_expiration_date 
        "Expiration date of priority status."
        self .status_description :str |None =status_description 
        "Priority status description."
        self .status_payment :str |None =status_payment 
        "Payment status (transaction)."
        self .views_counter :int =views_counter 
        "Number of views for the subject."
        self .is_editable :bool =is_editable 
        "Can you edit the product."
        self .approval_date :str |None =approval_date 
        "Date of publication."
        self .deleted_at :str |None =deleted_at 
        "Date of product removal."
        self .updated_at :str |None =updated_at 
        "Date of the last update of the product."
        self .created_at :str |None =created_at 
        "Date of product creation."


class ItemProfile :
    "Subject Profile.

    :param id: ID subject.
    :type id: `str`

    :param slug: Subject page name.
    :type slug: `str`

    :param priority: Subject priority.
    :type priority: `playerokapi.enums.PriorityTypes`

    :param status: Subject status.
    :type status: `playerokapi.enums.ItemStatuses`

    :param name: Subject name.
    :type name: `str`

    :param price: Subject price.
    :type price: `int`

    :param raw_price: Price without discount.
    :type raw_price: `int`

    :param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param attachment: File attachment.
    :type attachment: `playerokapi.types.FileObject`

    :param user: Seller profile.
    :type user: `playerokapi.types.UserProfile`

    :param approval_date: Approval date.
    :type approval_date: `str`

    :param priority_position: Priority position.
    :type priority_position: `int`

    :param views_counter: View count.
    :type views_counter: `int` or `None`

    :param fee_multiplier: Commission multiplier.
    :type fee_multiplier: `float`

    :param created_at: Creation date.
    :type created_at: `str`"

    def __init__ (self ,id :str ,slug :str ,priority :PriorityTypes ,status :ItemStatuses ,
    name :str ,price :int ,raw_price :int ,seller_type :UserTypes ,attachment :FileObject ,
    user :UserProfile ,approval_date :str ,priority_position :int ,views_counter :int |None ,
    fee_multiplier :float ,created_at :str ):
        self .id :str =id 
        "Item ID."
        self .slug :str =slug 
        "Page name subject."
        self .priority :PriorityTypes =priority 
        "Subject priority."
        self .status :ItemStatuses =status 
        "Subject Status."
        self .name :str =name 
        "Subject title."
        self .price :int =price 
        "Item price."
        self .raw_price :int =raw_price 
        "Price without discount consideration."
        self .seller_type :UserTypes =seller_type 
        "Sales Type."
        self .attachment :FileObject =attachment 
        "File-application."
        self .user :UserProfile =user 
        "Seller Profile."
        self .approval_date :str =approval_date 
        "Approval Date."
        self .priority_position :int =priority_position 
        "Priority position."
        self .views_counter :int |None =views_counter 
        "Number of views."
        self .fee_multiplier :float =fee_multiplier 
        "Commission multiplier."
        self .created_at :str =created_at 
        "Creation date."


class ItemProfilePageInfo :
    "Class describing page information about subjects.

:param start_cursor: Cursor of the beginning of the page.
:type start_cursor: str

:param end_cursor: Cursor of the end of the page.
:type end_cursor: str

:param has_previous_page: Has a previous page.
:type has_previous_page: bool

:param has_next_page: Has a next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Mouse cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Has a previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the next one."


class ItemProfileList :
    "Profile page items.

:param items: Items of the page.
:type items: list[playerokapi.types.Item]

:param page_info: Information about the page.
:type page_info: playerokapi.types.ItemProfilePageInfo

:param total_count: Total items.
:type total_count: int"

    def __init__ (self ,items :list [ItemProfile ],page_info :ItemProfilePageInfo ,
    total_count :int ):
        self .items :list [ItemProfile ]=items 
        "Page items."
        self .page_info :ItemProfilePageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All subjects."


class SBPBankMember :
    "Object members of SBP bank.

:param id: ID.
:type id: str

:param name: Name.
:type name: str

:param icon: URL icon.
:type icon: str"

    def __init__ (self ,id :str ,name :str ,icon :str ):
        self .id :str =id 
        """ ID. """
        self .name :str =name 
        "Title."
        self .icon :str =icon 
        "Icons URL."


class TransactionPaymentMethod :
    "Payment method transaction.

:param id: ID method.
:type id: playerokapi.types.TransactionPaymentMethodIds

:param name: Name method.
:type name: str

:param fee: Fee method.
:type fee: int

:param provider_id: ID provider transaction.
:type provider_id: playerokapi.types.TransactionProviderIds

:param account: Account method (?).
:type account: AccountProfile or None

:param props: Parameters provider transaction.
:type props: playerokapi.types.TransactionProviderProps

:param limits: Limits provider transaction.
:type limits: playerokapi.types.TransactionProviderLimits"

    def __init__ (self ,id :TransactionPaymentMethodIds ,name :str ,fee :int ,provider_id :TransactionProviderIds ,
    account :AccountProfile |None ,props :TransactionProviderProps ,limits :TransactionProviderLimits ):
        self .id :TransactionPaymentMethodIds =id 
        "Method ID."
        self .name :str =name 
        "Method name."
        self .fee :int =fee 
        "Method Commission."
        self .provider_id :TransactionProviderIds =provider_id 
        "Provider ID of transaction."
        self .account :AccountProfile |None =account 
        "Account method (?)."
        self .props :TransactionProviderProps =props 
        "Provider transaction parameters."
        self .limits :TransactionProviderLimits =limits 
        "Provider transaction limits."


class TransactionProviderLimitRange :
    "Transaction provider limit range.

:param min: Minimum amount (in rubles).
:type min: int

:param max: Maximum amount (in rubles).
:type max: int"

    def __init__ (self ,min :int ,max :int ):
        self .min :int =min 
        "Minimum amount (in rubles)."
        self .max :int =max 
        "Maximum sum (in rubles)."


class TransactionProviderLimits :
    "Limits of transaction provider.

:param incoming: For replenishment.
:type incoming: playerokapi.types.TransactionProviderLimitRange

:param outgoing: For withdrawal.
:type outgoing: playerokapi.types.TransactionProviderLimitRange"

    def __init__ (self ,incoming :TransactionProviderLimitRange ,outgoing :TransactionProviderLimitRange ):
        self .incoming :TransactionProviderLimitRange =incoming 
        "To replenishment."
        self .outgoing :TransactionProviderLimitRange =outgoing 
        "On output."


class TransactionProviderRequiredUserData :
    "Required user data for the transaction provider.

:param email: Is it necessary to specify EMail?
:type email: bool

:param phone_number: Is it necessary to specify a phone number?
:type phone_number: bool

:param erip_account_number: Is it necessary to specify an ERIP account number?
:type erip_account_number: bool or None"

    def __init__ (self ,email :bool ,phone_number :bool ,
    erip_account_number :bool |None ):
        self .email :bool =email 
        "Is it necessary to specify Email?"
        self .phone_number :bool =phone_number 
        "Is it necessary to indicate the phone number?"
        self .erip_account_number :bool |None =erip_account_number 
        "Is it necessary to indicate the account number in ERIP?"


class TransactionProviderProps :
    "Parameters of transaction provider.

:param required_user_data: Mandatory user data.
:type required_user_data: playerokapi.types.TransactionProviderRequiredUserData

:param tooltip: Hint.
:type tooltip: str or None"

    def __init__ (self ,required_user_data :TransactionProviderRequiredUserData ,
    tooltip :str |None ):
        self .required_user_data :TransactionProviderRequiredUserData =required_user_data 
        "Required user data."
        self .tooltip :str |None =tooltip 
        "Hint."


class TransactionProvider :
    "Object provider transaction.

:param id: ID provider.
:type id: playerokapi.enums.TransactionProviderIds

:param name: Name provider.
:type name: str

:param fee: Commission provider.
:type fee: int

:param min_fee_amount: Minimum commission.
:type min_fee_amount: int or None

:param description: Description provider.
:type description: str or None

:param account: Account provider (?).
:type account: playerokapi.types.AccountProfile or None

:param props: Provider parameters.
:type props: playerokapi.types.TransactionProviderProps

:param limits: Provider limits.
:type limits: playerokapi.types.TransactionProviderLimits

:param payment_methods: Payment methods.
:type payment_methods: list of playerokapi.types.TransactionPaymentMethod"

    def __init__ (self ,id :TransactionProviderIds ,name :str ,fee :int ,min_fee_amount :int |None ,
    description :str |None ,account :AccountProfile |None ,props :TransactionProviderProps ,
    limits :TransactionProviderLimits ,payment_methods :list [TransactionPaymentMethod ]):
        self .id :TransactionProviderIds =id 
        "Provider ID."
        self .name :str =name 
        "Provider's Name."
        self .fee :int =fee 
        "Provider Commission."
        self .min_fee_amount :int |None =min_fee_amount 
        "Minimum commission."
        self .description :str |None =description 
        "Description provider."
        self .account :AccountProfile |None =account 
        "Provider account."
        self .props :TransactionProviderProps =props 
        "Provider parameters."
        self .limits :TransactionProviderLimits =limits 
        "Provider limits."
        self .payment_methods :list [TransactionPaymentMethod ]=payment_methods 
        "Payment methods."


class Transaction :
    "Object transaction.

:param id: ID transaction.
:type id: str

:param operation: Type of performed operation.
:type operation: playerokapi.enums.TransactionOperations

:param direction: Direction of the transaction.
:type direction: playerokapi.enums.TransactionDirections

:param provider_id: ID payment provider.
:type provider_id: playerokapi.enums.TransactionProviderIds

:param provider: Transaction provider object.
:type provider: playerokapi.types.TransactionProvider

:param user: User who made the transaction object.
:type user: playerokapi.types.UserProfile

:param creator: User who created the transaction object or None.
:type creator: playerokapi.types.UserProfile or None

:param status: Processing transaction status.
:type status: playerokapi.enums.TransactionStatuses

:param status_description: Transaction status description or None.
:type status_description: str or None

:param status_expiration_date: Status expiration date or None.
:type status_expiration_date: str or None

:param value: Transaction amount.
:type value: int

:param fee: Transaction commission.
:type fee: int

:param created_at: Transaction creation date.
:type created_at: str

:param verified_at: Transaction verification date or None.
:type verified_at: str or None

:param verified_by: User who verified the transaction object or None.
:type verified_by: playerokapi.types.UserProfile or None

:param completed_at: Transaction completion date or None.
:type completed_at: str or None

:param completed_by: User who completed the transaction object or None.
:type completed_by: playerokapi.types.UserProfile or None

:param payment_method_id: Payment method ID or None.
:type payment_method_id: str or None

:param is_suspicious: Is the transaction suspicious or None.
:type is_suspicious: bool or None

:param sbp_bank_name: SBP bank name if transaction was made with SBP (or None).
:type sbp_bank_name: str or None"

    def __init__ (self ,id :str ,operation :TransactionOperations ,direction :TransactionDirections ,provider_id :TransactionProviderIds ,
    provider :TransactionProvider ,user :UserProfile ,creator :UserProfile ,status :TransactionStatuses ,status_description :str |None ,
    status_expiration_date :str |None ,value :int ,fee :int ,created_at :str ,verified_at :str |None ,verified_by :UserProfile |None ,
    completed_at :str |None ,completed_by :UserProfile |None ,payment_method_id :str |None ,is_suspicious :bool |None ,sbp_bank_name :str |None ):
        self .id :str =id 
        "Transaction ID."
        self .operation :TransactionOperations =operation 
        "Type of performed operation."
        self .direction :TransactionDirections =direction 
        "Transaction direction."
        self .provider_id :TransactionProviderIds =provider_id 
        "Payment provider ID."
        self .provider :TransactionProvider =provider 
        "Transaction Provider Object."
        self .user :UserProfile =user 
        "User transaction actor."
        self .creator :UserProfile |None =creator 
        "User transaction creator object."
        self .status :TransactionStatuses =status 
        "Transaction processing status."
        self .status_description :str |None =status_description 
        "Status Description."
        self .status_expiration_date :str |None =status_expiration_date 
        "Expiration date of the status."
        self .value :int =value 
        "Transaction sum."
        self .fee :int =fee 
        "Transaction Commission."
        self .created_at :str =created_at 
        "Date of transaction creation."
        self .verified_at :str |None =verified_at 
        "Date of transaction confirmation."
        self .verified_by :UserProfile |None =verified_by 
        "User object confirming the transaction."
        self .completed_at :str |None =completed_at 
        "Date of transaction execution."
        self .completed_by :UserProfile |None =completed_by 
        "User transaction object."
        self .payment_method_id :str |None =payment_method_id 
        "Payment method ID."
        self .is_suspicious :bool |None =is_suspicious 
        "Suspicious transaction."
        self .sbp_bank_name :str |None =sbp_bank_name 
        "Bank name SBP (if the transaction was made through SBP)."


class TransactionPageInfo :
    "PageTransactionInfo, describing information about a transaction page.

:param start_cursor: Cursor of the start page.
:type start_cursor: str

:param end_cursor: Cursor of the end page.
:type end_cursor: str

:param has_previous_page: Whether there is a previous page.
:type has_previous_page: bool

:param has_next_page: Whether there is a next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Mouse pointer started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Has previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have a next one."


class TransactionList :
    "Class describing a chat message page.

:param transactions: Transactions of the page.
:type transactions: list[playerokapi.types.Transaction]

:param page_info: Information about the page.
:type page_info: playerokapi.types.TransactionPageInfo

:param total_count: Total transactions on the page.
:type total_count: int"

    def __init__ (self ,transactions :list [Transaction ],page_info :TransactionPageInfo ,
    total_count :int ):
        self .transactions :list [Transaction ]=transactions 
        "Page transactions."
        self .page_info :TransactionPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All transactions on the page."


class UserBankCard :
    "User's bank card object.

:param id: ID of the card.
:type id: str

:param card_first_six: The first six digits of the card.
:type card_first_six: str

:param card_last_four: The last four digits of the card.
:type card_last_four: str

:param card_type: Type of bank card.
:type card_type: playerokapi.enums.BankCardTypes

:param is_chosen: Is this card chosen by default?
:type is_chosen: bool"

    def __init__ (self ,id :str ,card_first_six :str ,card_last_four :str ,
    card_type :BankCardTypes ,is_chosen :bool ):
        self .id :str =id 
        "ID card."
        self .card_first_six :str =card_first_six 
        "First six digits of the card."
        self .card_last_four :str =card_last_four 
        "Last four digits of the card."
        self .card_type :BankCardTypes =card_type 
        "Credit card type."
        self .is_chosen :bool =is_chosen 
        "Is this card selected as default?"


class UserBankCardPageInfo :
    "Class describing information about a user's bank card page.

:param start_cursor: Cursor of the page start.
:type start_cursor: str

:param end_cursor: Cursor of the page end.
:type end_cursor: str

:param has_previous_page: Whether there is a previous page.
:type has_previous_page: bool

:param has_next_page: Whether there is a next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Mouse cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Does have previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the next one."


class UserBankCardList :
    "Class describing a user's bank card page.

:param bank_cards: Bank cards of the page.
:type bank_cards: list[playerokapi.types.UserBankCard]

:param page_info: Information about the page.
:type page_info: playerokapi.types.UserBankCardPageInfo

:param total_count: Total number of bank cards on the page.
:type total_count: int"

    def __init__ (self ,bank_cards :list [UserBankCard ],
    page_info :UserBankCardPageInfo ,total_count :int ):
        self .bank_cards :list [UserBankCard ]=bank_cards 
        "Bank cards pages."
        self .page_info :UserBankCardPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "There are bank cards on the page."


class Moderator :
# TODO: Make the Moderator class

    def __init__ (self ):
        pass 


class TemporaryAttachmentUploadOutput :
    "Output data for temporary attachment loading
(for attached image).

:param id: ID of data.
:type id: str

:param url: URL of the image.
:type url: str

:param chat_id: ID of the chat where the image is sent.
:type chat_id: str

:param client_attachment_id: ID of the client file attachment.
:type client_attachment_id: str

:param expires_at: Expiration date.
:type expires_at: str"

    def __init__ (self ,id :str ,url :str ,chat_id :str ,
    client_attachment_id :str ,expires_at :str ):
        self .id :str =id 
        "User data."
        self .url :str =id 
        "Image URL."
        self .chat_id :str =id 
        "Chat ID where the image is sent."
        self .client_attachment_id :str =id 
        "Client application ID."
        self .expires_at :str =id 
        "Expiration Date."


class ChatMessageButton :
    "Message button object.

    :param type: Type of button.
    :type type: `playerokapi.types.ChatMessageButtonTypes`

    :param url: URL of the button.
    :type url: `str` or None

    :param text: Text of the button.
    :type text: `str`"

    def __init__ (self ,type :ChatMessageButtonTypes ,
    url :str |None ,text :str ,):
        self .type :ChatMessageButtonTypes =type 
        "Button type."
        self .url :str |None =url 
        "Button URL."
        self .text :str =text 
        "Button text."


class ChatMessage :
    "Class describing a message in a chat.

:param id: ID of the message.
:type id: `str`

:param text: Text of the message.
:type text: `str`

:param created_at: Date of creation of the message.
:type created_at: `str`

:param deleted_at: Date of deletion of the message.
:type deleted_at: `str` or `None`

:param is_read: Is the message read?
:type is_read: `bool`

:param is_suspicious: Is the message suspicious?
:type is_suspicious: `bool`

:param is_bulk_messaging: Is this a bulk messaging?
:type is_bulk_messaging: `bool`

:param game: Game related to the message.
:type game: `str` or `None`

:param file: File attached to the message.
:type file: `playerokapi.types.FileObject` or `None`

:param user: User who sent the message.
:type user: `playerokapi.types.UserProfile`

:param deal: Deal related to the message.
:type deal: `playerokapi.types.Deal` or `None`

:param item: Item related to the message (usually passes only the same deal in the variable deal).
:type item: `playerokapi.types.Item` or `None`

:param transaction: Transaction of the message.
:type transaction: `playerokapi.types.Transaction` or `None`

:param moderator: Moderator of the message.
:type moderator: `playerokapi.types.Moderator`

:param event_by_user: Event by user.
:type event_by_user: `playerokapi.types.UserProfile` or `None`

:param event_to_user: Event for user.
:type event_to_user: `playerokapi.types.UserProfile` or `None`

:param is_auto_response: Is this an auto-response?
:type is_auto_response: `bool`

:param event: Event of the message.
:type event: `playerokapi.types.Event` or `None`

:param buttons: Buttons of the message.
:type buttons: `list[playerokapi.types.MessageButton]`"

    def __init__ (self ,id :str ,text :str ,created_at :str ,deleted_at :str |None ,is_read :bool ,
    is_suspicious :bool ,is_bulk_messaging :bool ,game :Game |None ,file :FileObject |None ,
    user :UserProfile ,deal :ItemDeal |None ,item :ItemProfile |None ,transaction :Transaction |None ,
    moderator :Moderator |None ,event_by_user :UserProfile |None ,event_to_user :UserProfile |None ,
    is_auto_response :bool ,event :Event |None ,buttons :list [ChatMessageButton ]):
        self .id :str =id 
        "Message ID."
        self .text :str =text 
        "Text message."
        self .created_at :str =created_at 
        "Creation date of the message."
        self .deleted_at :str |None =deleted_at 
        "Date of message deletion."
        self .is_read :bool =is_read 
        "Read message."
        self .is_suspicious :bool =is_suspicious 
        "Suspect message."
        self .is_bulk_messaging :bool =is_bulk_messaging 
        "Mass mailing is this."
        self .game :Game |None =game 
        "Game to which the message relates."
        self .file :FileObject |None =file 
        "File attached to the message."
        self .user :UserProfile =user 
        "User who sent the message."
        self .deal :ItemDeal |None =deal 
        "Deal to which the message relates."
        self .item :ItemProfile |None =item 
        "Subject to which the message refers (usually transmitted only itself in a variable deal)."
        self .transaction :Transaction |None =transaction 
        "Transaction message."
        self .moderator :Moderator =moderator 
        "Moderator of the message."
        self .event_by_user :UserProfile |None =event_by_user 
        "User event."
        self .event_to_user :UserProfile |None =event_to_user 
        "Event for the user."
        self .is_auto_response :bool =is_auto_response 
        "Auto-response is this."
        self .event :Event |None =event 
        "Event message."
        self .buttons :list [ChatMessageButton ]=buttons 
        "Message buttons."


class ChatMessagePageInfo :
    "Page information class describing message page information.

:param start_cursor: Start cursor of the page.
:type start_cursor: str

:param end_cursor: End cursor of the page.
:type end_cursor: str

:param has_previous_page: Whether the previous page exists.
:type has_previous_page: bool

:param has_next_page: Whether the next page exists.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Mouse pointer started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Does it have a previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the following one."


class ChatMessageList :
    "Class, describing a chat message page.

:param messages: Messages of the page.
:type messages: list[playerokapi.types.ChatMessage]

:param page_info: Information about the page.
:type page_info: playerokapi.types.ChatMessagePageInfo

:param total_count: Total messages in the chat.
:type total_count: int"

    def __init__ (self ,messages :list [ChatMessage ],page_info :ChatMessagePageInfo ,
    total_count :int ):
        self .messages :list [ChatMessage ]=messages 
        "Page messages."
        self .page_info :ChatMessagePageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All messages in the chat."


class Chat :
    "Object chat.

:param id: ID chat.
:type id: str

:param type: Type chat.
:type type: playerokapi.enums.ChatTypes

:param status: Status chat.
:type status: playerokapi.enums.ChatStatuses or None

:param unread_messages_counter: Number of unread messages.
:type unread_messages_counter: int

:param bookmarked: Is the chat bookmarked?
:type bookmarked: bool or None

:param is_texting_allowed: Is texting allowed in the chat?
:type is_texting_allowed: bool or None

:param owner: Owner of the chat (only if it's a bot chat).
:type owner: bool or None

:param deals: Deals in the chat.
:type deals: list[playerokapi.types.ItemDeal] or None

:param last_message: Object of the last message in the chat
:type last_message: playerokapi.types.ChatMessage or None

:param users: Participants of the chat.
:type users: list[UserProfile]

:param started_at: Date of dialogue start.
:type started_at: str or None

:param finished_at: Date of dialogue end.
:type finished_at: str or None"

    def __init__ (self ,id :str ,type :ChatTypes ,status :ChatStatuses |None ,unread_messages_counter :int ,
    bookmarked :bool |None ,is_texting_allowed :bool |None ,owner :UserProfile |None ,deals :list [ItemDeal ]|None ,
    started_at :str |None ,finished_at :str |None ,last_message :ChatMessage |None ,users :list [UserProfile ]):
        self .id :str =id 
        "Chat ID."
        self .type :ChatTypes =type 
        "Chat type."
        self .status :ChatStatuses |None =status 
        "Chat status."
        self .unread_messages_counter :int =unread_messages_counter 
        "Unread messages quantity."
        self .bookmarked :bool |None =bookmarked 
        "In bookmarks or chat."
        self .is_texting_allowed :bool |None =is_texting_allowed 
        "Is it allowed to write in the chat."
        self .owner :UserProfile =owner 
        "Owner of the chat."
        self .deals :list [ItemDeal ]|None =deals 
        "Chat deals."
        self .last_message :ChatMessage |None =last_message 
        "Last message object in the chat."
        self .users :list [UserProfile ]=users 
        "Participants of the chat."
        self .started_at :str |None =started_at 
        "Date of the dialogue start."
        self .finished_at :str |None =finished_at 
        "Date of dialogue completion."


class ChatPageInfo :
    "Chat page information subclass.

:param start_cursor: Start cursor of the page.
:type start_cursor: str

:param end_cursor: End cursor of the page.
:type end_cursor: str

:param has_previous_page: Whether there is a previous page.
:type has_previous_page: bool

:param has_next_page: Whether there is a next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse end of page."
        self .has_previous_page :bool =has_previous_page 
        "Does have previous page."
        self .has_next_page :bool =has_next_page 
        "Does the next page exist."


class ChatList :
    "Class, describing a chat page.

:param chats: Chats of the page.
:type chats: list[playerokapi.types.Chat]

:param page_info: Information about the page.
:type page_info: playerokapi.types.ChatPageInfo

:param total_count: Total chats.
:type total_count: int"

    def __init__ (self ,chats :list [Chat ],page_info :ChatPageInfo ,
    total_count :int ):
        self .chats :list [Chat ]=chats 
        "Chat pages."
        self .page_info :ChatPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All chats."


class Review :
    "Object of review.

    :param id: ID of the review.
    :type id: `str`

    :param status: Status of the review.
    :type status: `playerokapi.enums.ReviewStatuses`

    :param text: Text of the review.
    :type text: `str` or `None`

    :param rating: Rating of the review.
    :type rating: `int`

    :param created_at: Date of creation of the review.
    :type created_at: `str`

    :param updated_at: Date of update of the review.
    :type updated_at: `str`

    :param deal: Deal related to the review.
    :type deal: `Deal`

    :param creator: Profile of the reviewer.
    :type creator: `UserProfile`

    :param moderator: Moderator who processed the review.
    :type moderator: `Moderator` or `None`

    :param user: Profile of the seller, related to the review.
    :type user: `UserProfile`"

    def __init__ (self ,id :str ,status :ReviewStatuses ,text :str |None ,rating :int ,
    created_at :str ,updated_at :str ,deal :ItemDeal ,creator :UserProfile ,
    moderator :Moderator |None ,user :UserProfile ):
        self .id :str =id 
        "Review ID."
        self .status :ReviewStatuses =status 
        "Status of review."
        self .text :str |None =text 
        "Customer Review."
        self .rating :int =rating 
        "Rating review."
        self .created_at :str =created_at 
        "Date of review creation."
        self .updated_at :str =updated_at 
        "Date of change in review."
        self .deal :ItemDeal =deal 
        "Deal related to the review."
        self .creator :UserProfile =creator 
        "Profile of the reviewer creator."
        self .moderator :Moderator |None =moderator 
        "Moderator, processed the review."
        self .user :UserProfile =user 
        "Seller profile, which the review refers to."


class ReviewPageInfo :
    "Page reviews information class.

:param start_cursor: Start page cursor.
:type start_cursor: str

:param end_cursor: End page cursor.
:type end_cursor: str

:param has_previous_page: Has previous page.
:type has_previous_page: bool

:param has_next_page: Has next page.
:type has_next_page: bool"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        "Mouse cursor started the page."
        self .end_cursor :str =end_cursor 
        "Mouse pointer of the end of the page."
        self .has_previous_page :bool =has_previous_page 
        "Has a previous page."
        self .has_next_page :bool =has_next_page 
        "Does the page have the following one."


class ReviewList :
    "Class, describing the page of reviews.

:param reviews: Reviews of the page.
:type reviews: list[playerokapi.types.Review]

:param page_info: Information about the page.
:type page_info: playerokapi.types.ReviewPageInfo

:param total_count: Total number of reviews.
:type total_count: int"

    def __init__ (self ,reviews :list [Review ],page_info :ReviewPageInfo ,
    total_count :int ):
        self .reviews :list [Review ]=reviews 
        "Reviews page."
        self .page_info :ReviewPageInfo =page_info 
        "Information about the page."
        self .total_count :int =total_count 
        "All reviews."