from __future__ import annotations
from typing import *
import json

from .account import Account, get_account
from . import parser
from .enums import *
from .misc import PERSISTED_QUERIES



class FileObject:
    """
    File object.

    :param id: File ID.
    :type id: `str`

    :param url: File URL.
    :type url: `str`

    :param filename: File name.
    :type filename: `str` or `None`

    :param mime: File MIME.
    :type mime: `str` or `None`
    """
    def __init__(self, id: str, url: str, 
                 filename: str | None, mime: str | None):
        self.id: str = id
        """ File ID. """
        self.url: str = url
        """ File URL. """
        self.filename: str | None = filename
        """ File name. """
        self.mime: str | None = mime
        """ File MIME. """


class AccountBalance:
    """
    Subclass describing account balance.

    :param id: Balance ID.
    :type id: `str`

    :param value: Balance amount.
    :type value: `int`

    :param frozen: Frozen balance amount.
    :type frozen: `int`

    :param available: Available balance amount.
    :type available: `int`

    :param withdrawable: Balance amount, available for withdrawal.
    :type withdrawable: `int`

    :param pending_income: Pending income.
    :type pending_income: `int`
    """
    def __init__(self, id: str, value: int, frozen: int, available: int, 
                 withdrawable: int, pending_income: int):
        self.id: str = id
        """ Balance ID. """
        self.value: int = value
        """ Total balance amount. """
        self.frozen: int = frozen
        """ Frozen balance amount. """
        self.available: int = available
        """ Available balance amount. """
        self.withdrawable: int = withdrawable
        """ Balance amount, available for withdrawal. """
        self.pending_income: int = pending_income
        """ Pending income. """


class AccountIncomingDealsStats:
    """
    Subclass describing account incoming deals stats.

    :param total: Total outgoing deals.
    :type total: `int`

    :param finished: Completed outgoing deals.
    :type finished: `int`
    """
    def __init__(self, total: int, finished: int):
        self.total: int = total
        """ Total outgoing deals. """
        self.finished: int = finished
        """ Number of completed outgoing deals. """


class AccountOutgoingDealsStats:
    """
    Subclass describing account outgoing deals stats.

    :param total: Total outgoing deals.
    :type total: `int`

    :param finished: Completed outgoing deals.
    :type finished: `int`
    """
    def __init__(self, total: int, finished: int):
        self.total = total
        """ Total outgoing deals. """
        self.finished = finished
        """ Number of completed outgoing deals. """


class AccountDealsStats:
    """
    Subclass describing account deals stats.

    :param incoming: Incoming deals.
    :type incoming: `playerokapi.types.AccountIncomingDealsStats`

    :param outgoing: Outgoing deals.
    :type outgoing: `playerokapi.types.AccountOutgoingDealsStats`
    """
    def __init__(self, incoming: AccountIncomingDealsStats, outgoing: AccountOutgoingDealsStats):
        self.incoming: AccountIncomingDealsStats = incoming
        """ Incoming deals. """
        self.outgoing: AccountOutgoingDealsStats = outgoing
        """ Outgoing deals. """


class AccountItemsStats:
    """
    Subclass describing account items stats.

    :param total: Total items.
    :type total: `int`

    :param finished: Completed items.
    :type finished: `int`
    """
    def __init__(self, total: int, finished: int):
        self.total: int = total
        """ Total items. """
        self.finished: int = finished
        """ Number of completed items." """


class AccountStats:
    """
    Subclass describing account stats.

    :param items: Items stats.
    :type items: `playerokapi.types.AccountItemsStats`

    :param deals: Deals stats.
    :type deals: `playerokapi.types.AccountDealsStats`
    """
    def __init__(self, items: AccountItemsStats, deals: AccountDealsStats):
        self.items: AccountItemsStats = items
        """ Items stats. """
        self.deals: AccountDealsStats = deals
        """ Deals stats. """


class AccountProfile:
    """
    Class describing account profile.

    :param id: Account ID.
    :type id: `str`

    :param username: Account username.
    :type username: `str`

    :param email: Account email.
    :type email: `str`

    :param balance: Account balance object.
    :type balance: `playerokapi.types.AccountBalance`

    :param stats: Account stats.
    :type stats: `str`

    :param role: Account role.
    :type role: `playerokapi.enums.UserTypes`

    :param avatar_url: Account avatar URL.
    :type avatar_url: `str`

    :param is_online: Whether currently online account."
    :type is_online: `bool`

    :param is_blocked: Whether blocked account."
    :type is_blocked: `bool`

    :param is_blocked_for: Block reason.
    :type is_blocked_for: `str`

    :param is_verified: Whether verified account."
    :type is_verified: `bool`

    :param rating: Account rating (0-5).
    :type rating: `int`

    :param reviews_count: Number of reviews on account."
    :type reviews_count: `int`

    :param created_at: Account creation date.
    :type created_at: `str`

    :param support_chat_id: Support chat ID.
    :type support_chat_id: `str`

    :param system_chat_id: System chat ID.
    :type system_chat_id: `str`

    :param has_frozen_balance: Whether balance is frozen on account."
    :type has_frozen_balance: `bool`

    :param has_enabled_notifications: Whether notifications are enabled on account."
    :type has_enabled_notifications: `bool`

    :param unread_chats_counter: Number of unread chats.
    :type unread_chats_counter: `int` or `None`
    """
    def __init__(self, id: str, username: str, email: str, balance: AccountBalance, stats: AccountStats, role: UserTypes, avatar_url: str, is_online: bool, is_blocked: bool,
                 is_blocked_for: str, is_verified: bool, rating: int, reviews_count: int, created_at: str, support_chat_id: str, system_chat_id: str,
                 has_frozen_balance: bool, has_enabled_notifications: bool, unread_chats_counter: int | None):
        self.id: str = id
        """ Account ID. """
        self.username: str = username
        """ Account username. """
        self.email: str = email
        """ Account email. """
        self.balance: AccountBalance = balance
        """ Account balance object. """
        self.stats: AccountStats = stats
        """ Account stats. """
        self.role: UserTypes  = role
        """ Account role. """
        self.avatar_url: str = avatar_url
        """ Account avatar URL. """
        self.is_online: bool = is_online
        """ Whether currently online account." """
        self.is_blocked: bool = is_blocked
        """ Whether blocked account." """
        self.is_blocked_for: str = is_blocked_for
        """ Block reason account." """
        self.is_verified: bool = is_verified
        """ Whether verified account." """
        self.rating: int = rating
        """ Account rating (0-5). """
        self.reviews_count: int = reviews_count
        """ Number of reviews on account." """
        self.created_at: str = created_at
        """ Account creation date. """
        self.support_chat_id: str = support_chat_id
        """ Support chat Account ID. """
        self.system_chat_id: str = system_chat_id
        """ System chat Account ID. """
        self.has_frozen_balance: bool = has_frozen_balance
        """ Whether balance is frozen on account." """
        self.has_enabled_notifications: bool = has_enabled_notifications
        """ Whether notifications are enabled on account." """
        self.unread_chats_counter: bool | None = unread_chats_counter
        """ Number of unread messages. """


