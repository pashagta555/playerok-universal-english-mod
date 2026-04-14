from __future__ import annotations
from typing import *
import json

from . import parser
from .enums import *
from .misc import PERSISTED_QUERIES



class FileObject:
    """
    Object file.

    :param id: ID file.
    :type id: `str`

    :param url: URL file.
    :type url: `str`

    :param filename: Name file.
    :type filename: `str` or `None`

    :param mime: Mime file.
    :type mime: `str` or `None`
    """

    def __init__(self, id: str, url: str, 
                 filename: str | None, mime: str | None):
        self.id: str = id
        """ ID file. """
        self.url: str = url
        """ URL file. """
        self.filename: str | None = filename
        """ Name file. """
        self.mime: str | None = mime
        """ Mime file. """


class AccountBalance:
    """
    Subclass, describing balance account.

    :param id: ID balance.
    :type id: `str`

    :param value: Sum balance.
    :type value: `int`

    :param frozen: Sum frozen balance.
    :type frozen: `int`

    :param available: Sum affordable balance.
    :type available: `int`

    :param withdrawable: Sum balance, affordable For output.
    :type withdrawable: `int`

    :param pending_income: Expected income.
    :type pending_income: `int`
    """

    def __init__(self, id: str, value: int, frozen: int, available: int, 
                 withdrawable: int, pending_income: int):
        self.id: str = id
        """ ID balance. """
        self.value: int = value
        """ Sum general balance. """
        self.frozen: int = frozen
        """ Sum frozen balance. """
        self.available: int = available
        """ Sum affordable balance. """
        self.withdrawable: int = withdrawable
        """ Sum balance, affordable For output. """
        self.pending_income: int = pending_income
        """ Expected income. """


class AccountIncomingDealsStats:
    """
    Subclass, describing statistics incoming transactions account.

    :param total: Total outgoing transactions.
    :type total: `int`

    :param finished: Completed outgoing transactions.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total: int = total
        """ Total outgoing transactions. """
        self.finished: int = finished
        """ Number-in completed outgoing transactions. """


class AccountOutgoingDealsStats:
    """
    Subclass, describing statistics outgoing transactions account.

    :param total: Total outgoing transactions.
    :type total: `int`

    :param finished: Completed outgoing transactions.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total = total
        """ Total outgoing transactions. """
        self.finished = finished
        """ Number-in completed outgoing transactions. """


class AccountDealsStats:
    """
    Subclass, describing statistics transactions account.

    :param incoming: Inbox deals.
    :type incoming: `playerokapi.types.AccountIncomingDealsStats`

    :param outgoing: Outgoing deals.
    :type outgoing: `playerokapi.types.AccountOutgoingDealsStats`
    """

    def __init__(self, incoming: AccountIncomingDealsStats, outgoing: AccountOutgoingDealsStats):
        self.incoming: AccountIncomingDealsStats = incoming
        """ Inbox deals. """
        self.outgoing: AccountOutgoingDealsStats = outgoing
        """ Outgoing deals. """


class AccountItemsStats:
    """
    Subclass, describing statistics items account.

    :param total: Total items.
    :type total: `int`

    :param finished: Completed items.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total: int = total
        """ Total items. """
        self.finished: int = finished
        """ Number-in completed items. """


class AccountStats:
    """
    Subclass, describing statistics account.

    :param items: Statistics items.
    :type items: `playerokapi.types.AccountItemsStats`

    :param deals: Statistics transactions.
    :type deals: `playerokapi.types.AccountDealsStats`
    """

    def __init__(self, items: AccountItemsStats, deals: AccountDealsStats):
        self.items: AccountItemsStats = items
        """ Statistics items. """
        self.deals: AccountDealsStats = deals
        """ Statistics transactions. """


class AccountProfile:
    """
    Class, describing profile account.

    :param id: ID account.
    :type id: `str`

    :param username: Nickname account.
    :type username: `str`

    :param email: Mail account.
    :type email: `str`

    :param balance: Object balance account.
    :type balance: `playerokapi.types.AccountBalance`

    :param stats: Statistics account.
    :type stats: `str`

    :param role: Role account.
    :type role: `playerokapi.enums.UserTypes`

    :param avatar_url: URL avatar account.
    :type avatar_url: `str`

    :param is_online: IN online whether Now account.
    :type is_online: `bool`

    :param is_blocked: Blocked whether account.
    :type is_blocked: `bool`

    :param is_blocked_for: Cause blocking.
    :type is_blocked_for: `str`

    :param is_verified: Verified whether account.
    :type is_verified: `bool`

    :param rating: Rating account (0-5).
    :type rating: `int`

    :param reviews_count: Number-in reviews on account.
    :type reviews_count: `int`

    :param created_at: Date creation account.
    :type created_at: `str`

    :param support_chat_id: ID chat support.
    :type support_chat_id: `str`

    :param system_chat_id: ID systemic chat.
    :type system_chat_id: `str`

    :param has_frozen_balance: Frozen whether balance on account.
    :type has_frozen_balance: `bool`

    :param has_enabled_notifications: Included whether notifications on account.
    :type has_enabled_notifications: `bool`

    :param unread_chats_counter: Quantity unread chats.
    :type unread_chats_counter: `int` or `None`
    """

    def __init__(self, id: str, username: str, email: str, balance: AccountBalance, stats: AccountStats, role: UserTypes, avatar_url: str, is_online: bool, is_blocked: bool,
                 is_blocked_for: str, is_verified: bool, rating: int, reviews_count: int, created_at: str, support_chat_id: str, system_chat_id: str,
                 has_frozen_balance: bool, has_enabled_notifications: bool, unread_chats_counter: int | None):
        self.id: str = id
        """ ID account. """
        self.username: str = username
        """ Nickname account. """
        self.email: str = email
        """ Mail account. """
        self.balance: AccountBalance = balance
        """ Object balance account. """
        self.stats: AccountStats = stats
        """ Statistics account. """
        self.role: UserTypes  = role
        """ Role account. """
        self.avatar_url: str = avatar_url
        """ URL avatar account. """
        self.is_online: bool = is_online
        """ IN online whether Now account. """
        self.is_blocked: bool = is_blocked
        """ Blocked whether account. """
        self.is_blocked_for: str = is_blocked_for
        """ Cause blocking account. """
        self.is_verified: bool = is_verified
        """ Verified whether account. """
        self.rating: int = rating
        """ Rating account (0-5). """
        self.reviews_count: int = reviews_count
        """ Number-in reviews on account. """
        self.created_at: str = created_at
        """ Date creation account. """
        self.support_chat_id: str = support_chat_id
        """ ID chat support account. """
        self.system_chat_id: str = system_chat_id
        """ ID systemic chat account. """
        self.has_frozen_balance: bool = has_frozen_balance
        """ Frozen whether balance on account. """
        self.has_enabled_notifications: bool = has_enabled_notifications
        """ Included whether notifications on account. """
        self.unread_chats_counter: bool | None = unread_chats_counter
        """ Quantity unread messages. """


class UserProfile:
    """
    Class, describing profile user.

    :param id: ID user.
    :type id: `str`

    :param username: Nickname user.
    :type username: `str`

    :param role: Role user.
    :type role: `playerokapi.enums.UserTypes`

    :param avatar_url: URL avatar user.
    :type avatar_url: `str`

    :param is_online: IN online whether Now user.
    :type is_online: `bool`

    :param is_blocked: Blocked whether user.
    :type is_blocked: `bool`

    :param rating: Rating user (0-5).
    :type rating: `int`

    :param reviews_count: Number-in reviews user.
    :type reviews_count: `int`

    :param support_chat_id: ID chat support.
    :type support_chat_id: `str` or `None`

    :param system_chat_id: ID systemic chat.
    :type system_chat_id: `str` or `None`

    :param created_at: Date creation account user.
    :type created_at: `str`
    """

    def __init__(self, id: str, username: str, role: UserTypes, avatar_url: str, is_online: bool, is_blocked: bool, 
                 rating: int, reviews_count: int, support_chat_id: str, system_chat_id: str | None, created_at: str | None):
        self.id: str = id
        """ ID user. """
        self.username: str = username
        """ Nickname user. """
        self.role: UserTypes = role
        """ Role user. """
        self.avatar_url: str = avatar_url
        """ URL avatar. """
        self.is_online: bool = is_online
        """ IN online whether Now user. """
        self.is_blocked: bool = is_blocked
        """ Blocked whether user. """
        self.rating: int = rating
        """ Rating user (0-5). """
        self.reviews_count: int = reviews_count
        """ Number-in reviews user. """
        self.support_chat_id: str | None = support_chat_id
        """ ID chat support. """
        self.system_chat_id: str | None = system_chat_id
        """ ID systemic chat. """
        self.created_at: str = created_at
        """ Date creation account user. """


    def get_items(
        self, 
        count: int = 24, 
        game_id: str | None = None, 
        category_id: str | None = None, 
        statuses: list[ItemStatuses] | None = None,
        after_cursor: str | None = None
    ) -> ItemProfileList:
        """
        Receives items user.

        :param count: Number-in items, which need to get (Not more 24 for one request), _optional_.
        :type count: `int`
        
        :param game_id: ID games/applications, whose items need to get, _optional_.
        :type game_id: `str` or `None`

        :param category_id: ID categories games/applications, whose items need to get, _optional_.
        :type category_id: `str` or `None`

        :param status: Array types items, which need to get. Some statuses Can get only, If This profile your account. If Not indicated, receives straightaway All possible.
        :type status: `list[playerokapi.enums.ItemStatuses]`

        :param after_cursor: Cursor, With whom will go parsing (If There is not - looking for With himself started pages), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page profiles items.
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
        Receives reviews user.

        :param count: Number-in reviews, which need to get (Not more 24 for one request), _optional_.
        :type count: `int`

        :param status: Type reviews, which need to get.
        :type status: `playerokapi.enums.ReviewStatuses`

        :param comment_required: Required whether comment V review, _optional_.
        :type comment_required: `bool`

        :param rating: Rating reviews (1-5), _optional_.
        :type rating: `int` or `None`

        :param game_id: ID games reviews, _optional_.
        :type game_id: `str` or `None`

        :param category_id: ID categories reviews, _optional_.
        :type category_id: `str` or `None`

        :param min_item_price: Minimum price subject review, _optional_.
        :type min_item_price: `bool` or `None`

        :param max_item_price: Maximum price subject review, _optional_.
        :type max_item_price: `bool` or `None`

        :param sort_direction: Type sorting.
        :type sort_direction: `playerokapi.enums.SortDirections`

        :param sort_field: Field, By to whom will go sorting (By default `createdAt` - By date)
        :type sort_field: `str`

        :param after_cursor: Cursor, With whom will go parsing (If There is not - looking for With himself started pages), _optional_.
        :type after_cursor: `str` or `None`
        
        :return: Page reviews.
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
    #TODO: Do Class event Event

    def __init__(self):
        pass


