from __future__ import annotations 
from typing import *
import json 

from .import parser 
from .enums import *
from .misc import PERSISTED_QUERIES 


class FileObject :
    'File object.\n\n    :param id: File ID.\n    :type id: `str`\n\n    :param url: URL of the file.\n    :type url: `str`\n\n    :param filename: The name of the file.\n    :type filename: `str` or `None`\n\n    :param mime: The mime of the file.\n    :type mime: `str` or `None`'

    def __init__ (self ,id :str ,url :str ,
    filename :str |None ,mime :str |None ):
        self .id :str =id 
        'File ID.'
        self .url :str =url 
        'File URL.'
        self .filename :str |None =filename 
        'File name.'
        self .mime :str |None =mime 
        'Mime file.'


class AccountBalance :
    'A subclass describing the account balance.\n\n    :param id: Balance ID.\n    :type id: `str`\n\n    :param value: Balance price.\n    :type value: `int`\n\n    :param frozen: Price of frozen balance.\n    :type frozen: `int`\n\n    :param available: Price of available balance.\n    :type available: `int`\n\n    :param withdrawable: Price of the balance available for withdrawal.\n    :type withdrawable: `int`\n\n    :param pending_income: Expected income.\n    :type pending_income: `int`'

    def __init__ (self ,id :str ,value :int ,frozen :int ,available :int ,
    withdrawable :int ,pending_income :int ):
        self .id :str =id 
        'Balance ID.'
        self .value :int =value 
        'Price of the total balance.'
        self .frozen :int =frozen 
        'Price frozen balance.'
        self .available :int =available 
        'Price of available balance.'
        self .withdrawable :int =withdrawable 
        'Price of the balance available for withdrawal.'
        self .pending_income :int =pending_income 
        'Expected income.'


class AccountIncomingDealsStats :
    'A subclass that describes the statistics of incoming transactions of an account.\n\n    :param total: Total outgoing transactions.\n    :type total: `int`\n\n    :param finished: Completed outgoing transactions.\n    :type finished: `int`'

    def __init__ (self ,total :int ,finished :int ):
        self .total :int =total 
        'Total outgoing transactions.'
        self .finished :int =finished 
        'Number of completed outgoing transactions.'


class AccountOutgoingDealsStats :
    'A subclass that describes the statistics of outgoing transactions of an account.\n\n    :param total: Total outgoing transactions.\n    :type total: `int`\n\n    :param finished: Completed outgoing transactions.\n    :type finished: `int`'

    def __init__ (self ,total :int ,finished :int ):
        self .total =total 
        'Total outgoing transactions.'
        self .finished =finished 
        'Number of completed outgoing transactions.'


class AccountDealsStats :
    'A subclass that describes account transaction statistics.\n\n    :param incoming: Incoming deal.\n    :type incoming: `playerokapi.types.AccountIncomingDealsStats`\n\n    :param outgoing: Outgoing deal.\n    :type outgoing: `playerokapi.types.AccountOutgoingDealsStats`'

    def __init__ (self ,incoming :AccountIncomingDealsStats ,outgoing :AccountOutgoingDealsStats ):
        self .incoming :AccountIncomingDealsStats =incoming 
        'Incoming deal.'
        self .outgoing :AccountOutgoingDealsStats =outgoing 
        'Outgoing deal.'


class AccountItemsStats :
    'A subclass that describes the statistics of account items.\n\n    :param total: Total items.\n    :type total: `int`\n\n    :param finished: Completed items.\n    :type finished: `int`'

    def __init__ (self ,total :int ,finished :int ):
        self .total :int =total 
        'Total items.'
        self .finished :int =finished 
        'Number of completed items.'


class AccountStats :
    'A subclass describing account statistics.\n\n    :param items: Item statistics.\n    :type items: `playerokapi.types.AccountItemsStats`\n\n    :param deals: Deal statistics.\n    :type deals: `playerokapi.types.AccountDealsStats`'

    def __init__ (self ,items :AccountItemsStats ,deals :AccountDealsStats ):
        self .items :AccountItemsStats =items 
        'Item statistics.'
        self .deals :AccountDealsStats =deals 
        'Transaction statistics.'


class AccountProfile :
    'A class describing the account profile.\n\n    :param id: Account ID.\n    :type id: `str`\n\n    :param username: Account nickname.\n    :type username: `str`\n\n    :param email: Account email.\n    :type email: `str`\n\n    :param balance: Account balance object.\n    :type balance: `playerokapi.types.AccountBalance`\n\n    :param stats: Account statistics.\n    :type stats: `str`\n\n    :param role: Account role.\n    :type role: `playerokapi.enums.UserTypes`\n\n    :param avatar_url: Account avatar URL.\n    :type avatar_url: `str`\n\n    :param is_online: Is your account online now?\n    :type is_online: `bool`\n\n    :param is_blocked: Whether the account is blocked.\n    :type is_blocked: `bool`\n\n    :param is_blocked_for: Reason for blocking.\n    :type is_blocked_for: `str`\n\n    :param is_verified: Whether the account is verified.\n    :type is_verified: `bool`\n\n    :param rating: Account rating (0-5).\n    :type rating: `int`\n\n    :param reviews_count: Number of reviews on the account.\n    :type reviews_count: `int`\n\n    :param created_at: Account creation date.\n    :type created_at: `str`\n\n    :param support_chat_id: Support chat ID.\n    :type support_chat_id: `str`\n\n    :param system_chat_id: System chat ID.\n    :type system_chat_id: `str`\n\n    :param has_frozen_balance: Whether the account balance is frozen.\n    :type has_frozen_balance: `bool`\n\n    :param has_enabled_notifications: Whether notifications are enabled on the account.\n    :type has_enabled_notifications: `bool`\n\n    :param unread_chats_counter: Number of unread chats.\n    :type unread_chats_counter: `int` or `None`'

    def __init__ (self ,id :str ,username :str ,email :str ,balance :AccountBalance ,stats :AccountStats ,role :UserTypes ,avatar_url :str ,is_online :bool ,is_blocked :bool ,
    is_blocked_for :str ,is_verified :bool ,rating :int ,reviews_count :int ,created_at :str ,support_chat_id :str ,system_chat_id :str ,
    has_frozen_balance :bool ,has_enabled_notifications :bool ,unread_chats_counter :int |None ):
        self .id :str =id 
        'Account ID.'
        self .username :str =username 
        'Account nickname.'
        self .email :str =email 
        'Account mail.'
        self .balance :AccountBalance =balance 
        'Account balance object.'
        self .stats :AccountStats =stats 
        'Account statistics.'
        self .role :UserTypes =role 
        'Account role.'
        self .avatar_url :str =avatar_url 
        'Account avatar URL.'
        self .is_online :bool =is_online 
        'Is your account online now?'
        self .is_blocked :bool =is_blocked 
        'Is the account blocked?'
        self .is_blocked_for :str =is_blocked_for 
        'Reason for account blocking.'
        self .is_verified :bool =is_verified 
        'Is the account verified?'
        self .rating :int =rating 
        'Account rating (0-5).'
        self .reviews_count :int =reviews_count 
        'Number of reviews on the account.'
        self .created_at :str =created_at 
        'Account creation date.'
        self .support_chat_id :str =support_chat_id 
        'Account support chat ID.'
        self .system_chat_id :str =system_chat_id 
        'Account system chat ID.'
        self .has_frozen_balance :bool =has_frozen_balance 
        'Is the account balance frozen?'
        self .has_enabled_notifications :bool =has_enabled_notifications 
        'Are notifications enabled on your account?'
        self .unread_chats_counter :bool |None =unread_chats_counter 
        'Number of unread messages.'


