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

    :param mime: File MIME type.
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
        """ File MIME type. """


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

    :param withdrawable: Withdrawable balance amount.
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
        """ Withdrawable balance amount. """
        self.pending_income: int = pending_income
        """ Pending income. """


class AccountIncomingDealsStats:
    """
    Subclass describing account incoming deals statistics.

    :param total: Total outgoing deals.
    :type total: `int`

    :param finished: Finished outgoing deals.
    :type finished: `int`
    """
    def __init__(self, total: int, finished: int):
        self.total: int = total
        """ Total outgoing deals. """
        self.finished: int = finished
        """ Number of finished outgoing deals. """


class AccountOutgoingDealsStats:
    """
    Subclass describing account outgoing deals statistics.

    :param total: Total outgoing deals.
    :type total: `int`

    :param finished: Finished outgoing deals.
    :type finished: `int`
    """
    def __init__(self, total: int, finished: int):
        self.total = total
        """ Total outgoing deals. """
        self.finished = finished
        """ Number of finished outgoing deals. """


class AccountDealsStats:
    """
    Subclass describing account deals statistics.

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
    Subclass describing account items statistics.

    :param total: Total items.
    :type total: `int`

    :param finished: Finished items.
    :type finished: `int`
    """
    def __init__(self, total: int, finished: int):
        self.total: int = total
        """ Total items. """
        self.finished: int = finished
        """ Number of finished items. """


