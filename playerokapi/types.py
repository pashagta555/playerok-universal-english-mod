from __future__ import annotations
from typing import *
import json

from . import parser
from .enums import *
from .misc import PERSISTED_QUERIES



class FileObject:
    """
File object.

:param id: File ID.
    :type id: `str`

:param url: URL of the file.
    :type url: `str`

:param filename: File name.
    :type filename: `str` or `None`

:param mime: The mime of the file.
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
""" Mime file. """


class AccountBalance:
    """
A subclass describing the account balance.

:param id: ID of the balance.
    :type id: `str`

:param value: Balance amount.
    :type value: `int`

:param frozen: Amount of frozen balance.
    :type frozen: `int`

:param available: Amount of available balance.
    :type available: `int`

:param withdrawable: The amount of balance available for withdrawal.
    :type withdrawable: `int`

:param pending_income: Expected income.
    :type pending_income: `int`
    """

    def __init__(self, id: str, value: int, frozen: int, available: int, 
                 withdrawable: int, pending_income: int):
        self.id: str = id
""" Balance ID. """
        self.value: int = value
""" Total balance amount. """
        self.frozen: int = frozen
""" Amount of frozen balance. """
        self.available: int = available
""" Amount of available balance. """
        self.withdrawable: int = withdrawable
""" Amount of balance available for withdrawal. """
        self.pending_income: int = pending_income
""" Expected income. """


class AccountIncomingDealsStats:
    """
A subclass that describes the statistics of incoming transactions of an account.

:param total: Total outgoing transactions.
    :type total: `int`

:param finished: Completed outgoing transactions.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total: int = total
""" Total outgoing transactions. """
        self.finished: int = finished
""" Number of completed outgoing transactions. """


class AccountOutgoingDealsStats:
    """
A subclass that describes the statistics of outgoing transactions of an account.

:param total: Total outgoing transactions.
    :type total: `int`

:param finished: Completed outgoing transactions.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total = total
""" Total outgoing transactions. """
        self.finished = finished
""" Number of completed outgoing transactions. """


class AccountDealsStats:
    """
A subclass that describes account transaction statistics.

:param incoming: Incoming transactions.
    :type incoming: `playerokapi.types.AccountIncomingDealsStats`

:param outgoing: Outgoing transactions.
    :type outgoing: `playerokapi.types.AccountOutgoingDealsStats`
    """

    def __init__(self, incoming: AccountIncomingDealsStats, outgoing: AccountOutgoingDealsStats):
        self.incoming: AccountIncomingDealsStats = incoming
""" Incoming transactions. """
        self.outgoing: AccountOutgoingDealsStats = outgoing
""" Outgoing transactions. """


class AccountItemsStats:
    """
A subclass that describes the statistics of account items.

:param total: Total items.
    :type total: `int`

:param finished: Completed items.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total: int = total
""" Total items. """
        self.finished: int = finished
""" Number of completed items. """


class AccountStats:
    """
A subclass describing account statistics.

:param items: Item statistics.
    :type items: `playerokapi.types.AccountItemsStats`

:param deals: Deal statistics.
    :type deals: `playerokapi.types.AccountDealsStats`
    """

    def __init__(self, items: AccountItemsStats, deals: AccountDealsStats):
        self.items: AccountItemsStats = items
""" Item statistics. """
        self.deals: AccountDealsStats = deals
""" Transaction statistics. """


class AccountProfile:
    """
A class describing the account profile.

:param id: Account ID.
    :type id: `str`

:param username: Nickname of the account.
    :type username: `str`

:param email: Account email.
    :type email: `str`

:param balance: Object balance account.
    :type balance: `playerokapi.types.AccountBalance`

:param stats: Account statistics.
    :type stats: `str`

:param role: Account role.
    :type role: `playerokapi.enums.UserTypes`

:param avatar_url: Account avatar URL.
    :type avatar_url: `str`

:param is_online: Is your account online now?
    :type is_online: `bool`

:param is_blocked: Whether the account is blocked.
    :type is_blocked: `bool`

:param is_blocked_for: Reason for blocking.
    :type is_blocked_for: `str`

:param is_verified: Whether the account is verified.
    :type is_verified: `bool`

:param rating: Account rating (0-5).
    :type rating: `int`

:param reviews_count: Number of reviews on the account.
    :type reviews_count: `int`

:param created_at: Account creation date.
    :type created_at: `str`

:param support_chat_id: Support chat ID.
    :type support_chat_id: `str`

:param system_chat_id: System chat ID.
    :type system_chat_id: `str`

:param has_frozen_balance: Whether the account balance is frozen.
    :type has_frozen_balance: `bool`

:param has_enabled_notifications: Whether notifications are enabled on the account.
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
""" Account nickname. """
        self.email: str = email
""" Account mail. """
        self.balance: AccountBalance = balance
""" Account balance object. """
        self.stats: AccountStats = stats
""" Account statistics. """
        self.role: UserTypes  = role
""" Account role. """
        self.avatar_url: str = avatar_url
""" Account avatar URL. """
        self.is_online: bool = is_online
""" Is your account online now. """
        self.is_blocked: bool = is_blocked
""" Is the account blocked. """
        self.is_blocked_for: str = is_blocked_for
""" Reason for account blocking. """
        self.is_verified: bool = is_verified
""" Is the account verified. """
        self.rating: int = rating
""" Account rating (0-5). """
        self.reviews_count: int = reviews_count
""" Number of reviews on the account. """
        self.created_at: str = created_at
""" Account creation date. """
        self.support_chat_id: str = support_chat_id
""" Account support chat ID. """
        self.system_chat_id: str = system_chat_id
""" Account system chat ID. """
        self.has_frozen_balance: bool = has_frozen_balance
""" Is the account balance frozen. """
        self.has_enabled_notifications: bool = has_enabled_notifications
""" Are notifications enabled on your account. """
        self.unread_chats_counter: bool | None = unread_chats_counter
""" Number of unread messages. """


class UserProfile:
    """
A class describing the user profile.

:param id: User ID.
    :type id: `str`

:param username: User nickname.
    :type username: `str`

:param role: User role.
    :type role: `playerokapi.enums.UserTypes`

:param avatar_url: URL of the user's avatar.
    :type avatar_url: `str`

:param is_online: Is the user online now?
    :type is_online: `bool`

:param is_blocked: Whether the user is blocked.
    :type is_blocked: `bool`

:param rating: User rating (0-5).
    :type rating: `int`

:param reviews_count: Number of user reviews.
    :type reviews_count: `int`

:param support_chat_id: Support chat ID.
    :type support_chat_id: `str` or `None`

:param system_chat_id: System chat ID.
    :type system_chat_id: `str` or `None`