class UserProfile :
    "A class describing the user profile.\n\n    :param id: User ID.\n    :type id: `str`\n\n    :param username: User nickname.\n    :type username: `str`\n\n    :param role: User role.\n    :type role: `playerokapi.enums.UserTypes`\n\n    :param avatar_url: URL of the user's avatar.\n    :type avatar_url: `str`\n\n    :param is_online: Is the user online now?\n    :type is_online: `bool`\n\n    :param is_blocked: Whether the user is blocked.\n    :type is_blocked: `bool`\n\n    :param rating: User rating (0-5).\n    :type rating: `int`\n\n    :param reviews_count: Number of user reviews.\n    :type reviews_count: `int`\n\n    :param support_chat_id: Support chat ID.\n    :type support_chat_id: `str` or `None`\n\n    :param system_chat_id: System chat ID.\n    :type system_chat_id: `str` or `None`\n\n    :param created_at: Date the user account was created.\n    :type created_at: `str`"

    def __init__ (self ,id :str ,username :str ,role :UserTypes ,avatar_url :str ,is_online :bool ,is_blocked :bool ,
    rating :int ,reviews_count :int ,support_chat_id :str ,system_chat_id :str |None ,created_at :str |None ):
        self .id :str =id 
        'User ID.'
        self .username :str =username 
        'User nickname.'
        self .role :UserTypes =role 
        'User role.'
        self .avatar_url :str =avatar_url 
        'Avatar URL.'
        self .is_online :bool =is_online 
        'Is the user online now?'
        self .is_blocked :bool =is_blocked 
        'Whether the user is blocked.'
        self .rating :int =rating 
        'User rating (0-5).'
        self .reviews_count :int =reviews_count 
        'Number of user reviews.'
        self .support_chat_id :str |None =support_chat_id 
        'Support chat ID.'
        self .system_chat_id :str |None =system_chat_id 
        'System chat ID.'
        self .created_at :str =created_at 
        'The date the user account was created.'


    def get_items (
    self ,
    count :int =24 ,
    game_id :str |None =None ,
    category_id :str |None =None ,
    statuses :list [ItemStatuses ]|None =None ,
    after_cursor :str |None =None 
    )->ItemProfileList :
        "Retrieves the user's items.\n\n        :param count: Number of items to receive (no more than 24 per request), _optional_.\n        :type count: `int`\n        \n        :param game_id: ID of the game/application whose items you want to receive, _optional_.\n        :type game_id: `str` or `None`\n\n        :param category_id: ID of the category of the game/application whose items you want to receive, _optional_.\n        :type category_id: `str` or `None`\n\n        :param status: An array of item types to receive. Some statuses can only be obtained if this is your account profile. If not specified, gets all possible ones at once.\n        :type status: `list[playerokapi.enums.ItemStatuses]`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Item profile page.\n        :rtype: `PlayerokAPI.types.ItemProfileList`"
        from .account import get_account 
        account =get_account ()

        headers ={
        'Accept':'*/*',
        'Content-Type':'application/json',
        'Origin':account .base_url 
        }
        filter ={
        'userId':self .id ,
        'status':[status .name for status in statuses ]if statuses else None 
        }
        if game_id :filter ['gameId']=game_id 
        elif category_id :filter ['gameCategoryId']=category_id 

        payload ={
        'operationName':'items',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':filter ,
        'showForbiddenImage':False 
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('items')
        }
        })
        }

        r =account .request ('get',f"{account .base_url }/graphql",headers ,payload ).json ()
        return parser .item_profile_list (r ['data']['items'])

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
    sort_field :str ='createdAt',
    after_cursor :str |None =None 
    )->ReviewList :
        'Receives user feedback.\n\n        :param count: Number of reviews to receive (no more than 24 per request), _optional_.\n        :type count: `int`\n\n        :param status: Type of feedback to receive.\n        :type status: `playerokapi.enums.ReviewStatuses`\n\n        :param comment_required: Is a comment required in a review, _optional_.\n        :type comment_required: `bool`\n\n        :param rating: Review rating (1-5), _optional_.\n        :type rating: `int` or `None`\n\n        :param game_id: Review game ID, _optional_.\n        :type game_id: `str` or `None`\n\n        :param category_id: Review category ID, _optional_.\n        :type category_id: `str` or `None`\n\n        :param min_item_price: Minimum price of the review item, _optional_.\n        :type min_item_price: `bool` or `None`\n\n        :param max_item_price: Maximum price of the review item, _optional_.\n        :type max_item_price: `bool` or `None`\n\n        :param sort_direction: Sort type.\n        :type sort_direction: `playerokapi.enums.SortDirections`\n\n        :param sort_field: The field by which the sorting will be performed (by default `createdAt` - by date)\n        :type sort_field: `str`\n\n        :param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.\n        :type after_cursor: `str` or `None`\n        \n        :return: Reviews page.\n        :rtype: `PlayerokAPI.types.ReviewList`'
        from .account import get_account 
        account =get_account ()

        headers ={
        'Accept':'*/*',
        'Content-Type':'application/json',
        'Origin':account .base_url ,
        }

        filters ={'userId':self .id ,'status':[status .name ]if status else None }
        if comment_required is not None :
            filters ['hasComment']=comment_required 
        if game_id is not None :
            filters ['gameId']=game_id 
        if category_id is not None :
            filters ['categoryId']=category_id 
        if rating is not None :
            filters ['rating']=rating 
        if min_item_price is not None or max_item_price is not None :
            item_price ={}
            if min_item_price is not None :
                item_price ['min']=min_item_price 
            if max_item_price is not None :
                item_price ['max']=max_item_price 
            filters ['itemPrice']=item_price 
        payload ={
        'operationName':'testimonials',
        'variables':json .dumps ({
        'pagination':{
        'first':count ,
        'after':after_cursor 
        },
        'filter':filters ,
        'sort':{
        'direction':sort_direction .name if sort_direction else None ,
        'field':sort_field 
        }
        }),
        'extensions':json .dumps ({
        'persistedQuery':{
        'version':1 ,
        'sha256Hash':PERSISTED_QUERIES .get ('testimonials')
        }
        })
        }

        r =account .request ('get',f"{account .base_url }/graphql",headers ,payload ).json ()
        return parser .review_list (r ['data']['testimonials'])


class Event :
#TODO: Make an Event class

    def __init__ (self ):
        pass 


class ItemDeal :
    'A deal object with an item.\n\n    :param id: deal ID.\n    :type id: `str`\n\n    :param status: Status of the deal.\n    :type status: `playerokapi.enums.ItemDealStatuses`\n\n    :param status_expiration_date: Status expiration date.\n    :type status_expiration_date: `str` or `None`\n\n    :param status_description: Description of the deal status.\n    :type status_description: `str` or `None`\n\n    :param direction: Direction of the deal (buy/sell).\n    :type direction: `playerokapi.enums.ItemDealDirections`\n\n    :param obtaining: Receiving a deal.\n    :type obtaining: `str` or `None`\n\n    :param has_problem: Is there a problem in the transaction.\n    :type has_problem: `bool`\n\n    :param report_problem_enabled: Whether problem reporting is enabled.\n    :type report_problem_enabled: `bool` or `None`\n\n    :param completed_user: Profile of the user who confirmed the transaction.\n    :type completed_user: `playerokapi.types.UserProfile` or `None`\n\n    :param props: Deal details.\n    :type props: `str` or `None`\n\n    :param previous_status: Previous Status of the.\n    :type previous_status: `playerokapi.enums.ItemDealStatuses` or `None`\n\n    :param completed_at: Deal confirmation date.\n    :type completed_at: `str` or `None`\n\n    :param created_at: Date the deal was created.\n    :type created_at: `str` or `None`\n\n    :param logs: Deal logs.\n    :type logs: `list[playerokapi.types.ItemLog]` or `None`\n\n    :param transaction: Transaction deal.\n    :type transaction: `playerokapi.types.Transaction` or `None`\n\n    :param user: Profile of the user who made the transaction.\n    :type user: `playerokapi.types.UserProfile`\n\n    :param chat: Chat deal (only its ID is transmitted).\n    :type chat: `playerokapi.types.Chat` or `None`\n\n    :param item: Item deal.\n    :type item: `playerokapi.types.Item`\n\n    :param review: Review of the transaction.\n    :type review: `playerokapi.types.Review` or `None`\n\n    :param obtaining_fields: Receiving fields.\n    :type obtaining_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`\n\n    :param comment_from_buyer: Comment from the buyer.\n    :type comment_from_buyer: `str` or `None`'

    def __init__ (self ,id :str ,status :ItemDealStatuses ,status_expiration_date :str |None ,status_description :str |None ,
    direction :ItemDealDirections ,obtaining :str |None ,has_problem :bool ,report_problem_enabled :bool |None ,
    completed_user :UserProfile |None ,props :str |None ,previous_status :ItemDealStatuses |None ,
    completed_at :str ,created_at :str ,logs :list [ItemLog ]|None ,transaction :Transaction |None ,
    user :UserProfile ,chat :Chat |None ,item :Item ,review :Review |None ,obtaining_fields :list [GameCategoryDataField ]|None ,
    comment_from_buyer :str |None ):
        self .id :str =id 
        ' ID deal. '
        self .status :ItemDealStatuses =status 
        ' Status of the deal. '
        self .status_expiration_date :str |None =status_expiration_date 
        'Status expiration date.'
        self .status_description :str |None =status_description 
        'Description of the deal status.'
        self .direction :ItemDealDirections =direction 
        'Deal direction (buy/sell).'
        self .obtaining :str |None =obtaining 
        'Receiving a deal.'
        self .has_problem :bool =has_problem 
        'Is there a problem with the deal?'
        self .report_problem_enabled :bool |None =report_problem_enabled 
        'Is appealing the problem included?'
        self .completed_user :UserProfile |None =completed_user 
        'Profile of the user who confirmed the transaction.'
        self .props :str |None =props 
        'Details of the deal.'
        self .previous_status :ItemDealStatuses |None =previous_status 
        'Previous Status of the.'
        self .completed_at :str |None =completed_at 
        'Deal confirmation date.'
        self .created_at :str |None =created_at 
        'Deal creation date.'
        self .logs :list [ItemLog ]|None =logs 
        'Logi deal.'
        self .transaction :Transaction |None =transaction 
        'Transaction deal.'
        self .user :UserProfile =user 
        'Profile of the user who made the transaction.'
        self .chat :Chat |None =chat 
        'Chat deal (only his ID is transmitted).'
        self .item :Item =item 
        ' Item deal. '
        self .review :Review |None =review 
        'Feedback on the deal.'
        self .obtaining_fields :list [GameCategoryDataField ]|None =obtaining_fields 
        'The resulting fields.'
        self .comment_from_buyer :str |None =comment_from_buyer 
        'Comment from the buyer.'


class ItemDealPageInfo :
    'A subclass that describes information about the deals page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class ItemDealList :
    'A class that describes the reviews page.\n\n    :param deals: Page deals.\n    :type deals: `list[playerokapi.types.ItemDeal]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.ItemDealPageInfo`\n\n    :param total_count: Total transactions.\n    :type total_count: `int`'

    def __init__ (self ,deals :list [ItemDeal ],page_info :ItemDealPageInfo ,
    total_count :int ):
        self .deals :list [ItemDeal ]=deals 
        'Deals page.'
        self .page_info :ItemDealPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total transactions.'