class ItemDeal:
    """
    Object deals With subject.

    :param id: ID deals.
    :type id: `str`

    :param status: Status deals.
    :type status: `playerokapi.enums.ItemDealStatuses`

    :param status_expiration_date: Date expiration status.
    :type status_expiration_date: `str` or `None`

    :param status_description: Description status deals.
    :type status_description: `str` or `None`

    :param direction: Direction deals (purchase/sale).
    :type direction: `playerokapi.enums.ItemDealDirections`

    :param obtaining: Receipt deals.
    :type obtaining: `str` or `None`

    :param has_problem: Eat whether problem V deal.
    :type has_problem: `bool`

    :param report_problem_enabled: Included whether appeal problems.
    :type report_problem_enabled: `bool` or `None`

    :param completed_user: Profile user, confirmed deal.
    :type completed_user: `playerokapi.types.UserProfile` or `None`

    :param props: Details deals.
    :type props: `str` or `None`

    :param previous_status: Previous status.
    :type previous_status: `playerokapi.enums.ItemDealStatuses` or `None`

    :param completed_at: Date confirmation deals.
    :type completed_at: `str` or `None`

    :param created_at: Date creation deals.
    :type created_at: `str` or `None`

    :param logs: Logs deals.
    :type logs: `list[playerokapi.types.ItemLog]` or `None`

    :param transaction: Transaction deals.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param user: Profile user, committed deal.
    :type user: `playerokapi.types.UserProfile`

    :param chat: Chat deals (transmitted only his ID).
    :type chat: `playerokapi.types.Chat` or `None`

    :param item: Item deals.
    :type item: `playerokapi.types.Item`

    :param review: Review By deal.
    :type review: `playerokapi.types.Review` or `None`

    :param obtaining_fields: Received fields.
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
        """ ID deals. """
        self.status: ItemDealStatuses = status
        """ Status deals. """
        self.status_expiration_date: str | None = status_expiration_date
        """ Date expiration status. """
        self.status_description: str | None = status_description
        """ Description status deals. """
        self.direction: ItemDealDirections = direction
        """ Direction deals (purchase/sale). """
        self.obtaining: str | None = obtaining
        """ Receipt deals. """
        self.has_problem: bool = has_problem
        """ Eat whether problem V deal. """
        self.report_problem_enabled: bool | None = report_problem_enabled
        """ Included whether appeal problems. """
        self.completed_user: UserProfile | None = completed_user
        """ Profile user, confirmed deal. """
        self.props: str | None = props
        """ Details deals. """
        self.previous_status: ItemDealStatuses | None = previous_status
        """ Previous status. """
        self.completed_at: str | None = completed_at
        """ Date confirmation deals. """
        self.created_at: str | None = created_at
        """ Date creation deals. """
        self.logs: list[ItemLog] | None = logs
        """ Logs deals. """
        self.transaction: Transaction | None = transaction
        """ Transaction deals. """
        self.user: UserProfile = user
        """ Profile user, committed deal. """
        self.chat: Chat | None = chat
        """ Chat deals (transmitted only his ID). """
        self.item: Item = item
        """ Item deals. """
        self.review: Review | None = review
        """ Review By deal. """
        self.obtaining_fields: list[GameCategoryDataField] | None = obtaining_fields
        """ Received fields. """
        self.comment_from_buyer: str | None = comment_from_buyer
        """ Comment from buyer. """


class ItemDealPageInfo:
    """
    Subclass, describing information O page transactions.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class ItemDealList:
    """
    Class, describing page reviews.

    :param deals: Transactions pages.
    :type deals: `list[playerokapi.types.ItemDeal]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.ItemDealPageInfo`

    :param total_count: Total transactions.
    :type total_count: `int`
    """

    def __init__(self, deals: list[ItemDeal], page_info: ItemDealPageInfo,
                 total_count: int):
        self.deals: list[ItemDeal] = deals
        """ Transactions pages. """
        self.page_info: ItemDealPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total transactions. """


class GameCategoryAgreement:
    """
    Subclass, describing agreements buyer.

    :param id: ID agreements.
    :type id: `str`

    :param description: Description agreements.
    :type description: `str`

    :param icontype: Type icons agreements.
    :type icontype: `playerokapi.enums.GameCategoryAgreementIconTypes`

    :param sequence: Subsequence agreements.
    :type sequence: `str`
    """

    def __init__(self, id: str, description: str, 
                 icontype: GameCategoryAgreementIconTypes, sequence: int):
        self.id: str = id
        """ ID agreements. """
        self.description: str = description
        """ Description agreements. """
        self.icontype: GameCategoryAgreementIconTypes = icontype
        """ Type icons agreements. """
        self.sequence: str = sequence
        """ Subsequence agreements. """


class GameCategoryAgreementPageInfo:
    """
    Subclass, describing information O page agreements buyer.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class GameCategoryAgreementList:
    """
    Class, describing page agreements buyer.

    :param agreements: Agreements pages.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.GameCategoryAgreementPageInfo`

    :param total_count: Total agreements.
    :type total_count: `int`
    """

    def __init__(self, agreements: list[GameCategoryAgreement], page_info: GameCategoryAgreementPageInfo,
                 total_count: int):
        self.agreements: list[GameCategoryAgreement] = agreements
        """ Agreements pages. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total agreements. """