:param created_at: Date the user account was created.
    :type created_at: `str`
    """

    def __init__(self, id: str, username: str, role: UserTypes, avatar_url: str, is_online: bool, is_blocked: bool, 
                 rating: int, reviews_count: int, support_chat_id: str, system_chat_id: str | None, created_at: str | None):
        self.id: str = id
""" User ID. """
        self.username: str = username
""" User nickname. """
        self.role: UserTypes = role
""" User role. """
        self.avatar_url: str = avatar_url
""" Avatar URL. """
        self.is_online: bool = is_online
""" Is the user online now. """
        self.is_blocked: bool = is_blocked
""" Whether the user is blocked. """
        self.rating: int = rating
""" User rating (0-5). """
        self.reviews_count: int = reviews_count
""" Number of user reviews. """
        self.support_chat_id: str | None = support_chat_id
""" Support chat ID. """
        self.system_chat_id: str | None = system_chat_id
""" System chat ID. """
        self.created_at: str = created_at
""" Date the user account was created. """


    def get_items(
        self, 
        count: int = 24, 
        game_id: str | None = None, 
        category_id: str | None = None, 
        statuses: list[ItemStatuses] | None = None,
        after_cursor: str | None = None
    ) -> ItemProfileList:
        """
Retrieves the user's items.

:param count: Number of items to receive (no more than 24 per request), _optional_.
        :type count: `int`
        
:param game_id: ID of the game/application whose items you want to receive, _optional_.
        :type game_id: `str` or `None`

:param category_id: ID of the category of the game/application whose items you want to receive, _optional_.
        :type category_id: `str` or `None`

:param status: An array of item types to receive. Some statuses can only be obtained if this is your account profile. If not specified, gets all possible ones at once.
        :type status: `list[playerokapi.enums.ItemStatuses]`

:param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
:return: Item profile page.
        :rtype: `PlayerokAPI.types.ItemProfileList`
        """
        from .account import get_account
        account = get_account()
        
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": account.base_url
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

        r = account.request("get", f"{account.base_url}/graphql", headers, payload).json()
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
Receives user feedback.

:param count: Number of reviews to receive (no more than 24 per request), _optional_.
        :type count: `int`

:param status: Type of feedback to receive.
        :type status: `playerokapi.enums.ReviewStatuses`

:param comment_required: Is a comment required in a review, _optional_.
        :type comment_required: `bool`

:param rating: Review rating (1-5), _optional_.
        :type rating: `int` or `None`

:param game_id: Review game ID, _optional_.
        :type game_id: `str` or `None`

:param category_id: Review category ID, _optional_.
        :type category_id: `str` or `None`

:param min_item_price: Minimum price of the review item, _optional_.
        :type min_item_price: `bool` or `None`

:param max_item_price: Maximum price of the review item, _optional_.
        :type max_item_price: `bool` or `None`

:param sort_direction: Sort type.
        :type sort_direction: `playerokapi.enums.SortDirections`

:param sort_field: The field by which the sorting will be performed (by default `createdAt` - by date)
        :type sort_field: `str`

:param after_cursor: The cursor from which the parsing will take place (if not present, it searches from the very beginning of the page), _optional_.
        :type after_cursor: `str` or `None`
        
:return: Reviews page.
        :rtype: `PlayerokAPI.types.ReviewList`
        """
        from .account import get_account
        account = get_account()
        
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "Origin": account.base_url,
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
        
        r = account.request("get", f"{account.base_url}/graphql", headers, payload).json()
        return parser.review_list(r["data"]["testimonials"])


class Event:
#TODO: Make an Event class

    def __init__(self):
        pass


class ItemDeal:
    """
The object of the transaction with the item.

:param id: Transaction ID.
    :type id: `str`

:param status: Transaction status.
    :type status: `playerokapi.enums.ItemDealStatuses`

:param status_expiration_date: Status expiration date.
    :type status_expiration_date: `str` or `None`

:param status_description: Description of the transaction status.
    :type status_description: `str` or `None`

:param direction: Direction of the transaction (buy/sell).
    :type direction: `playerokapi.enums.ItemDealDirections`

:param obtaining: Receiving a deal.
    :type obtaining: `str` or `None`

:param has_problem: Is there a problem in the transaction.
    :type has_problem: `bool`

:param report_problem_enabled: Whether problem reporting is enabled.
    :type report_problem_enabled: `bool` or `None`

:param completed_user: Profile of the user who confirmed the transaction.
    :type completed_user: `playerokapi.types.UserProfile` or `None`

:param props: Transaction details.
    :type props: `str` or `None`

:param previous_status: Previous status.
    :type previous_status: `playerokapi.enums.ItemDealStatuses` or `None`

:param completed_at: Transaction confirmation date.
    :type completed_at: `str` or `None`

:param created_at: The date the deal was created.
    :type created_at: `str` or `None`

:param logs: Transaction logs.
    :type logs: `list[playerokapi.types.ItemLog]` or `None`

:param transaction: The transaction transaction.
    :type transaction: `playerokapi.types.Transaction` or `None`

:param user: Profile of the user who made the transaction.
    :type user: `playerokapi.types.UserProfile`

:param chat: Transaction chat (only its ID is transmitted).
    :type chat: `playerokapi.types.Chat` or `None`

:param item: Subject of the transaction.
    :type item: `playerokapi.types.Item`

:param review: Review of the transaction.
    :type review: `playerokapi.types.Review` or `None`

:param obtaining_fields: Receiving fields.
    :type obtaining_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

:param comment_from_buyer: Comment from the buyer.
    :type comment_from_buyer: `str` or `None`
    """

    def __init__(self, id: str, status: ItemDealStatuses, status_expiration_date: str | None, status_description: str | None, 
                 direction: ItemDealDirections, obtaining: str | None, has_problem: bool, report_problem_enabled: bool | None, 
                 completed_user: UserProfile | None, props: str | None, previous_status: ItemDealStatuses | None, 
                 completed_at: str, created_at: str, logs: list[ItemLog] | None, transaction: Transaction | None,
                 user: UserProfile, chat: Chat | None, item: Item, review: Review | None, obtaining_fields: list[GameCategoryDataField] | None,
                 comment_from_buyer: str | None):
        self.id: str = id
""" Transaction ID. """
        self.status: ItemDealStatuses = status
""" Transaction status. """
        self.status_expiration_date: str | None = status_expiration_date
""" Status expiration date. """
        self.status_description: str | None = status_description
""" Description of the transaction status. """
        self.direction: ItemDealDirections = direction
""" Transaction direction (buy/sell). """
        self.obtaining: str | None = obtaining
""" Receiving a deal. """
        self.has_problem: bool = has_problem
""" Is there a problem with the transaction. """
        self.report_problem_enabled: bool | None = report_problem_enabled