class UserProfile:
    """
    Class describing user profile.

    :param id: User ID.
    :type id: `str`

    :param username: User username.
    :type username: `str`

    :param role: User role.
    :type role: `playerokapi.enums.UserTypes`

    :param avatar_url: User avatar URL.
    :type avatar_url: `str`

    :param is_online: Whether currently online user."
    :type is_online: `bool`

    :param is_blocked: Whether blocked user."
    :type is_blocked: `bool`

    :param rating: User rating (0-5).
    :type rating: `int`

    :param reviews_count: Number of reviews user."
    :type reviews_count: `int`

    :param support_chat_id: Support chat ID.
    :type support_chat_id: `str` or `None`

    :param system_chat_id: System chat ID.
    :type system_chat_id: `str` or `None`

    :param created_at: Account creation date user."
    :type created_at: `str`
    """
    def __init__(self, id: str, username: str, role: UserTypes, avatar_url: str, is_online: bool, is_blocked: bool, 
                 rating: int, reviews_count: int, support_chat_id: str, system_chat_id: str | None, created_at: str | None):
        self.id: str = id
        """ User ID. """
        self.username: str = username
        """ User username. """
        self.role: UserTypes = role
        """ User role. """
        self.avatar_url: str = avatar_url
        """ Avatar URL. """
        self.is_online: bool = is_online
        """ Whether currently online user." """
        self.is_blocked: bool = is_blocked
        """ Whether blocked user." """
        self.rating: int = rating
        """ User rating (0-5). """
        self.reviews_count: int = reviews_count
        """ Number of reviews user." """
        self.support_chat_id: str | None = support_chat_id
        """ Support chat ID. """
        self.system_chat_id: str | None = system_chat_id
        """ System chat ID. """
        self.created_at: str = created_at
        """ Account creation date user." """

        self.__account: Account | None = get_account()
        """ Account object (for methods)." """


    def get_items(
        self, 
        count: int = 24, 
        game_id: str | None = None, 
        category_id: str | None = None, 
        statuses: list[ItemStatuses] | None = None,
        after_cursor: str | None = None
    ) -> ItemProfileList:
        """
        Gets user items.

        :param count: Number of items, to fetch (max 24 per request), optional."
        :type count: `int`
        
        :param game_id: Game/application ID whose items to fetch, optional."
        :type game_id: `str` or `None`

        :param category_id: Category game/application ID whose items to fetch, optional."
        :type category_id: `str` or `None`

        :param status: Item status types to fetch. Some statuses only for own account profile. If omitted, all are fetched.
        :type status: `list[playerokapi.enums.ItemStatuses]`

        :param after_cursor: Cursor to start from (if none, from page start), optional."
        :type after_cursor: `str` or `None`
        
        :return: Page of item profiles."
        :rtype: `PlayerokAPI.types.ItemProfileList`
        """
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": self.__account.base_url
        }
        filter = {
            "userId": self.id, 
            "status": [status.name for status in statuses] if statuses else None
        }
        if game_id: filter["gameId"] = game_id
        elif category_id: filter["gameCategoryId"] = category_id
        
        payload = {
            "operationName": "items",
            "variables": json.dumps({
                "pagination": {
                    "first": count, 
                    "after": after_cursor
                }, 
                "filter": filter, 
                "showForbiddenImage": False
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("items")
                }
            })
        }

        r = self.__account.request("get", f"{self.__account.base_url}/graphql", headers, payload).json()
        return parser.item_profile_list(r["data"]["items"])

    def get_reviews(
        self, 
        count: int = 24, 
        status: ReviewStatuses = ReviewStatuses.APPROVED, 
        comment_required: bool = False, 
        rating: int | None = None, 
        game_id: str | None = None, 
        category_id: str | None = None, 
        min_item_price: int | None = None, 
        max_item_price: int | None = None, 
        sort_direction: SortDirections = SortDirections.DESC, 
        sort_field: str = "createdAt", 
        after_cursor: str | None = None
    ) -> ReviewList:
        """
        Gets user reviews.

        :param count: Number of reviews, to fetch (max 24 per request), optional."
        :type count: `int`

        :param status: Review status to fetch."
        :type status: `playerokapi.enums.ReviewStatuses`

        :param comment_required: Whether review must have comment, optional."
        :type comment_required: `bool`

        :param rating: Review rating (1-5), optional."
        :type rating: `int` or `None`

        :param game_id: Reviews game ID, optional."
        :type game_id: `str` or `None`

        :param category_id: Reviews category ID, optional."
        :type category_id: `str` or `None`

        :param min_item_price: Review item min price, optional."
        :type min_item_price: `bool` or `None`

        :param max_item_price: Review item max price, optional."
        :type max_item_price: `bool` or `None`

        :param sort_direction: Sort direction."
        :type sort_direction: `playerokapi.enums.SortDirections`

        :param sort_field: Sort field (default `createdAt`)"
        :type sort_field: `str`

        :param after_cursor: Cursor to start from (if none, from page start), optional."
        :type after_cursor: `str` or `None`
        
        :return: Page of reviews."
        :rtype: `PlayerokAPI.types.ReviewList`
        """
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": self.__account.base_url,
        }

        filters = {"userId": self.id, "status": [status.name] if status else None}
        if comment_required is not None:
            filters["hasComment"] = comment_required
        if game_id is not None:
            filters["gameId"] = game_id
        if category_id is not None:
            filters["categoryId"] = category_id
        if rating is not None:
            filters["rating"] = rating
        if min_item_price is not None or max_item_price is not None:
            item_price = {}
            if min_item_price is not None:
                item_price["min"] = min_item_price
            if max_item_price is not None:
                item_price["max"] = max_item_price
            filters["itemPrice"] = item_price
        payload = {
            "operationName": "testimonials",
            "variables": json.dumps({
                "pagination": {
                    "first": count, 
                    "after": after_cursor
                }, 
                "filter": filters, 
                "sort": {
                    "direction": sort_direction.name if sort_direction else None, 
                    "field": sort_field
                }
            }),
            "extensions": json.dumps({
                "persistedQuery": {
                    "version": 1, 
                    "sha256Hash": PERSISTED_QUERIES.get("testimonials")
                }
            })
        }
        
        r = self.__account.request("get", f"{self.__account.base_url}/graphql", headers, payload).json()
        return parser.review_list(r["data"]["testimonials"])


class Event:
    #TODO: Сделать класс ивента Event

    def __init__(self):
        pass


class ItemDeal:
    """
    Item deal object.

    :param id: Deal ID.
    :type id: `str`

    :param status: Deal status.
    :type status: `playerokapi.enums.ItemDealStatuses`

    :param status_expiration_date: Status expiration date.
    :type status_expiration_date: `str` or `None`

    :param status_description: Status description deal."
    :type status_description: `str` or `None`

    :param direction: Deal direction (buy/sell).
    :type direction: `playerokapi.enums.ItemDealDirections`

    :param obtaining: Deal obtaining.
    :type obtaining: `str` or `None`

    :param has_problem: Whether deal has problem.
    :type has_problem: `bool`

    :param report_problem_enabled: Whether problem appeal is enabled.
    :type report_problem_enabled: `bool` or `None`

    :param completed_user: User who confirmed deal.
    :type completed_user: `playerokapi.types.UserProfile` or `None`

    :param props: Deal props.
    :type props: `str` or `None`

    :param previous_status: Previous status.
    :type previous_status: `playerokapi.enums.ItemDealStatuses` or `None`

    :param completed_at: Deal confirmation date.
    :type completed_at: `str` or `None`

    :param created_at: Creation date deal."
    :type created_at: `str` or `None`

    :param logs: Deal logs.
    :type logs: `list[playerokapi.types.ItemLog]` or `None`

    :param transaction: Deal transaction.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param user: User who made the deal.
    :type user: `playerokapi.types.UserProfile`

    :param chat: Deal chat (only ID passed).
    :type chat: `playerokapi.types.Chat` or `None`

    :param item: Deal item.
    :type item: `playerokapi.types.Item`

    :param review: Deal review.
    :type review: `playerokapi.types.Review` or `None`

    :param obtaining_fields: Obtaining fields.
    :type obtaining_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param comment_from_buyer: Comment from buyer.
    :type comment_from_buyer: `str` or `None`
    """
    def __init__(self, id: str, status: ItemDealStatuses, status_expiration_date: str | None, status_description: str | None, 
                 direction: ItemDealDirections, obtaining: str | None, has_problem: bool, report_problem_enabled: bool | None, 
                 completed_user: UserProfile | None, props: str | None, previous_status: ItemDealStatuses | None, 
                 completed_at: str, created_at: str, logs: list[ItemLog] | None, transaction: Transaction | None,
                 user: UserProfile, chat: Chat | None, item: Item, review: Review | None, obtaining_fields: list[GameCategoryDataField] | None,
                 comment_from_buyer: str | None):
        self.id: str = id
        """ Deal ID. """
        self.status: ItemDealStatuses = status
        """ Deal status. """
        self.status_expiration_date: str | None = status_expiration_date
        """ Status expiration date. """
        self.status_description: str | None = status_description
        """ Status description deal." """
        self.direction: ItemDealDirections = direction
        """ Deal direction (buy/sell). """
        self.obtaining: str | None = obtaining
        """ Deal obtaining. """
        self.has_problem: bool = has_problem
        """ Whether deal has problem. """
        self.report_problem_enabled: bool | None = report_problem_enabled
        """ Whether problem appeal is enabled. """
        self.completed_user: UserProfile | None = completed_user
        """ User who confirmed deal. """
        self.props: str | None = props
        """ Deal props. """
        self.previous_status: ItemDealStatuses | None = previous_status
        """ Previous status. """
        self.completed_at: str | None = completed_at
        """ Deal confirmation date. """
        self.created_at: str | None = created_at
        """ Creation date deal." """
        self.logs: list[ItemLog] | None = logs
        """ Deal logs. """
        self.transaction: Transaction | None = transaction
        """ Deal transaction. """
        self.user: UserProfile = user
        """ User who made the deal. """
        self.chat: Chat | None = chat
        """ Deal chat (only ID passed). """
        self.item: Item = item
        """ Deal item. """
        self.review: Review | None = review
        """ Deal review. """
        self.obtaining_fields: list[GameCategoryDataField] | None = obtaining_fields
        """ Obtaining fields. """
        self.comment_from_buyer: str | None = comment_from_buyer
        """ Comment from buyer. """