class GameCategoryAgreement :
    'A subclass describing buyer agreements.\n\n    :param id: Agreement ID.\n    :type id: `str`\n\n    :param description: Description of the agreement.\n    :type description: `str`\n\n    :param icontype: Agreement icon type.\n    :type icontype: `playerokapi.enums.GameCategoryAgreementIconTypes`\n\n    :param sequence: Agreement sequence.\n    :type sequence: `str`'

    def __init__ (self ,id :str ,description :str ,
    icontype :GameCategoryAgreementIconTypes ,sequence :int ):
        self .id :str =id 
        'Agreement ID.'
        self .description :str =description 
        'Description of the agreement.'
        self .icontype :GameCategoryAgreementIconTypes =icontype 
        'Agreement icon type.'
        self .sequence :str =sequence 
        'Consistency of agreement.'


class GameCategoryAgreementPageInfo :
    'A subclass that describes information about the buyer agreements page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class GameCategoryAgreementList :
    'A class that describes the buyer agreements page.\n\n    :param agreements: Page agreements.\n    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.GameCategoryAgreementPageInfo`\n\n    :param total_count: Total agreements.\n    :type total_count: `int`'

    def __init__ (self ,agreements :list [GameCategoryAgreement ],page_info :GameCategoryAgreementPageInfo ,
    total_count :int ):
        self .agreements :list [GameCategoryAgreement ]=agreements 
        'Page conventions.'
        self .page_info :GameCategoryAgreementPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total agreements.'


class GameCategoryObtainingType :
    'A subclass that describes the type (method) of obtaining an item in a category.\n\n    :param id: Method ID.\n    :type id: `str`\n\n    :param name: Name of the method.\n    :type name: `str`\n\n    :param description: Description of the method.\n    :type description: `str`\n\n    :param game_category_id: Method game category ID.\n    :type game_category_id: `str`\n\n    :param no_comment_from_buyer: No comment from the buyer?\n    :type no_comment_from_buyer: `bool`\n\n    :param instruction_for_buyer: Instructions for the buyer.\n    :type instruction_for_buyer: `str`\n\n    :param instruction_for_seller: Instructions for the seller.\n    :type instruction_for_seller: `str`\n\n    :param sequence: Method sequence.\n    :type sequence: `int`\n\n    :param fee_multiplier: Commission multiplier.\n    :type fee_multiplier: `float`\n\n    :param agreements: Buyer to buy/seller to sell agreements.\n    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`\n\n    :param props: Category proportions.\n    :type props: `playerokapi.types.GameCategoryProps`'

    def __init__ (self ,id :str ,name :str ,description :str ,game_category_id :str ,no_comment_from_buyer :bool ,
    instruction_for_buyer :str |None ,instruction_for_seller :str |None ,sequence :int ,fee_multiplier :float ,
    agreements :list [GameCategoryAgreement ],props :GameCategoryProps ):
        self .id :str =id 
        'Method ID.'
        self .name :str =name 
        'Name of the method.'
        self .description :str =description 
        'Description of the method.'
        self .game_category_id :str =game_category_id 
        'Mode game category ID.'
        self .no_comment_from_buyer :bool =no_comment_from_buyer 
        'No comment from the buyer?'
        self .instruction_for_buyer :str |None =instruction_for_buyer 
        'Instructions for the buyer.'
        self .instruction_for_seller :str |None =instruction_for_seller 
        'Instructions for the seller.'
        self .sequence :int =sequence 
        'Sequence of method.'
        self .fee_multiplier :float =fee_multiplier 
        'Commission multiplier.'
        self .agreements :list [GameCategoryAgreement ]=agreements 
        'Buyer to buy/seller to sell agreements.'
        self .props :GameCategoryProps =props 
        'Category proportions.'


class GameCategoryObtainingTypePageInfo :
    'A subclass that describes information about the page of types (methods) of obtaining an item in a category.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class GameCategoryObtainingTypeList :
    'A class that describes a page of types (methods) of obtaining an item in a category.\n\n    :param obtaining_types: Page methods.\n    :type obtaining_types: `list[playerokapi.types.GameCategoryObtainingType]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.GameCategoryObtainingTypePageInfo`\n\n    :param total_count: Total ways.\n    :type total_count: `int`'

    def __init__ (self ,obtaining_types :list [GameCategoryObtainingType ],page_info :GameCategoryObtainingTypePageInfo ,
    total_count :int ):
        self .obtaining_types :list [GameCategoryObtainingType ]=obtaining_types 
        'Page conventions.'
        self .page_info :GameCategoryAgreementPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total ways.'


class GameCategoryDataField :
    "A subclass that describes the data fields for an item in a category (which are sent after purchase).\n\n    :param id: ID of the data field.\n    :type id: `str`\n\n    :param label: The label is the name of the field.\n    :type label: `str`\n\n    :param type: The type of the data field.\n    :type type: `playerokapi.enums.GameCategoryDataFieldTypes`\n\n    :param input_type: The type of the field's input value.\n    :type input_type: `playerokapi.enums.GameCategoryDataFieldInputTypes`\n\n    :param copyable: Whether the value can be copied from the field.\n    :type copyable: `bool`\n\n    :param hidden: Whether the data in the field is hidden.\n    :type hidden: `bool`\n\n    :param required: Is this field required?\n    :type required: `bool`\n\n    :param value: The value of the data in the field.\n    :type value: `str` or `None`"

    def __init__ (self ,id :str ,label :str ,type :GameCategoryDataFieldTypes ,
    input_type :GameCategoryDataFieldInputTypes ,copyable :bool ,
    hidden :bool ,required :bool ,value :str |None ):
        self .id :str =id 
        'ID of the data field.'
        self .label :str =label 
        'The inscription is the name of the field.'
        self .type :GameCategoryDataFieldTypes =type 
        'Data field type.'
        self .input_type :GameCategoryDataFieldInputTypes =input_type 
        'The type of field value to be entered.'
        self .copyable :bool =copyable 
        'Whether copying of a value from a field is allowed.'
        self .hidden :bool =hidden 
        'Is the data hidden in the field?'
        self .required :bool =required 
        'Is this field required?'
        self .value :str |None =value 
        'The value of the data in the field.'


class GameCategoryDataFieldPageInfo :
    'A subclass that describes information about the item data fields page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class GameCategoryDataFieldList :
    'A class that describes a page of fields with item data.\n\n    :param data_fields: Fields with data for an item in a category on the page.\n    :type data_fields: `list[playerokapi.types.GameCategoryDataField]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.GameCategoryDataFieldPageInfo`\n\n    :param total_count: Total data fields.\n    :type total_count: `int`'

    def __init__ (self ,data_fields :list [GameCategoryDataField ],
    page_info :GameCategoryDataFieldPageInfo ,total_count :int ):
        self .data_fields :list [GameCategoryDataField ]=data_fields 
        'Fields with data for an item in a category on the page.'
        self .page_info :GameCategoryDataFieldPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total data fields.'


class GameCategoryProps :
    'A subclass describing the proportions of a category.\n\n    :param min_reviews: Minimum number of reviews.\n    :type min_reviews: `int`\n\n    :param min_reviews_for_seller: Minimum number of reviews for a seller.\n    :type min_reviews_for_seller: `int`'

    def __init__ (self ,min_reviews :int ,min_reviews_for_seller :int ):
        self .min_reviews :int =min_reviews 
        'Minimum number of reviews.'
        self .min_reviews_for_seller :int =min_reviews_for_seller 
        'Minimum number of reviews for a seller.'


class GameCategoryOption :
    'A subclass describing a category option.\n\n    :param id: Option ID.\n    :type id: `str`\n\n    :param group: Option group.\n    :type group: `str`\n\n    :param label: The inscription is the name of the option.\n    :type label: `str`\n\n    :param type: Option type.\n    :type type: `playerokapi.enums.GameCategoryOptionTypes`\n\n    :param field: Field name (for payload request to the site).\n    :type field: `str`\n\n    :param value: Field value (for payload request to the site).\n    :type value: `str`\n\n    :param value_range_limit: Value range limit.\n    :type value_range_limit: `int` or `None`'

    def __init__ (self ,id :str ,group :str ,label :str ,type :GameCategoryOptionTypes ,
    field :str ,value :str ,value_range_limit :int |None ):
        self .id :str =id 
        'ID options.'
        self .group :str =group 
        'Option group.'
        self .label :str =label 
        'The inscription is the name of the option.'
        self .type :GameCategoryOptionTypes =type 
        'Type options.'
        self .field :str =field 
        'Field name (for payload request to the site).'
        self .value :str =value 
        'Field value (for payload request to the site).'
        self .value_range_limit :int |None =value_range_limit 
        'Value spread limit.'


class GameCategoryInstruction :
    'A subclass that describes information about the sales/purchase instructions page in a category.\n\n    :param id: Instruction ID.\n    :type id: `str`\n\n    :param text: Instruction text.\n    :type text: `str`'

    def __init__ (self ,id :str ,text :str ):
        self .id :str =id 
        'Instruction ID.'
        self .text :str =text 
        'Instruction text.'