""" Is appealing the problem enabled. """
        self.completed_user: UserProfile | None = completed_user
""" Profile of the user who confirmed the transaction. """
        self.props: str | None = props
""" Transaction details. """
        self.previous_status: ItemDealStatuses | None = previous_status
""" Previous status. """
        self.completed_at: str | None = completed_at
""" Date of transaction confirmation. """
        self.created_at: str | None = created_at
""" Date of transaction creation. """
        self.logs: list[ItemLog] | None = logs
""" Transaction logs. """
        self.transaction: Transaction | None = transaction
""" Deal transaction. """
        self.user: UserProfile = user
""" Profile of the user who made the transaction. """
        self.chat: Chat | None = chat
""" Transaction chat (only its ID is transmitted). """
        self.item: Item = item
""" Subject transactions. """
        self.review: Review | None = review
""" Feedback on the transaction. """
        self.obtaining_fields: list[GameCategoryDataField] | None = obtaining_fields
""" Retrieved fields. """
        self.comment_from_buyer: str | None = comment_from_buyer
""" Comment from the buyer. """


class ItemDealPageInfo:
    """
A subclass that describes information about the deals page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class ItemDealList:
    """
A class that describes the reviews page.

:param deals: Page deals.
    :type deals: `list[playerokapi.types.ItemDeal]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.ItemDealPageInfo`

:param total_count: Total transactions.
    :type total_count: `int`
    """

    def __init__(self, deals: list[ItemDeal], page_info: ItemDealPageInfo,
                 total_count: int):
        self.deals: list[ItemDeal] = deals
""" Deals page. """
        self.page_info: ItemDealPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total transactions. """


class GameCategoryAgreement:
    """
A subclass describing buyer agreements.

:param id: Agreement ID.
    :type id: `str`

:param description: Description of the agreement.
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
""" Description of the agreement. """
        self.icontype: GameCategoryAgreementIconTypes = icontype
""" Agreement icon type. """
        self.sequence: str = sequence
""" Sequence of agreement. """


class GameCategoryAgreementPageInfo:
    """
A subclass that describes information about the buyer agreements page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class GameCategoryAgreementList:
    """
A class that describes the buyer agreements page.

:param agreements: Page agreements.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.GameCategoryAgreementPageInfo`

:param total_count: Total agreements.
    :type total_count: `int`
    """

    def __init__(self, agreements: list[GameCategoryAgreement], page_info: GameCategoryAgreementPageInfo,
                 total_count: int):
        self.agreements: list[GameCategoryAgreement] = agreements
""" Page conventions. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total agreements. """


class GameCategoryObtainingType:
    """
A subclass that describes the type (method) of obtaining an item in a category.

:param id: ID of the capability.
    :type id: `str`

:param name: Name of the method.
    :type name: `str`

:param description: Description of the method.
    :type description: `str`

:param game_category_id: Method game category ID.
    :type game_category_id: `str`

:param no_comment_from_buyer: No comment from the buyer?
    :type no_comment_from_buyer: `bool`

:param instruction_for_buyer: Instructions for the buyer.
    :type instruction_for_buyer: `str`

:param instruction_for_seller: Instructions for the seller.
    :type instruction_for_seller: `str`

:param sequence: Method sequence.
    :type sequence: `int`

:param fee_multiplier: Commission multiplier.
    :type fee_multiplier: `float`

:param agreements: Buyer to buy/seller to sell agreements.
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
""" Name of the method. """
        self.description: str = description
""" Description of the method. """
        self.game_category_id: str = game_category_id
""" Method game category ID. """
        self.no_comment_from_buyer: bool = no_comment_from_buyer
""" No comment from the buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
""" Instructions for the buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
""" Instructions for the seller. """
        self.sequence: int = sequence
""" Sequence of method. """
        self.fee_multiplier: float = fee_multiplier
""" Commission multiplier. """
        self.agreements: list[GameCategoryAgreement] = agreements
""" Buyer to buy/seller to sell agreements. """
        self.props: GameCategoryProps = props
""" Category proportions. """


class GameCategoryObtainingTypePageInfo:
    """
A subclass that describes information about the page of types (methods) of obtaining an item in a category.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class GameCategoryObtainingTypeList:
    """
A class that describes a page of types (methods) of obtaining an item in a category.

:param obtaining_types: Page methods.
    :type obtaining_types: `list[playerokapi.types.GameCategoryObtainingType]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.GameCategoryObtainingTypePageInfo`

:param total_count: Total ways.
    :type total_count: `int`
    """

    def __init__(self, obtaining_types: list[GameCategoryObtainingType], page_info: GameCategoryObtainingTypePageInfo,
                 total_count: int):
        self.obtaining_types: list[GameCategoryObtainingType] = obtaining_types
""" Page conventions. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total ways. """


class GameCategoryDataField:
    """
A subclass that describes the data fields for an item in a category (which are sent after purchase).

:param id: ID of the data field.
    :type id: `str`

:param label: The label is the name of the field.
    :type label: `str`

:param type: The type of the data field.
    :type type: `playerokapi.enums.GameCategoryDataFieldTypes`

:param input_type: The type of the field's input value.
    :type input_type: `playerokapi.enums.GameCategoryDataFieldInputTypes`

:param copyable: Whether the value can be copied from the field.
    :type copyable: `bool`

:param hidden: Whether the data in the field is hidden.
    :type hidden: `bool`

:param required: Is this field required?
    :type required: `bool`

:param value: The value of the data in the field.
    :type value: `str` or `None`
    """

    def __init__(self, id: str, label: str, type: GameCategoryDataFieldTypes,
                 input_type: GameCategoryDataFieldInputTypes, copyable: bool, 
                 hidden: bool, required: bool, value: str | None):
        self.id: str = id
""" ID of the data field. """
        self.label: str = label
""" The inscription is the name of the field. """
        self.type: GameCategoryDataFieldTypes = type
""" Data field type. """
        self.input_type: GameCategoryDataFieldInputTypes = input_type
""" Type of field value to be entered. """
        self.copyable: bool = copyable
""" Whether copying of a value from a field is allowed. """
        self.hidden: bool = hidden
""" Whether the data in the field is hidden. """
        self.required: bool = required
""" Is this field required. """
        self.value: str | None = value
""" The value of the data in the field. """


class GameCategoryDataFieldPageInfo:
    """
A subclass that describes information about the item data fields page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class GameCategoryDataFieldList:
    """
A class that describes a page of fields with item data.