class GameCategoryObtainingType:
    """
    Subclass, describing type (way) receiving subject V categories.

    :param id: ID way.
    :type id: `str`

    :param name: Name way.
    :type name: `str`

    :param description: Description way.
    :type description: `str`

    :param game_category_id: ID categories games way.
    :type game_category_id: `str`

    :param no_comment_from_buyer: Without comments from buyer?
    :type no_comment_from_buyer: `bool`

    :param instruction_for_buyer: Instructions For buyer.
    :type instruction_for_buyer: `str`

    :param instruction_for_seller: Instructions For seller.
    :type instruction_for_seller: `str`

    :param sequence: Subsequence way.
    :type sequence: `int`

    :param fee_multiplier: Factor commissions.
    :type fee_multiplier: `float`

    :param agreements: Agreements buyer on purchase/seller on sale.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param props: Proportions categories.
    :type props: `playerokapi.types.GameCategoryProps`
    """

    def __init__(self, id: str, name: str, description: str, game_category_id: str, no_comment_from_buyer: bool,
                 instruction_for_buyer: str | None, instruction_for_seller: str | None, sequence: int, fee_multiplier: float,
                 agreements: list[GameCategoryAgreement], props: GameCategoryProps):
        self.id: str = id
        """ ID way. """
        self.name: str = name
        """ Name way. """
        self.description: str = description
        """ Description way. """
        self.game_category_id: str = game_category_id
        """ ID categories games way. """
        self.no_comment_from_buyer: bool = no_comment_from_buyer
        """ Without comments from buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
        """ Instructions For buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
        """ Instructions For seller. """
        self.sequence: int = sequence
        """ Subsequence way. """
        self.fee_multiplier: float = fee_multiplier
        """ Factor commissions. """
        self.agreements: list[GameCategoryAgreement] = agreements
        """ Agreements buyer on purchase/seller on sale. """
        self.props: GameCategoryProps = props
        """ Proportions categories. """


class GameCategoryObtainingTypePageInfo:
    """
    Subclass, describing information O page types (ways) receiving subject V categories.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class GameCategoryObtainingTypeList:
    """
    Class, describing page types (ways) receiving subject V categories.

    :param obtaining_types: Methods pages.
    :type obtaining_types: `list[playerokapi.types.GameCategoryObtainingType]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.GameCategoryObtainingTypePageInfo`

    :param total_count: Total ways.
    :type total_count: `int`
    """

    def __init__(self, obtaining_types: list[GameCategoryObtainingType], page_info: GameCategoryObtainingTypePageInfo,
                 total_count: int):
        self.obtaining_types: list[GameCategoryObtainingType] = obtaining_types
        """ Agreements pages. """
        self.page_info: GameCategoryAgreementPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total ways. """


class GameCategoryDataField:
    """
    Subclass, describing fields With data subject V categories (which are sent after purchases).

    :param id: ID fields With data.
    :type id: `str`

    :param label: Inscription-Name fields.
    :type label: `str`

    :param type: Type fields With data.
    :type type: `playerokapi.enums.GameCategoryDataFieldTypes`

    :param input_type: Type input values fields.
    :type input_type: `playerokapi.enums.GameCategoryDataFieldInputTypes`

    :param copyable: Allowed whether copying values With fields.
    :type copyable: `bool`

    :param hidden: Hidden whether data V field.
    :type hidden: `bool`

    :param required: Necessarily whether This field.
    :type required: `bool`

    :param value: Meaning data V field.
    :type value: `str` or `None`
    """

    def __init__(self, id: str, label: str, type: GameCategoryDataFieldTypes,
                 input_type: GameCategoryDataFieldInputTypes, copyable: bool, 
                 hidden: bool, required: bool, value: str | None):
        self.id: str = id
        """ ID fields With data. """
        self.label: str = label
        """ Inscription-Name fields. """
        self.type: GameCategoryDataFieldTypes = type
        """ Type fields With data. """
        self.input_type: GameCategoryDataFieldInputTypes = input_type
        """ Type input values fields. """
        self.copyable: bool = copyable
        """ Allowed whether copying values With fields. """
        self.hidden: bool = hidden
        """ Hidden whether data V field. """
        self.required: bool = required
        """ Necessarily whether This field. """
        self.value: str | None = value
        """ Meaning data V field. """