class GameCategoryInstructionPageInfo :
    'A subclass that describes instructions for selling/purchasing in a category.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class GameCategoryInstructionList :
    'A class that describes a page of instructions for selling/purchasing in a category.\n\n    :param instructions: Page instructions.\n    :type instructions: `list[playerokapi.types.GameCategoryInstruction]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.GameCategoryInstructionPageInfo`\n\n    :param total_count: Total instructions.\n    :type total_count: `int`'

    def __init__ (self ,instructions :list [GameCategoryInstruction ],page_info :GameCategoryInstructionPageInfo ,
    total_count :int ):
        self .instructions :list [GameCategoryInstruction ]=instructions 
        'Page conventions.'
        self .page_info :GameCategoryInstructionPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total instructions.'


class GameCategory :
    'Game/application category object.\n\n    :param id: Category ID.\n    :type id: `str`\n\n    :param slug: Category page name.\n    :type slug: `str`\n\n    :param name: Category name.\n    :type name: `str`\n\n    :param category_id: ID of the parent category.\n    :type category_id: `str` or `None`\n\n    :param game_id: Category game ID.\n    :type game_id: `str` or `None`\n\n    :param obtaining: Receiving type.\n    :type obtaining: `str` or `None` or `None`\n\n    :param options: Category options.\n    :type options: `list[playerokapi.types.GameCategoryOption]` or `None`\n\n    :param props: Category proportions.\n    :type props: `playerokapi.types.GameCategoryProps` or `None`\n\n    :param no_comment_from_buyer: No comment from the buyer?\n    :type no_comment_from_buyer: `bool` or `None`\n\n    :param instruction_for_buyer: Instructions for the buyer.\n    :type instruction_for_buyer: `str` or `None`\n\n    :param instruction_for_seller: Instructions for the seller.\n    :type instruction_for_seller: `str` or `None`\n\n    :param use_custom_obtaining: Whether custom obtaining is used.\n    :type use_custom_obtaining: `bool`\n\n    :param auto_confirm_period: Auto-confirmation period for deal of this category.\n    :type auto_confirm_period: `playerokapi.enums.GameCategoryAutoConfirmPeriods` or `None`\n\n    :param auto_moderation_mode: Whether automatic moderation is enabled.\n    :type auto_moderation_mode: `bool` or `None`\n\n    :param agreements: Buyer agreements.\n    :type agreements: `list[playerokapi.types.GameCategoryAgreement]` or `None`\n\n    :param fee_multiplier: Commission multiplier.\n    :type fee_multiplier: `float` or `None`'

    def __init__ (self ,id :str ,slug :str ,name :str ,category_id :str |None ,game_id :str |None ,
    obtaining :str |None ,options :list [GameCategoryOption ]|None ,props :GameCategoryProps |None ,
    no_comment_from_buyer :bool |None ,instruction_for_buyer :str |None ,instruction_for_seller :str |None ,
    use_custom_obtaining :bool ,auto_confirm_period :GameCategoryAutoConfirmPeriods |None ,
    auto_moderation_mode :bool |None ,agreements :list [GameCategoryAgreement ]|None ,fee_multiplier :float |None ):
        self .id :str =id 
        'Category ID.'
        self .slug :str =slug 
        'The name of the category page.'
        self .name :str =name 
        'Category name.'
        self .category_id :str |None =category_id 
        'ID of the parent category.'
        self .game_id :str |None =game_id 
        'Category game ID.'
        self .obtaining :str |None =obtaining 
        'Receipt type.'
        self .options :list [GameCategoryOption ]|None =options 
        'Category options.'
        self .props :str |None =props 
        'Category proportions.'
        self .no_comment_from_buyer :bool |None =no_comment_from_buyer 
        'No comment from the buyer?'
        self .instruction_for_buyer :str |None =instruction_for_buyer 
        'Instructions for the buyer.'
        self .instruction_for_seller :str |None =instruction_for_seller 
        'Instructions for the seller.'
        self .use_custom_obtaining :bool =use_custom_obtaining 
        'Is custom receiving used?'
        self .auto_confirm_period :GameCategoryAutoConfirmPeriods |None =auto_confirm_period 
        'The period of auto-confirmation deal of this category.'
        self .auto_moderation_mode :bool |None =auto_moderation_mode 
        'Is automatic moderation enabled?'
        self .agreements :list [GameCategoryAgreement ]|None =agreements 
        'Buyer agreements.'
        self .fee_multiplier :float |None =fee_multiplier 
        'Commission multiplier.'


class Game :
    'Game/application object.\n\n    :param id: Game/application ID.\n    :type id: `str`\n\n    :param slug: Game/application page name.\n    :type slug: `str`\n\n    :param name: Name of the game/application.\n    :type name: `str`\n\n    :param type: Type: game or application.\n    :type type: `playerokapi.enums.GameTypes`\n\n    :param logo: Game/application logo.\n    :type logo: `playerokapi.types.FileObject`\n\n    :param banner: Game/application banner.\n    :type banner: `FileObject`\n\n    :param categories: List of game/application categories.\n    :type categories: `list[playerokapi.types.GameCategory]`\n\n    :param created_at: Creation date.\n    :type created_at: `str`'

    def __init__ (self ,id :str ,slug :str ,name :str ,type :GameTypes ,
    logo :FileObject ,banner :FileObject ,categories :list [GameCategory ],
    created_at :str ):
        self .id :str =id 
        'Game/application ID.'
        self .slug :str =slug 
        'Game/application page name.'
        self .name :str =name 
        'Name of the game/application.'
        self .type :GameTypes =type 
        'Type: game or application.'
        self .logo :FileObject =logo 
        'Game/application logo.'
        self .banner :FileObject =banner 
        'Game/application banner.'
        self .categories :list [GameCategory ]=categories 
        'List of game/application categories.'
        self .created_at :str =created_at 
        'Creation date.'


class GameProfile :
    'Game/application profile.\n\n    :param id: Game/application ID.\n    :type id: `str`\n\n    :param slug: Game/application page name.\n    :type slug: `str`\n\n    :param name: Name of the game/application.\n    :type name: `str`\n\n    :param type: Type: game or application.\n    :type type: `playerokapi.types.GameTypes`\n\n    :param logo: Game/application logo.\n    :type logo: `playerokapi.types.FileObject`'

    def __init__ (self ,id :str ,slug :str ,name :str ,
    type :GameTypes ,logo :FileObject ):
        self .id :str =id 
        'Game/application ID.'
        self .slug :str =slug 
        'Game/application page name.'
        self .name :str =name 
        'Name of the game/application.'
        self .type :GameTypes =id 
        'Type: game or application.'
        self .logo :FileObject =logo 
        'Game/application logo.'


class GamePageInfo :
    'A subclass that describes information about the games page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class GameList :
    'A class describing the games page.\n\n    :param games: Games/applications pages.\n    :type games: `list[playerokapi.types.Game]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.ChatPageInfo`\n\n    :param total_count: Total games.\n    :type total_count: `int`'

    def __init__ (self ,games :list [Game ],page_info :GamePageInfo ,
    total_count :int ):
        self .games :list [Game ]=games 
        'Games/applications pages.'
        self .page_info :ChatPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total games.'


class ItemPriorityStatusPriceRange :
    'A subclass that describes the price range of an item suitable for the definition. priority status.\n\n    :param min: Minimum price of the item.\n    :type min: `int`\n\n    :param max: Maximum price of an item.\n    :type max: `int`'

    def __init__ (self ,min :int ,max :str ):
        self .min :int =min 
        'Minimum price of an item (in rubles).'
        self .max :int =max 
        'Maximum price of an item (in rubles).'


class ItemPriorityStatus :
    "A class describing the Status of the item's priority.\n\n    :param id: Priority status ID.\n    :type id: `str`\n\n    :param price: Status price (in rubles).\n    :type price: `int`\n\n    :param name: Name of the status.\n    :type name: `str`\n\n    :param type: Status type.\n    :type type: `playerokapi.enums.PriorityTypes`\n\n    :param period: Duration of the status (in days).\n    :type period: `str`\n\n    :param price_range: Price range of the status item.\n    :type price_range: `playerokapi.types.ItemPriorityStatusPriceRange`"

    def __init__ (self ,id :str ,price :int ,name :str ,type :PriorityTypes ,
    period :int ,price_range :ItemPriorityStatusPriceRange ):
        self .id :str =id 
        'Priority Status ID.'
        self .price :int =price 
        'Status price (in rubles).'
        self .name :str =name 
        'Status name.'
        self .type :PriorityTypes =type 
        'Status type.'
        self .period :int =period 
        'Duration of status (in days).'
        self .price_range :ItemPriorityStatusPriceRange =price_range 
        'Price range of a status item.'


class ItemLog :
    'A subclass that describes an action log with an item.\n    \n    :param id: Log ID.\n    :type id: `str`\n    \n    :param event: Log event.\n    :type event: `playerokapi.enums.ItemLogEvents`\n    \n    :param created_at: Log creation date.\n    :type created_at: `str`\n    \n    :param user: Profile of the user who made the log.\n    :type user: `playerokapi.types.UserProfile`'

    def __init__ (self ,id :str ,event :ItemLogEvents ,created_at :str ,
    user :UserProfile ):
        self .id :str =id 
        'Logo ID.'
        self .event :ItemLogEvents =event 
        'Log event.'
        self .created_at :str =created_at 
        'Log creation date.'
        self .user :UserProfile =user 
        'Profile of the user who made the log.'