:param data_fields: Fields with data for an item in a category on the page.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.GameCategoryDataFieldPageInfo`

:param total_count: Total data fields.
    :type total_count: `int`
    """

    def __init__(self, data_fields: list[GameCategoryDataField], 
                 page_info: GameCategoryDataFieldPageInfo, total_count: int):
        self.data_fields: list[GameCategoryDataField] = data_fields
""" Fields with data for an item in a category on the page. """
        self.page_info: GameCategoryDataFieldPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total data fields. """


class GameCategoryProps:
    """
A subclass describing the proportions of a category.

:param min_reviews: Minimum number of reviews.
    :type min_reviews: `int`

:param min_reviews_for_seller: Minimum number of reviews for a seller.
    :type min_reviews_for_seller: `int`
    """

    def __init__(self, min_reviews: int, min_reviews_for_seller: int):
        self.min_reviews: int = min_reviews
""" Minimum number of reviews. """
        self.min_reviews_for_seller: int = min_reviews_for_seller
""" Minimum number of reviews for a seller. """


class GameCategoryOption:
    """
A subclass describing a category option.

:param id: ID options.
    :type id: `str`

:param group: Option group.
    :type group: `str`

:param label: The inscription is the name of the option.
    :type label: `str`

:param type: Type options.
    :type type: `playerokapi.enums.GameCategoryOptionTypes`

:param field: Field name (for payload request to the site).
    :type field: `str`

:param value: Field value (for payload request to the site).
    :type value: `str`

:param value_range_limit: Value range limit.
    :type value_range_limit: `int` or `None`
    """

    def __init__(self, id: str, group: str, label: str, type: GameCategoryOptionTypes,
                 field: str, value: str, value_range_limit: int | None):
        self.id: str = id
""" ID options. """
        self.group: str = group
""" Option group. """
        self.label: str = label
""" The inscription is the name of the option. """
        self.type: GameCategoryOptionTypes = type
""" Type options. """
        self.field: str = field
""" Field name (for payload request to the site). """
        self.value: str = value
""" Field value (for payload request to the site). """
        self.value_range_limit: int | None = value_range_limit
""" Value spread limit. """


class GameCategoryInstruction:
    """
A subclass that describes information about the sales/purchase instructions page in a category.

:param id: ID of the instruction.
    :type id: `str`

:param text: Instruction text.
    :type text: `str`
    """

    def __init__(self, id: str, text: str):
        self.id: str = id
""" Instruction ID. """
        self.text: str = text
""" Text of instructions. """


class GameCategoryInstructionPageInfo:
    """
A subclass that describes instructions for selling/purchasing in a category.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class GameCategoryInstructionList:
    """
A class that describes a page of instructions for selling/purchasing in a category.

:param instructions: Page instructions.
    :type instructions: `list[playerokapi.types.GameCategoryInstruction]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.GameCategoryInstructionPageInfo`

:param total_count: Total instructions.
    :type total_count: `int`
    """

    def __init__(self, instructions: list[GameCategoryInstruction], page_info: GameCategoryInstructionPageInfo,
                 total_count: int):
        self.instructions: list[GameCategoryInstruction] = instructions
""" Page conventions. """
        self.page_info: GameCategoryInstructionPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total instructions. """


class GameCategory:
    """
Game/application category object.

:param id: Category ID.
    :type id: `str`

:param slug: Category page name.
    :type slug: `str`

:param name: Category name.
    :type name: `str`

:param category_id: ID of the parent category.
    :type category_id: `str` or `None`

:param game_id: Category game ID.
    :type game_id: `str` or `None`

:param obtaining: Type obtained.
    :type obtaining: `str` or `None` or `None`

:param options: Category options.
    :type options: `list[playerokapi.types.GameCategoryOption]` or `None`

:param props: Category proportions.
    :type props: `playerokapi.types.GameCategoryProps` or `None`

:param no_comment_from_buyer: No comment from the buyer?
    :type no_comment_from_buyer: `bool` or `None`

:param instruction_for_buyer: Instructions for the buyer.
    :type instruction_for_buyer: `str` or `None`

:param instruction_for_seller: Instructions for the seller.
    :type instruction_for_seller: `str` or `None`

:param use_custom_obtaining: Whether custom obtaining is used.
    :type use_custom_obtaining: `bool`

:param auto_confirm_period: Auto-confirmation period for a transaction in this category.
    :type auto_confirm_period: `playerokapi.enums.GameCategoryAutoConfirmPeriods` or `None`

:param auto_moderation_mode: Whether automatic moderation is enabled.
    :type auto_moderation_mode: `bool` or `None`

:param agreements: Buyer agreements.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]` or `None`

:param fee_multiplier: Commission multiplier.
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
""" Receipt type. """
        self.options: list[GameCategoryOption] | None = options
""" Category options. """
        self.props: str | None = props
""" Category proportions. """
        self.no_comment_from_buyer: bool | None = no_comment_from_buyer
""" No comment from the buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
""" Instructions for the buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
""" Instructions for the seller. """
        self.use_custom_obtaining: bool = use_custom_obtaining
""" Whether custom receiving is used. """
        self.auto_confirm_period: GameCategoryAutoConfirmPeriods | None = auto_confirm_period
""" Auto-confirmation period for transactions of this category. """
        self.auto_moderation_mode: bool | None = auto_moderation_mode
""" Is automatic moderation enabled. """
        self.agreements: list[GameCategoryAgreement] | None = agreements
""" Buyer Agreement. """
        self.fee_multiplier: float | None = fee_multiplier
""" Commission multiplier. """


class Game:
    """
Game/application object.

:param id: Game/application ID.
    :type id: `str`

:param slug: Game/application page name.
    :type slug: `str`

:param name: Name of the game/application.
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

:param name: Name of the game/application.
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
A subclass that describes information about the games page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class GameList:
    """
A class describing the games page.

:param games: Games/applications pages.
    :type games: `list[playerokapi.types.Game]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.ChatPageInfo`

:param total_count: Total games.
    :type total_count: `int`
    """

    def __init__(self, games: list[Game], page_info: GamePageInfo,
                 total_count: int):
        self.games: list[Game] = games
""" Games/applications pages. """
        self.page_info: ChatPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total games. """


class ItemPriorityStatusPriceRange:
    """
A subclass that describes the price range of an item suitable for the definition. priority status.

:param min: Minimum price of the item.
    :type min: `int`

:param max: Maximum price of an item.
    :type max: `int`
    """

    def __init__(self, min: int, max: str):
        self.min: int = min
""" Minimum price of the item (in rubles). """
        self.max: int = max
""" Maximum price of an item (in rubles). """


class ItemPriorityStatus:
    """
A class describing the priority status of an item.

:param id: ID of the priority status.
    :type id: `str`

:param price: Status price (in rubles).
    :type price: `int`

:param name: Name of the status.
    :type name: `str`

:param type: Status type.
    :type type: `playerokapi.enums.PriorityTypes`

:param period: Duration of the status (in days).
    :type period: `str`

:param price_range: Price range of the status item.
    :type price_range: `playerokapi.types.ItemPriorityStatusPriceRange`
    """

    def __init__(self, id: str, price: int, name: str, type: PriorityTypes,
                 period: int, price_range: ItemPriorityStatusPriceRange):
        self.id: str = id