class AccountStats:
    """
    Subclass describing account statistics.

    :param items: Items statistics.
    :type items: `playerokapi.types.AccountItemsStats`

    :param deals: Deals statistics.
    :type deals: `playerokapi.types.AccountDealsStats`
    """
    def __init__(self, items: AccountItemsStats, deals: AccountDealsStats):
        self.items: AccountItemsStats = items
        """ Items statistics. """
        self.deals: AccountDealsStats = deals
        """ Deals statistics. """


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

    :param stats: Account statistics.
    :type stats: `str`

    :param role: Account role.
    :type role: `playerokapi.enums.UserTypes`

    :param avatar_url: Account avatar URL.
    :type avatar_url: `str`

    :param is_online: Whether account is currently online.
    :type is_online: `bool`

    :param is_blocked: Whether account is blocked.
    :type is_blocked: `bool`

    :param is_blocked_for: Block reason.
    :type is_blocked_for: `str`

    :param is_verified: Whether account is verified.
    :type is_verified: `bool`

    :param rating: Account rating (0-5).
    :type rating: `int`

    :param reviews_count: Number of reviews on account.
    :type reviews_count: `int`

    :param created_at: Account creation date.
    :type created_at: `str`

    :param support_chat_id: Support chat ID.
    :type support_chat_id: `str`

    :param system_chat_id: System chat ID.
    :type system_chat_id: `str`

    :param has_frozen_balance: Whether account balance is frozen.
    :type has_frozen_balance: `bool`

    :param has_enabled_notifications: Whether account notifications are enabled.
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
        """ Account statistics. """
        self.role: UserTypes  = role
        """ Account role. """
        self.avatar_url: str = avatar_url
        """ Account avatar URL. """
        self.is_online: bool = is_online
        """ Whether account is currently online. """
        self.is_blocked: bool = is_blocked
        """ Whether account is blocked. """
        self.is_blocked_for: str = is_blocked_for
        """ Account block reason. """
        self.is_verified: bool = is_verified
        """ Whether account is verified. """
        self.rating: int = rating
        """ Account rating (0-5). """
        self.reviews_count: int = reviews_count
        """ Number of reviews on account. """
        self.created_at: str = created_at
        """ Account creation date. """
        self.support_chat_id: str = support_chat_id
        """ Account support chat ID. """
        self.system_chat_id: str = system_chat_id
        """ Account system chat ID. """
        self.has_frozen_balance: bool = has_frozen_balance
        """ Whether account balance is frozen. """
        self.has_enabled_notifications: bool = has_enabled_notifications
        """ Whether account notifications are enabled. """
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

    :param is_online: Whether user is currently online.
    :type is_online: `bool`

    :param is_blocked: Whether user is blocked.
    :type is_blocked: `bool`

    :param rating: User rating (0-5).
    :type rating: `int`

    :param reviews_count: Number of user reviews.
    :type reviews_count: `int`

    :param support_chat_id: Support chat ID.
    :type support_chat_id: `str` or `None`

    :param system_chat_id: System chat ID.
    :type system_chat_id: `str` or `None`

    :param created_at: User account creation date.
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
        """ Whether user is currently online. """
        self.is_blocked: bool = is_blocked
        """ Whether user is blocked. """
        self.rating: int = rating
        """ User rating (0-5). """
        self.reviews_count: int = reviews_count
        """ Number of user reviews. """
        self.support_chat_id: str | None = support_chat_id
        """ Support chat ID. """
        self.system_chat_id: str | None = system_chat_id
        """ System chat ID. """
        self.created_at: str = created_at
        """ User account creation date. """

        self.__account: Account | None = get_account()
        """ Account object (for methods). """


    def get_items(
        self, 
        count: int = 24, 
        statuses: list[ItemStatuses] | None = None,
        after_cursor: str | None = None
    ) -> ItemProfileList:
        """
        Gets user items.

        :param count: Number of items to get (no more than 24 per request), _optional_.
        :type count: `int`

        :param status: Array of item types to get. Some statuses can only be obtained if this is your account profile. If not specified, gets all possible at once.
        :type status: `list[playerokapi.enums.ItemStatuses]`

        :param after_cursor: Cursor to start parsing from (if not present - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of item profiles.
        :rtype: `PlayerokAPI.types.ItemProfileList`
        """
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": self.__account.base_url
        }
        payload = {
            "operationName": "items",
            "variables": json.dumps({
                "pagination": {
                    "first": count, 
                    "after": after_cursor
                }, 
                "filter": {
                    "userId": self.id, 
                    "status": [status.name for status in statuses] if statuses else None
                }, 
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

        :param count: Number of reviews to get (no more than 24 per request), _optional_.
        :type count: `int`

        :param status: Type of reviews to get.
        :type status: `playerokapi.enums.ReviewStatuses`

        :param comment_required: Whether comment is required in review, _optional_.
        :type comment_required: `bool`

        :param rating: Review rating (1-5), _optional_.
        :type rating: `int` or `None`

        :param game_id: Game ID of reviews, _optional_.
        :type game_id: `str` or `None`

        :param category_id: Category ID of reviews, _optional_.
        :type category_id: `str` or `None`

        :param min_item_price: Minimum price of review item, _optional_.
        :type min_item_price: `bool` or `None`

        :param max_item_price: Maximum price of review item, _optional_.
        :type max_item_price: `bool` or `None`

        :param sort_direction: Sort type.
        :type sort_direction: `playerokapi.enums.SortDirections`

        :param sort_field: Field to sort by (default `createdAt` - by date)
        :type sort_field: `str`

        :param after_cursor: Cursor to start parsing from (if not present - searches from the beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page of reviews.
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
    #TODO: Make Event event class

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

    :param status_description: Deal status description.
    :type status_description: `str` or `None`

    :param direction: Deal direction (purchase/sale).
    :type direction: `playerokapi.enums.ItemDealDirections`

    :param obtaining: Deal obtaining.
    :type obtaining: `str` or `None`

    :param has_problem: Whether deal has a problem.
    :type has_problem: `bool`

    :param report_problem_enabled: Whether problem appeal is enabled.
    :type report_problem_enabled: `bool` or `None`

    :param completed_user: Profile of user who confirmed the deal.
    :type completed_user: `playerokapi.types.UserProfile` or `None`

    :param props: Deal requisites.
    :type props: `str` or `None`

    :param previous_status: Previous status.
    :type previous_status: `playerokapi.enums.ItemDealStatuses` or `None`

    :param completed_at: Deal confirmation date.
    :type completed_at: `str` or `None`

    :param created_at: Deal creation date.
    :type created_at: `str` or `None`

    :param logs: Deal logs.
    :type logs: `list[playerokapi.types.ItemLog]` or `None`

    :param transaction: Deal transaction.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param user: Profile of user who made the deal.
    :type user: `playerokapi.types.UserProfile`

    :param chat: Deal chat (only ID is passed).
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
        """ Deal status description. """
        self.direction: ItemDealDirections = direction
        """ Deal direction (purchase/sale). """
        self.obtaining: str | None = obtaining
        """ Deal obtaining. """
        self.has_problem: bool = has_problem
        """ Whether deal has a problem. """
        self.report_problem_enabled: bool | None = report_problem_enabled
        """ Whether problem appeal is enabled. """
        self.completed_user: UserProfile | None = completed_user
        """ Profile of user who confirmed the deal. """
        self.props: str | None = props
        """ Deal requisites. """
        self.previous_status: ItemDealStatuses | None = previous_status
        """ Previous status. """
        self.completed_at: str | None = completed_at
        """ Deal confirmation date. """
        self.created_at: str | None = created_at
        """ Deal creation date. """
        self.logs: list[ItemLog] | None = logs
        """ Deal logs. """
        self.transaction: Transaction | None = transaction
        """ Deal transaction. """
        self.user: UserProfile = user
        """ Profile of user who made the deal. """
        self.chat: Chat | None = chat
        """ Deal chat (only ID is passed). """
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
    Subclass describing deals page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class ItemDealList:
    """
    Class describing reviews page.

    :param deals: Page deals.
    :type deals: `list[playerokapi.types.ItemDeal]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.ItemDealPageInfo`

    :param total_count: Total deals.
    :type total_count: `int`
    """
    def __init__(self, deals: list[ItemDeal], page_info: ItemDealPageInfo,
                 total_count: int):
        self.deals: list[ItemDeal] = deals
        """ Page deals. """
        self.page_info: ItemDealPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total deals. """


class GameCategoryAgreement:
    """
    Subclass describing buyer agreements.

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
    Subclass describing buyer agreements page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class GameCategoryAgreementList:
    """
    Class describing buyer agreements page.

    :param agreements: Page agreements.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.GameCategoryAgreementPageInfo`

    :param total_count: Total agreements.
    :type total_count: `int`
    """
    def __init__(self, agreements: list[GameCategoryAgreement], page_info: GameCategoryAgreementPageInfo,
                 total_count: int):
        self.agreements: list[GameCategoryAgreement] = agreements
        """ Page agreements. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total agreements. """


class GameCategoryObtainingType:
    """
    Subclass describing category item obtaining type (method).

    :param id: Method ID.
    :type id: `str`

    :param name: Method name.
    :type name: `str`

    :param description: Method description.
    :type description: `str`

    :param game_category_id: Method game category ID.
    :type game_category_id: `str`

    :param no_comment_from_buyer: Without comment from buyer?
    :type no_comment_from_buyer: `bool`

    :param instruction_for_buyer: Instruction for buyer.
    :type instruction_for_buyer: `str`

    :param instruction_for_seller: Instruction for seller.
    :type instruction_for_seller: `str`

    :param sequence: Method sequence.
    :type sequence: `int`

    :param fee_multiplier: Fee multiplier.
    :type fee_multiplier: `float`

    :param agreements: Buyer purchase agreements / seller sale agreements.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param props: Category proportions.
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
        """ Method game category ID. """
        self.no_comment_from_buyer: bool = no_comment_from_buyer
        """ Without comment from buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
        """ Instruction for buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
        """ Instruction for seller. """
        self.sequence: int = sequence
        """ Method sequence. """
        self.fee_multiplier: float = fee_multiplier
        """ Fee multiplier. """
        self.agreements: list[GameCategoryAgreement] = agreements
        """ Buyer purchase agreements / seller sale agreements. """
        self.props: GameCategoryProps = props
        """ Category proportions. """


class GameCategoryObtainingTypePageInfo:
    """
    Subclass describing category item obtaining types (methods) page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class GameCategoryObtainingTypeList:
    """
    Class describing category item obtaining types (methods) page.

    :param obtaining_types: Page methods.
    :type obtaining_types: `list[playerokapi.types.GameCategoryObtainingType]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.GameCategoryObtainingTypePageInfo`

    :param total_count: Total methods.
    :type total_count: `int`
    """
    def __init__(self, obtaining_types: list[GameCategoryObtainingType], page_info: GameCategoryObtainingTypePageInfo,
                 total_count: int):
        self.obtaining_types: list[GameCategoryObtainingType] = obtaining_types
        """ Page agreements. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total methods. """


class GameCategoryDataField:
    """
    Subclass describing category item data fields (which are sent after purchase).

    :param id: Data field ID.
    :type id: `str`

    :param label: Field label-name.
    :type label: `str`

    :param type: Data field type.
    :type type: `playerokapi.enums.GameCategoryDataFieldTypes`

    :param input_type: Field input value type.
    :type input_type: `playerokapi.enums.GameCategoryDataFieldInputTypes`

    :param copyable: Whether field value copying is allowed.
    :type copyable: `bool`

    :param hidden: Whether field data is hidden.
    :type hidden: `bool`

    :param required: Whether this field is required.
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
        """ Field label-name. """
        self.type: GameCategoryDataFieldTypes = type
        """ Data field type. """
        self.input_type: GameCategoryDataFieldInputTypes = input_type
        """ Field input value type. """
        self.copyable: bool = copyable
        """ Whether field value copying is allowed. """
        self.hidden: bool = hidden
        """ Whether field data is hidden. """
        self.required: bool = required
        """ Whether this field is required. """
        self.value: str | None = value
        """ Field data value. """


class GameCategoryDataFieldPageInfo:
    """
    Subclass describing item data fields page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class GameCategoryDataFieldList:
    """
    Class describing item data fields page.

    :param data_fields: Category item data fields on the page.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.GameCategoryDataFieldPageInfo`

    :param total_count: Total data fields.
    :type total_count: `int`
    """
    def __init__(self, data_fields: list[GameCategoryDataField], 
                 page_info: GameCategoryDataFieldPageInfo, total_count: int):
        self.data_fields: list[GameCategoryDataField] = data_fields
        """ Category item data fields on the page. """
        self.page_info: GameCategoryDataFieldPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total data fields. """


class GameCategoryProps:
    """
    Subclass describing category proportions.

    :param min_reviews: Minimum number of reviews.
    :type min_reviews: `int`

    :param min_reviews_for_seller: Minimum number of reviews for seller.
    :type min_reviews_for_seller: `int`
    """
    def __init__(self, min_reviews: int, min_reviews_for_seller: int):
        self.min_reviews: int = min_reviews
        """ Minimum number of reviews. """
        self.min_reviews_for_seller: int = min_reviews_for_seller
        """ Minimum number of reviews for seller. """


class GameCategoryOption:
    """
    Subclass describing category option.

    :param id: Option ID.
    :type id: `str`

    :param group: Option group.
    :type group: `str`

    :param label: Option label-name.
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
        """ Option label-name. """
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
    Subclass describing information about the instruction page for selling/buying in a category.

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
    Subclass describing instruction for selling/buying in a category.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class GameCategoryInstructionList:
    """
    Class describing the page of instructions for selling/buying in a category.

    :param instructions: Page instructions.
    :type instructions: `list[playerokapi.types.GameCategoryInstruction]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.GameCategoryInstructionPageInfo`

    :param total_count: Total instructions count.
    :type total_count: `int`
    """
    def __init__(self, instructions: list[GameCategoryInstruction], page_info: GameCategoryInstructionPageInfo,
                 total_count: int):
        self.instructions: list[GameCategoryInstruction] = instructions
        """ Page agreements. """
        self.page_info: GameCategoryInstructionPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total instructions count. """


class GameCategory:
    """
    Game/application category object.

    :param id: Category ID.
    :type id: `str`

    :param slug: Category page name.
    :type slug: `str`

    :param name: Category name.
    :type name: `str`

    :param category_id: Parent category ID.
    :type category_id: `str` or `None`

    :param game_id: Category game ID.
    :type game_id: `str` or `None`

    :param obtaining: Obtaining type.
    :type obtaining: `str` or `None` or `None`

    :param options: Category options.
    :type options: `list[playerokapi.types.GameCategoryOption]` or `None`

    :param props: Category proportions.
    :type props: `playerokapi.types.GameCategoryProps` or `None`

    :param no_comment_from_buyer: Without comment from buyer?
    :type no_comment_from_buyer: `bool` or `None`

    :param instruction_for_buyer: Instruction for buyer.
    :type instruction_for_buyer: `str` or `None`

    :param instruction_for_seller: Instruction for seller.
    :type instruction_for_seller: `str` or `None`

    :param use_custom_obtaining: Whether custom obtaining is used.
    :type use_custom_obtaining: `bool`

    :param auto_confirm_period: Auto-confirmation period for deals of this category.
    :type auto_confirm_period: `playerokapi.enums.GameCategoryAutoConfirmPeriods` or `None`

    :param auto_moderation_mode: Whether automatic moderation is enabled.
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
        """ Category page name. """
        self.name: str = name
        """ Category name. """
        self.category_id: str | None = category_id
        """ Parent category ID. """
        self.game_id: str | None = game_id
        """ Category game ID. """
        self.obtaining: str | None = obtaining
        """ Obtaining type. """
        self.options: list[GameCategoryOption] | None = options
        """ Category options. """
        self.props: str | None = props
        """ Category proportions. """
        self.no_comment_from_buyer: bool | None = no_comment_from_buyer
        """ Without comment from buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
        """ Instruction for buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
        """ Instruction for seller. """
        self.use_custom_obtaining: bool = use_custom_obtaining
        """ Whether custom obtaining is used. """
        self.auto_confirm_period: GameCategoryAutoConfirmPeriods | None = auto_confirm_period
        """ Auto-confirmation period for deals of this category. """
        self.auto_moderation_mode: bool | None = auto_moderation_mode
        """ Whether automatic moderation is enabled. """
        self.agreements: list[GameCategoryAgreement] | None = agreements
        """ Buyer agreements. """
        self.fee_multiplier: float | None = fee_multiplier
        """ Fee multiplier. """


class Game:
    """
    Game/application object.

    :param id: Game/application ID.
    :type id: `str`

    :param slug: Game/application page name.
    :type slug: `str`

    :param name: Game/application name.
    :type name: `str`

    :param type: Type: game or application.
    :type type: `playerokapi.enums.GameTypes`

    :param logo: Game/application logo.
    :type logo: `playerokapi.types.FileObject`

    :param banner: Game/application banner.
    :type banner: `FileObject`

    :param categories: List of game/application categories.
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
        """ Game/application page name. """
        self.name: str = name
        """ Game/application name. """
        self.type: GameTypes = type
        """ Type: game or application. """
        self.logo: FileObject = logo
        """ Game/application logo. """
        self.banner: FileObject = banner
        """ Game/application banner. """
        self.categories: list[GameCategory] = categories
        """ List of game/application categories. """
        self.created_at: str = created_at
        """ Creation date. """


class GameProfile:
    """
    Game/application profile.

    :param id: Game/application ID.
    :type id: `str`

    :param slug: Game/application page name.
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
        """ Game/application page name. """
        self.name: str = name
        """ Game/application name. """
        self.type: GameTypes = id
        """ Type: game or application. """
        self.logo: FileObject = logo
        """ Game/application logo. """


class GamePageInfo:
    """
    Subclass describing games page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class GameList:
    """
    Class describing games page.

    :param games: Page games/applications.
    :type games: `list[playerokapi.types.Game]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Total games.
    :type total_count: `int`
    """
    def __init__(self, games: list[Game], page_info: GamePageInfo,
                 total_count: int):
        self.games: list[Game] = games
        """ Page games/applications. """
        self.page_info: ChatPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total games. """


class ItemPriorityStatusPriceRange:
    """
    Subclass describing price range of item suitable for specific priority status.

    :param min: Minimum item price.
    :type min: `int`

    :param max: Maximum item price.
    :type max: `int`
    """
    def __init__(self, min: int, max: str):
        self.min: int = min
        """ Minimum item price (in rubles). """
        self.max: int = max
        """ Maximum item price (in rubles). """


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
    
    :param created_at: Log creation date.
    :type created_at: `str`
    
    :param user: User profile who performed the log.
    :type user: `playerokapi.types.UserProfile`
    """
    def __init__(self, id: str, event: ItemLogEvents, created_at: str,
                 user: UserProfile):
        self.id: str = id
        """ Log ID. """
        self.event: ItemLogEvents = event
        """ Log event. """
        self.created_at: str = created_at
        """ Log creation date. """
        self.user: UserProfile = user
        """ User profile who performed the log. """


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

    :param obtaining_type: Obtaining method.
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

    :param slug: Item page name.
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
        """ Item page name. """
        self.name: str = name
        """ Item name. """
        self.description: str = description
        """ Item description. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        """ Obtaining method. """
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
        """ Item page name. """
        self.status: ItemStatuses = status
        """ Item status. """
        self.user: UserProfile = user
        """ Seller profile. """


class MyItem:
    """
    Own item object.

    :param id: Item ID.
    :type id: `str`

    :param slug: Item page name.
    :type slug: `str`

    :param name: Item name.
    :type name: `str`

    :param description: Item description.
    :type description: `str`

    :param status: Item status.
    :type status: `playerokapi.enums.ItemStatuses`

    :param obtaining_type: Obtaining method.
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

    :param seller_notified_about_fee_change: Whether seller was notified about fee change.
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

    :param status_expiration_date: Priority status expiration date.
    :type status_expiration_date: `str` or `None`

    :param status_description: Priority status description.
    :type status_description: `str` or `None`

    :param status_payment: Status payment (transaction).
    :type status_payment: `playerokapi.types.Transaction` or `None`

    :param views_counter: Item views count.
    :type views_counter: `int`

    :param is_editable: Whether item can be edited.
    :type is_editable: `bool`

    :param approval_date: Item publication date.
    :type approval_date: `str` or `None`

    :param deleted_at: Item deletion date.
    :type deleted_at: `str` or `None`

    :param updated_at: Item last update date.
    :type updated_at: `str` or `None`

    :param created_at: Item creation date.
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
        """ Item page name. """
        self.name: str = name
        """ Item name. """
        self.status: ItemStatuses = status
        """ Item status. """
        self.description: str = description
        """ Item description. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        """ Obtaining method. """
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
        """ Whether seller was notified about fee change. """
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
        """ Priority status expiration date. """
        self.status_description: str | None = status_description
        """ Priority status description. """
        self.status_payment: str | None = status_payment
        """ Status payment (transaction). """
        self.views_counter: int = views_counter
        """ Item views count. """
        self.is_editable: bool = is_editable
        """ Whether item can be edited. """
        self.approval_date: str | None = approval_date
        """ Item publication date. """
        self.deleted_at: str | None = deleted_at
        """ Item deletion date. """
        self.updated_at: str | None = updated_at
        """ Item last update date. """
        self.created_at: str | None = created_at
        """ Item creation date. """


class ItemProfile:
    """
    Item profile.

    :param id: Item ID.
    :type id: `str`

    :param slug: Item page name.
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
        """ Item page name. """
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
    Subclass describing items page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class ItemProfileList:
    """
    Items page profile.

    :param items: Page items.
    :type items: `list[playerokapi.types.Item]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.ItemProfilePageInfo`

    :param total_count: Total items.
    :type total_count: `int`
    """
    def __init__(self, items: list[ItemProfile], page_info: ItemProfilePageInfo,
                 total_count: int):
        self.items: list[ItemProfile] = items
        """ Page items. """
        self.page_info: ItemProfilePageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total items. """


class SBPBankMember:
    """
    SBP bank members object.

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

    :param provider_id: Transaction provider ID.
    :type provider_id: `playerokapi.types.TransactionProviderIds`

    :param account: Method account (?).
    :type account: `AccountProfile` or `None`

    :param props: Transaction provider parameters.
    :type props: `playerokapi.types.TransactionProviderProps`

    :param limits: Transaction provider limits.
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
        """ Transaction provider ID. """
        self.account: AccountProfile | None = account
        """ Method account (?). """
        self.props: TransactionProviderProps = props
        """ Transaction provider parameters. """
        self.limits: TransactionProviderLimits = limits
        """ Transaction provider limits. """


class TransactionProviderLimitRange:
    """
    Transaction provider limit range.

    :param min: Minimum amount (in rubles).
    :type min: `int`

    :param max: Maximum amount (in rubles).
    :type max: `int`
    """
    def __init__(self, min: int, max: int):
        self.min: int = min
        """ Minimum amount (in rubles). """
        self.max: int = max
        """ Maximum amount (in rubles). """


class TransactionProviderLimits:
    """
    Transaction provider limits.

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
    Required user data for transaction provider.

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
    Transaction provider parameters.

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

    :param min_fee_amount: Minimum fee.
    :type min_fee_amount: `int` or `None`

    :param description: Provider description.
    :type description: `str` or `None`

    :param account: Provider account (?).
    :type account: `playerokapi.types.AccountProfile` or `None`

    :param props: Provider parameters.
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
        """ Minimum fee. """
        self.description: str | None = description
        """ Provider description. """
        self.account: AccountProfile | None = account
        """ Provider account (?). """
        self.props: TransactionProviderProps = props
        """ Provider parameters. """
        self.limits: TransactionProviderLimits = limits
        """ Provider limits. """
        self.payment_methods: list[TransactionPaymentMethod] = payment_methods
        """ Payment methods. """


class Transaction:
    """
    Transaction object.

    :param id: Transaction ID.
    :type id: `str`

    :param operation: Completed operation type.
    :type operation: `playerokapi.enums.TransactionOperations`

    :param direction: Transaction direction.
    :type direction: `playerokapi.enums.TransactionDirections`

    :param provider_id: Payment provider ID.
    :type provider_id: `playerokapi.enums.TransactionProviderIds`

    :param provider: Transaction provider object.
    :type provider: `playerokapi.types.TransactionProvider`

    :param user: Transaction performer user object.
    :type user: `playerokapi.types.UserProfile`

    :param creator: Transaction creator user object.
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

    :param created_at: Transaction creation date.
    :type created_at: `str`

    :param verified_at: Transaction verification date.
    :type verified_at: `str` or `None`

    :param verified_by: User object who verified the transaction.
    :type verified_by: `playerokapi.types.UserProfile` or `None`

    :param completed_at: Transaction completion date.
    :type completed_at: `str` or `None`

    :param completed_by: User object who completed the transaction.
    :type completed_by: `playerokapi.types.UserProfile` or `None`

    :param payment_method_id: Payment method ID.
    :type payment_method_id: `str` or `None`

    :param is_suspicious: Whether transaction is suspicious.
    :type is_suspicious: `bool` or `None`

    :param sbp_bank_name: SBP bank name (if transaction was made using SBP).
    :type sbp_bank_name: `str` or `None`
    """
    def __init__(self, id: str, operation: TransactionOperations, direction: TransactionDirections, provider_id: TransactionProviderIds, 
                 provider: TransactionProvider, user: UserProfile, creator: UserProfile, status: TransactionStatuses, status_description: str | None, 
                 status_expiration_date: str | None, value: int, fee: int, created_at: str, verified_at: str | None, verified_by: UserProfile | None, 
                 completed_at: str | None, completed_by: UserProfile | None, payment_method_id: str | None, is_suspicious: bool | None, sbp_bank_name: str | None):
        self.id: str = id
        """ Transaction ID. """
        self.operation: TransactionOperations = operation
        """ Completed operation type. """
        self.direction: TransactionDirections = direction
        """ Transaction direction. """
        self.provider_id: TransactionProviderIds = provider_id
        """ Payment provider ID. """
        self.provider: TransactionProvider = provider
        """ Transaction provider object. """
        self.user: UserProfile = user
        """ Transaction performer user object. """
        self.creator: UserProfile | None = creator
        """ Transaction creator user object. """
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
        """ Transaction creation date. """
        self.verified_at: str | None = verified_at
        """ Transaction verification date. """
        self.verified_by: UserProfile | None = verified_by
        """ User object who verified the transaction. """
        self.completed_at: str | None = completed_at
        """ Transaction completion date. """
        self.completed_by: UserProfile | None = completed_by
        """ User object who completed the transaction. """
        self.payment_method_id: str | None = payment_method_id
        """ Payment method ID. """
        self.is_suspicious: bool | None = is_suspicious
        """ Whether transaction is suspicious. """
        self.sbp_bank_name: str | None = sbp_bank_name
        """ SBP bank name (if transaction was made using SBP). """


class TransactionPageInfo:
    """
    Subclass describing transactions page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class TransactionList:
    """
    Class describing chat messages page.

    :param transactions: Page transactions.
    :type transactions: `list[playerokapi.types.Transaction]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.TransactionPageInfo`

    :param total_count: Total transactions on page.
    :type total_count: `int`
    """
    def __init__(self, transactions: list[Transaction], page_info: TransactionPageInfo,
                 total_count: int):
        self.transactions: list[Transaction] = transactions
        """ Page transactions. """
        self.page_info: TransactionPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total transactions on page. """


class UserBankCard:
    """
    User bank card object.

    :param id: Card ID.
    :type id: `str`

    :param card_first_six: First six digits of card.
    :type card_first_six: `str`

    :param card_last_four: Last four digits of card.
    :type card_last_four: `str`

    :param card_type: Bank card type.
    :type card_type: `playerokapi.enums.BankCardTypes`

    :param is_chosen: Whether this card is chosen as default?
    :type is_chosen: `bool`
    """
    def __init__(self, id: str, card_first_six: str, card_last_four: str,
                 card_type: BankCardTypes, is_chosen: bool):
        self.id: str = id
        """ Card ID. """
        self.card_first_six: str = card_first_six
        """ First six digits of card. """
        self.card_last_four: str = card_last_four
        """ Last four digits of card. """
        self.card_type: BankCardTypes = card_type
        """ Bank card type. """
        self.is_chosen: bool = is_chosen
        """ Whether this card is chosen as default? """


class UserBankCardPageInfo:
    """
    Subclass describing user bank cards page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class UserBankCardList:
    """
    Class describing user bank cards page.

    :param bank_cards: Page bank cards.
    :type bank_cards: `list[playerokapi.types.UserBankCard]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.UserBankCardPageInfo`

    :param total_count: Total bank cards on page.
    :type total_count: `int`
    """
    def __init__(self, bank_cards: list[UserBankCard], 
                 page_info: UserBankCardPageInfo, total_count: int):
        self.bank_cards: list[UserBankCard] = bank_cards
        """ Page bank cards. """
        self.page_info: UserBankCardPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total bank cards on page. """


class Moderator:
    # TODO: Make Moderator class

    def __init__(self):
        pass


class ChatMessageButton:
    """
    Chat message button object.

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
    Class describing chat message.

    :param id: Message ID.
    :type id: `str`

    :param text: Message text.
    :type text: `str`

    :param created_at: Message creation date.
    :type created_at: `str`

    :param deleted_at: Message deletion date.
    :type deleted_at: `str` or `None`

    :param is_read: Whether message is read.
    :type is_read: `bool`

    :param is_suspicious: Whether message is suspicious.
    :type is_suspicious: `bool`

    :param is_bulk_messaging: Whether this is bulk messaging.
    :type is_bulk_messaging: `bool`

    :param game: Game that the message relates to.
    :type game: `str` or `None`

    :param file: File attached to message.
    :type file: `playerokapi.types.FileObject` or `None`

    :param user: User who sent the message.
    :type user: `playerokapi.types.UserProfile`

    :param deal: Deal that the message relates to.
    :type deal: `playerokapi.types.Deal` or `None`

    :param item: Item that the message relates to (usually only the deal itself is passed to the deal variable).
    :type item: `playerokapi.types.Item` or `None`

    :param transaction: Message transaction.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param moderator: Message moderator.
    :type moderator: `playerokapi.types.Moderator`

    :param event_by_user: Event from user.
    :type event_by_user: `playerokapi.types.UserProfile` or `None`

    :param event_to_user: Event for user.
    :type event_to_user: `playerokapi.types.UserProfile` or `None`

    :param is_auto_response: Whether this is auto-response.
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
        """ Message creation date. """
        self.deleted_at: str | None = deleted_at
        """ Message deletion date. """
        self.is_read: bool = is_read
        """ Whether message is read. """
        self.is_suspicious: bool = is_suspicious
        """ Whether message is suspicious. """
        self.is_bulk_messaging: bool = is_bulk_messaging
        """ Whether this is bulk messaging. """
        self.game: Game | None  = game
        """ Game that the message relates to. """
        self.file: FileObject | None  = file
        """ File attached to message. """
        self.user: UserProfile = user
        """ User who sent the message. """
        self.deal: ItemDeal | None = deal
        """ Deal that the message relates to. """
        self.item: ItemProfile | None = item
        """ Item that the message relates to (usually only the deal itself is passed to the deal variable). """
        self.transaction: Transaction | None = transaction
        """ Message transaction. """
        self.moderator: Moderator = moderator
        """ Message moderator. """
        self.event_by_user: UserProfile | None = event_by_user
        """ Event from user. """
        self.event_to_user: UserProfile | None = event_to_user
        """ Event for user. """
        self.is_auto_response: bool = is_auto_response
        """ Whether this is auto-response. """
        self.event: Event | None = event
        """ Message event. """
        self.buttons: list[ChatMessageButton] = buttons
        """ Message buttons. """


class ChatMessagePageInfo:
    """
    Subclass describing messages page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class ChatMessageList:
    """
    Class describing chat messages page.

    :param messages: Page messages.
    :type messages: `list[playerokapi.types.ChatMessage]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.ChatMessagePageInfo`

    :param total_count: Total messages in chat.
    :type total_count: `int`
    """
    def __init__(self, messages: list[ChatMessage], page_info: ChatMessagePageInfo,
                 total_count: int):
        self.messages: list[ChatMessage] = messages
        """ Page messages. """
        self.page_info: ChatMessagePageInfo = page_info
        """ Page information. """
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

    :param unread_messages_counter: Unread messages count.
    :type unread_messages_counter: `int`

    :param bookmarked: Whether chat is bookmarked.
    :type bookmarked: `bool` or `None`

    :param is_texting_allowed: Whether texting is allowed in chat.
    :type is_texting_allowed: `bool` or `None`

    :param owner: Chat owner (only if this is a bot chat).
    :type owner: `bool` or `None`

    :param deals: Deals in chat.
    :type deals: `list[playerokapi.types.ItemDeal]` or `None`

    :param last_message: Last message object in chat
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
        """ Whether texting is allowed in chat. """
        self.owner: UserProfile = owner
        """ Chat owner. """
        self.deals: list[ItemDeal] | None = deals
        """ Deals in chat. """
        self.last_message: ChatMessage | None = last_message
        """ Last message object in chat. """
        self.users: list[UserProfile] = users
        """ Chat participants. """
        self.started_at: str | None = started_at
        """ Dialog start date. """
        self.finished_at: str | None = finished_at
        """ Dialog end date. """


class ChatPageInfo:
    """
    Subclass describing chats page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class ChatList:
    """
    Class describing chats page.

    :param chats: Page chats.
    :type chats: `list[playerokapi.types.Chat]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Total chats.
    :type total_count: `int`
    """
    def __init__(self, chats: list[Chat], page_info: ChatPageInfo,
                 total_count: int):
        self.chats: list[Chat] = chats
        """ Page chats. """
        self.page_info: ChatPageInfo = page_info
        """ Page information. """
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

    :param created_at: Review creation date.
    :type created_at: `str`

    :param updated_at: Review update date.
    :type updated_at: `str`

    :param deal: Deal associated with review.
    :type deal: `Deal`

    :param creator: Review creator profile.
    :type creator: `UserProfile`

    :param moderator: Moderator who processed the review.
    :type moderator: `Moderator` or `None`

    :param user: Seller profile that the review relates to.
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
        """ Review creation date. """
        self.updated_at: str = updated_at
        """ Review update date. """
        self.deal: ItemDeal = deal
        """ Deal associated with review. """
        self.creator: UserProfile = creator
        """ Review creator profile. """
        self.moderator: Moderator | None = moderator
        """ Moderator who processed the review. """
        self.user: UserProfile = user
        """ Seller profile that the review relates to. """


class ReviewPageInfo:
    """
    Subclass describing reviews page information.

    :param start_cursor: Page start cursor.
    :type start_cursor: `str`

    :param end_cursor: Page end cursor.
    :type end_cursor: `str`

    :param has_previous_page: Whether has previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Whether has next page.
    :type has_next_page: `bool`
    """
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Page start cursor. """
        self.end_cursor: str = end_cursor
        """ Page end cursor. """
        self.has_previous_page: bool = has_previous_page
        """ Whether has previous page. """
        self.has_next_page: bool = has_next_page
        """ Whether has next page. """


class ReviewList:
    """
    Class describing reviews page.

    :param reviews: Page reviews.
    :type reviews: `list[playerokapi.types.Review]`

    :param page_info: Page information.
    :type page_info: `playerokapi.types.ReviewPageInfo`

    :param total_count: Total reviews.
    :type total_count: `int`
    """
    def __init__(self, reviews: list[Review], page_info: ReviewPageInfo,
                 total_count: int):
        self.reviews: list[Review] = reviews
        """ Page reviews. """
        self.page_info: ReviewPageInfo = page_info
        """ Page information. """
        self.total_count: int = total_count
        """ Total reviews. """