class GameCategoryDataFieldPageInfo:
    """
    Subclass, describing information O page fields With data subject.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class GameCategoryDataFieldList:
    """
    Class, describing page fields With data subject.

    :param data_fields: Fields With data subject V categories on page.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.GameCategoryDataFieldPageInfo`

    :param total_count: Total fields With data.
    :type total_count: `int`
    """

    def __init__(self, data_fields: list[GameCategoryDataField], 
                 page_info: GameCategoryDataFieldPageInfo, total_count: int):
        self.data_fields: list[GameCategoryDataField] = data_fields
        """ Fields With data subject V categories on page. """
        self.page_info: GameCategoryDataFieldPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total fields With data. """


class GameCategoryProps:
    """
    Subclass, describing proportions categories.

    :param min_reviews: Minimum quantity reviews.
    :type min_reviews: `int`

    :param min_reviews_for_seller: Minimum quantity reviews For seller.
    :type min_reviews_for_seller: `int`
    """

    def __init__(self, min_reviews: int, min_reviews_for_seller: int):
        self.min_reviews: int = min_reviews
        """ Minimum quantity reviews. """
        self.min_reviews_for_seller: int = min_reviews_for_seller
        """ Minimum quantity reviews For seller. """


class GameCategoryOption:
    """
    Subclass, describing option categories.

    :param id: ID options.
    :type id: `str`

    :param group: Group options.
    :type group: `str`

    :param label: Inscription-Name options.
    :type label: `str`

    :param type: Type options.
    :type type: `playerokapi.enums.GameCategoryOptionTypes`

    :param field: Name fields (For payload request on website).
    :type field: `str`

    :param value: Meaning fields (For payload request on website).
    :type value: `str`

    :param value_range_limit: Limit spread By meaning.
    :type value_range_limit: `int` or `None`
    """

    def __init__(self, id: str, group: str, label: str, type: GameCategoryOptionTypes,
                 field: str, value: str, value_range_limit: int | None):
        self.id: str = id
        """ ID options. """
        self.group: str = group
        """ Group options. """
        self.label: str = label
        """ Inscription-Name options. """
        self.type: GameCategoryOptionTypes = type
        """ Type options. """
        self.field: str = field
        """ Name fields (For payload request on website). """
        self.value: str = value
        """ Meaning fields (For payload request on website). """
        self.value_range_limit: int | None = value_range_limit
        """ Limit spread By meaning. """


class GameCategoryInstruction:
    """
    Subclass, describing information O page instructions By sale/purchase V categories.

    :param id: ID instructions.
    :type id: `str`

    :param text: Text instructions.
    :type text: `str`
    """

    def __init__(self, id: str, text: str):
        self.id: str = id
        """ ID instructions. """
        self.text: str = text
        """ Text instructions. """


class GameCategoryInstructionPageInfo:
    """
    Subclass, describing instructions By sale/purchase V categories.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class GameCategoryInstructionList:
    """
    Class, describing page instructions By sale/purchase V categories.

    :param instructions: Instructions pages.
    :type instructions: `list[playerokapi.types.GameCategoryInstruction]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.GameCategoryInstructionPageInfo`

    :param total_count: Total instructions.
    :type total_count: `int`
    """

    def __init__(self, instructions: list[GameCategoryInstruction], page_info: GameCategoryInstructionPageInfo,
                 total_count: int):
        self.instructions: list[GameCategoryInstruction] = instructions
        """ Agreements pages. """
        self.page_info: GameCategoryInstructionPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total instructions. """


class GameCategory:
    """
    Object categories games/applications.

    :param id: ID categories.
    :type id: `str`

    :param slug: Name pages categories.
    :type slug: `str`

    :param name: Name categories.
    :type name: `str`

    :param category_id: ID parental categories.
    :type category_id: `str` or `None`

    :param game_id: ID games categories.
    :type game_id: `str` or `None`

    :param obtaining: Type receiving.
    :type obtaining: `str` or `None` or `None`

    :param options: Options categories.
    :type options: `list[playerokapi.types.GameCategoryOption]` or `None`

    :param props: Proportions categories.
    :type props: `playerokapi.types.GameCategoryProps` or `None`

    :param no_comment_from_buyer: Without comments from buyer?
    :type no_comment_from_buyer: `bool` or `None`

    :param instruction_for_buyer: Instructions For buyer.
    :type instruction_for_buyer: `str` or `None`

    :param instruction_for_seller: Instructions For seller.
    :type instruction_for_seller: `str` or `None`

    :param use_custom_obtaining: Used whether custom receiving.
    :type use_custom_obtaining: `bool`

    :param auto_confirm_period: Period auto-confirmation deals this categories.
    :type auto_confirm_period: `playerokapi.enums.GameCategoryAutoConfirmPeriods` or `None`

    :param auto_moderation_mode: Enabled whether automatic moderation.
    :type auto_moderation_mode: `bool` or `None`

    :param agreements: Agreements buyer.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]` or `None`

    :param fee_multiplier: Factor commissions.
    :type fee_multiplier: `float` or `None`
    """

    def __init__(self, id: str, slug: str, name: str, category_id: str | None, game_id: str | None,
                 obtaining: str | None, options: list[GameCategoryOption] | None, props: GameCategoryProps | None, 
                 no_comment_from_buyer: bool | None, instruction_for_buyer: str | None, instruction_for_seller: str | None, 
                 use_custom_obtaining: bool, auto_confirm_period: GameCategoryAutoConfirmPeriods | None, 
                 auto_moderation_mode: bool | None, agreements: list[GameCategoryAgreement] | None, fee_multiplier: float | None):
        self.id: str = id
        """ ID categories. """
        self.slug: str = slug
        """ Name pages categories. """
        self.name: str = name
        """ Name categories. """
        self.category_id: str | None = category_id
        """ ID parental categories. """
        self.game_id: str | None = game_id
        """ ID games categories. """
        self.obtaining: str | None = obtaining
        """ Type receiving. """
        self.options: list[GameCategoryOption] | None = options
        """ Options categories. """
        self.props: str | None = props
        """ Proportions categories. """
        self.no_comment_from_buyer: bool | None = no_comment_from_buyer
        """ Without comments from buyer? """
        self.instruction_for_buyer: str | None = instruction_for_buyer
        """ Instructions For buyer. """
        self.instruction_for_seller: str | None = instruction_for_seller
        """ Instructions For seller. """
        self.use_custom_obtaining: bool = use_custom_obtaining
        """ Used whether custom receiving. """
        self.auto_confirm_period: GameCategoryAutoConfirmPeriods | None = auto_confirm_period
        """ Period auto-confirmation deals this categories. """
        self.auto_moderation_mode: bool | None = auto_moderation_mode
        """ Enabled whether automatic moderation. """
        self.agreements: list[GameCategoryAgreement] | None = agreements
        """ Agreements buyer. """
        self.fee_multiplier: float | None = fee_multiplier
        """ Factor commissions. """


class Game:
    """
    Object games/applications.

    :param id: ID games/applications.
    :type id: `str`

    :param slug: Name pages games/applications.
    :type slug: `str`

    :param name: Name games/applications.
    :type name: `str`

    :param type: Type: game or application.
    :type type: `playerokapi.enums.GameTypes`

    :param logo: Logo games/applications.
    :type logo: `playerokapi.types.FileObject`

    :param banner: Banner games/applications.
    :type banner: `FileObject`

    :param categories: List categories games/applications.
    :type categories: `list[playerokapi.types.GameCategory]`

    :param created_at: Date creation.
    :type created_at: `str`
    """

    def __init__(self, id: str, slug: str, name: str, type: GameTypes, 
                 logo: FileObject, banner: FileObject, categories: list[GameCategory], 
                 created_at: str):
        self.id: str = id
        """ ID games/applications. """
        self.slug: str = slug
        """ Name pages games/applications. """
        self.name: str = name
        """ Name games/applications. """
        self.type: GameTypes = type
        """ Type: game or application. """
        self.logo: FileObject = logo
        """ Logo games/applications. """
        self.banner: FileObject = banner
        """ Banner games/applications. """
        self.categories: list[GameCategory] = categories
        """ List categories games/applications. """
        self.created_at: str = created_at
        """ Date creation. """


class GameProfile:
    """
    Profile games/applications.

    :param id: ID games/applications.
    :type id: `str`

    :param slug: Name pages games/applications.
    :type slug: `str`

    :param name: Name games/applications.
    :type name: `str`

    :param type: Type: game or application.
    :type type: `playerokapi.types.GameTypes`

    :param logo: Logo games/applications.
    :type logo: `playerokapi.types.FileObject`
    """

    def __init__(self, id: str, slug: str, name: str, 
                 type: GameTypes, logo: FileObject):
        self.id: str = id
        """ ID games/applications. """
        self.slug: str = slug
        """ Name pages games/applications. """
        self.name: str = name
        """ Name games/applications. """
        self.type: GameTypes = id
        """ Type: game or application. """
        self.logo: FileObject = logo
        """ Logo games/applications. """


class GamePageInfo:
    """
    Subclass, describing information O page games.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class GameList:
    """
    Class, describing page games.

    :param games: Games/applications pages.
    :type games: `list[playerokapi.types.Game]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Total games.
    :type total_count: `int`
    """

    def __init__(self, games: list[Game], page_info: GamePageInfo,
                 total_count: int):
        self.games: list[Game] = games
        """ Games/applications pages. """
        self.page_info: ChatPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total games. """


class ItemPriorityStatusPriceRange:
    """
    Subclass, describing price range subject, suitable For def. status priority.

    :param min: Minimum price subject.
    :type min: `int`

    :param max: Maximum price subject.
    :type max: `int`
    """

    def __init__(self, min: int, max: str):
        self.min: int = min
        """ Minimum price subject (V rubles). """
        self.max: int = max
        """ Maximum price subject (V rubles). """


class ItemPriorityStatus:
    """
    Class, describing status priority subject.

    :param id: ID status priority.
    :type id: `str`

    :param price: Price status (V rubles).
    :type price: `int`

    :param name: Name status.
    :type name: `str`

    :param type: Type status.
    :type type: `playerokapi.enums.PriorityTypes`

    :param period: Duration status (V days).
    :type period: `str`

    :param price_range: Price range subject status.
    :type price_range: `playerokapi.types.ItemPriorityStatusPriceRange`
    """

    def __init__(self, id: str, price: int, name: str, type: PriorityTypes,
                 period: int, price_range: ItemPriorityStatusPriceRange):
        self.id: str = id
        """ ID status priority. """
        self.price: int = price
        """ Price status (V rubles). """
        self.name: str = name
        """ Name status. """
        self.type: PriorityTypes = type
        """ Type status. """
        self.period: int = period
        """ Duration status (V days). """
        self.price_range: ItemPriorityStatusPriceRange = price_range
        """ Price range subject status. """


class ItemLog:
    """
    Subclass, describing log actions With subject.
    
    :param id: ID log.
    :type id: `str`
    
    :param event: Event log.
    :type event: `playerokapi.enums.ItemLogEvents`
    
    :param created_at: Date creation log.
    :type created_at: `str`
    
    :param user: Profile user, committed log.
    :type user: `playerokapi.types.UserProfile`
    """

    def __init__(self, id: str, event: ItemLogEvents, created_at: str,
                 user: UserProfile):
        self.id: str = id
        """ ID log. """
        self.event: ItemLogEvents = event
        """ Event log. """
        self.created_at: str = created_at
        """ Date creation log. """
        self.user: UserProfile = user
        """ Profile user, committed log. """


class Item:
    """
    Object subject.

    :param id: ID subject.
    :type id: `str`

    :param name: Name subject.
    :type name: `str`

    :param description: Description subject.
    :type description: `str`

    :param status: Status subject.
    :type status: `playerokapi.enums.ItemStatuses`

    :param obtaining_type: Way receiving.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

    :param price: Price subject.
    :type price: `int`

    :param raw_price: Price without accounting discounts.
    :type raw_price: `int`

    :param priority_position: Priority position.
    :type priority_position: `int`

    :param attachments: Files-applications.
    :type attachments: `list[playerokapi.types.FileObject]`

    :param attributes: Attributes subject.
    :type attributes: `dict`

    :param category: Category games subject.
    :type category: `playerokapi.types.GameCategory`

    :param comment: Comment subject.
    :type comment: `str` or `None`

    :param data_fields: Fields data subject.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param fee_multiplier: Factor commissions.
    :type fee_multiplier: `float`

    :param game: Profile games subject.
    :type game: `playerokapi.types.GameProfile`

    :param seller_type: Type seller.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param slug: Name pages subject.
    :type slug: `str`

    :param user: Profile seller.
    :type user: `playerokapi.types.UserProfile`
    """

    def __init__(self, id: str, slug: str, name: str, description: str, obtaining_type: GameCategoryObtainingType | None, price: int, raw_price: int, priority_position: int,
                 attachments: list[FileObject], attributes: dict, category: GameCategory, comment: str | None, data_fields: list[GameCategoryDataField] | None, 
                 fee_multiplier: float, game: GameProfile, seller_type: UserTypes, status: ItemStatuses, user: UserProfile):
        self.id: str = id
        """ ID subject. """
        self.slug: str = slug
        """ Name pages subject. """
        self.name: str = name
        """ Name subject. """
        self.description: str = description
        """ Description subject. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        """ Way receiving. """
        self.price: int = price
        """ Price subject. """
        self.raw_price: int = raw_price
        """ Price without accounting discounts. """
        self.priority_position: int = priority_position
        """ Priority position. """
        self.attachments: list[FileObject] = attachments
        """ Files-applications. """
        self.attributes: dict = attributes
        """ Attributes subject. """
        self.category: GameCategory = category
        """ Category games subject. """
        self.comment: str | None = comment
        """ Comment subject. """
        self.data_fields: list[GameCategoryDataField] | None = data_fields
        """ Fields data subject. """
        self.fee_multiplier: float = fee_multiplier
        """ Factor commissions. """
        self.game: GameProfile = game
        """ Profile games subject. """
        self.seller_type: UserTypes = seller_type
        """ Type seller. """
        self.slug: str = slug
        """ Name pages subject. """
        self.status: ItemStatuses = status
        """ Status subject. """
        self.user: UserProfile = user
        """ Profile seller. """