class ItemDealPageInfo:
    """
    Subclass describing deal page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class ItemDealList:
    """
    Class describing a page of reviews.

    :param deals: Page deals.
    :type deals: `list[playerokapi.types.ItemDeal]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.ItemDealPageInfo`

    :param total_count: Total deals.
    :type total_count: `int`
    """
    def __init__(self, deals: list[ItemDeal], page_info: ItemDealPageInfo,
                 total_count: int):
        self.deals: list[ItemDeal] = deals
        """ Page deals. """
        self.page_info: ItemDealPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total deals. """


class GameCategoryAgreement:
    """
    Subclass describing buyer agreements."

    :param id: Agreement ID.
    :type id: `str`

    :param description: Agreement description.
    :type description: `str`

    :param icontype: Agreement icon type.
    :type icontype: `playerokapi.enums.GameCategoryAgreementIconTypes`

    :param sequence: Agreement sequence.
    :type sequence: `str`
    """
    def __init__(self, id: str, description: str, 
                 icontype: GameCategoryAgreementIconTypes, sequence: int):
        self.id: str = id
        """ Agreement ID. """
        self.description: str = description
        """ Agreement description. """
        self.icontype: GameCategoryAgreementIconTypes = icontype
        """ Agreement icon type. """
        self.sequence: str = sequence
        """ Agreement sequence. """


class GameCategoryAgreementPageInfo:
    """
    Subclass describing buyer agreement page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class GameCategoryAgreementList:
    """
    Class describing buyer agreement page.

    :param agreements: Page agreements.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.GameCategoryAgreementPageInfo`

    :param total_count: Total agreements.
    :type total_count: `int`
    """
    def __init__(self, agreements: list[GameCategoryAgreement], page_info: GameCategoryAgreementPageInfo,
                 total_count: int):
        self.agreements: list[GameCategoryAgreement] = agreements
        """ Page agreements. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total agreements. """


class GameCategoryObtainingType:
    """
    Subclass describing category item obtaining type.

    :param id: Method ID.
    :type id: `str`

    :param name: Method name.
    :type name: `str`

    :param description: Method description.
    :type description: `str`

    :param game_category_id: Category Game Method ID.
    :type game_category_id: `str`

    :param no_comment_from_buyer: No comment from buyer?
    :type no_comment_from_buyer: `bool`

    :param instruction_for_buyer: Instruction for buyer.
    :type instruction_for_buyer: `str`

    :param instruction_for_seller: Instruction for seller.
    :type instruction_for_seller: `str`

    :param sequence: Method sequence.
    :type sequence: `int`

    :param fee_multiplier: Fee multiplier.
    :type fee_multiplier: `float`

    :param agreements: Buyer agreements for buy/sell."
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param props: Category props.
    :type props: `playerokapi.types.GameCategoryProps`
    """
    def __init__(self, id: str, name: str, description: str, game_category_id: str, no_comment_from_buyer: bool,
                 instruction_for_buyer: str | None, instruction_for_seller: str | None, sequence: int, fee_multiplier: float,
                 agreements: list[GameCategoryAgreement], props: GameCategoryProps):
        self.id: str = id
        """ Method ID. """
        self.name: str = name
        """ Method name. """
        self.description: str = description
        """ Method description. """
        self.game_category_id: str = game_category_id
        """ Category Game Method ID. """
        self.no_comment_from_buyer: bool = no_comment_from_buyer
        """ No comment from buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
        """ Instruction for buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
        """ Instruction for seller. """
        self.sequence: int = sequence
        """ Method sequence. """
        self.fee_multiplier: float = fee_multiplier
        """ Fee multiplier. """
        self.agreements: list[GameCategoryAgreement] = agreements
        """ Buyer agreements for buy/sell." """
        self.props: GameCategoryProps = props
        """ Category props. """


class GameCategoryObtainingTypePageInfo:
    """
    Subclass describing category obtaining types page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class GameCategoryObtainingTypeList:
    """
    Class describing category item obtaining types page."

    :param obtaining_types: Page methods.
    :type obtaining_types: `list[playerokapi.types.GameCategoryObtainingType]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.GameCategoryObtainingTypePageInfo`

    :param total_count: Total methods.
    :type total_count: `int`
    """
    def __init__(self, obtaining_types: list[GameCategoryObtainingType], page_info: GameCategoryObtainingTypePageInfo,
                 total_count: int):
        self.obtaining_types: list[GameCategoryObtainingType] = obtaining_types
        """ Page agreements. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total methods. """


class GameCategoryDataField:
    """
    Subclass describing category item data fields (sent after purchase).

    :param id: Data field ID.
    :type id: `str`

    :param label: Field label.
    :type label: `str`

    :param type: Data field type.
    :type type: `playerokapi.enums.GameCategoryDataFieldTypes`

    :param input_type: Field input value type.
    :type input_type: `playerokapi.enums.GameCategoryDataFieldInputTypes`

    :param copyable: Whether field value is copyable.
    :type copyable: `bool`

    :param hidden: Whether field data is hidden.
    :type hidden: `bool`

    :param required: Whether field is required.
    :type required: `bool`

    :param value: Field data value.
    :type value: `str` or `None`
    """
    def __init__(self, id: str, label: str, type: GameCategoryDataFieldTypes,
                 input_type: GameCategoryDataFieldInputTypes, copyable: bool, 
                 hidden: bool, required: bool, value: str | None):
        self.id: str = id
        """ Data field ID. """
        self.label: str = label
        """ Field label. """
        self.type: GameCategoryDataFieldTypes = type
        """ Data field type. """
        self.input_type: GameCategoryDataFieldInputTypes = input_type
        """ Field input value type. """
        self.copyable: bool = copyable
        """ Whether field value is copyable. """
        self.hidden: bool = hidden
        """ Whether field data is hidden. """
        self.required: bool = required
        """ Whether field is required. """
        self.value: str | None = value
        """ Field data value. """


class GameCategoryDataFieldPageInfo:
    """
    Subclass describing item data fields page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class GameCategoryDataFieldList:
    """
    Class describing item data fields page."

    :param data_fields: Category item data fields on page.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.GameCategoryDataFieldPageInfo`

    :param total_count: Total data fields.
    :type total_count: `int`
    """
    def __init__(self, data_fields: list[GameCategoryDataField], 
                 page_info: GameCategoryDataFieldPageInfo, total_count: int):
        self.data_fields: list[GameCategoryDataField] = data_fields
        """ Category item data fields on page. """
        self.page_info: GameCategoryDataFieldPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total data fields. """


class GameCategoryProps:
    """
    Subclass describing category props.

    :param min_reviews: Min reviews count.
    :type min_reviews: `int`

    :param min_reviews_for_seller: Min reviews count for seller.
    :type min_reviews_for_seller: `int`
    """
    def __init__(self, min_reviews: int, min_reviews_for_seller: int):
        self.min_reviews: int = min_reviews
        """ Min reviews count. """
        self.min_reviews_for_seller: int = min_reviews_for_seller
        """ Min reviews count for seller. """


class GameCategoryOption:
    """
    Subclass describing category option.

    :param id: Option ID.
    :type id: `str`

    :param group: Option group.
    :type group: `str`

    :param label: Option label.
    :type label: `str`

    :param type: Option type.
    :type type: `playerokapi.enums.GameCategoryOptionTypes`

    :param field: Field name (for site request payload).
    :type field: `str`

    :param value: Field value (for site request payload).
    :type value: `str`

    :param value_range_limit: Value range limit.
    :type value_range_limit: `int` or `None`
    """
    def __init__(self, id: str, group: str, label: str, type: GameCategoryOptionTypes,
                 field: str, value: str, value_range_limit: int | None):
        self.id: str = id
        """ Option ID. """
        self.group: str = group
        """ Option group. """
        self.label: str = label
        """ Option label. """
        self.type: GameCategoryOptionTypes = type
        """ Option type. """
        self.field: str = field
        """ Field name (for site request payload). """
        self.value: str = value
        """ Field value (for site request payload). """
        self.value_range_limit: int | None = value_range_limit
        """ Value range limit. """