""" Priority Status ID. """
        self.price: int = price
""" Status price (in rubles). """
        self.name: str = name
""" Status name. """
        self.type: PriorityTypes = type
""" Status type. """
        self.period: int = period
""" Status duration (in days). """
        self.price_range: ItemPriorityStatusPriceRange = price_range
""" Price range of the status item. """


class ItemLog:
    """
A subclass that describes an action log with an item.
    
:param id: ID of the logo.
    :type id: `str`
    
:param event: Log event.
    :type event: `playerokapi.enums.ItemLogEvents`
    
:param created_at: Log creation date.
    :type created_at: `str`
    
:param user: Profile of the user who made the log.
    :type user: `playerokapi.types.UserProfile`
    """

    def __init__(self, id: str, event: ItemLogEvents, created_at: str,
                 user: UserProfile):
        self.id: str = id
""" Logo ID. """
        self.event: ItemLogEvents = event
""" Log event. """
        self.created_at: str = created_at
""" Log creation date. """
        self.user: UserProfile = user
""" Profile of the user who made the login. """


class Item:
    """
Item object.

:param id: Item ID.
    :type id: `str`

:param name: Name of the item.
    :type name: `str`

:param description: Description of the item.
    :type description: `str`

:param status: Item status.
    :type status: `playerokapi.enums.ItemStatuses`

:param obtaining_type: Method of obtaining.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

:param price: Item price.
    :type price: `int`

:param raw_price: Price excluding discount.
    :type raw_price: `int`

:param priority_position: Priority position.
    :type priority_position: `int`

:param attachments: Attachment files.
    :type attachments: `list[playerokapi.types.FileObject]`

:param attributes: Attributes of the object.
    :type attributes: `dict`

:param category: Game category of the item.
    :type category: `playerokapi.types.GameCategory`

:param comment: Comment on the item.
    :type comment: `str` or `None`

:param data_fields: Item data fields.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

:param fee_multiplier: Commission multiplier.
    :type fee_multiplier: `float`

:param game: Game profile of the item.
    :type game: `playerokapi.types.GameProfile`

:param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

:param slug: Item page name.
    :type slug: `str`

:param user: The seller's profile.
    :type user: `playerokapi.types.UserProfile`
    """

    def __init__(self, id: str, slug: str, name: str, description: str, obtaining_type: GameCategoryObtainingType | None, price: int, raw_price: int, priority_position: int,
                 attachments: list[FileObject], attributes: dict, category: GameCategory, comment: str | None, data_fields: list[GameCategoryDataField] | None, 
                 fee_multiplier: float, game: GameProfile, seller_type: UserTypes, status: ItemStatuses, user: UserProfile):
        self.id: str = id
""" Subject ID. """
        self.slug: str = slug
""" Item page name. """
        self.name: str = name
""" Subject title. """
        self.description: str = description
""" Description of the item. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
""" Method of receipt. """
        self.price: int = price
""" Price the item. """
        self.raw_price: int = raw_price
""" Price excluding discount. """
        self.priority_position: int = priority_position
""" Priority position. """
        self.attachments: list[FileObject] = attachments
""" Application files. """
        self.attributes: dict = attributes
""" Item attributes. """
        self.category: GameCategory = category
""" Game category of the item. """
        self.comment: str | None = comment
""" Comment on the item. """
        self.data_fields: list[GameCategoryDataField] | None = data_fields
""" Item data fields. """
        self.fee_multiplier: float = fee_multiplier
""" Commission multiplier. """
        self.game: GameProfile = game
""" Game profile of the item. """
        self.seller_type: UserTypes = seller_type
""" Seller type. """
        self.slug: str = slug
""" Item page name. """
        self.status: ItemStatuses = status
""" Item status. """
        self.user: UserProfile = user
""" Seller's profile. """


class MyItem:
    """
The object of its subject.

:param id: Item ID.
    :type id: `str`

:param slug: Item page name.
    :type slug: `str`

:param name: Name of the item.
    :type name: `str`

:param description: Description of the item.
    :type description: `str`

:param status: Item status.
    :type status: `playerokapi.enums.ItemStatuses`

:param obtaining_type: Method of obtaining.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

:param price: Item price.
    :type price: `int`

:param prev_price: Previous price.
    :type prev_price: `int`

:param raw_price: Price excluding discount.
    :type raw_price: `int`

:param priority_position: Priority position.
    :type priority_position: `int`

:param attachments: Attachment files.
    :type attachments: `list[playerokapi.types.FileObject]`

:param attributes: Attributes of the object.
    :type attributes: `dict`

:param category: Game category of the item.
    :type category: `playerokapi.types.GameCategory`

:param comment: Comment on the item.
    :type comment: `str` or `None`

:param data_fields: Item data fields.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

:param fee_multiplier: Commission multiplier.
    :type fee_multiplier: `float`

:param prev_fee_multiplier: Previous commission multiplier.
    :type prev_fee_multiplier: `float`

:param seller_notified_about_fee_change: Whether the seller is notified about the change in commission.
    :type seller_notified_about_fee_change: `bool`

:param game: Game profile of the item.
    :type game: `playerokapi.types.GameProfile`

:param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

:param user: The seller's profile.
    :type user: `playerokapi.types.UserProfile`

:param buyer: Seller profile.
    :type user: `playerokapi.types.UserProfile`

:param priority: Priority status of the item.
    :type priority: `playerokapi.types.PriorityTypes`

:param priority_price: Priority status prices.
    :type priority_price: `int`

:param sequence: Position of the item in the user's product table.
    :type sequence: `int` or `None`

:param status_expiration_date: Priority status expiration date.
    :type status_expiration_date: `str` or `None`

:param status_description: Description of the priority status.
    :type status_description: `str` or `None`

:param status_payment: Payment status (transaction).
    :type status_payment: `playerokapi.types.Transaction` or `None`

:param views_counter: Number of views of the item.
    :type views_counter: `int`

:param is_editable: Is it possible to edit the product.
    :type is_editable: `bool`

:param approval_date: Product publication date.
    :type approval_date: `str` or `None`

:param deleted_at: Date the product was deleted.
    :type deleted_at: `str` or `None`

:param updated_at: Date the product was last updated.
    :type updated_at: `str` or `None`

:param created_at: Product creation date.
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
""" Subject ID. """
        self.slug: str = slug
""" Item page name. """
        self.name: str = name
""" Subject title. """
        self.status: ItemStatuses = status
""" Item status. """
        self.description: str = description
""" Description of the item. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
""" Method of receipt. """
        self.price: int = price