class MyItem:
    """
    Object his subject.

    :param id: ID subject.
    :type id: `str`

    :param slug: Name pages subject.
    :type slug: `str`

    :param name: Name subject.
    :type name: `str`

    :param description: Description subject.
    :type description: `str`

    :param status: Status subject.
    :type status: `playerokapi.enums.ItemStatuses`

    :param obtaining_type: Way receiving.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

    :param price: Price subject.
    :type price: `int`

    :param prev_price: Previous price.
    :type prev_price: `int`

    :param raw_price: Price without accounting discounts.
    :type raw_price: `int`

    :param priority_position: Priority position.
    :type priority_position: `int`

    :param attachments: Files-applications.
    :type attachments: `list[playerokapi.types.FileObject]`

    :param attributes: Attributes subject.
    :type attributes: `dict`

    :param category: Category games subject.
    :type category: `playerokapi.types.GameCategory`

    :param comment: Comment subject.
    :type comment: `str` or `None`

    :param data_fields: Fields data subject.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param fee_multiplier: Factor commissions.
    :type fee_multiplier: `float`

    :param prev_fee_multiplier: Previous factor commissions.
    :type prev_fee_multiplier: `float`

    :param seller_notified_about_fee_change: Notified whether salesman O shift commissions.
    :type seller_notified_about_fee_change: `bool`

    :param game: Profile games subject.
    :type game: `playerokapi.types.GameProfile`

    :param seller_type: Type seller.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param user: Profile seller.
    :type user: `playerokapi.types.UserProfile`

    :param buyer: Profile seller.
    :type user: `playerokapi.types.UserProfile`

    :param priority: Status priority subject.
    :type priority: `playerokapi.types.PriorityTypes`

    :param priority_price: Prices status priority.
    :type priority_price: `int`

    :param sequence: Position subject V table goods users.
    :type sequence: `int` or `None`

    :param status_expiration_date: Date expiration status priority.
    :type status_expiration_date: `str` or `None`

    :param status_description: Description status priority.
    :type status_description: `str` or `None`

    :param status_payment: Payment status (transaction).
    :type status_payment: `playerokapi.types.Transaction` or `None`

    :param views_counter: Quantity views subject.
    :type views_counter: `int`

    :param is_editable: Can whether edit product.
    :type is_editable: `bool`

    :param approval_date: Date publications goods.
    :type approval_date: `str` or `None`

    :param deleted_at: Date removal goods.
    :type deleted_at: `str` or `None`

    :param updated_at: Date last updates goods.
    :type updated_at: `str` or `None`

    :param created_at: Date creation goods.
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
        """ ID subject. """
        self.slug: str = slug
        """ Name pages subject. """
        self.name: str = name
        """ Name subject. """
        self.status: ItemStatuses = status
        """ Status subject. """
        self.description: str = description
        """ Description subject. """
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        """ Way receiving. """
        self.price: int = price
        """ Price subject. """
        self.prev_price: int = prev_price
        """ Previous price. """
        self.raw_price: int = raw_price
        """ Price without accounting discounts. """
        self.priority_position: int = priority_position
        """ Priority position. """
        self.attachments: list[FileObject] = attachments
        """ Files-applications. """
        self.attributes: dict = attributes
        """ Attributes subject. """
        self.category: GameCategory = category
        """ Category games subject. """
        self.comment: str | None = comment
        """ Comment subject. """
        self.data_fields: list[GameCategoryDataField] | None = data_fields
        """ Fields data subject. """
        self.fee_multiplier: float = fee_multiplier
        """ Factor commissions. """
        self.prev_fee_multiplier: float = prev_fee_multiplier
        """ Previous factor commissions. """
        self.seller_notified_about_fee_change: bool = seller_notified_about_fee_change
        """ Notified whether salesman O shift commissions. """
        self.game: GameProfile = game
        """ Profile games subject. """
        self.seller_type: UserTypes = seller_type
        """ Type seller. """
        self.user: UserProfile = user
        """ Profile seller. """
        self.buyer: UserProfile = buyer
        """ Profile buyer subject (If sold). """
        self.priority: PriorityTypes = priority
        """ Status priority subject. """
        self.priority_price: int = priority_price
        """ Prices status priority. """
        self.sequence: int | None = sequence
        """ Position subject V table goods users. """
        self.status_expiration_date: str | None = status_expiration_date
        """ Date expiration status priority. """
        self.status_description: str | None = status_description
        """ Description status priority. """
        self.status_payment: str | None = status_payment
        """ Payment status (transaction). """
        self.views_counter: int = views_counter
        """ Quantity views subject. """
        self.is_editable: bool = is_editable
        """ Can whether edit product. """
        self.approval_date: str | None = approval_date
        """ Date publications goods. """
        self.deleted_at: str | None = deleted_at
        """ Date removal goods. """
        self.updated_at: str | None = updated_at
        """ Date last updates goods. """
        self.created_at: str | None = created_at
        """ Date creation goods. """


class ItemProfile:
    """
    Profile subject.

    :param id: ID subject.
    :type id: `str`

    :param slug: Name pages subject.
    :type slug: `str`

    :param priority: Priority subject.
    :type priority: `playerokapi.enums.PriorityTypes`

    :param status: Status subject.
    :type status: `playerokapi.enums.ItemStatuses`

    :param name: Name subject.
    :type name: `str`

    :param price: Price subject.
    :type price: `int`

    :param raw_price: Price without accounting discounts.
    :type raw_price: `int`

    :param seller_type: Type seller.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param attachment: File-application.
    :type attachment: `playerokapi.types.FileObject`

    :param user: Profile seller.
    :type user: `playerokapi.types.UserProfile`

    :param approval_date: Date approval.
    :type approval_date: `str`

    :param priority_position: Priority position.
    :type priority_position: `int`

    :param views_counter: Quantity views.
    :type views_counter: `int` or `None`

    :param fee_multiplier: Factor commissions.
    :type fee_multiplier: `float`

    :param created_at: Date creation.
    :type created_at: `str`
    """

    def __init__(self, id: str, slug: str, priority: PriorityTypes, status: ItemStatuses,
                 name: str, price: int, raw_price: int, seller_type: UserTypes, attachment: FileObject,
                 user: UserProfile, approval_date: str, priority_position: int, views_counter: int | None, 
                 fee_multiplier: float, created_at: str):
        self.id: str = id
        """ ID subject. """
        self.slug: str = slug
        """ Name pages subject. """
        self.priority: PriorityTypes = priority
        """ Priority subject. """
        self.status: ItemStatuses = status
        """ Status subject. """
        self.name: str = name
        """ Name subject. """
        self.price: int = price
        """ Price subject. """
        self.raw_price: int = raw_price
        """ Price without accounting discounts. """
        self.seller_type: UserTypes = seller_type
        """ Type seller. """
        self.attachment: FileObject = attachment
        """ File-application. """
        self.user: UserProfile = user
        """ Profile seller. """
        self.approval_date: str = approval_date
        """ Date approval. """
        self.priority_position: int = priority_position
        """ Priority position. """
        self.views_counter: int | None = views_counter
        """ Quantity views. """
        self.fee_multiplier: float = fee_multiplier
        """ Factor commissions. """
        self.created_at: str = created_at
        """ Date creation. """


class ItemProfilePageInfo:
    """
    Subclass, describing information O page items.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class ItemProfileList:
    """
    Profile pages items.

    :param items: Items pages.
    :type items: `list[playerokapi.types.Item]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.ItemProfilePageInfo`

    :param total_count: Total items.
    :type total_count: `int`
    """

    def __init__(self, items: list[ItemProfile], page_info: ItemProfilePageInfo,
                 total_count: int):
        self.items: list[ItemProfile] = items
        """ Items pages. """
        self.page_info: ItemProfilePageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total items. """


class SBPBankMember:
    """
    Object members SBP jar.

    :param id: ID.
    :type id: `str`

    :param name: Name.
    :type name: `str`

    :param icon: URL icons.
    :type icon: `str`
    """

    def __init__(self, id: str, name: str, icon: str):
        self.id: str = id
        """ ID. """
        self.name: str = name
        """ Name. """
        self.icon: str = icon
        """ URL icons. """


class TransactionPaymentMethod:
    """
    Payment method transactions.

    :param id: ID method.
    :type id: `playerokapi.types.TransactionPaymentMethodIds`

    :param name: Name method.
    :type name: `str`

    :param fee: Commission method.
    :type fee: `int`

    :param provider_id: ID provider transactions.
    :type provider_id: `playerokapi.types.TransactionProviderIds`

    :param account: Account method (?).
    :type account: `AccountProfile` or `None`

    :param props: Options provider transactions.
    :type props: `playerokapi.types.TransactionProviderProps`

    :param limits: Limits provider transactions.
    :type limits: `playerokapi.types.TransactionProviderLimits`
    """

    def __init__(self, id: TransactionPaymentMethodIds, name: str, fee: int, provider_id: TransactionProviderIds,
                 account: AccountProfile | None, props: TransactionProviderProps, limits: TransactionProviderLimits):
        self.id: TransactionPaymentMethodIds = id
        """ ID method. """
        self.name: str = name
        """ Name method. """
        self.fee: int = fee
        """ Commission method. """
        self.provider_id: TransactionProviderIds = provider_id
        """ ID provider transactions. """
        self.account: AccountProfile | None = account
        """ Account method (?). """
        self.props: TransactionProviderProps = props
        """ Options provider transactions. """
        self.limits: TransactionProviderLimits = limits
        """ Limits provider transactions. """


class TransactionProviderLimitRange:
    """
    Range limits provider transactions.

    :param min: Minimum sum (V rubles).
    :type min: `int`

    :param max: Maximum sum (V rubles).
    :type max: `int`
    """

    def __init__(self, min: int, max: int):
        self.min: int = min
        """ Minimum sum (V rubles). """
        self.max: int = max
        """ Maximum sum (V rubles). """


class TransactionProviderLimits:
    """
    Limits provider transactions.

    :param incoming: On replenishment.
    :type incoming: `playerokapi.types.TransactionProviderLimitRange`

    :param outgoing: On conclusion.
    :type outgoing: `playerokapi.types.TransactionProviderLimitRange`
    """

    def __init__(self, incoming: TransactionProviderLimitRange, outgoing: TransactionProviderLimitRange):
        self.incoming: TransactionProviderLimitRange = incoming
        """ On replenishment. """
        self.outgoing: TransactionProviderLimitRange = outgoing
        """ On conclusion. """


class TransactionProviderRequiredUserData:
    """
    Mandatory custom data provider transactions.

    :param email: Necessarily whether indicate EMail?
    :type email: `bool`

    :param phone_number: Necessarily whether indicate number phone?
    :type phone_number: `bool`

    :param erip_account_number: Necessarily whether indicate number account ERIP?
    :type erip_account_number: `bool` or `None`
    """

    def __init__(self, email: bool, phone_number: bool, 
                 erip_account_number: bool | None):
        self.email: bool = email
        """ Necessarily whether indicate EMail? """
        self.phone_number: bool = phone_number
        """ Necessarily whether indicate number phone? """
        self.erip_account_number: bool | None = erip_account_number
        """ Necessarily whether indicate number account ERIP? """


class TransactionProviderProps:
    """
    Options provider transactions.

    :param required_user_data: Mandatory custom data.
    :type required_user_data: `playerokapi.types.TransactionProviderRequiredUserData`

    :param tooltip: Clue.
    :type tooltip: `str` or `None`
    """

    def __init__(self, required_user_data: TransactionProviderRequiredUserData,
                 tooltip: str | None):
        self.required_user_data: TransactionProviderRequiredUserData = required_user_data
        """ Mandatory custom data. """
        self.tooltip: str | None = tooltip
        """ Clue. """


class TransactionProvider:
    """
    Object provider transactions.

    :param id: ID provider.
    :type id: `playerokapi.enums.TransactionProviderIds`

    :param name: Name provider.
    :type name: `str`

    :param fee: Commission provider.
    :type fee: `int`

    :param min_fee_amount: Minimum commission.
    :type min_fee_amount: `int` or `None`

    :param description: Description provider.
    :type description: `str` or `None`

    :param account: Account provider (?).
    :type account: `playerokapi.types.AccountProfile` or `None`

    :param props: Options provider.
    :type props: `playerokapi.types.TransactionProviderProps`

    :param limits: Limits provider.
    :type limits: `playerokapi.types.TransactionProviderLimits`

    :param payment_methods: Payment methods.
    :type payment_methods: `list` of `playerokapi.types.TransactionPaymentMethod`
    """

    def __init__(self, id: TransactionProviderIds, name: str, fee: int, min_fee_amount: int | None, 
                 description: str | None, account: AccountProfile | None, props: TransactionProviderProps, 
                 limits: TransactionProviderLimits, payment_methods: list[TransactionPaymentMethod]):
        self.id: TransactionProviderIds = id
        """ ID provider. """
        self.name: str = name
        """ Name provider. """
        self.fee: int = fee
        """ Commission provider. """
        self.min_fee_amount: int | None = min_fee_amount
        """ Minimum commission. """
        self.description: str | None = description
        """ Description provider. """
        self.account: AccountProfile | None = account
        """ Account provider (?). """
        self.props: TransactionProviderProps = props
        """ Options provider. """
        self.limits: TransactionProviderLimits = limits
        """ Limits provider. """
        self.payment_methods: list[TransactionPaymentMethod] = payment_methods
        """ Payment methods. """


class Transaction:
    """
    Object transactions.

    :param id: ID transactions.
    :type id: `str`

    :param operation: Type completed operations.
    :type operation: `playerokapi.enums.TransactionOperations`

    :param direction: Direction transactions.
    :type direction: `playerokapi.enums.TransactionDirections`

    :param provider_id: ID payment provider.
    :type provider_id: `playerokapi.enums.TransactionProviderIds`

    :param provider: Object provider transactions.
    :type provider: `playerokapi.types.TransactionProvider`

    :param user: Object user-perpetrator transactions.
    :type user: `playerokapi.types.UserProfile`

    :param creator: Object user-creator transactions.
    :type creator: `playerokapi.types.UserProfile` or `None`

    :param status: Status processing transactions.
    :type status: `playerokapi.enums.TransactionStatuses`

    :param status_description: Description status.
    :type status_description: `str` or `None`

    :param status_expiration_date: Date expiration status.
    :type status_expiration_date: `str` or `None`

    :param value: Sum transactions.
    :type value: `int`

    :param fee: Commission transactions.
    :type fee: `int`

    :param created_at: Date creation transactions.
    :type created_at: `str`

    :param verified_at: Date confirmation transactions.
    :type verified_at: `str` or `None`

    :param verified_by: Object user, confirmed transaction.
    :type verified_by: `playerokapi.types.UserProfile` or `None`

    :param completed_at: Date execution transactions.
    :type completed_at: `str` or `None`

    :param completed_by: Object user, fulfilled transaction.
    :type completed_by: `playerokapi.types.UserProfile` or `None`

    :param payment_method_id: ID way payment.
    :type payment_method_id: `str` or `None`

    :param is_suspicious: Suspicious whether transaction.
    :type is_suspicious: `bool` or `None`

    :param sbp_bank_name: Name jar SBP (If transaction was committed With with help SBP).
    :type sbp_bank_name: `str` or `None`
    """

    def __init__(self, id: str, operation: TransactionOperations, direction: TransactionDirections, provider_id: TransactionProviderIds, 
                 provider: TransactionProvider, user: UserProfile, creator: UserProfile, status: TransactionStatuses, status_description: str | None, 
                 status_expiration_date: str | None, value: int, fee: int, created_at: str, verified_at: str | None, verified_by: UserProfile | None, 
                 completed_at: str | None, completed_by: UserProfile | None, payment_method_id: str | None, is_suspicious: bool | None, sbp_bank_name: str | None):
        self.id: str = id
        """ ID transactions. """
        self.operation: TransactionOperations = operation
        """ Type completed operations. """
        self.direction: TransactionDirections = direction
        """ Direction transactions. """
        self.provider_id: TransactionProviderIds = provider_id
        """ ID payment provider. """
        self.provider: TransactionProvider = provider
        """ Object provider transactions. """
        self.user: UserProfile = user
        """ Object user-perpetrator transactions. """
        self.creator: UserProfile | None = creator
        """ Object user-creator transactions. """
        self.status: TransactionStatuses = status
        """ Status processing transactions. """
        self.status_description: str | None = status_description
        """ Description status. """
        self.status_expiration_date: str | None = status_expiration_date
        """ Date expiration status. """
        self.value: int = value
        """ Sum transactions. """
        self.fee: int = fee
        """ Commission transactions. """
        self.created_at: str = created_at
        """ Date creation transactions. """
        self.verified_at: str | None = verified_at
        """ Date confirmation transactions. """
        self.verified_by: UserProfile | None = verified_by
        """ Object user, confirmed transaction. """
        self.completed_at: str | None = completed_at
        """ Date execution transactions. """
        self.completed_by: UserProfile | None = completed_by
        """ Object user, fulfilled transaction. """
        self.payment_method_id: str | None = payment_method_id
        """ ID way payment. """
        self.is_suspicious: bool | None = is_suspicious
        """ Suspicious whether transaction. """
        self.sbp_bank_name: str | None = sbp_bank_name
        """ Name jar SBP (If transaction was committed With with help SBP). """


class TransactionPageInfo:
    """
    Subclass, describing information O page transactions.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class TransactionList:
    """
    Class, describing page messages chat.

    :param transactions: Transactions pages.
    :type transactions: `list[playerokapi.types.Transaction]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.TransactionPageInfo`

    :param total_count: Total transactions on page.
    :type total_count: `int`
    """

    def __init__(self, transactions: list[Transaction], page_info: TransactionPageInfo,
                 total_count: int):
        self.transactions: list[Transaction] = transactions
        """ Transactions pages. """
        self.page_info: TransactionPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total transactions on page. """


class UserBankCard:
    """
    Object banking cards user.

    :param id: ID cards.
    :type id: `str`

    :param card_first_six: First six numbers cards.
    :type card_first_six: `str`

    :param card_last_four: Latest four numbers cards.
    :type card_last_four: `str`

    :param card_type: Type banking cards.
    :type card_type: `playerokapi.enums.BankCardTypes`

    :param is_chosen: Selected whether this map How By default?
    :type is_chosen: `bool`
    """

    def __init__(self, id: str, card_first_six: str, card_last_four: str,
                 card_type: BankCardTypes, is_chosen: bool):
        self.id: str = id
        """ ID cards. """
        self.card_first_six: str = card_first_six
        """ First six numbers cards. """
        self.card_last_four: str = card_last_four
        """ Latest four numbers cards. """
        self.card_type: BankCardTypes = card_type
        """ Type banking cards. """
        self.is_chosen: bool = is_chosen
        """ Selected whether this map How By default? """


class UserBankCardPageInfo:
    """
    Subclass, describing information O page banking kart user.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class UserBankCardList:
    """
    Class, describing page banking kart user.

    :param bank_cards: Banking cards pages.
    :type bank_cards: `list[playerokapi.types.UserBankCard]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.UserBankCardPageInfo`

    :param total_count: Total banking kart on page.
    :type total_count: `int`
    """

    def __init__(self, bank_cards: list[UserBankCard], 
                 page_info: UserBankCardPageInfo, total_count: int):
        self.bank_cards: list[UserBankCard] = bank_cards
        """ Banking cards pages. """
        self.page_info: UserBankCardPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total banking kart on page. """


class Moderator:
    # TODO: Do Class moderator Moderator

    def __init__(self):
        pass


class ChatMessageButton:
    """
    Object buttons messages.

    :param type: Type buttons.
    :type type: `playerokapi.types.ChatMessageButtonTypes`

    :param url: URL buttons.
    :type url: `str` or None

    :param text: Text buttons.
    :type text: `str`
    """

    def __init__(self, type: ChatMessageButtonTypes, 
                 url: str | None, text: str,):
        self.type: ChatMessageButtonTypes = type
        """ Type buttons. """
        self.url: str | None = url
        """ URL buttons. """
        self.text: str = text
        """ Text buttons. """


class ChatMessage:
    """
    Class, describing message V chat.

    :param id: ID messages.
    :type id: `str`

    :param text: Text messages.
    :type text: `str`

    :param created_at: Date creation messages.
    :type created_at: `str`

    :param deleted_at: Date removal messages.
    :type deleted_at: `str` or `None`

    :param is_read: Read whether message.
    :type is_read: `bool`

    :param is_suspicious: Suspicious whether message.
    :type is_suspicious: `bool`

    :param is_bulk_messaging: Mass whether This newsletter.
    :type is_bulk_messaging: `bool`

    :param game: Game, To which applies message.
    :type game: `str` or `None`

    :param file: File, attached To message.
    :type file: `playerokapi.types.FileObject` or `None`

    :param user: User, which sent message.
    :type user: `playerokapi.types.UserProfile`

    :param deal: Deal, To which applies message.
    :type deal: `playerokapi.types.Deal` or `None`

    :param item: Item, To to whom applies message (usually transmitted only herself deal V variable deal).
    :type item: `playerokapi.types.Item` or `None`

    :param transaction: Transaction messages.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param moderator: Moderator messages.
    :type moderator: `playerokapi.types.Moderator`

    :param event_by_user: Event from user.
    :type event_by_user: `playerokapi.types.UserProfile` or `None`

    :param event_to_user: Event For user.
    :type event_to_user: `playerokapi.types.UserProfile` or `None`

    :param is_auto_response: Auto-answer whether This.
    :type is_auto_response: `bool`

    :param event: Event messages.
    :type event: `playerokapi.types.Event` or `None`

    :param buttons: Buttons messages.
    :type buttons: `list[playerokapi.types.MessageButton]`
    """

    def __init__(self, id: str, text: str, created_at: str, deleted_at: str | None, is_read: bool, 
                 is_suspicious: bool, is_bulk_messaging: bool, game: Game | None, file: FileObject | None,
                 user: UserProfile, deal: ItemDeal | None, item: ItemProfile | None, transaction: Transaction | None,
                 moderator: Moderator | None, event_by_user: UserProfile | None, event_to_user: UserProfile | None, 
                 is_auto_response: bool, event: Event | None, buttons: list[ChatMessageButton]):
        self.id: str = id
        """ ID messages. """
        self.text: str = text
        """ Text messages. """
        self.created_at: str = created_at
        """ Date creation messages. """
        self.deleted_at: str | None = deleted_at
        """ Date removal messages. """
        self.is_read: bool = is_read
        """ Read whether message. """
        self.is_suspicious: bool = is_suspicious
        """ Suspicious whether message. """
        self.is_bulk_messaging: bool = is_bulk_messaging
        """ Mass whether This newsletter. """
        self.game: Game | None  = game
        """ Game, To which applies message. """
        self.file: FileObject | None  = file
        """ File, attached To message. """
        self.user: UserProfile = user
        """ User, which sent message. """
        self.deal: ItemDeal | None = deal
        """ Deal, To which applies message. """
        self.item: ItemProfile | None = item
        """ Item, To to whom applies message (usually transmitted only herself deal V variable deal). """
        self.transaction: Transaction | None = transaction
        """ Transaction messages. """
        self.moderator: Moderator = moderator
        """ Moderator messages. """
        self.event_by_user: UserProfile | None = event_by_user
        """ Event from user. """
        self.event_to_user: UserProfile | None = event_to_user
        """ Event For user. """
        self.is_auto_response: bool = is_auto_response
        """ Auto-answer whether This. """
        self.event: Event | None = event
        """ Event messages. """
        self.buttons: list[ChatMessageButton] = buttons
        """ Buttons messages. """


class ChatMessagePageInfo:
    """
    Subclass, describing information O page messages.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class ChatMessageList:
    """
    Class, describing page messages chat.

    :param messages: Messages pages.
    :type messages: `list[playerokapi.types.ChatMessage]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.ChatMessagePageInfo`

    :param total_count: Total messages V chat.
    :type total_count: `int`
    """

    def __init__(self, messages: list[ChatMessage], page_info: ChatMessagePageInfo,
                 total_count: int):
        self.messages: list[ChatMessage] = messages
        """ Messages pages. """
        self.page_info: ChatMessagePageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total messages V chat. """


class Chat:
    """
    Object chat.

    :param id: ID chat.
    :type id: `str`

    :param type: Type chat.
    :type type: `playerokapi.enums.ChatTypes`

    :param status: Status chat.
    :type status: `playerokapi.enums.ChatStatuses` or `None`

    :param unread_messages_counter: Quantity unread messages.
    :type unread_messages_counter: `int`

    :param bookmarked: IN bookmarks whether chat.
    :type bookmarked: `bool` or `None`

    :param is_texting_allowed: Allowed whether write V chat.
    :type is_texting_allowed: `bool` or `None`

    :param owner: Owner chat (only If This chat With bot).
    :type owner: `bool` or `None`

    :param deals: Transactions V chat.
    :type deals: `list[playerokapi.types.ItemDeal]` or `None`

    :param last_message: Object last messages V chat
    :type last_message: `playerokapi.types.ChatMessage` or `None`

    :param users: Participants chat.
    :type users: `list[UserProfile]`

    :param started_at: Date started dialogue.
    :type started_at: `str` or `None`

    :param finished_at: Date completion dialogue.
    :type finished_at: `str` or `None`
    """

    def __init__(self, id: str, type: ChatTypes, status: ChatStatuses | None, unread_messages_counter: int, 
                 bookmarked: bool | None, is_texting_allowed: bool | None, owner: UserProfile | None, deals: list[ItemDeal] | None,
                 started_at: str | None, finished_at: str | None, last_message: ChatMessage | None, users: list[UserProfile]):
        self.id: str = id
        """ ID chat. """
        self.type: ChatTypes = type
        """ Type chat. """
        self.status: ChatStatuses | None = status
        """ Status chat. """
        self.unread_messages_counter: int = unread_messages_counter
        """ Quantity unread messages. """
        self.bookmarked: bool | None = bookmarked
        """ IN bookmarks whether chat. """
        self.is_texting_allowed: bool | None = is_texting_allowed
        """ Allowed whether write V chat. """
        self.owner: UserProfile = owner
        """ Owner chat. """
        self.deals: list[ItemDeal] | None = deals
        """ Transactions V chat. """
        self.last_message: ChatMessage | None = last_message
        """ Object last messages V chat. """
        self.users: list[UserProfile] = users
        """ Participants chat. """
        self.started_at: str | None = started_at
        """ Date started dialogue. """
        self.finished_at: str | None = finished_at
        """ Date completion dialogue. """


class ChatPageInfo:
    """
    Subclass, describing information O page chats.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class ChatList:
    """
    Class, describing page chats.

    :param chats: Chats pages.
    :type chats: `list[playerokapi.types.Chat]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Total chats.
    :type total_count: `int`
    """

    def __init__(self, chats: list[Chat], page_info: ChatPageInfo,
                 total_count: int):
        self.chats: list[Chat] = chats
        """ Chats pages. """
        self.page_info: ChatPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total chats. """


class Review:
    """
    Object review.

    :param id: ID review.
    :type id: `str`

    :param status: Status review.
    :type status: `playerokapi.enums.ReviewStatuses`

    :param text: Text review.
    :type text: `str` or `None`

    :param rating: Rating review.
    :type rating: `int`

    :param created_at: Date creation review.
    :type created_at: `str`

    :param updated_at: Date changes review.
    :type updated_at: `str`

    :param deal: Deal, related With review.
    :type deal: `Deal`

    :param creator: Profile creator review.
    :type creator: `UserProfile`

    :param moderator: Moderator, processed review.
    :type moderator: `Moderator` or `None`

    :param user: Profile seller, To to whom applies review.
    :type user: `UserProfile`
    """

    def __init__(self, id: str, status: ReviewStatuses, text: str | None, rating: int,
                 created_at: str, updated_at: str, deal: ItemDeal, creator: UserProfile, 
                 moderator: Moderator | None, user: UserProfile):
        self.id: str = id
        """ ID review. """
        self.status: ReviewStatuses = status
        """ Status review. """
        self.text: str | None = text
        """ Text review. """
        self.rating: int = rating
        """ Rating review. """
        self.created_at: str = created_at
        """ Date creation review. """
        self.updated_at: str = updated_at
        """ Date changes review. """
        self.deal: ItemDeal = deal
        """ Deal, related With review. """
        self.creator: UserProfile = creator
        """ Profile creator review. """
        self.moderator: Moderator | None = moderator
        """ Moderator, processed review. """
        self.user: UserProfile = user
        """ Profile seller, To to whom applies review. """


class ReviewPageInfo:
    """
    Subclass, describing information O page reviews.

    :param start_cursor: Cursor started pages.
    :type start_cursor: `str`

    :param end_cursor: Kursok end pages.
    :type end_cursor: `str`

    :param has_previous_page: Has whether previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Has whether next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Cursor started pages. """
        self.end_cursor: str = end_cursor
        """ Cursor end pages. """
        self.has_previous_page: bool = has_previous_page
        """ Has whether previous page. """
        self.has_next_page: bool = has_next_page
        """ Has whether next page. """


class ReviewList:
    """
    Class, describing page reviews.

    :param reviews: Reviews pages.
    :type reviews: `list[playerokapi.types.Review]`

    :param page_info: Information O page.
    :type page_info: `playerokapi.types.ReviewPageInfo`

    :param total_count: Total reviews.
    :type total_count: `int`
    """

    def __init__(self, reviews: list[Review], page_info: ReviewPageInfo,
                 total_count: int):
        self.reviews: list[Review] = reviews
        """ Reviews pages. """
        self.page_info: ReviewPageInfo = page_info
        """ Information O page. """
        self.total_count: int = total_count
        """ Total reviews. """