class GameCategoryInstruction:
    """
    Subclass describing category instruction page info.

    :param id: Instruction ID.
    :type id: `str`

    :param text: Instruction text.
    :type text: `str`
    """
    def __init__(self, id: str, text: str):
        self.id: str = id
        """ Instruction ID. """
        self.text: str = text
        """ Instruction text. """


class GameCategoryInstructionPageInfo:
    """
    Subclass describing category instruction.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class GameCategoryInstructionList:
    """
    Class describing category buy/sell instructions page.

    :param instructions: Page instructions.
    :type instructions: `list[playerokapi.types.GameCategoryInstruction]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.GameCategoryInstructionPageInfo`

    :param total_count: Total instructions.
    :type total_count: `int`
    """
    def __init__(self, instructions: list[GameCategoryInstruction], page_info: GameCategoryInstructionPageInfo,
                 total_count: int):
        self.instructions: list[GameCategoryInstruction] = instructions
        """ Page agreements. """
        self.page_info: GameCategoryInstructionPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total instructions. """


class GameCategory:
    """
    Game/application category object.

    :param id: Category ID.
    :type id: `str`

    :param slug: Category page slug.
    :type slug: `str`

    :param name: Category name.
    :type name: `str`

    :param category_id: Parent category ID.
    :type category_id: `str` or `None`

    :param game_id: Game Category ID.
    :type game_id: `str` or `None`

    :param obtaining: Obtaining type.
    :type obtaining: `str` or `None` or `None`

    :param options: Category options.
    :type options: `list[playerokapi.types.GameCategoryOption]` or `None`

    :param props: Category props.
    :type props: `playerokapi.types.GameCategoryProps` or `None`

    :param no_comment_from_buyer: No comment from buyer?
    :type no_comment_from_buyer: `bool` or `None`

    :param instruction_for_buyer: Instruction for buyer.
    :type instruction_for_buyer: `str` or `None`

    :param instruction_for_seller: Instruction for seller.
    :type instruction_for_seller: `str` or `None`

    :param use_custom_obtaining: Whether custom obtaining is used.
    :type use_custom_obtaining: `bool`

    :param auto_confirm_period: Auto-confirm period for this category.
    :type auto_confirm_period: `playerokapi.enums.GameCategoryAutoConfirmPeriods` or `None`

    :param auto_moderation_mode: Whether auto moderation is enabled.
    :type auto_moderation_mode: `bool` or `None`

    :param agreements: Buyer agreements.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]` or `None`

    :param fee_multiplier: Fee multiplier.
    :type fee_multiplier: `float` or `None`
    """
    def __init__(self, id: str, slug: str, name: str, category_id: str | None, game_id: str | None,
                 obtaining: str | None, options: list[GameCategoryOption] | None, props: GameCategoryProps | None, 
                 no_comment_from_buyer: bool | None, instruction_for_buyer: str | None, instruction_for_seller: str | None, 
                 use_custom_obtaining: bool, auto_confirm_period: GameCategoryAutoConfirmPeriods | None, 
                 auto_moderation_mode: bool | None, agreements: list[GameCategoryAgreement] | None, fee_multiplier: float | None):
        self.id: str = id
        """ Category ID. """
        self.slug: str = slug
        """ Category page slug. """
        self.name: str = name
        """ Category name. """
        self.category_id: str | None = category_id
        """ Parent category ID. """
        self.game_id: str | None = game_id
        """ Game Category ID. """
        self.obtaining: str | None = obtaining
        """ Obtaining type. """
        self.options: list[GameCategoryOption] | None = options
        """ Category options. """
        self.props: str | None = props
        """ Category props. """
        self.no_comment_from_buyer: bool | None = no_comment_from_buyer
        """ No comment from buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
        """ Instruction for buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
        """ Instruction for seller. """
        self.use_custom_obtaining: bool = use_custom_obtaining
        """ Whether custom obtaining is used. """
        self.auto_confirm_period: GameCategoryAutoConfirmPeriods | None = auto_confirm_period
        """ Auto-confirm period for this category. """
        self.auto_moderation_mode: bool | None = auto_moderation_mode
        """ Whether auto moderation is enabled. """
        self.agreements: list[GameCategoryAgreement] | None = agreements
        """ Buyer agreements. """
        self.fee_multiplier: float | None = fee_multiplier
        """ Fee multiplier. """


class Game:
    """
    Game/application object.

    :param id: Game/application ID.
    :type id: `str`

    :param slug: Game/application page slug.
    :type slug: `str`

    :param name: Game/application name.
    :type name: `str`

    :param type: Type: game or application.
    :type type: `playerokapi.enums.GameTypes`

    :param logo: Game/application logo.
    :type logo: `playerokapi.types.FileObject`

    :param banner: Game/application banner.
    :type banner: `FileObject`

    :param categories: Game/application categories list.
    :type categories: `list[playerokapi.types.GameCategory]`

    :param created_at: Creation date.
    :type created_at: `str`
    """
    def __init__(self, id: str, slug: str, name: str, type: GameTypes, 
                 logo: FileObject, banner: FileObject, categories: list[GameCategory], 
                 created_at: str):
        self.id: str = id
        """ Game/application ID. """
        self.slug: str = slug
        """ Game/application page slug. """
        self.name: str = name
        """ Game/application name. """
        self.type: GameTypes = type
        """ Type: game or application. """
        self.logo: FileObject = logo
        """ Game/application logo. """
        self.banner: FileObject = banner
        """ Game/application banner. """
        self.categories: list[GameCategory] = categories
        """ Game/application categories list. """
        self.created_at: str = created_at
        """ Creation date. """


class GameProfile:
    """
    Game/application profile.

    :param id: Game/application ID.
    :type id: `str`

    :param slug: Game/application page slug.
    :type slug: `str`

    :param name: Game/application name.
    :type name: `str`

    :param type: Type: game or application.
    :type type: `playerokapi.types.GameTypes`

    :param logo: Game/application logo.
    :type logo: `playerokapi.types.FileObject`
    """
    def __init__(self, id: str, slug: str, name: str, 
                 type: GameTypes, logo: FileObject):
        self.id: str = id
        """ Game/application ID. """
        self.slug: str = slug
        """ Game/application page slug. """
        self.name: str = name
        """ Game/application name. """
        self.type: GameTypes = id
        """ Type: game or application. """
        self.logo: FileObject = logo
        """ Game/application logo. """