""" Price the item. """
        self.prev_price: int = prev_price
""" Previous price. """
        self.raw_price: int = raw_price
""" Price excluding discount. """
        self.priority_position: int = priority_position
""" Priority position. """
        self.attachments: list[FileObject] = attachments
""" Application files. """
        self.attributes: dict = attributes
""" Item attributes. """
        self.category: GameCategory = category
""" Game category of the item. """
        self.comment: str | None = comment
""" Comment on the item. """
        self.data_fields: list[GameCategoryDataField] | None = data_fields
""" Item data fields. """
        self.fee_multiplier: float = fee_multiplier
""" Commission multiplier. """
        self.prev_fee_multiplier: float = prev_fee_multiplier
""" Previous commission multiplier. """
        self.seller_notified_about_fee_change: bool = seller_notified_about_fee_change
""" Has the seller been notified of the commission change. """
        self.game: GameProfile = game
""" Game profile of the item. """
        self.seller_type: UserTypes = seller_type
""" Seller type. """
        self.user: UserProfile = user
""" Seller's profile. """
        self.buyer: UserProfile = buyer
""" Profile of the buyer of the item (if sold). """
        self.priority: PriorityTypes = priority
""" Item priority status. """
        self.priority_price: int = priority_price
""" Priority status prices. """
        self.sequence: int | None = sequence
""" Position of the item in the user's product table. """
        self.status_expiration_date: str | None = status_expiration_date
""" Priority status expiration date. """
        self.status_description: str | None = status_description
""" Description of the priority status. """
        self.status_payment: str | None = status_payment
""" Payment status (transaction). """
        self.views_counter: int = views_counter
""" Number of views of the item. """
        self.is_editable: bool = is_editable
""" Is it possible to edit a product. """
        self.approval_date: str | None = approval_date
""" Product publication date. """
        self.deleted_at: str | None = deleted_at
""" Date the item was removed. """
        self.updated_at: str | None = updated_at
""" Date of last update of the product. """
        self.created_at: str | None = created_at
""" Date of creation of the product. """


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

:param name: Name of the item.
    :type name: `str`

:param price: Item price.
    :type price: `int`

:param raw_price: Price excluding discount.
    :type raw_price: `int`

:param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

:param attachment: File attachment.
    :type attachment: `playerokapi.types.FileObject`

:param user: The seller's profile.
    :type user: `playerokapi.types.UserProfile`

:param approval_date: Approval date.
    :type approval_date: `str`

:param priority_position: Priority position.
    :type priority_position: `int`

:param views_counter: Number of views.
    :type views_counter: `int` or `None`

:param fee_multiplier: Commission multiplier.
    :type fee_multiplier: `float`

:param created_at: Creation date.
    :type created_at: `str`
    """

    def __init__(self, id: str, slug: str, priority: PriorityTypes, status: ItemStatuses,
                 name: str, price: int, raw_price: int, seller_type: UserTypes, attachment: FileObject,
                 user: UserProfile, approval_date: str, priority_position: int, views_counter: int | None, 
                 fee_multiplier: float, created_at: str):
        self.id: str = id
""" Subject ID. """
        self.slug: str = slug
""" Item page name. """
        self.priority: PriorityTypes = priority
""" Item priority. """
        self.status: ItemStatuses = status
""" Item status. """
        self.name: str = name
""" Subject title. """
        self.price: int = price
""" Price the item. """
        self.raw_price: int = raw_price
""" Price excluding discount. """
        self.seller_type: UserTypes = seller_type
""" Seller type. """
        self.attachment: FileObject = attachment
""" File attachment. """
        self.user: UserProfile = user
""" Seller's profile. """
        self.approval_date: str = approval_date
""" Date approved. """
        self.priority_position: int = priority_position
""" Priority position. """
        self.views_counter: int | None = views_counter
""" Number of views. """
        self.fee_multiplier: float = fee_multiplier
""" Commission multiplier. """
        self.created_at: str = created_at
""" Creation date. """


class ItemProfilePageInfo:
    """
A subclass that describes information about the items page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class ItemProfileList:
    """
Items page profile.

:param items: Page items.
    :type items: `list[playerokapi.types.Item]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.ItemProfilePageInfo`

:param total_count: Total items.
    :type total_count: `int`
    """

    def __init__(self, items: list[ItemProfile], page_info: ItemProfilePageInfo,
                 total_count: int):
        self.items: list[ItemProfile] = items
""" Page items. """
        self.page_info: ItemProfilePageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total items. """


class SBPBankMember:
    """
Object of SBP Bank members.

    :param id: ID.
    :type id: `str`

:param name: Name.
    :type name: `str`

:param icon: URL of the icon.
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
Payment method of the transaction.

:param id: Method ID.
    :type id: `playerokapi.types.TransactionPaymentMethodIds`

:param name: Name of the method.
    :type name: `str`

:param fee: Method commission.
    :type fee: `int`

:param provider_id: ID of the transaction provider.
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
""" Commission method. """
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

:param incoming: For replenishment.
    :type incoming: `playerokapi.types.TransactionProviderLimitRange`

:param outgoing: To output.
    :type outgoing: `playerokapi.types.TransactionProviderLimitRange`
    """

    def __init__(self, incoming: TransactionProviderLimitRange, outgoing: TransactionProviderLimitRange):
        self.incoming: TransactionProviderLimitRange = incoming
""" For replenishment. """
        self.outgoing: TransactionProviderLimitRange = outgoing
""" To conclusion. """


class TransactionProviderRequiredUserData:
    """
Required transaction provider user data.

:param email: Is it necessary to specify EMail?
    :type email: `bool`

:param phone_number: Is it necessary to indicate a phone number?
    :type phone_number: `bool`

:param erip_account_number: Is it mandatory to specify the ERIP account number?
    :type erip_account_number: `bool` or `None`
    """

    def __init__(self, email: bool, phone_number: bool, 
                 erip_account_number: bool | None):
        self.email: bool = email
""" Is it necessary to indicate EMail? """
        self.phone_number: bool = phone_number
""" Is it necessary to indicate a phone number? """
        self.erip_account_number: bool | None = erip_account_number
""" Is it necessary to specify an ERIP account number? """


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
""" Clue. """