class Item :
    'Item object.\n\n    :param id: Item ID.\n    :type id: `str`\n\n    :param name: Name of the item.\n    :type name: `str`\n\n    :param description: Description of the item.\n    :type description: `str`\n\n    :param status: Status of the item.\n    :type status: `playerokapi.enums.ItemStatuses`\n\n    :param obtaining_type: Method of obtaining.\n    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`\n\n    :param price: The price of the item.\n    :type price: `int`\n\n    :param raw_price: Price excluding discount.\n    :type raw_price: `int`\n\n    :param priority_position: Priority position.\n    :type priority_position: `int`\n\n    :param attachments: Attachment files.\n    :type attachments: `list[playerokapi.types.FileObject]`\n\n    :param attributes: Item attributes.\n    :type attributes: `dict`\n\n    :param category: Game category of the item.\n    :type category: `playerokapi.types.GameCategory`\n\n    :param comment: Comment on the item.\n    :type comment: `str` or `None`\n\n    :param data_fields: Item data fields.\n    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`\n\n    :param fee_multiplier: Commission multiplier.\n    :type fee_multiplier: `float`\n\n    :param game: Game profile of the item.\n    :type game: `playerokapi.types.GameProfile`\n\n    :param seller_type: Seller type.\n    :type seller_type: `playerokapi.enums.UserTypes`\n\n    :param slug: Item page name.\n    :type slug: `str`\n\n    :param user: Seller profile.\n    :type user: `playerokapi.types.UserProfile`'

    def __init__ (self ,id :str ,slug :str ,name :str ,description :str ,obtaining_type :GameCategoryObtainingType |None ,price :int ,raw_price :int ,priority_position :int ,
    attachments :list [FileObject ],attributes :dict ,category :GameCategory ,comment :str |None ,data_fields :list [GameCategoryDataField ]|None ,
    fee_multiplier :float ,game :GameProfile ,seller_type :UserTypes ,status :ItemStatuses ,user :UserProfile ):
        self .id :str =id 
        'Item ID.'
        self .slug :str =slug 
        'Item page name.'
        self .name :str =name 
        'Title of the subject.'
        self .description :str =description 
        'Description of the item.'
        self .obtaining_type :GameCategoryObtainingType |None =obtaining_type 
        'Method of receipt.'
        self .price :int =price 
        'Price the item.'
        self .raw_price :int =raw_price 
        'Price excluding discount.'
        self .priority_position :int =priority_position 
        'Priority position.'
        self .attachments :list [FileObject ]=attachments 
        'Application files.'
        self .attributes :dict =attributes 
        'Item attributes.'
        self .category :GameCategory =category 
        'Game category of the item.'
        self .comment :str |None =comment 
        'Item comment.'
        self .data_fields :list [GameCategoryDataField ]|None =data_fields 
        'Item data fields.'
        self .fee_multiplier :float =fee_multiplier 
        'Commission multiplier.'
        self .game :GameProfile =game 
        'Item game profile.'
        self .seller_type :UserTypes =seller_type 
        'Seller type.'
        self .slug :str =slug 
        'Item page name.'
        self .status :ItemStatuses =status 
        'Status of the case.'
        self .user :UserProfile =user 
        'Seller profile.'


class MyItem :
    "The object of its subject.\n\n    :param id: Item ID.\n    :type id: `str`\n\n    :param slug: Item page name.\n    :type slug: `str`\n\n    :param name: Name of the item.\n    :type name: `str`\n\n    :param description: Description of the item.\n    :type description: `str`\n\n    :param status: Status of the item.\n    :type status: `playerokapi.enums.ItemStatuses`\n\n    :param obtaining_type: Method of obtaining.\n    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`\n\n    :param price: The price of the item.\n    :type price: `int`\n\n    :param prev_price: Previous price.\n    :type prev_price: `int`\n\n    :param raw_price: Price excluding discount.\n    :type raw_price: `int`\n\n    :param priority_position: Priority position.\n    :type priority_position: `int`\n\n    :param attachments: Attachment files.\n    :type attachments: `list[playerokapi.types.FileObject]`\n\n    :param attributes: Item attributes.\n    :type attributes: `dict`\n\n    :param category: Game category of the item.\n    :type category: `playerokapi.types.GameCategory`\n\n    :param comment: Comment on the item.\n    :type comment: `str` or `None`\n\n    :param data_fields: Item data fields.\n    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`\n\n    :param fee_multiplier: Commission multiplier.\n    :type fee_multiplier: `float`\n\n    :param prev_fee_multiplier: Previous commission multiplier.\n    :type prev_fee_multiplier: `float`\n\n    :param seller_notified_about_fee_change: Whether the seller is notified about the change in commission.\n    :type seller_notified_about_fee_change: `bool`\n\n    :param game: Game profile of the item.\n    :type game: `playerokapi.types.GameProfile`\n\n    :param seller_type: Seller type.\n    :type seller_type: `playerokapi.enums.UserTypes`\n\n    :param user: Seller profile.\n    :type user: `playerokapi.types.UserProfile`\n\n    :param buyer: Seller profile.\n    :type user: `playerokapi.types.UserProfile`\n\n    :param priority: Status of the priority of the item.\n    :type priority: `playerokapi.types.PriorityTypes`\n\n    :param priority_price: Priority status prices.\n    :type priority_price: `int`\n\n    :param sequence: Position of the item in the user's product table.\n    :type sequence: `int` or `None`\n\n    :param status_expiration_date: Priority status expiration date.\n    :type status_expiration_date: `str` or `None`\n\n    :param status_description: Description of the priority status.\n    :type status_description: `str` or `None`\n\n    :param status_payment: Payment status (transaction).\n    :type status_payment: `playerokapi.types.Transaction` or `None`\n\n    :param views_counter: Number of views of the item.\n    :type views_counter: `int`\n\n    :param is_editable: Is it possible to edit the product.\n    :type is_editable: `bool`\n\n    :param approval_date: Product publication date.\n    :type approval_date: `str` or `None`\n\n    :param deleted_at: Date the product was deleted.\n    :type deleted_at: `str` or `None`\n\n    :param updated_at: Date the product was last updated.\n    :type updated_at: `str` or `None`\n\n    :param created_at: Product creation date.\n    :type created_at: `str` or `None`"

    def __init__ (self ,id :str ,slug :str ,name :str ,description :str ,obtaining_type :GameCategoryObtainingType |None ,price :int ,raw_price :int ,priority_position :int ,
    attachments :list [FileObject ],attributes :dict ,buyer :UserProfile ,category :GameCategory ,comment :str |None ,
    data_fields :list [GameCategoryDataField ]|None ,fee_multiplier :float ,game :GameProfile ,seller_type :UserTypes ,status :ItemStatuses ,
    user :UserProfile ,prev_price :int ,prev_fee_multiplier :float ,seller_notified_about_fee_change :bool ,
    priority :PriorityTypes ,priority_price :int ,sequence :int |None ,status_expiration_date :str |None ,status_description :str |None ,
    status_payment :Transaction |None ,views_counter :int ,is_editable :bool ,approval_date :str |None ,deleted_at :str |None ,
    updated_at :str |None ,created_at :str |None ):
        self .id :str =id 
        'Item ID.'
        self .slug :str =slug 
        'Item page name.'
        self .name :str =name 
        'Title of the subject.'
        self .status :ItemStatuses =status 
        'Status of the case.'
        self .description :str =description 
        'Description of the item.'
        self .obtaining_type :GameCategoryObtainingType |None =obtaining_type 
        'Method of receipt.'
        self .price :int =price 
        'Price the item.'
        self .prev_price :int =prev_price 
        'Previous price.'
        self .raw_price :int =raw_price 
        'Price excluding discount.'
        self .priority_position :int =priority_position 
        'Priority position.'
        self .attachments :list [FileObject ]=attachments 
        'Application files.'
        self .attributes :dict =attributes 
        'Item attributes.'
        self .category :GameCategory =category 
        'Game category of the item.'
        self .comment :str |None =comment 
        'Item comment.'
        self .data_fields :list [GameCategoryDataField ]|None =data_fields 
        'Item data fields.'
        self .fee_multiplier :float =fee_multiplier 
        'Commission multiplier.'
        self .prev_fee_multiplier :float =prev_fee_multiplier 
        'Previous commission multiplier.'
        self .seller_notified_about_fee_change :bool =seller_notified_about_fee_change 
        'Has the seller been notified of the commission change?'
        self .game :GameProfile =game 
        'Item game profile.'
        self .seller_type :UserTypes =seller_type 
        'Seller type.'
        self .user :UserProfile =user 
        'Seller profile.'
        self .buyer :UserProfile =buyer 
        'Buyer profile of the item (if sold).'
        self .priority :PriorityTypes =priority 
        'Status of the priority of the case.'
        self .priority_price :int =priority_price 
        'Priority status prices.'
        self .sequence :int |None =sequence 
        "The item's position in the users' product table."
        self .status_expiration_date :str |None =status_expiration_date 
        'Priority status expiration date.'
        self .status_description :str |None =status_description 
        'Description of the priority status.'
        self .status_payment :str |None =status_payment 
        'Payment status (transaction).'
        self .views_counter :int =views_counter 
        'Number of views of the item.'
        self .is_editable :bool =is_editable 
        'Is it possible to edit a product?'
        self .approval_date :str |None =approval_date 
        'Product publication date.'
        self .deleted_at :str |None =deleted_at 
        'Date the item was removed.'
        self .updated_at :str |None =updated_at 
        'Date the product was last updated.'
        self .created_at :str |None =created_at 
        'Product creation date.'