class GamePageInfo:
    """
    Subclass describing games page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class GameList:
    """
    Class describing games page.

    :param games: Page games/applications.
    :type games: `list[playerokapi.types.Game]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Total games.
    :type total_count: `int`
    """
    def __init__(self, games: list[Game], page_info: GamePageInfo,
                 total_count: int):
        self.games: list[Game] = games
        """ Page games/applications. """
        self.page_info: ChatPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total games. """


class ItemPriorityStatusPriceRange:
    """
    Subclass describing item price range for priority status.

    :param min: Item min price.
    :type min: `int`

    :param max: Item max price.
    :type max: `int`
    """
    def __init__(self, min: int, max: str):
        self.min: int = min
        """ Item min price (in rubles). """
        self.max: int = max
        """ Item max price (in rubles). """


class ItemPriorityStatus:
    """
    Class describing item priority status.

    :param id: Priority status ID.
    :type id: `str`

    :param price: Status price (in rubles).
    :type price: `int`

    :param name: Status name.
    :type name: `str`

    :param type: Status type.
    :type type: `playerokapi.enums.PriorityTypes`

    :param period: Status duration (in days).
    :type period: `str`

    :param price_range: Status item price range.
    :type price_range: `playerokapi.types.ItemPriorityStatusPriceRange`
    """
    def __init__(self, id: str, price: int, name: str, type: PriorityTypes,
                 period: int, price_range: ItemPriorityStatusPriceRange):
        self.id: str = id
        """ Priority status ID. """
        self.price: int = price
        """ Status price (in rubles). """
        self.name: str = name
        """ Status name. """
        self.type: PriorityTypes = type
        """ Status type. """
        self.period: int = period
        """ Status duration (in days). """
        self.price_range: ItemPriorityStatusPriceRange = price_range
        """ Status item price range. """


class ItemLog:
    """
    Subclass describing item action log.
    
    :param id: Log ID.
    :type id: `str`
    
    :param event: Log event.
    :type event: `playerokapi.enums.ItemLogEvents`
    
    :param created_at: Creation date of log.
    :type created_at: `str`
    
    :param user: User who performed the log.
    :type user: `playerokapi.types.UserProfile`
    """
    def __init__(self, id: str, event: ItemLogEvents, created_at: str,
                 user: UserProfile):
        self.id: str = id
        """ Log ID. """
        self.event: ItemLogEvents = event
        """ Log event. """
        self.created_at: str = created_at
        """ Creation date of log. """
        self.user: UserProfile = user
        """ User who performed the log. """


class Item:
    """
    Item object.

    :param id: Item ID.
    :type id: `str`

    :param name: Item name.
    :type name: `str`

    :param description: Item description.
    :type description: `str`

    :param status: Item status.
    :type status: `playerokapi.enums.ItemStatuses`

    :param obtaining_type: Obtaining type.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

    :param price: Item price.
    :type price: `int`

    :param raw_price: Price without discount.
    :type raw_price: `int`

    :param priority_position: Priority position.
    :type priority_position: `int`

    :param attachments: Attachment files.
    :type attachments: `list[playerokapi.types.FileObject]`

    :param attributes: Item attributes.
    :type attributes: `dict`

    :param category: Item game category.
    :type category: `playerokapi.types.GameCategory`

    :param comment: Item comment.
    :type comment: `str` or `None`

    :param data_fields: Item data fields.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param fee_multiplier: Fee multiplier.
    :type fee_multiplier: `float`

    :param game: Item game profile.
    :type game: `playerokapi.types.GameProfile`

    :param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param slug: Item page slug.
    :type slug: `str`

    :param user: Seller profile.
    :type user: `playerokapi.types.UserProfile`
    """
    def __init__(self, id: str, slug: str, name: str, description: str, obtaining_type: GameCategoryObtainingType | None, price: int, raw_price: int, priority_position: int,
                 attachments: list[FileObject], attributes: dict, category: GameCategory, comment: str | None, data_fields: list[GameCategoryDataField] | None, 
                 fee_multiplier: float, game: GameProfile, seller_type: UserTypes, status: ItemStatuses, user: UserProfile):
        self.id: str = id
        """ Item ID. """
        self.slug: str = slug
        """ Item page slug. """
        self.name: str = name
        """ Item name. """
        self.description: str = description
        """ Item description. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        """ Obtaining type. """
        self.price: int = price
        """ Item price. """
        self.raw_price: int = raw_price
        """ Price without discount. """
        self.priority_position: int = priority_position
        """ Priority position. """
        self.attachments: list[FileObject] = attachments
        """ Attachment files. """
        self.attributes: dict = attributes
        """ Item attributes. """
        self.category: GameCategory = category
        """ Item game category. """
        self.comment: str | None = comment
        """ Item comment. """
        self.data_fields: list[GameCategoryDataField] | None = data_fields
        """ Item data fields. """
        self.fee_multiplier: float = fee_multiplier
        """ Fee multiplier. """
        self.game: GameProfile = game
        """ Item game profile. """
        self.seller_type: UserTypes = seller_type
        """ Seller type. """
        self.slug: str = slug
        """ Item page slug. """
        self.status: ItemStatuses = status
        """ Item status. """
        self.user: UserProfile = user
        """ Seller profile. """


class MyItem:
    """
    Own item object.

    :param id: Item ID.
    :type id: `str`

    :param slug: Item page slug.
    :type slug: `str`

    :param name: Item name.
    :type name: `str`

    :param description: Item description.
    :type description: `str`

    :param status: Item status.
    :type status: `playerokapi.enums.ItemStatuses`

    :param obtaining_type: Obtaining type.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

    :param price: Item price.
    :type price: `int`

    :param prev_price: Previous price.
    :type prev_price: `int`

    :param raw_price: Price without discount.
    :type raw_price: `int`

    :param priority_position: Priority position.
    :type priority_position: `int`

    :param attachments: Attachment files.
    :type attachments: `list[playerokapi.types.FileObject]`

    :param attributes: Item attributes.
    :type attributes: `dict`

    :param category: Item game category.
    :type category: `playerokapi.types.GameCategory`

    :param comment: Item comment.
    :type comment: `str` or `None`

    :param data_fields: Item data fields.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param fee_multiplier: Fee multiplier.
    :type fee_multiplier: `float`

    :param prev_fee_multiplier: Previous fee multiplier.
    :type prev_fee_multiplier: `float`

    :param seller_notified_about_fee_change: Whether seller was notified of fee change.
    :type seller_notified_about_fee_change: `bool`

    :param game: Item game profile.
    :type game: `playerokapi.types.GameProfile`

    :param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param user: Seller profile.
    :type user: `playerokapi.types.UserProfile`

    :param buyer: Seller profile.
    :type user: `playerokapi.types.UserProfile`

    :param priority: Item priority status.
    :type priority: `playerokapi.types.PriorityTypes`

    :param priority_price: Priority status price.
    :type priority_price: `int`

    :param sequence: Item position in user items table.
    :type sequence: `int` or `None`

    :param status_expiration_date: Status expiration date of priority.
    :type status_expiration_date: `str` or `None`

    :param status_description: Status description of priority.
    :type status_description: `str` or `None`

    :param status_payment: Status payment (transaction).
    :type status_payment: `playerokapi.types.Transaction` or `None`

    :param views_counter: Item views count.
    :type views_counter: `int`

    :param is_editable: Whether item is editable.
    :type is_editable: `bool`

    :param approval_date: Item publication date.
    :type approval_date: `str` or `None`

    :param deleted_at: Item deletion date.
    :type deleted_at: `str` or `None`

    :param updated_at: Item last update date.
    :type updated_at: `str` or `None`

    :param created_at: Creation date of item.
    :type created_at: `str` or `None`
    """
    def __init__(self, id: str, slug: str, name: str, description: str, obtaining_type: GameCategoryObtainingType | None, price: int, raw_price: int, priority_position: int,
                 attachments: list[FileObject], attributes: dict, buyer: UserProfile, category: GameCategory, comment: str | None,
                 data_fields: list[GameCategoryDataField] | None, fee_multiplier: float, game: GameProfile, seller_type: UserTypes, status: ItemStatuses,
                 user: UserProfile, prev_price: int, prev_fee_multiplier: float, seller_notified_about_fee_change: bool, 
                 priority: PriorityTypes, priority_price: int, sequence: int | None, status_expiration_date: str | None, status_description: str | None,
                 status_payment: Transaction | None, views_counter: int, is_editable: bool, approval_date: str | None, deleted_at: str | None, 
                 updated_at: str | None, created_at: str | None):
        self.id: str = id
        """ Item ID. """
        self.slug: str = slug
        """ Item page slug. """
        self.name: str = name
        """ Item name. """
        self.status: ItemStatuses = status
        """ Item status. """
        self.description: str = description
        """ Item description. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        """ Obtaining type. """
        self.price: int = price
        """ Item price. """
        self.prev_price: int = prev_price
        """ Previous price. """
        self.raw_price: int = raw_price
        """ Price without discount. """
        self.priority_position: int = priority_position
        """ Priority position. """
        self.attachments: list[FileObject] = attachments
        """ Attachment files. """
        self.attributes: dict = attributes
        """ Item attributes. """
        self.category: GameCategory = category
        """ Item game category. """
        self.comment: str | None = comment
        """ Item comment. """
        self.data_fields: list[GameCategoryDataField] | None = data_fields
        """ Item data fields. """
        self.fee_multiplier: float = fee_multiplier
        """ Fee multiplier. """
        self.prev_fee_multiplier: float = prev_fee_multiplier
        """ Previous fee multiplier. """
        self.seller_notified_about_fee_change: bool = seller_notified_about_fee_change
        """ Whether seller was notified of fee change. """
        self.game: GameProfile = game
        """ Item game profile. """
        self.seller_type: UserTypes = seller_type
        """ Seller type. """
        self.user: UserProfile = user
        """ Seller profile. """
        self.buyer: UserProfile = buyer
        """ Item buyer profile (if sold). """
        self.priority: PriorityTypes = priority
        """ Item priority status. """
        self.priority_price: int = priority_price
        """ Priority status price. """
        self.sequence: int | None = sequence
        """ Item position in user items table. """
        self.status_expiration_date: str | None = status_expiration_date
        """ Status expiration date of priority. """
        self.status_description: str | None = status_description
        """ Status description of priority. """
        self.status_payment: str | None = status_payment
        """ Status payment (transaction). """
        self.views_counter: int = views_counter
        """ Item views count. """
        self.is_editable: bool = is_editable
        """ Whether item is editable. """
        self.approval_date: str | None = approval_date
        """ Item publication date. """
        self.deleted_at: str | None = deleted_at
        """ Item deletion date. """
        self.updated_at: str | None = updated_at
        """ Item last update date. """
        self.created_at: str | None = created_at
        """ Creation date of item. """


class ItemProfile:
    """
    Item profile.

    :param id: Item ID.
    :type id: `str`

    :param slug: Item page slug.
    :type slug: `str`

    :param priority: Item priority.
    :type priority: `playerokapi.enums.PriorityTypes`

    :param status: Item status.
    :type status: `playerokapi.enums.ItemStatuses`

    :param name: Item name.
    :type name: `str`

    :param price: Item price.
    :type price: `int`

    :param raw_price: Price without discount.
    :type raw_price: `int`

    :param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param attachment: Attachment file.
    :type attachment: `playerokapi.types.FileObject`

    :param user: Seller profile.
    :type user: `playerokapi.types.UserProfile`

    :param approval_date: Approval date.
    :type approval_date: `str`

    :param priority_position: Priority position.
    :type priority_position: `int`

    :param views_counter: Views count.
    :type views_counter: `int` or `None`

    :param fee_multiplier: Fee multiplier.
    :type fee_multiplier: `float`

    :param created_at: Creation date.
    :type created_at: `str`
    """
    def __init__(self, id: str, slug: str, priority: PriorityTypes, status: ItemStatuses,
                 name: str, price: int, raw_price: int, seller_type: UserTypes, attachment: FileObject,
                 user: UserProfile, approval_date: str, priority_position: int, views_counter: int | None, 
                 fee_multiplier: float, created_at: str):
        self.id: str = id
        """ Item ID. """
        self.slug: str = slug
        """ Item page slug. """
        self.priority: PriorityTypes = priority
        """ Item priority. """
        self.status: ItemStatuses = status
        """ Item status. """
        self.name: str = name
        """ Item name. """
        self.price: int = price
        """ Item price. """
        self.raw_price: int = raw_price
        """ Price without discount. """
        self.seller_type: UserTypes = seller_type
        """ Seller type. """
        self.attachment: FileObject = attachment
        """ Attachment file. """
        self.user: UserProfile = user
        """ Seller profile. """
        self.approval_date: str = approval_date
        """ Approval date. """
        self.priority_position: int = priority_position
        """ Priority position. """
        self.views_counter: int | None = views_counter
        """ Views count. """
        self.fee_multiplier: float = fee_multiplier
        """ Fee multiplier. """
        self.created_at: str = created_at
        """ Creation date. """


class ItemProfilePageInfo:
    """
    Subclass describing item profiles page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class ItemProfileList:
    """
    Item profile list.

    :param items: Page items.
    :type items: `list[playerokapi.types.Item]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.ItemProfilePageInfo`

    :param total_count: Total items.
    :type total_count: `int`
    """
    def __init__(self, items: list[ItemProfile], page_info: ItemProfilePageInfo,
                 total_count: int):
        self.items: list[ItemProfile] = items
        """ Page items. """
        self.page_info: ItemProfilePageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total items. """


class SBPBankMember:
    """
    SBP bank member object.

    :param id: ID.
    :type id: `str`

    :param name: Name.
    :type name: `str`

    :param icon: Icon URL.
    :type icon: `str`
    """
    def __init__(self, id: str, name: str, icon: str):
        self.id: str = id
        """ ID. """
        self.name: str = name
        """ Name. """
        self.icon: str = icon
        """ Icon URL. """


class TransactionPaymentMethod:
    """
    Transaction payment method.

    :param id: Method ID.
    :type id: `playerokapi.types.TransactionPaymentMethodIds`

    :param name: Method name.
    :type name: `str`

    :param fee: Method fee.
    :type fee: `int`

    :param provider_id: Provider ID transaction.
    :type provider_id: `playerokapi.types.TransactionProviderIds`

    :param account: Method account (?).
    :type account: `AccountProfile` or `None`

    :param props: Provider params transaction.
    :type props: `playerokapi.types.TransactionProviderProps`

    :param limits: Provider limits transaction.
    :type limits: `playerokapi.types.TransactionProviderLimits`
    """
    def __init__(self, id: TransactionPaymentMethodIds, name: str, fee: int, provider_id: TransactionProviderIds,
                 account: AccountProfile | None, props: TransactionProviderProps, limits: TransactionProviderLimits):
        self.id: TransactionPaymentMethodIds = id
        """ Method ID. """
        self.name: str = name
        """ Method name. """
        self.fee: int = fee
        """ Method fee. """
        self.provider_id: TransactionProviderIds = provider_id
        """ Provider ID transaction. """
        self.account: AccountProfile | None = account
        """ Method account (?). """
        self.props: TransactionProviderProps = props
        """ Provider params transaction. """
        self.limits: TransactionProviderLimits = limits
        """ Provider limits transaction. """


class TransactionProviderLimitRange:
    """
    Transaction provider limit range.

    :param min: Min amount (in rubles).
    :type min: `int`

    :param max: Max amount (in rubles).
    :type max: `int`
    """
    def __init__(self, min: int, max: int):
        self.min: int = min
        """ Min amount (in rubles). """
        self.max: int = max
        """ Max amount (in rubles). """


class TransactionProviderLimits:
    """
    Provider limits transaction.

    :param incoming: For deposit.
    :type incoming: `playerokapi.types.TransactionProviderLimitRange`

    :param outgoing: For withdrawal.
    :type outgoing: `playerokapi.types.TransactionProviderLimitRange`
    """
    def __init__(self, incoming: TransactionProviderLimitRange, outgoing: TransactionProviderLimitRange):
        self.incoming: TransactionProviderLimitRange = incoming
        """ For deposit. """
        self.outgoing: TransactionProviderLimitRange = outgoing
        """ For withdrawal. """


class TransactionProviderRequiredUserData:
    """
    Transaction provider required user data.

    :param email: Is email required?
    :type email: `bool`

    :param phone_number: Is phone number required?
    :type phone_number: `bool`

    :param erip_account_number: Is ERIP account number required?
    :type erip_account_number: `bool` or `None`
    """
    def __init__(self, email: bool, phone_number: bool, 
                 erip_account_number: bool | None):
        self.email: bool = email
        """ Is email required? """
        self.phone_number: bool = phone_number
        """ Is phone number required? """
        self.erip_account_number: bool | None = erip_account_number
        """ Is ERIP account number required? """


class TransactionProviderProps:
    """
    Provider params transaction.

    :param required_user_data: Required user data.
    :type required_user_data: `playerokapi.types.TransactionProviderRequiredUserData`

    :param tooltip: Tooltip.
    :type tooltip: `str` or `None`
    """
    def __init__(self, required_user_data: TransactionProviderRequiredUserData,
                 tooltip: str | None):
        self.required_user_data: TransactionProviderRequiredUserData = required_user_data
        """ Required user data. """
        self.tooltip: str | None = tooltip
        """ Tooltip. """


class TransactionProvider:
    """
    Transaction provider object.

    :param id: Provider ID.
    :type id: `playerokapi.enums.TransactionProviderIds`

    :param name: Provider name.
    :type name: `str`

    :param fee: Provider fee.
    :type fee: `int`

    :param min_fee_amount: Min fee.
    :type min_fee_amount: `int` or `None`

    :param description: Provider description.
    :type description: `str` or `None`

    :param account: Provider account (?).
    :type account: `playerokapi.types.AccountProfile` or `None`

    :param props: Provider params.
    :type props: `playerokapi.types.TransactionProviderProps`

    :param limits: Provider limits.
    :type limits: `playerokapi.types.TransactionProviderLimits`

    :param payment_methods: Payment methods.
    :type payment_methods: `list` of `playerokapi.types.TransactionPaymentMethod`
    """
    def __init__(self, id: TransactionProviderIds, name: str, fee: int, min_fee_amount: int | None, 
                 description: str | None, account: AccountProfile | None, props: TransactionProviderProps, 
                 limits: TransactionProviderLimits, payment_methods: list[TransactionPaymentMethod]):
        self.id: TransactionProviderIds = id
        """ Provider ID. """
        self.name: str = name
        """ Provider name. """
        self.fee: int = fee
        """ Provider fee. """
        self.min_fee_amount: int | None = min_fee_amount
        """ Min fee. """
        self.description: str | None = description
        """ Provider description. """
        self.account: AccountProfile | None = account
        """ Provider account (?). """
        self.props: TransactionProviderProps = props
        """ Provider params. """
        self.limits: TransactionProviderLimits = limits
        """ Provider limits. """
        self.payment_methods: list[TransactionPaymentMethod] = payment_methods
        """ Payment methods. """


class Transaction:
    """
    Transaction object.

    :param id: Transaction ID.
    :type id: `str`

    :param operation: Operation type.
    :type operation: `playerokapi.enums.TransactionOperations`

    :param direction: Transaction direction.
    :type direction: `playerokapi.enums.TransactionDirections`

    :param provider_id: Payment provider ID.
    :type provider_id: `playerokapi.enums.TransactionProviderIds`

    :param provider: Transaction provider object.
    :type provider: `playerokapi.types.TransactionProvider`

    :param user: Transaction user object.
    :type user: `playerokapi.types.UserProfile`

    :param creator: Transaction creator object.
    :type creator: `playerokapi.types.UserProfile` or `None`

    :param status: Transaction processing status.
    :type status: `playerokapi.enums.TransactionStatuses`

    :param status_description: Status description.
    :type status_description: `str` or `None`

    :param status_expiration_date: Status expiration date.
    :type status_expiration_date: `str` or `None`

    :param value: Transaction amount.
    :type value: `int`

    :param fee: Transaction fee.
    :type fee: `int`

    :param created_at: Creation date transaction.
    :type created_at: `str`

    :param verified_at: Transaction confirmation date.
    :type verified_at: `str` or `None`

    :param verified_by: User who confirmed transaction.
    :type verified_by: `playerokapi.types.UserProfile` or `None`

    :param completed_at: Transaction completion date.
    :type completed_at: `str` or `None`

    :param completed_by: User who completed transaction.
    :type completed_by: `playerokapi.types.UserProfile` or `None`

    :param payment_method_id: Payment method ID.
    :type payment_method_id: `str` or `None`

    :param is_suspicious: Whether transaction is suspicious.
    :type is_suspicious: `bool` or `None`

    :param sbp_bank_name: SBP bank name (if transaction was via SBP).
    :type sbp_bank_name: `str` or `None`
    """
    def __init__(self, id: str, operation: TransactionOperations, direction: TransactionDirections, provider_id: TransactionProviderIds, 
                 provider: TransactionProvider, user: UserProfile, creator: UserProfile, status: TransactionStatuses, status_description: str | None, 
                 status_expiration_date: str | None, value: int, fee: int, created_at: str, verified_at: str | None, verified_by: UserProfile | None, 
                 completed_at: str | None, completed_by: UserProfile | None, payment_method_id: str | None, is_suspicious: bool | None, sbp_bank_name: str | None):
        self.id: str = id
        """ Transaction ID. """
        self.operation: TransactionOperations = operation
        """ Operation type. """
        self.direction: TransactionDirections = direction
        """ Transaction direction. """
        self.provider_id: TransactionProviderIds = provider_id
        """ Payment provider ID. """
        self.provider: TransactionProvider = provider
        """ Transaction provider object. """
        self.user: UserProfile = user
        """ Transaction user object. """
        self.creator: UserProfile | None = creator
        """ Transaction creator object. """
        self.status: TransactionStatuses = status
        """ Transaction processing status. """
        self.status_description: str | None = status_description
        """ Status description. """
        self.status_expiration_date: str | None = status_expiration_date
        """ Status expiration date. """
        self.value: int = value
        """ Transaction amount. """
        self.fee: int = fee
        """ Transaction fee. """
        self.created_at: str = created_at
        """ Creation date transaction. """
        self.verified_at: str | None = verified_at
        """ Transaction confirmation date. """
        self.verified_by: UserProfile | None = verified_by
        """ User who confirmed transaction. """
        self.completed_at: str | None = completed_at
        """ Transaction completion date. """
        self.completed_by: UserProfile | None = completed_by
        """ User who completed transaction. """
        self.payment_method_id: str | None = payment_method_id
        """ Payment method ID. """
        self.is_suspicious: bool | None = is_suspicious
        """ Whether transaction is suspicious. """
        self.sbp_bank_name: str | None = sbp_bank_name
        """ SBP bank name (if transaction was via SBP). """


class TransactionPageInfo:
    """
    Subclass describing transactions page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class TransactionList:
    """
    Class describing a chat message page.

    :param transactions: Page transactions.
    :type transactions: `list[playerokapi.types.Transaction]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.TransactionPageInfo`

    :param total_count: Total transactions on page.
    :type total_count: `int`
    """
    def __init__(self, transactions: list[Transaction], page_info: TransactionPageInfo,
                 total_count: int):
        self.transactions: list[Transaction] = transactions
        """ Page transactions. """
        self.page_info: TransactionPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total transactions on page. """


class UserBankCard:
    """
    User bank card object.

    :param id: Card ID.
    :type id: `str`

    :param card_first_six: Card first six digits.
    :type card_first_six: `str`

    :param card_last_four: Card last four digits.
    :type card_last_four: `str`

    :param card_type: Bank card type.
    :type card_type: `playerokapi.enums.BankCardTypes`

    :param is_chosen: Whether this card is default?
    :type is_chosen: `bool`
    """
    def __init__(self, id: str, card_first_six: str, card_last_four: str,
                 card_type: BankCardTypes, is_chosen: bool):
        self.id: str = id
        """ Card ID. """
        self.card_first_six: str = card_first_six
        """ Card first six digits. """
        self.card_last_four: str = card_last_four
        """ Card last four digits. """
        self.card_type: BankCardTypes = card_type
        """ Bank card type. """
        self.is_chosen: bool = is_chosen
        """ Whether this card is default? """


class UserBankCardPageInfo:
    """
    Subclass describing user bank cards page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class UserBankCardList:
    """
    Class describing user bank cards page.

    :param bank_cards: Page bank cards.
    :type bank_cards: `list[playerokapi.types.UserBankCard]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.UserBankCardPageInfo`

    :param total_count: Total bank cards on page.
    :type total_count: `int`
    """
    def __init__(self, bank_cards: list[UserBankCard], 
                 page_info: UserBankCardPageInfo, total_count: int):
        self.bank_cards: list[UserBankCard] = bank_cards
        """ Page bank cards. """
        self.page_info: UserBankCardPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total bank cards on page. """


class Moderator:
    # TODO: Сделать класс модератора Moderator

    def __init__(self):
        pass


class ChatMessageButton:
    """
    Message button object.

    :param type: Button type.
    :type type: `playerokapi.types.ChatMessageButtonTypes`

    :param url: Button URL.
    :type url: `str` or None

    :param text: Button text.
    :type text: `str`
    """
    def __init__(self, type: ChatMessageButtonTypes, 
                 url: str | None, text: str,):
        self.type: ChatMessageButtonTypes = type
        """ Button type. """
        self.url: str | None = url
        """ Button URL. """
        self.text: str = text
        """ Button text. """


class ChatMessage:
    """
    Class describing a chat message.

    :param id: Message ID.
    :type id: `str`

    :param text: Message text.
    :type text: `str`

    :param created_at: Creation date of message.
    :type created_at: `str`

    :param deleted_at: Message deletion date.
    :type deleted_at: `str` or `None`

    :param is_read: Whether message is read.
    :type is_read: `bool`

    :param is_suspicious: Whether message is suspicious.
    :type is_suspicious: `bool`

    :param is_bulk_messaging: Whether this is bulk messaging.
    :type is_bulk_messaging: `bool`

    :param game: Game the message belongs to.
    :type game: `str` or `None`

    :param file: Message attachment file.
    :type file: `playerokapi.types.FileObject` or `None`

    :param user: User who sent the message.
    :type user: `playerokapi.types.UserProfile`

    :param deal: Deal the message belongs to.
    :type deal: `playerokapi.types.Deal` or `None`

    :param item: Item the message belongs to (usually deal is passed in deal var).
    :type item: `playerokapi.types.Item` or `None`

    :param transaction: Message transaction.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param moderator: Message moderator.
    :type moderator: `playerokapi.types.Moderator`

    :param event_by_user: Event from user.
    :type event_by_user: `playerokapi.types.UserProfile` or `None`

    :param event_to_user: Event for user.
    :type event_to_user: `playerokapi.types.UserProfile` or `None`

    :param is_auto_response: Whether this is auto-reply.
    :type is_auto_response: `bool`

    :param event: Message event.
    :type event: `playerokapi.types.Event` or `None`

    :param buttons: Message buttons.
    :type buttons: `list[playerokapi.types.MessageButton]`
    """
    def __init__(self, id: str, text: str, created_at: str, deleted_at: str | None, is_read: bool, 
                 is_suspicious: bool, is_bulk_messaging: bool, game: Game | None, file: FileObject | None,
                 user: UserProfile, deal: ItemDeal | None, item: ItemProfile | None, transaction: Transaction | None,
                 moderator: Moderator | None, event_by_user: UserProfile | None, event_to_user: UserProfile | None, 
                 is_auto_response: bool, event: Event | None, buttons: list[ChatMessageButton]):
        self.id: str = id
        """ Message ID. """
        self.text: str = text
        """ Message text. """
        self.created_at: str = created_at
        """ Creation date of message. """
        self.deleted_at: str | None = deleted_at
        """ Message deletion date. """
        self.is_read: bool = is_read
        """ Whether message is read. """
        self.is_suspicious: bool = is_suspicious
        """ Whether message is suspicious. """
        self.is_bulk_messaging: bool = is_bulk_messaging
        """ Whether this is bulk messaging. """
        self.game: Game | None  = game
        """ Game the message belongs to. """
        self.file: FileObject | None  = file
        """ Message attachment file. """
        self.user: UserProfile = user
        """ User who sent the message. """
        self.deal: ItemDeal | None = deal
        """ Deal the message belongs to. """
        self.item: ItemProfile | None = item
        """ Item the message belongs to (usually deal is passed in deal var). """
        self.transaction: Transaction | None = transaction
        """ Message transaction. """
        self.moderator: Moderator = moderator
        """ Message moderator. """
        self.event_by_user: UserProfile | None = event_by_user
        """ Event from user. """
        self.event_to_user: UserProfile | None = event_to_user
        """ Event for user. """
        self.is_auto_response: bool = is_auto_response
        """ Whether this is auto-reply. """
        self.event: Event | None = event
        """ Message event. """
        self.buttons: list[ChatMessageButton] = buttons
        """ Message buttons. """


class ChatMessagePageInfo:
    """
    Subclass describing messages page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class ChatMessageList:
    """
    Class describing a chat message page.

    :param messages: Page messages.
    :type messages: `list[playerokapi.types.ChatMessage]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.ChatMessagePageInfo`

    :param total_count: Total messages in chat.
    :type total_count: `int`
    """
    def __init__(self, messages: list[ChatMessage], page_info: ChatMessagePageInfo,
                 total_count: int):
        self.messages: list[ChatMessage] = messages
        """ Page messages. """
        self.page_info: ChatMessagePageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total messages in chat. """


class Chat:
    """
    Chat object.

    :param id: Chat ID.
    :type id: `str`

    :param type: Chat type.
    :type type: `playerokapi.enums.ChatTypes`

    :param status: Chat status.
    :type status: `playerokapi.enums.ChatStatuses` or `None`

    :param unread_messages_counter: Number of unread messages.
    :type unread_messages_counter: `int`

    :param bookmarked: Whether chat is bookmarked.
    :type bookmarked: `bool` or `None`

    :param is_texting_allowed: Whether writing to chat is allowed.
    :type is_texting_allowed: `bool` or `None`

    :param owner: Chat owner (only if this is a bot chat).
    :type owner: `bool` or `None`

    :param deals: Deals in chat.
    :type deals: `list[playerokapi.types.ItemDeal]` or `None`

    :param last_message: Last chat message object
    :type last_message: `playerokapi.types.ChatMessage` or `None`

    :param users: Chat participants.
    :type users: `list[UserProfile]`

    :param started_at: Dialog start date.
    :type started_at: `str` or `None`

    :param finished_at: Dialog end date.
    :type finished_at: `str` or `None`
    """
    def __init__(self, id: str, type: ChatTypes, status: ChatStatuses | None, unread_messages_counter: int, 
                 bookmarked: bool | None, is_texting_allowed: bool | None, owner: UserProfile | None, deals: list[ItemDeal] | None,
                 started_at: str | None, finished_at: str | None, last_message: ChatMessage | None, users: list[UserProfile]):
        self.id: str = id
        """ Chat ID. """
        self.type: ChatTypes = type
        """ Chat type. """
        self.status: ChatStatuses | None = status
        """ Chat status. """
        self.unread_messages_counter: int = unread_messages_counter
        """ Number of unread messages. """
        self.bookmarked: bool | None = bookmarked
        """ Whether chat is bookmarked. """
        self.is_texting_allowed: bool | None = is_texting_allowed
        """ Whether writing to chat is allowed. """
        self.owner: UserProfile = owner
        """ Chat owner. """
        self.deals: list[ItemDeal] | None = deals
        """ Deals in chat. """
        self.last_message: ChatMessage | None = last_message
        """ Last chat message object. """
        self.users: list[UserProfile] = users
        """ Chat participants. """
        self.started_at: str | None = started_at
        """ Dialog start date. """
        self.finished_at: str | None = finished_at
        """ Dialog end date. """


class ChatPageInfo:
    """
    Subclass describing chats page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class ChatList:
    """
    Class describing chats page.

    :param chats: Page chats.
    :type chats: `list[playerokapi.types.Chat]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Total chats.
    :type total_count: `int`
    """
    def __init__(self, chats: list[Chat], page_info: ChatPageInfo,
                 total_count: int):
        self.chats: list[Chat] = chats
        """ Page chats. """
        self.page_info: ChatPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total chats. """