class TransactionProvider:
    """
Transaction provider object.

:param id: Provider ID.
    :type id: `playerokapi.enums.TransactionProviderIds`

:param name: Provider name.
    :type name: `str`

:param fee: Provider commission.
    :type fee: `int`

:param min_fee_amount: Minimum commission.
    :type min_fee_amount: `int` or `None`

:param description: Description of the provider.
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
""" Provider commission. """
        self.min_fee_amount: int | None = min_fee_amount
""" Minimum commission. """
        self.description: str | None = description
""" Description of the provider. """
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

:param operation: Type of operation performed.
    :type operation: `playerokapi.enums.TransactionOperations`

:param direction: Transaction direction.
    :type direction: `playerokapi.enums.TransactionDirections`

:param provider_id: Payment provider ID.
    :type provider_id: `playerokapi.enums.TransactionProviderIds`

:param provider: Transaction provider object.
    :type provider: `playerokapi.types.TransactionProvider`

:param user: Transaction user object.
    :type user: `playerokapi.types.UserProfile`

:param creator: Object of the user who created the transaction.
    :type creator: `playerokapi.types.UserProfile` or `None`

:param status: Transaction processing status.
    :type status: `playerokapi.enums.TransactionStatuses`

:param status_description: Description of the status.
    :type status_description: `str` or `None`

:param status_expiration_date: Status expiration date.
    :type status_expiration_date: `str` or `None`

:param value: Transaction amount.
    :type value: `int`

:param fee: Transaction commission.
    :type fee: `int`

:param created_at: Date the transaction was created.
    :type created_at: `str`

:param verified_at: Transaction confirmation date.
    :type verified_at: `str` or `None`

:param verified_by: Object of the user who confirmed the transaction.
    :type verified_by: `playerokapi.types.UserProfile` or `None`

:param completed_at: The date the transaction was completed.
    :type completed_at: `str` or `None`

:param completed_by: Object of the user who completed the transaction.
    :type completed_by: `playerokapi.types.UserProfile` or `None`

:param payment_method_id: Payment method ID.
    :type payment_method_id: `str` or `None`

:param is_suspicious: Is the transaction suspicious?
    :type is_suspicious: `bool` or `None`

:param sbp_bank_name: SBP bank name (if the transaction was made using SBP).
    :type sbp_bank_name: `str` or `None`
    """

    def __init__(self, id: str, operation: TransactionOperations, direction: TransactionDirections, provider_id: TransactionProviderIds, 
                 provider: TransactionProvider, user: UserProfile, creator: UserProfile, status: TransactionStatuses, status_description: str | None, 
                 status_expiration_date: str | None, value: int, fee: int, created_at: str, verified_at: str | None, verified_by: UserProfile | None, 
                 completed_at: str | None, completed_by: UserProfile | None, payment_method_id: str | None, is_suspicious: bool | None, sbp_bank_name: str | None):
        self.id: str = id
""" Transaction ID. """
        self.operation: TransactionOperations = operation
""" Type of operation performed. """
        self.direction: TransactionDirections = direction
""" Transaction direction. """
        self.provider_id: TransactionProviderIds = provider_id
""" Payment provider ID. """
        self.provider: TransactionProvider = provider
""" Transaction provider object. """
        self.user: UserProfile = user
""" Object of the user who performed the transaction. """
        self.creator: UserProfile | None = creator
""" Object of the user who created the transaction. """
        self.status: TransactionStatuses = status
""" Transaction processing status. """
        self.status_description: str | None = status_description
""" Description of status. """
        self.status_expiration_date: str | None = status_expiration_date
""" Status expiration date. """
        self.value: int = value
""" Transaction amount. """
        self.fee: int = fee
""" Transaction fee. """
        self.created_at: str = created_at
""" Transaction creation date. """
        self.verified_at: str | None = verified_at
""" Transaction confirmation date. """
        self.verified_by: UserProfile | None = verified_by
""" Object of the user who confirmed the transaction. """
        self.completed_at: str | None = completed_at
""" Transaction execution date. """
        self.completed_by: UserProfile | None = completed_by
""" The object of the user who performed the transaction. """
        self.payment_method_id: str | None = payment_method_id
""" Payment method ID. """
        self.is_suspicious: bool | None = is_suspicious
""" Is the transaction suspicious. """
        self.sbp_bank_name: str | None = sbp_bank_name
""" SBP bank name (if the transaction was completed using SBP). """


class TransactionPageInfo:
    """
A subclass that describes transaction page information.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class TransactionList:
    """
A class that describes a chat message page.

:param transactions: Page transactions.
    :type transactions: `list[playerokapi.types.Transaction]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.TransactionPageInfo`

:param total_count: Total transactions on the page.
    :type total_count: `int`
    """

    def __init__(self, transactions: list[Transaction], page_info: TransactionPageInfo,
                 total_count: int):
        self.transactions: list[Transaction] = transactions
""" Page transactions. """
        self.page_info: TransactionPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total transactions on the page. """


class UserBankCard:
    """
User's bank card object.

:param id: Card ID.
    :type id: `str`

:param card_first_six: The first six digits of the card.
    :type card_first_six: `str`

:param card_last_four: Last four digits of the card.
    :type card_last_four: `str`

:param card_type: Bank card type.
    :type card_type: `playerokapi.enums.BankCardTypes`

:param is_chosen: Is this map selected as the default?
    :type is_chosen: `bool`
    """

    def __init__(self, id: str, card_first_six: str, card_last_four: str,
                 card_type: BankCardTypes, is_chosen: bool):
        self.id: str = id
""" Card ID. """
        self.card_first_six: str = card_first_six
""" First six digits of the card. """
        self.card_last_four: str = card_last_four
""" Last four digits of the card. """
        self.card_type: BankCardTypes = card_type
""" Bank card type. """
        self.is_chosen: bool = is_chosen
""" Is this map selected as the default? """


class UserBankCardPageInfo:
    """
A subclass that describes information about the user's bank cards page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class UserBankCardList:
    """
A class describing the user's bank cards page.

:param bank_cards: Bank cards page.
    :type bank_cards: `list[playerokapi.types.UserBankCard]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.UserBankCardPageInfo`

:param total_count: Total bank cards on the page.
    :type total_count: `int`
    """

    def __init__(self, bank_cards: list[UserBankCard], 
                 page_info: UserBankCardPageInfo, total_count: int):
        self.bank_cards: list[UserBankCard] = bank_cards
""" Bank cards pages. """
        self.page_info: UserBankCardPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total bank cards on the page. """


class Moderator:
# TODO: Make a moderator class Moderator

    def __init__(self):
        pass