class ItemProfile :
    'Item profile.\n\n    :param id: Item ID.\n    :type id: `str`\n\n    :param slug: Item page name.\n    :type slug: `str`\n\n    :param priority: Item priority.\n    :type priority: `playerokapi.enums.PriorityTypes`\n\n    :param status: Status of the item.\n    :type status: `playerokapi.enums.ItemStatuses`\n\n    :param name: Name of the item.\n    :type name: `str`\n\n    :param price: The price of the item.\n    :type price: `int`\n\n    :param raw_price: Price excluding discount.\n    :type raw_price: `int`\n\n    :param seller_type: Seller type.\n    :type seller_type: `playerokapi.enums.UserTypes`\n\n    :param attachment: File attachment.\n    :type attachment: `playerokapi.types.FileObject`\n\n    :param user: Seller profile.\n    :type user: `playerokapi.types.UserProfile`\n\n    :param approval_date: Approval date.\n    :type approval_date: `str`\n\n    :param priority_position: Priority position.\n    :type priority_position: `int`\n\n    :param views_counter: Number of views.\n    :type views_counter: `int` or `None`\n\n    :param fee_multiplier: Commission multiplier.\n    :type fee_multiplier: `float`\n\n    :param created_at: Creation date.\n    :type created_at: `str`'

    def __init__ (self ,id :str ,slug :str ,priority :PriorityTypes ,status :ItemStatuses ,
    name :str ,price :int ,raw_price :int ,seller_type :UserTypes ,attachment :FileObject ,
    user :UserProfile ,approval_date :str ,priority_position :int ,views_counter :int |None ,
    fee_multiplier :float ,created_at :str ):
        self .id :str =id 
        'Item ID.'
        self .slug :str =slug 
        'Item page name.'
        self .priority :PriorityTypes =priority 
        'Item priority.'
        self .status :ItemStatuses =status 
        'Status of the case.'
        self .name :str =name 
        'Title of the subject.'
        self .price :int =price 
        'Price the item.'
        self .raw_price :int =raw_price 
        'Price excluding discount.'
        self .seller_type :UserTypes =seller_type 
        'Seller type.'
        self .attachment :FileObject =attachment 
        'File attachment.'
        self .user :UserProfile =user 
        'Seller profile.'
        self .approval_date :str =approval_date 
        'Date of approvals.'
        self .priority_position :int =priority_position 
        'Priority position.'
        self .views_counter :int |None =views_counter 
        'Number of views.'
        self .fee_multiplier :float =fee_multiplier 
        'Commission multiplier.'
        self .created_at :str =created_at 
        'Creation date.'


class ItemProfilePageInfo :
    'A subclass that describes information about the items page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class ItemProfileList :
    'Items page profile.\n\n    :param items: Page items.\n    :type items: `list[playerokapi.types.Item]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.ItemProfilePageInfo`\n\n    :param total_count: Total items.\n    :type total_count: `int`'

    def __init__ (self ,items :list [ItemProfile ],page_info :ItemProfilePageInfo ,
    total_count :int ):
        self .items :list [ItemProfile ]=items 
        'Page items.'
        self .page_info :ItemProfilePageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total items.'


class SBPBankMember :
    'Object of SBP Bank members.\n\n    :param id: ID.\n    :type id: `str`\n\n    :param name: Name.\n    :type name: `str`\n\n    :param icon: URL of the icon.\n    :type icon: `str`'

    def __init__ (self ,id :str ,name :str ,icon :str ):
        self .id :str =id 
        ' ID. '
        self .name :str =name 
        'Name.'
        self .icon :str =icon 
        'Icon URL.'


class TransactionPaymentMethod :
    'Payment method of the transaction.\n\n    :param id: Method ID.\n    :type id: `playerokapi.types.TransactionPaymentMethodIds`\n\n    :param name: Name of the method.\n    :type name: `str`\n\n    :param fee: Method commission.\n    :type fee: `int`\n\n    :param provider_id: ID of the transaction provider.\n    :type provider_id: `playerokapi.types.TransactionProviderIds`\n\n    :param account: Method account (?).\n    :type account: `AccountProfile` or `None`\n\n    :param props: Transaction provider parameters.\n    :type props: `playerokapi.types.TransactionProviderProps`\n\n    :param limits: Transaction provider limits.\n    :type limits: `playerokapi.types.TransactionProviderLimits`'

    def __init__ (self ,id :TransactionPaymentMethodIds ,name :str ,fee :int ,provider_id :TransactionProviderIds ,
    account :AccountProfile |None ,props :TransactionProviderProps ,limits :TransactionProviderLimits ):
        self .id :TransactionPaymentMethodIds =id 
        'Method ID.'
        self .name :str =name 
        'Method name.'
        self .fee :int =fee 
        'Commission method.'
        self .provider_id :TransactionProviderIds =provider_id 
        'Transaction provider ID.'
        self .account :AccountProfile |None =account 
        'Method account (?).'
        self .props :TransactionProviderProps =props 
        'Transaction provider parameters.'
        self .limits :TransactionProviderLimits =limits 
        'Transaction provider limits.'


class TransactionProviderLimitRange :
    'Transaction provider limit range.\n\n    :param min: Minimum Price (in rubles).\n    :type min: `int`\n\n    :param max: Maximum Price (in rubles).\n    :type max: `int`'

    def __init__ (self ,min :int ,max :int ):
        self .min :int =min 
        'Minimum Price (in rubles).'
        self .max :int =max 
        'Maximum Price (in rubles).'


class TransactionProviderLimits :
    'Transaction provider limits.\n\n    :param incoming: For replenishment.\n    :type incoming: `playerokapi.types.TransactionProviderLimitRange`\n\n    :param outgoing: To output.\n    :type outgoing: `playerokapi.types.TransactionProviderLimitRange`'

    def __init__ (self ,incoming :TransactionProviderLimitRange ,outgoing :TransactionProviderLimitRange ):
        self .incoming :TransactionProviderLimitRange =incoming 
        'For replenishment.'
        self .outgoing :TransactionProviderLimitRange =outgoing 
        'To the conclusion.'


class TransactionProviderRequiredUserData :
    'Required transaction provider user data.\n\n    :param email: Is it necessary to specify EMail?\n    :type email: `bool`\n\n    :param phone_number: Is it necessary to indicate a phone number?\n    :type phone_number: `bool`\n\n    :param erip_account_number: Is it necessary to indicate the ERIP account number?\n    :type erip_account_number: `bool` or `None`'

    def __init__ (self ,email :bool ,phone_number :bool ,
    erip_account_number :bool |None ):
        self .email :bool =email 
        'Is it necessary to indicate EMail?'
        self .phone_number :bool =phone_number 
        'Is it necessary to provide a phone number?'
        self .erip_account_number :bool |None =erip_account_number 
        'Is it mandatory to specify the ERIP account number?'


class TransactionProviderProps :
    'Transaction provider parameters.\n\n    :param required_user_data: Required user data.\n    :type required_user_data: `playerokapi.types.TransactionProviderRequiredUserData`\n\n    :param tooltip: Hint.\n    :type tooltip: `str` or `None`'

    def __init__ (self ,required_user_data :TransactionProviderRequiredUserData ,
    tooltip :str |None ):
        self .required_user_data :TransactionProviderRequiredUserData =required_user_data 
        'Required user data.'
        self .tooltip :str |None =tooltip 
        'Clue.'


class TransactionProvider :
    'Transaction provider object.\n\n    :param id: Provider ID.\n    :type id: `playerokapi.enums.TransactionProviderIds`\n\n    :param name: Provider name.\n    :type name: `str`\n\n    :param fee: Provider commission.\n    :type fee: `int`\n\n    :param min_fee_amount: Minimum commission.\n    :type min_fee_amount: `int` or `None`\n\n    :param description: Description of the provider.\n    :type description: `str` or `None`\n\n    :param account: Provider account (?).\n    :type account: `playerokapi.types.AccountProfile` or `None`\n\n    :param props: Provider parameters.\n    :type props: `playerokapi.types.TransactionProviderProps`\n\n    :param limits: Provider limits.\n    :type limits: `playerokapi.types.TransactionProviderLimits`\n\n    :param payment_methods: Payment methods.\n    :type payment_methods: `list` of `playerokapi.types.TransactionPaymentMethod`'

    def __init__ (self ,id :TransactionProviderIds ,name :str ,fee :int ,min_fee_amount :int |None ,
    description :str |None ,account :AccountProfile |None ,props :TransactionProviderProps ,
    limits :TransactionProviderLimits ,payment_methods :list [TransactionPaymentMethod ]):
        self .id :TransactionProviderIds =id 
        'Provider ID.'
        self .name :str =name 
        'Provider name.'
        self .fee :int =fee 
        'Provider commission.'
        self .min_fee_amount :int |None =min_fee_amount 
        'Minimum commission.'
        self .description :str |None =description 
        'Provider description.'
        self .account :AccountProfile |None =account 
        'Provider account (?).'
        self .props :TransactionProviderProps =props 
        'Provider settings.'
        self .limits :TransactionProviderLimits =limits 
        'Provider limits.'
        self .payment_methods :list [TransactionPaymentMethod ]=payment_methods 
        'Payment methods.'