class Review:
    """
    Review object.

    :param id: Review ID.
    :type id: `str`

    :param status: Review status.
    :type status: `playerokapi.enums.ReviewStatuses`

    :param text: Review text.
    :type text: `str` or `None`

    :param rating: Review rating.
    :type rating: `int`

    :param created_at: Creation date of review.
    :type created_at: `str`

    :param updated_at: Review update date.
    :type updated_at: `str`

    :param deal: Deal linked to review.
    :type deal: `Deal`

    :param creator: Review creator profile.
    :type creator: `UserProfile`

    :param moderator: Moderator who processed review.
    :type moderator: `Moderator` or `None`

    :param user: Seller profile the review refers to.
    :type user: `UserProfile`
    """
    def __init__(self, id: str, status: ReviewStatuses, text: str | None, rating: int,
                 created_at: str, updated_at: str, deal: ItemDeal, creator: UserProfile, 
                 moderator: Moderator | None, user: UserProfile):
        self.id: str = id
        """ Review ID. """
        self.status: ReviewStatuses = status
        """ Review status. """
        self.text: str | None = text
        """ Review text. """
        self.rating: int = rating
        """ Review rating. """
        self.created_at: str = created_at
        """ Creation date of review. """
        self.updated_at: str = updated_at
        """ Review update date. """
        self.deal: ItemDeal = deal
        """ Deal linked to review. """
        self.creator: UserProfile = creator
        """ Review creator profile. """
        self.moderator: Moderator | None = moderator
        """ Moderator who processed review. """
        self.user: UserProfile = user
        """ Seller profile the review refers to. """


class ReviewPageInfo:
    """
    Subclass describing reviews page info.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Has previous page. """
        self.has_next_page: bool = has_next_page
        """ Has next page. """


class ReviewList:
    """
    Class describing a page of reviews.

    :param reviews: Page reviews.
    :type reviews: `list[playerokapi.types.Review]`

    :param page_info: Page info.
    :type page_info: `playerokapi.types.ReviewPageInfo`

    :param total_count: Total reviews.
    :type total_count: `int`
    """
    def __init__(self, reviews: list[Review], page_info: ReviewPageInfo,
                 total_count: int):
        self.reviews: list[Review] = reviews
        """ Page reviews. """
        self.page_info: ReviewPageInfo = page_info
        """ Page info. """
        self.total_count: int = total_count
        """ Total reviews. """