class ChatMessageButton:
    """
Message button object.

:param type: Button type.
    :type type: `playerokapi.types.ChatMessageButtonTypes`

:param url: URL of buttons.
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
A class describing a chat message.

:param id: Message ID.
    :type id: `str`

:param text: Message text.
    :type text: `str`

:param created_at: Date the message was created.
    :type created_at: `str`

:param deleted_at: Date the message was deleted.
    :type deleted_at: `str` or `None`

:param is_read: Whether the message has been read.
    :type is_read: `bool`

:param is_suspicious: Is the message suspicious?
    :type is_suspicious: `bool`

:param is_bulk_messaging: Is this a mass mailing?
    :type is_bulk_messaging: `bool`

:param game: The game the message refers to.
    :type game: `str` or `None`

:param file: File attached to the message.
    :type file: `playerokapi.types.FileObject` or `None`

:param user: The user who sent the message.
    :type user: `playerokapi.types.UserProfile`

:param deal: The deal the message refers to.
    :type deal: `playerokapi.types.Deal` or `None`

:param item: The item the message relates to (usually only the deal itself is passed to the deal variable).
    :type item: `playerokapi.types.Item` or `None`

:param transaction: Message transaction.
    :type transaction: `playerokapi.types.Transaction` or `None`

:param moderator: Message moderator.
    :type moderator: `playerokapi.types.Moderator`

:param event_by_user: Event from the user.
    :type event_by_user: `playerokapi.types.UserProfile` or `None`

:param event_to_user: Event for the user.
    :type event_to_user: `playerokapi.types.UserProfile` or `None`

:param is_auto_response: Is this an auto-response?
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
""" Date the message was created. """
        self.deleted_at: str | None = deleted_at
""" Date the message was deleted. """
        self.is_read: bool = is_read
""" Has the message been read. """
        self.is_suspicious: bool = is_suspicious
""" Is the message suspicious. """
        self.is_bulk_messaging: bool = is_bulk_messaging
""" Is this a mass mailing. """
        self.game: Game | None  = game
""" Game the message refers to. """
        self.file: FileObject | None  = file
""" File attached to message. """
        self.user: UserProfile = user
""" The user who sent the message. """
        self.deal: ItemDeal | None = deal
""" The transaction to which the message relates. """
        self.item: ItemProfile | None = item
""" The item to which the message relates (usually only the deal itself is transferred to the deal variable). """
        self.transaction: Transaction | None = transaction
""" Message transaction. """
        self.moderator: Moderator = moderator
""" Message moderator. """
        self.event_by_user: UserProfile | None = event_by_user
""" Event from the user. """
        self.event_to_user: UserProfile | None = event_to_user
""" Event for the user. """
        self.is_auto_response: bool = is_auto_response
""" Is this an auto-response. """
        self.event: Event | None = event
""" Event messages. """
        self.buttons: list[ChatMessageButton] = buttons
""" Message buttons. """


class ChatMessagePageInfo:
    """
A subclass that describes information about the messages page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class ChatMessageList:
    """
A class that describes a chat message page.

:param messages: Page messages.
    :type messages: `list[playerokapi.types.ChatMessage]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.ChatMessagePageInfo`

:param total_count: Total messages in the chat.
    :type total_count: `int`
    """

    def __init__(self, messages: list[ChatMessage], page_info: ChatMessagePageInfo,
                 total_count: int):
        self.messages: list[ChatMessage] = messages
""" Page messages. """
        self.page_info: ChatMessagePageInfo = page_info
""" Information about the page. """
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

:param bookmarked: Is the chat bookmarked?
    :type bookmarked: `bool` or `None`

:param is_texting_allowed: Is it allowed to write in the chat.
    :type is_texting_allowed: `bool` or `None`

:param owner: The owner of the chat (only if it is a chat with a bot).
    :type owner: `bool` or `None`

:param deals: Deals in chat.
    :type deals: `list[playerokapi.types.ItemDeal]` or `None`

:param last_message: Last chat message object
    :type last_message: `playerokapi.types.ChatMessage` or `None`

:param users: Chat participants.
    :type users: `list[UserProfile]`

:param started_at: Dialogue start date.
    :type started_at: `str` or `None`

:param finished_at: The date the dialogue was completed.
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
""" I bookmarked chat. """
        self.is_texting_allowed: bool | None = is_texting_allowed
""" Is it allowed to write in the chat. """
        self.owner: UserProfile = owner
""" Chat owner. """
        self.deals: list[ItemDeal] | None = deals
""" Chat transactions. """
        self.last_message: ChatMessage | None = last_message
""" Object of the last chat message. """
        self.users: list[UserProfile] = users
""" Chat participants. """
        self.started_at: str | None = started_at
""" Start date of the dialogue. """
        self.finished_at: str | None = finished_at
""" Date the dialogue ended. """


class ChatPageInfo:
    """
A subclass that describes information about the chats page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class ChatList:
    """
A class describing a chat page.

:param chats: Chat pages.
    :type chats: `list[playerokapi.types.Chat]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.ChatPageInfo`

:param total_count: Total chats.
    :type total_count: `int`
    """

    def __init__(self, chats: list[Chat], page_info: ChatPageInfo,
                 total_count: int):
        self.chats: list[Chat] = chats
""" Chat pages. """
        self.page_info: ChatPageInfo = page_info
""" Information about the page. """
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

:param created_at: Date the review was created.
    :type created_at: `str`

:param updated_at: Date the review was modified.
    :type updated_at: `str`

:param deal: Deal associated with the review.
    :type deal: `Deal`

:param creator: Profile of the review creator.
    :type creator: `UserProfile`

:param moderator: The moderator who processed the review.
    :type moderator: `Moderator` or `None`

:param user: Profile of the seller to whom the review relates.
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
""" Date the review was created. """
        self.updated_at: str = updated_at
""" Date the review was modified. """
        self.deal: ItemDeal = deal
""" Transaction associated with a review. """
        self.creator: UserProfile = creator
""" Profile of the review creator. """
        self.moderator: Moderator | None = moderator
""" Moderator who processed the review. """
        self.user: UserProfile = user
""" Profile of the seller to whom the review relates. """


class ReviewPageInfo:
    """
A subclass that describes information about the reviews page.

:param start_cursor: Page start cursor.
    :type start_cursor: `str`

:param end_cursor: End of page cursor.
    :type end_cursor: `str`

:param has_previous_page: Whether it has a previous page.
    :type has_previous_page: `bool`

:param has_next_page: Whether it has a next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
""" Start of page cursor. """
        self.end_cursor: str = end_cursor
""" End of page cursor. """
        self.has_previous_page: bool = has_previous_page
""" Whether there is a previous page. """
        self.has_next_page: bool = has_next_page
""" Does the next page have """


class ReviewList:
    """
A class that describes the reviews page.

:param reviews: Reviews page.
    :type reviews: `list[playerokapi.types.Review]`

:param page_info: Information about the page.
    :type page_info: `playerokapi.types.ReviewPageInfo`

:param total_count: Total reviews.
    :type total_count: `int`
    """

    def __init__(self, reviews: list[Review], page_info: ReviewPageInfo,
                 total_count: int):
        self.reviews: list[Review] = reviews
""" Reviews page. """
        self.page_info: ReviewPageInfo = page_info
""" Information about the page. """
        self.total_count: int = total_count
""" Total reviews. """