class Transaction :
    'Transaction object.\n\n    :param id: Transaction ID.\n    :type id: `str`\n\n    :param operation: Type of operation performed.\n    :type operation: `playerokapi.enums.TransactionOperations`\n\n    :param direction: Transaction direction.\n    :type direction: `playerokapi.enums.TransactionDirections`\n\n    :param provider_id: Payment provider ID.\n    :type provider_id: `playerokapi.enums.TransactionProviderIds`\n\n    :param provider: Transaction provider object.\n    :type provider: `playerokapi.types.TransactionProvider`\n\n    :param user: Transaction user object.\n    :type user: `playerokapi.types.UserProfile`\n\n    :param creator: Object of the user who created the transaction.\n    :type creator: `playerokapi.types.UserProfile` or `None`\n\n    :param status: Status of the transaction processing.\n    :type status: `playerokapi.enums.TransactionStatuses`\n\n    :param status_description: Description of the status.\n    :type status_description: `str` or `None`\n\n    :param status_expiration_date: Status expiration date.\n    :type status_expiration_date: `str` or `None`\n\n    :param value: Price of the transaction.\n    :type value: `int`\n\n    :param fee: Transaction commission.\n    :type fee: `int`\n\n    :param created_at: Date the transaction was created.\n    :type created_at: `str`\n\n    :param verified_at: Transaction confirmation date.\n    :type verified_at: `str` or `None`\n\n    :param verified_by: Object of the user who confirmed the transaction.\n    :type verified_by: `playerokapi.types.UserProfile` or `None`\n\n    :param completed_at: The date the transaction was completed.\n    :type completed_at: `str` or `None`\n\n    :param completed_by: Object of the user who completed the transaction.\n    :type completed_by: `playerokapi.types.UserProfile` or `None`\n\n    :param payment_method_id: Payment method ID.\n    :type payment_method_id: `str` or `None`\n\n    :param is_suspicious: Is the transaction suspicious?\n    :type is_suspicious: `bool` or `None`\n\n    :param sbp_bank_name: SBP bank name (if the transaction was made using SBP).\n    :type sbp_bank_name: `str` or `None`'

    def __init__ (self ,id :str ,operation :TransactionOperations ,direction :TransactionDirections ,provider_id :TransactionProviderIds ,
    provider :TransactionProvider ,user :UserProfile ,creator :UserProfile ,status :TransactionStatuses ,status_description :str |None ,
    status_expiration_date :str |None ,value :int ,fee :int ,created_at :str ,verified_at :str |None ,verified_by :UserProfile |None ,
    completed_at :str |None ,completed_by :UserProfile |None ,payment_method_id :str |None ,is_suspicious :bool |None ,sbp_bank_name :str |None ):
        self .id :str =id 
        'Transaction ID.'
        self .operation :TransactionOperations =operation 
        'The type of operation performed.'
        self .direction :TransactionDirections =direction 
        'Transaction direction.'
        self .provider_id :TransactionProviderIds =provider_id 
        'Payment provider ID.'
        self .provider :TransactionProvider =provider 
        'Transaction provider object.'
        self .user :UserProfile =user 
        'Transaction user object.'
        self .creator :UserProfile |None =creator 
        'Transaction creator user object.'
        self .status :TransactionStatuses =status 
        'Status of the transaction processing.'
        self .status_description :str |None =status_description 
        'Description of the status.'
        self .status_expiration_date :str |None =status_expiration_date 
        'Status expiration date.'
        self .value :int =value 
        'Price transaction.'
        self .fee :int =fee 
        'Transaction fee.'
        self .created_at :str =created_at 
        'The date the transaction was created.'
        self .verified_at :str |None =verified_at 
        'Transaction confirmation date.'
        self .verified_by :UserProfile |None =verified_by 
        'An object of the user who confirmed the transaction.'
        self .completed_at :str |None =completed_at 
        'The date the transaction was executed.'
        self .completed_by :UserProfile |None =completed_by 
        'An object of the user who performed the transaction.'
        self .payment_method_id :str |None =payment_method_id 
        'Payment method ID.'
        self .is_suspicious :bool |None =is_suspicious 
        'Is the transaction suspicious?'
        self .sbp_bank_name :str |None =sbp_bank_name 
        'SBP bank name (if the transaction was made using SBP).'


class TransactionPageInfo :
    'A subclass that describes transaction page information.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class TransactionList :
    'A class that describes a chat message page.\n\n    :param transactions: Page transactions.\n    :type transactions: `list[playerokapi.types.Transaction]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.TransactionPageInfo`\n\n    :param total_count: Total transactions on the page.\n    :type total_count: `int`'

    def __init__ (self ,transactions :list [Transaction ],page_info :TransactionPageInfo ,
    total_count :int ):
        self .transactions :list [Transaction ]=transactions 
        'Page transactions.'
        self .page_info :TransactionPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total transactions per page.'


class UserBankCard :
    "User's bank card object.\n\n    :param id: Card ID.\n    :type id: `str`\n\n    :param card_first_six: The first six digits of the card.\n    :type card_first_six: `str`\n\n    :param card_last_four: Last four digits of the card.\n    :type card_last_four: `str`\n\n    :param card_type: Bank card type.\n    :card_type: `playerokapi.enums.BankCardTypes`\n\n    :param is_chosen: Is this map selected as the default?\n    :type is_chosen: `bool`"

    def __init__ (self ,id :str ,card_first_six :str ,card_last_four :str ,
    card_type :BankCardTypes ,is_chosen :bool ):
        self .id :str =id 
        'ID card.'
        self .card_first_six :str =card_first_six 
        'The first six digits of the card.'
        self .card_last_four :str =card_last_four 
        'Last four digits of the card.'
        self .card_type :BankCardTypes =card_type 
        'Bank card type.'
        self .is_chosen :bool =is_chosen 
        'Is this card selected as the default?'


class UserBankCardPageInfo :
    "A subclass that describes information about the user's bank cards page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`"

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class UserBankCardList :
    "A class describing the user's bank cards page.\n\n    :param bank_cards: Bank cards page.\n    :type bank_cards: `list[playerokapi.types.UserBankCard]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.UserBankCardPageInfo`\n\n    :param total_count: Total bank cards on the page.\n    :type total_count: `int`"

    def __init__ (self ,bank_cards :list [UserBankCard ],
    page_info :UserBankCardPageInfo ,total_count :int ):
        self .bank_cards :list [UserBankCard ]=bank_cards 
        'Bank cards page.'
        self .page_info :UserBankCardPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total bank cards on the page.'


class Moderator :
# TODO: Make a moderator class Moderator

    def __init__ (self ):
        pass 


class TemporaryAttachmentUploadOutput :
    'Output for downloading temporary attachment\n    (image attached to post).\n\n    :param id: Data ID.\n    :type id: `str`\n\n    :param url: Image URL.\n    :type url: `str`\n\n    :param chat_id: ID of the chat where the image is sent.\n    :type chat_id: `str`\n\n    :param client_attachment_id: ID of the client attachment file.\n    :type client_attachment_id: `str`\n\n    :param expires_at: Expiration date.\n    :type expires_at: `str`'

    def __init__ (self ,id :str ,url :str ,chat_id :str ,
    client_attachment_id :str ,expires_at :str ):
        self .id :str =id 
        'Data ID.'
        self .url :str =id 
        'Image URL.'
        self .chat_id :str =id 
        'ID of the chat where the image is sent.'
        self .client_attachment_id :str =id 
        'ID applications the client.'
        self .expires_at :str =id 
        'Expiration date.'


class ChatMessageButton :
    'Message button object.\n\n    :param type: Button type.\n    :type type: `playerokapi.types.ChatMessageButtonTypes`\n\n    :param url: Button URL.\n    :type url: `str` or None\n\n    :param text: Button text.\n    :type text: `str`'

    def __init__ (self ,type :ChatMessageButtonTypes ,
    url :str |None ,text :str ,):
        self .type :ChatMessageButtonTypes =type 
        'Button type.'
        self .url :str |None =url 
        'Button URL.'
        self .text :str =text 
        'Button text.'


class ChatMessage :
    'A class that describes a message in chat.\n\n    :param id: Message ID.\n    :type id: `str`\n\n    :param text: Message text.\n    :type text: `str`\n\n    :param created_at: Date the message was created.\n    :type created_at: `str`\n\n    :param deleted_at: Date the message was deleted.\n    :type deleted_at: `str` or `None`\n\n    :param is_read: Whether the message has been read.\n    :type is_read: `bool`\n\n    :param is_suspicious: Is the message suspicious?\n    :type is_suspicious: `bool`\n\n    :param is_bulk_messaging: Is this a mass mailing?\n    :type is_bulk_messaging: `bool`\n\n    :param game: The game the message refers to.\n    :type game: `str` or `None`\n\n    :param file: File attached to the message.\n    :type file: `playerokapi.types.FileObject` or `None`\n\n    :param user: The user who sent the message.\n    :type user: `playerokapi.types.UserProfile`\n\n    :param deal: The deal the message refers to.\n    :type deal: `playerokapi.types.Deal` or `None`\n\n    :param item: Item to which the message relates (usually only the deal itself is passed to the deal variable).\n    :type item: `playerokapi.types.Item` or `None`\n\n    :param transaction: Message transaction.\n    :type transaction: `playerokapi.types.Transaction` or `None`\n\n    :param moderator: Message moderator.\n    :type moderator: `playerokapi.types.Moderator`\n\n    :param event_by_user: Event from the user.\n    :type event_by_user: `playerokapi.types.UserProfile` or `None`\n\n    :param event_to_user: Event for the user.\n    :type event_to_user: `playerokapi.types.UserProfile` or `None`\n\n    :param is_auto_response: Is this an auto-response?\n    :type is_auto_response: `bool`\n\n    :param event: Message event.\n    :type event: `playerokapi.types.Event` or `None`\n\n    :param buttons: Message buttons.\n    :type buttons: `list[playerokapi.types.MessageButton]`'

    def __init__ (self ,id :str ,text :str ,created_at :str ,deleted_at :str |None ,is_read :bool ,
    is_suspicious :bool ,is_bulk_messaging :bool ,game :Game |None ,file :FileObject |None ,
    user :UserProfile ,deal :ItemDeal |None ,item :ItemProfile |None ,transaction :Transaction |None ,
    moderator :Moderator |None ,event_by_user :UserProfile |None ,event_to_user :UserProfile |None ,
    is_auto_response :bool ,event :Event |None ,buttons :list [ChatMessageButton ]):
        self .id :str =id 
        'Message ID.'
        self .text :str =text 
        'Message text.'
        self .created_at :str =created_at 
        'Date the message was created.'
        self .deleted_at :str |None =deleted_at 
        'Date the message was deleted.'
        self .is_read :bool =is_read 
        'Has the message been read?'
        self .is_suspicious :bool =is_suspicious 
        'Is the message suspicious?'
        self .is_bulk_messaging :bool =is_bulk_messaging 
        'Is this a mass mailing?'
        self .game :Game |None =game 
        'The game the message refers to.'
        self .file :FileObject |None =file 
        'File attached to message.'
        self .user :UserProfile =user 
        'The user who sent the message.'
        self .deal :ItemDeal |None =deal 
        'The transaction to which the message relates.'
        self .item :ItemProfile |None =item 
        'Item to which the message relates (usually only the deal itself is passed to the deal variable).'
        self .transaction :Transaction |None =transaction 
        'Message transaction.'
        self .moderator :Moderator =moderator 
        'Post moderator.'
        self .event_by_user :UserProfile |None =event_by_user 
        'User event.'
        self .event_to_user :UserProfile |None =event_to_user 
        'Event for the user.'
        self .is_auto_response :bool =is_auto_response 
        'Is it an auto-response?'
        self .event :Event |None =event 
        'Event messages.'
        self .buttons :list [ChatMessageButton ]=buttons 
        'Message buttons.'


class ChatMessagePageInfo :
    'A subclass that describes information about the messages page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class ChatMessageList :
    'A class that describes a chat message page.\n\n    :param messages: Page messages.\n    :type messages: `list[playerokapi.types.ChatMessage]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.ChatMessagePageInfo`\n\n    :param total_count: Total messages in chat.\n    :type total_count: `int`'

    def __init__ (self ,messages :list [ChatMessage ],page_info :ChatMessagePageInfo ,
    total_count :int ):
        self .messages :list [ChatMessage ]=messages 
        'Page messages.'
        self .page_info :ChatMessagePageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total messages in chat.'


class Chat :
    'Chat object.\n\n    :param id: Chat ID.\n    :type id: `str`\n\n    :param type: Chat type.\n    :type type: `playerokapi.enums.ChatTypes`\n\n    :param status: Status of the chat.\n    :type status: `playerokapi.enums.ChatStatuses` or `None`\n\n    :param unread_messages_counter: Number of unread messages.\n    :type unread_messages_counter: `int`\n\n    :param bookmarked: Is the chat bookmarked?\n    :type bookmarked: `bool` or `None`\n\n    :param is_texting_allowed: Is it allowed to write in the chat.\n    :type is_texting_allowed: `bool` or `None`\n\n    :param owner: The owner of the chat (only if it is a chat with a bot).\n    :type owner: `bool` or `None`\n\n    :param deals: Deals in chat.\n    :type deals: `list[playerokapi.types.ItemDeal]` or `None`\n\n    :param last_message: Last message object in chat\n    :type last_message: `playerokapi.types.ChatMessage` or `None`\n\n    :param users: Chat participants.\n    :type users: `list[UserProfile]`\n\n    :param started_at: Dialogue start date.\n    :type started_at: `str` or `None`\n\n    :param finished_at: The date the dialogue was completed.\n    :type finished_at: `str` or `None`'

    def __init__ (self ,id :str ,type :ChatTypes ,status :ChatStatuses |None ,unread_messages_counter :int ,
    bookmarked :bool |None ,is_texting_allowed :bool |None ,owner :UserProfile |None ,deals :list [ItemDeal ]|None ,
    started_at :str |None ,finished_at :str |None ,last_message :ChatMessage |None ,users :list [UserProfile ]):
        self .id :str =id 
        'Chat ID.'
        self .type :ChatTypes =type 
        'Chat type.'
        self .status :ChatStatuses |None =status 
        'Status of the чата.'
        self .unread_messages_counter :int =unread_messages_counter 
        'Number of unread messages.'
        self .bookmarked :bool |None =bookmarked 
        'I bookmarked chat.'
        self .is_texting_allowed :bool |None =is_texting_allowed 
        'Is it allowed to write in the chat?'
        self .owner :UserProfile =owner 
        'Owner of the chat.'
        self .deals :list [ItemDeal ]|None =deals 
        'Transactions in chat.'
        self .last_message :ChatMessage |None =last_message 
        'The last message object in chat.'
        self .users :list [UserProfile ]=users 
        'Chat participants.'
        self .started_at :str |None =started_at 
        'Dialogue start date.'
        self .finished_at :str |None =finished_at 
        'Dialogue end date.'


class ChatPageInfo :
    'A subclass that describes information about the chats page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class ChatList :
    'A class describing a chat page.\n\n    :param chats: Chat pages.\n    :type chats: `list[playerokapi.types.Chat]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.ChatPageInfo`\n\n    :param total_count: Total chats.\n    :type total_count: `int`'

    def __init__ (self ,chats :list [Chat ],page_info :ChatPageInfo ,
    total_count :int ):
        self .chats :list [Chat ]=chats 
        'Chat pages.'
        self .page_info :ChatPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total chats.'


class Review :
    'Review object.\n\n    :param id: Review ID.\n    :type id: `str`\n\n    :param status: Status of the review.\n    :type status: `playerokapi.enums.ReviewStatuses`\n\n    :param text: Review text.\n    :type text: `str` or `None`\n\n    :param rating: Review rating.\n    :type rating: `int`\n\n    :param created_at: Date the review was created.\n    :type created_at: `str`\n\n    :param updated_at: Date the review was modified.\n    :type updated_at: `str`\n\n    :param deal: Deal associated with the review.\n    :type deal: `Deal`\n\n    :param creator: Profile of the review creator.\n    :type creator: `UserProfile`\n\n    :param moderator: The moderator who processed the review.\n    :type moderator: `Moderator` or `None`\n\n    :param user: Profile of the seller to whom the review relates.\n    :type user: `UserProfile`'

    def __init__ (self ,id :str ,status :ReviewStatuses ,text :str |None ,rating :int ,
    created_at :str ,updated_at :str ,deal :ItemDeal ,creator :UserProfile ,
    moderator :Moderator |None ,user :UserProfile ):
        self .id :str =id 
        'Review ID.'
        self .status :ReviewStatuses =status 
        'Status of the review.'
        self .text :str |None =text 
        'Review text.'
        self .rating :int =rating 
        'Review rating.'
        self .created_at :str =created_at 
        'Date the review was created.'
        self .updated_at :str =updated_at 
        'Review modification date.'
        self .deal :ItemDeal =deal 
        'Review related transaction.'
        self .creator :UserProfile =creator 
        'Profile of the review creator.'
        self .moderator :Moderator |None =moderator 
        'The moderator who processed the review.'
        self .user :UserProfile =user 
        'Profile of the seller to whom the review relates.'


class ReviewPageInfo :
    'A subclass that describes information about the reviews page.\n\n    :param start_cursor: Page start cursor.\n    :type start_cursor: `str`\n\n    :param end_cursor: End of page cursor.\n    :type end_cursor: `str`\n\n    :param has_previous_page: Whether it has a previous page.\n    :type has_previous_page: `bool`\n\n    :param has_next_page: Whether it has a next page.\n    :type has_next_page: `bool`'

    def __init__ (self ,start_cursor :str ,end_cursor :str ,
    has_previous_page :bool ,has_next_page :bool ):
        self .start_cursor :str =start_cursor 
        'Top of page cursor.'
        self .end_cursor :str =end_cursor 
        'End of page cursor.'
        self .has_previous_page :bool =has_previous_page 
        'Does the previous page have.'
        self .has_next_page :bool =has_next_page 
        'Does the next page have.'


class ReviewList :
    'A class that describes the reviews page.\n\n    :param reviews: Reviews page.\n    :type reviews: `list[playerokapi.types.Review]`\n\n    :param page_info: Information about the page.\n    :type page_info: `playerokapi.types.ReviewPageInfo`\n\n    :param total_count: Total reviews.\n    :type total_count: `int`'

    def __init__ (self ,reviews :list [Review ],page_info :ReviewPageInfo ,
    total_count :int ):
        self .reviews :list [Review ]=reviews 
        'Reviews page.'
        self .page_info :ReviewPageInfo =page_info 
        'Page information.'
        self .total_count :int =total_count 
        'Total reviews.'