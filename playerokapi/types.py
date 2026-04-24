from __future__ import annotations
from typing import *
import json
from . import parser
from .enums import *
from .misc import PERSISTED_QUERIES

class FileObject:
    """
    Объект файла.

    :param id: File ID.
    :type id: `str`

    :param url: File URL.
    :type url: `str`

    :param filename: File name.
    :type filename: `str` or `None`

    :param mime: Mime file.
    :type mime: `str` or `None`
    """

    def __init__(self, id: str, url: str, filename: str | None, mime: str | None):
        self.id: str = id
        ' File ID. '
        self.url: str = url
        ' File URL. '
        self.filename: str | None = filename
        ' File name. '
        self.mime: str | None = mime
        ' Mime file. '

class AccountBalance:
    """
    Подкласс, описывающий баланс аккаунта.

    :param id: Balance ID.
    :type id: `str`

    :param value: Sum баланса.
    :type value: `int`

    :param frozen: Frozen balance amount.
    :type frozen: `int`

    :param available: Available balance amount.
    :type available: `int`

    :param withdrawable: Sum баланса, доступного для вывода.
    :type withdrawable: `int`

    :param pending_income: Expected income.
    :type pending_income: `int`
    """

    def __init__(self, id: str, value: int, frozen: int, available: int, withdrawable: int, pending_income: int):
        self.id: str = id
        ' Balance ID. '
        self.value: int = value
        ' Total balance amount. '
        self.frozen: int = frozen
        ' Frozen balance amount. '
        self.available: int = available
        ' Available balance amount. '
        self.withdrawable: int = withdrawable
        ' Sum баланса, доступного для вывода. '
        self.pending_income: int = pending_income
        ' Expected income. '

class AccountIncomingDealsStats:
    """
    Подкласс, описывающий статистику входящих deals аккаунта.

    :param total: Total исходящих deals.
    :type total: `int`

    :param finished: Завершённых исходящих deals.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total: int = total
        ' Total исходящих deals. '
        self.finished: int = finished
        ' Кол-во завершённых исходящих deals. '

class AccountOutgoingDealsStats:
    """
    Подкласс, описывающий статистику исходящих deals аккаунта.

    :param total: Total исходящих deals.
    :type total: `int`

    :param finished: Завершённых исходящих deals.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total = total
        ' Total исходящих deals. '
        self.finished = finished
        ' Кол-во завершённых исходящих deals. '

class AccountDealsStats:
    """
    Подкласс, описывающий статистику deals аккаунта.

    :param incoming: Incoming transactions.
    :type incoming: `playerokapi.types.AccountIncomingDealsStats`

    :param outgoing: Outgoing transactions.
    :type outgoing: `playerokapi.types.AccountOutgoingDealsStats`
    """

    def __init__(self, incoming: AccountIncomingDealsStats, outgoing: AccountOutgoingDealsStats):
        self.incoming: AccountIncomingDealsStats = incoming
        ' Incoming transactions. '
        self.outgoing: AccountOutgoingDealsStats = outgoing
        ' Outgoing transactions. '

class AccountItemsStats:
    """
    Подкласс, описывающий статистику items аккаунта.

    :param total: Total items.
    :type total: `int`

    :param finished: Завершённых items.
    :type finished: `int`
    """

    def __init__(self, total: int, finished: int):
        self.total: int = total
        ' Total items. '
        self.finished: int = finished
        ' Кол-во завершённых items. '

class AccountStats:
    """
    Подкласс, описывающий статистику аккаунта.

    :param items: Statistics items.
    :type items: `playerokapi.types.AccountItemsStats`

    :param deals: Statistics deals.
    :type deals: `playerokapi.types.AccountDealsStats`
    """

    def __init__(self, items: AccountItemsStats, deals: AccountDealsStats):
        self.items: AccountItemsStats = items
        ' Statistics items. '
        self.deals: AccountDealsStats = deals
        ' Statistics deals. '

class AccountProfile:
    """
    Класс, описывающий профиль аккаунта.

    :param id: ID аккаунта.
    :type id: `str`

    :param username: Никнейм аккаунта.
    :type username: `str`

    :param email: Почта аккаунта.
    :type email: `str`

    :param balance: Объект баланса аккаунта.
    :type balance: `playerokapi.types.AccountBalance`

    :param stats: Статистика аккаунта.
    :type stats: `str`

    :param role: Роль аккаунта.
    :type role: `playerokapi.enums.UserTypes`

    :param avatar_url: URL аватара аккаунта.
    :type avatar_url: `str`

    :param is_online: В онлайне ли сейчас аккаунт.
    :type is_online: `bool`

    :param is_blocked: Заблокирован ли аккаунт.
    :type is_blocked: `bool`

    :param is_blocked_for: Причина блокировки.
    :type is_blocked_for: `str`

    :param is_verified: Верифицирован ли аккаунт.
    :type is_verified: `bool`

    :param rating: Рейтинг аккаунта (0-5).
    :type rating: `int`

    :param reviews_count: Кол-во отзывов на аккаунте.
    :type reviews_count: `int`

    :param created_at: Дата создания аккаунта.
    :type created_at: `str`

    :param support_chat_id: ID чата поддержки.
    :type support_chat_id: `str`

    :param system_chat_id: ID системного чата.
    :type system_chat_id: `str`

    :param has_frozen_balance: Заморожен ли баланс на аккаунте.
    :type has_frozen_balance: `bool`

    :param has_enabled_notifications: Включены ли уведомления на аккаунте.
    :type has_enabled_notifications: `bool`

    :param unread_chats_counter: Количество непрочитанных чатов.
    :type unread_chats_counter: `int` or `None`
    """

    def __init__(self, id: str, username: str, email: str, balance: AccountBalance, stats: AccountStats, role: UserTypes, avatar_url: str, is_online: bool, is_blocked: bool, is_blocked_for: str, is_verified: bool, rating: int, reviews_count: int, created_at: str, support_chat_id: str, system_chat_id: str, has_frozen_balance: bool, has_enabled_notifications: bool, unread_chats_counter: int | None):
        self.id: str = id
        ' Account ID. '
        self.username: str = username
        ' Username аккаунта. '
        self.email: str = email
        ' Account mail. '
        self.balance: AccountBalance = balance
        ' Account balance object. '
        self.stats: AccountStats = stats
        ' Account statistics. '
        self.role: UserTypes = role
        ' Account role. '
        self.avatar_url: str = avatar_url
        ' Account Avatar URL. '
        self.is_online: bool = is_online
        ' Is your account online now?. '
        self.is_blocked: bool = is_blocked
        ' Is your account blocked?. '
        self.is_blocked_for: str = is_blocked_for
        ' Reason for account blocking. '
        self.is_verified: bool = is_verified
        ' Is your account verified?. '
        self.rating: int = rating
        ' Рейтинг аккаунта (0-5). '
        self.reviews_count: int = reviews_count
        ' Кол-во отзывов on аккаунте. '
        self.created_at: str = created_at
        ' Account creation date. '
        self.support_chat_id: str = support_chat_id
        ' Account support chat ID. '
        self.system_chat_id: str = system_chat_id
        ' Account system chat ID. '
        self.has_frozen_balance: bool = has_frozen_balance
        ' Заморожен ли баланс on аккаунте. '
        self.has_enabled_notifications: bool = has_enabled_notifications
        ' Включены ли уведомления on аккаунте. '
        self.unread_chats_counter: bool | None = unread_chats_counter
        ' Number of unread messages. '

class UserProfile:
    """
    Класс, описывающий профиль пользователя.

    :param id: ID пользователя.
    :type id: `str`

    :param username: Никнейм пользователя.
    :type username: `str`

    :param role: Роль пользователя.
    :type role: `playerokapi.enums.UserTypes`

    :param avatar_url: URL аватара пользователя.
    :type avatar_url: `str`

    :param is_online: В онлайне ли сейчас пользователь.
    :type is_online: `bool`

    :param is_blocked: Заблокирован ли пользователь.
    :type is_blocked: `bool`

    :param rating: Рейтинг пользователя (0-5).
    :type rating: `int`

    :param reviews_count: Кол-во отзывов пользователя.
    :type reviews_count: `int`

    :param support_chat_id: ID чата поддержки.
    :type support_chat_id: `str` or `None`

    :param system_chat_id: ID системного чата.
    :type system_chat_id: `str` or `None`

    :param created_at: Дата создания аккаунта пользователя.
    :type created_at: `str`
    """

    def __init__(self, id: str, username: str, role: UserTypes, avatar_url: str, is_online: bool, is_blocked: bool, rating: int, reviews_count: int, support_chat_id: str, system_chat_id: str | None, created_at: str | None):
        self.id: str = id
        ' User ID. '
        self.username: str = username
        ' Username пользователя. '
        self.role: UserTypes = role
        ' User Role. '
        self.avatar_url: str = avatar_url
        ' Avatar URL. '
        self.is_online: bool = is_online
        ' Is the user online now?. '
        self.is_blocked: bool = is_blocked
        ' Is the user blocked?. '
        self.rating: int = rating
        ' Рейтинг пользователя (0-5). '
        self.reviews_count: int = reviews_count
        ' Кол-во отзывов пользователя. '
        self.support_chat_id: str | None = support_chat_id
        ' Support chat ID. '
        self.system_chat_id: str | None = system_chat_id
        ' System chat ID. '
        self.created_at: str = created_at
        ' Account creation date пользователя. '

    def get_items(self, count: int=24, game_id: str | None=None, category_id: str | None=None, statuses: list[ItemStatuses] | None=None, after_cursor: str | None=None) -> ItemProfileList:
        """
        Получает предметы пользователя.

        :param count: Кол-во предеметов, которые нужно получить (не более 24 за один запрос), _опционально_.
        :type count: `int`
        
        :param game_id: ID игры/приложения, чьи предметы нужно получить, _опционально_.
        :type game_id: `str` or `None`

        :param category_id: ID категории игры/приложения, чьи предметы нужно получить, _опционально_.
        :type category_id: `str` or `None`

        :param status: Массив типов предметов, которые нужно получить. Некоторые статусы можно получить только, если это профиль вашего аккаунта. Если не указано, получает сразу все возможные.
        :type status: `list[playerokapi.enums.ItemStatuses]`

        :param after_cursor: Курсор, с которого будет идти парсинг (если нету - ищет с самого начала страницы), _опционально_.
        :type after_cursor: `str` or `None`
        
        :return: Страница профилей предметов.
        :rtype: `PlayerokAPI.types.ItemProfileList`
        """
        from .account import get_account
        account = get_account()
        headers = {'Accept': '*/*', 'Content-Type': 'application/json', 'Origin': account.base_url}
        filter = {'userId': self.id, 'status': [status.name for status in statuses] if statuses else None}
        if game_id:
            filter['gameId'] = game_id
        elif category_id:
            filter['gameCategoryId'] = category_id
        payload = {'operationName': 'items', 'variables': json.dumps({'pagination': {'first': count, 'after': after_cursor}, 'filter': filter, 'showForbiddenImage': False}), 'extensions': json.dumps({'persistedQuery': {'version': 1, 'sha256Hash': PERSISTED_QUERIES.get('items')}})}
        r = account.request('get', f'{account.base_url}/graphql', headers, payload).json()
        return parser.item_profile_list(r['data']['items'])

    def get_reviews(self, count: int=24, status: ReviewStatuses=ReviewStatuses.APPROVED, comment_required: bool=False, rating: int | None=None, game_id: str | None=None, category_id: str | None=None, min_item_price: int | None=None, max_item_price: int | None=None, sort_direction: SortDirections=SortDirections.DESC, sort_field: str='createdAt', after_cursor: str | None=None) -> ReviewList:
        """
        Получает отзывы пользователя.

        :param count: Кол-во отзывов, которые нужно получить (не более 24 за один запрос), _опционально_.
        :type count: `int`

        :param status: Тип отзывов, которые нужно получить.
        :type status: `playerokapi.enums.ReviewStatuses`

        :param comment_required: Обязателен ли комментарий в отзыве, _опционально_.
        :type comment_required: `bool`

        :param rating: Рейтинг отзывов (1-5), _опционально_.
        :type rating: `int` or `None`

        :param game_id: ID игры отзывов, _опционально_.
        :type game_id: `str` or `None`

        :param category_id: ID категории отзывов, _опционально_.
        :type category_id: `str` or `None`

        :param min_item_price: Минимальная цена предмета отзыва, _опционально_.
        :type min_item_price: `bool` or `None`

        :param max_item_price: Максимальная цена предмета отзыва, _опционально_.
        :type max_item_price: `bool` or `None`

        :param sort_direction: Тип сортировки.
        :type sort_direction: `playerokapi.enums.SortDirections`

        :param sort_field: Поле, по которому будет идти сортировка (по умолчанию `createdAt` - по дате)
        :type sort_field: `str`

        :param after_cursor: Курсор, с которого будет идти парсинг (если нету - ищет с самого начала страницы), _опционально_.
        :type after_cursor: `str` or `None`
        
        :return: Страница отзывов.
        :rtype: `PlayerokAPI.types.ReviewList`
        """
        from .account import get_account
        account = get_account()
        headers = {'Accept': '*/*', 'Content-Type': 'application/json', 'Origin': account.base_url}
        filters = {'userId': self.id, 'status': [status.name] if status else None}
        if comment_required is not None:
            filters['hasComment'] = comment_required
        if game_id is not None:
            filters['gameId'] = game_id
        if category_id is not None:
            filters['categoryId'] = category_id
        if rating is not None:
            filters['rating'] = rating
        if min_item_price is not None or max_item_price is not None:
            item_price = {}
            if min_item_price is not None:
                item_price['min'] = min_item_price
            if max_item_price is not None:
                item_price['max'] = max_item_price
            filters['itemPrice'] = item_price
        payload = {'operationName': 'testimonials', 'variables': json.dumps({'pagination': {'first': count, 'after': after_cursor}, 'filter': filters, 'sort': {'direction': sort_direction.name if sort_direction else None, 'field': sort_field}}), 'extensions': json.dumps({'persistedQuery': {'version': 1, 'sha256Hash': PERSISTED_QUERIES.get('testimonials')}})}
        r = account.request('get', f'{account.base_url}/graphql', headers, payload).json()
        return parser.review_list(r['data']['testimonials'])

class Event:

    def __init__(self):
        pass

class ItemDeal:
    """
    Объект сделки с предметом.

    :param id: ID сделки.
    :type id: `str`

    :param status: Статус сделки.
    :type status: `playerokapi.enums.ItemDealStatuses`

    :param status_expiration_date: Дата истечения статуса.
    :type status_expiration_date: `str` or `None`

    :param status_description: Описание статуса сделки.
    :type status_description: `str` or `None`

    :param direction: Направление сделки (покупка/продажа).
    :type direction: `playerokapi.enums.ItemDealDirections`

    :param obtaining: Получение сделки.
    :type obtaining: `str` or `None`

    :param has_problem: Есть ли проблема в сделке.
    :type has_problem: `bool`

    :param report_problem_enabled: Включено ли обжалование проблемы.
    :type report_problem_enabled: `bool` or `None`

    :param completed_user: Профиль пользователя, подтвердившего сделку.
    :type completed_user: `playerokapi.types.UserProfile` or `None`

    :param props: Реквизиты сделки.
    :type props: `str` or `None`

    :param previous_status: Предыдущий статус.
    :type previous_status: `playerokapi.enums.ItemDealStatuses` or `None`

    :param completed_at: Дата подтверждения сделки.
    :type completed_at: `str` or `None`

    :param created_at: Дата создания сделки.
    :type created_at: `str` or `None`

    :param logs: Логи сделки.
    :type logs: `list[playerokapi.types.ItemLog]` or `None`

    :param transaction: Транзакция сделки.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param user: Профиль пользователя, совершившего сделку.
    :type user: `playerokapi.types.UserProfile`

    :param chat: Чат сделки (передаётся только его ID).
    :type chat: `playerokapi.types.Chat` or `None`

    :param item: Предмет сделки.
    :type item: `playerokapi.types.Item`

    :param review: Отзыв по сделке.
    :type review: `playerokapi.types.Review` or `None`

    :param obtaining_fields: Получаемые поля.
    :type obtaining_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param comment_from_buyer: Комментарий от покупателя.
    :type comment_from_buyer: `str` or `None`
    """

    def __init__(self, id: str, status: ItemDealStatuses, status_expiration_date: str | None, status_description: str | None, direction: ItemDealDirections, obtaining: str | None, has_problem: bool, report_problem_enabled: bool | None, completed_user: UserProfile | None, props: str | None, previous_status: ItemDealStatuses | None, completed_at: str, created_at: str, logs: list[ItemLog] | None, transaction: Transaction | None, user: UserProfile, chat: Chat | None, item: Item, review: Review | None, obtaining_fields: list[GameCategoryDataField] | None, comment_from_buyer: str | None):
        self.id: str = id
        ' Transaction ID. '
        self.status: ItemDealStatuses = status
        ' Status сделки. '
        self.status_expiration_date: str | None = status_expiration_date
        ' Status expiration date. '
        self.status_description: str | None = status_description
        ' Description of the transaction status. '
        self.direction: ItemDealDirections = direction
        ' Направление сделки (покупка/продажа). '
        self.obtaining: str | None = obtaining
        ' Receiving a deal. '
        self.has_problem: bool = has_problem
        ' Is there a problem with the deal?. '
        self.report_problem_enabled: bool | None = report_problem_enabled
        ' Is problem appeal included?. '
        self.completed_user: UserProfile | None = completed_user
        ' Profile пользователя, подтвердившего сделку. '
        self.props: str | None = props
        ' Transaction details. '
        self.previous_status: ItemDealStatuses | None = previous_status
        ' Previous status. '
        self.completed_at: str | None = completed_at
        ' Transaction confirmation date. '
        self.created_at: str | None = created_at
        ' Deal creation date. '
        self.logs: list[ItemLog] | None = logs
        ' Transaction logs. '
        self.transaction: Transaction | None = transaction
        ' Deal transaction. '
        self.user: UserProfile = user
        ' Profile пользователя, совершившего сделку. '
        self.chat: Chat | None = chat
        ' Чат сделки (передаётся только его ID). '
        self.item: Item = item
        ' Subject transactions. '
        self.review: Review | None = review
        ' Feedback on the deal. '
        self.obtaining_fields: list[GameCategoryDataField] | None = obtaining_fields
        ' Retrieved fields. '
        self.comment_from_buyer: str | None = comment_from_buyer
        ' Comment from buyer. '

class ItemDealPageInfo:
    """
    Подкласс, описывающий информацию о странице deals.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class ItemDealList:
    """
    Класс, описывающий страницу отзывов.

    :param deals: Сделки страницы.
    :type deals: `list[playerokapi.types.ItemDeal]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.ItemDealPageInfo`

    :param total_count: Всего сделок.
    :type total_count: `int`
    """

    def __init__(self, deals: list[ItemDeal], page_info: ItemDealPageInfo, total_count: int):
        self.deals: list[ItemDeal] = deals
        ' Deals Page. '
        self.page_info: ItemDealPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total deals. '

class GameCategoryAgreement:
    """
    Подкласс, описывающий соглашения покупателя.

    :param id: Agreement ID.
    :type id: `str`

    :param description: Description of the agreement.
    :type description: `str`

    :param icontype: Agreement icon type.
    :type icontype: `playerokapi.enums.GameCategoryAgreementIconTypes`

    :param sequence: Sequence of agreement.
    :type sequence: `str`
    """

    def __init__(self, id: str, description: str, icontype: GameCategoryAgreementIconTypes, sequence: int):
        self.id: str = id
        ' Agreement ID. '
        self.description: str = description
        ' Description of the agreement. '
        self.icontype: GameCategoryAgreementIconTypes = icontype
        ' Agreement icon type. '
        self.sequence: str = sequence
        ' Sequence of agreement. '

class GameCategoryAgreementPageInfo:
    """
    Подкласс, описывающий информацию о странице соглашений покупателя.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class GameCategoryAgreementList:
    """
    Класс, описывающий страницу соглашений покупателя.

    :param agreements: Соглашения страницы.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.GameCategoryAgreementPageInfo`

    :param total_count: Всего соглашений.
    :type total_count: `int`
    """

    def __init__(self, agreements: list[GameCategoryAgreement], page_info: GameCategoryAgreementPageInfo, total_count: int):
        self.agreements: list[GameCategoryAgreement] = agreements
        ' Page Conventions. '
        self.page_info: GameCategoryAgreementPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total соглашений. '

class GameCategoryObtainingType:
    """
    Подкласс, описывающий тип (способ) получения предмета в категории.

    :param id: ID способа.
    :type id: `str`

    :param name: Название способа.
    :type name: `str`

    :param description: Описание способа.
    :type description: `str`

    :param game_category_id: ID категории игры способа.
    :type game_category_id: `str`

    :param no_comment_from_buyer: Без комментария от покупателя?
    :type no_comment_from_buyer: `bool`

    :param instruction_for_buyer: Инструкция для покупателя.
    :type instruction_for_buyer: `str`

    :param instruction_for_seller: Инструкция для продавца.
    :type instruction_for_seller: `str`

    :param sequence: Последовательность способа.
    :type sequence: `int`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float`

    :param agreements: Соглашения покупателя на покупку/продавца на продажу.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]`

    :param props: Пропорции категории.
    :type props: `playerokapi.types.GameCategoryProps`
    """

    def __init__(self, id: str, name: str, description: str, game_category_id: str, no_comment_from_buyer: bool, instruction_for_buyer: str | None, instruction_for_seller: str | None, sequence: int, fee_multiplier: float, agreements: list[GameCategoryAgreement], props: GameCategoryProps):
        self.id: str = id
        ' Method ID. '
        self.name: str = name
        ' Method name. '
        self.description: str = description
        ' Description of the method. '
        self.game_category_id: str = game_category_id
        ' Mode game category ID. '
        self.no_comment_from_buyer: bool = no_comment_from_buyer
        ' No comment from buyer? '
        self.instruction_for_buyer: str | None = instruction_for_buyer
        " Buyer's instructions. "
        self.instruction_for_seller: str | None = instruction_for_seller
        ' Instructions for the seller. '
        self.sequence: int = sequence
        ' Sequence of method. '
        self.fee_multiplier: float = fee_multiplier
        ' Commission multiplier. '
        self.agreements: list[GameCategoryAgreement] = agreements
        ' Соглашения покупателя на покупку/продавца на продажу. '
        self.props: GameCategoryProps = props
        ' Category proportions. '

class GameCategoryObtainingTypePageInfo:
    """
    Подкласс, описывающий информацию о странице типов (способов) получения предмета в категории.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class GameCategoryObtainingTypeList:
    """
    Класс, описывающий страницу типов (способов) получения предмета в категории.

    :param obtaining_types: Способы страницы.
    :type obtaining_types: `list[playerokapi.types.GameCategoryObtainingType]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.GameCategoryObtainingTypePageInfo`

    :param total_count: Всего способов.
    :type total_count: `int`
    """

    def __init__(self, obtaining_types: list[GameCategoryObtainingType], page_info: GameCategoryObtainingTypePageInfo, total_count: int):
        self.obtaining_types: list[GameCategoryObtainingType] = obtaining_types
        ' Page Conventions. '
        self.page_info: GameCategoryAgreementPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total способов. '

class GameCategoryDataField:
    """
    Подкласс, описывающий поля с данными предмета в категории (которые отправляются после покупки).

    :param id: ID поля с данными.
    :type id: `str`

    :param label: Надпись-название поля.
    :type label: `str`

    :param type: Тип поля с данными.
    :type type: `playerokapi.enums.GameCategoryDataFieldTypes`

    :param input_type: Тип вводимого значения поля.
    :type input_type: `playerokapi.enums.GameCategoryDataFieldInputTypes`

    :param copyable: Разрешено ли копирование значения с поля.
    :type copyable: `bool`

    :param hidden: Скрыты ли данные в поле.
    :type hidden: `bool`

    :param required: Обязательно ли это поле.
    :type required: `bool`

    :param value: Значение данных в поле.
    :type value: `str` or `None`
    """

    def __init__(self, id: str, label: str, type: GameCategoryDataFieldTypes, input_type: GameCategoryDataFieldInputTypes, copyable: bool, hidden: bool, required: bool, value: str | None):
        self.id: str = id
        ' Data field ID. '
        self.label: str = label
        ' Надпись-название поля. '
        self.type: GameCategoryDataFieldTypes = type
        ' Data field type. '
        self.input_type: GameCategoryDataFieldInputTypes = input_type
        ' Field input type. '
        self.copyable: bool = copyable
        ' Is copying a value from a field allowed?. '
        self.hidden: bool = hidden
        ' Is the data hidden in the field?. '
        self.required: bool = required
        ' Is this field required?. '
        self.value: str | None = value
        ' Data value in the field. '

class GameCategoryDataFieldPageInfo:
    """
    Подкласс, описывающий информацию о странице полей с данными предмета.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class GameCategoryDataFieldList:
    """
    Класс, описывающий страницу полей с данными предмета.

    :param data_fields: Поля с данными предмета в категории на странице.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.GameCategoryDataFieldPageInfo`

    :param total_count: Всего полей с данными.
    :type total_count: `int`
    """

    def __init__(self, data_fields: list[GameCategoryDataField], page_info: GameCategoryDataFieldPageInfo, total_count: int):
        self.data_fields: list[GameCategoryDataField] = data_fields
        ' Поля с данными предмета в категории on странице. '
        self.page_info: GameCategoryDataFieldPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total полей с данными. '

class GameCategoryProps:
    """
    Подкласс, описывающий пропорции категории.

    :param min_reviews: Minimum number of reviews.
    :type min_reviews: `int`

    :param min_reviews_for_seller: Minimum number of reviews для продавца.
    :type min_reviews_for_seller: `int`
    """

    def __init__(self, min_reviews: int, min_reviews_for_seller: int):
        self.min_reviews: int = min_reviews
        ' Minimum number of reviews. '
        self.min_reviews_for_seller: int = min_reviews_for_seller
        ' Minimum number of reviews для продавца. '

class GameCategoryOption:
    """
    Подкласс, описывающий опцию категории.

    :param id: ID опции.
    :type id: `str`

    :param group: Группа опции.
    :type group: `str`

    :param label: Надпись-название опции.
    :type label: `str`

    :param type: Тип опции.
    :type type: `playerokapi.enums.GameCategoryOptionTypes`

    :param field: Название поля (для payload запроса на сайт).
    :type field: `str`

    :param value: Значение поля (для payload запроса на сайт).
    :type value: `str`

    :param value_range_limit: Лимит разброса по значению.
    :type value_range_limit: `int` or `None`
    """

    def __init__(self, id: str, group: str, label: str, type: GameCategoryOptionTypes, field: str, value: str, value_range_limit: int | None):
        self.id: str = id
        ' ID options. '
        self.group: str = group
        ' Option group. '
        self.label: str = label
        ' Надпись-название опции. '
        self.type: GameCategoryOptionTypes = type
        ' Type options. '
        self.field: str = field
        ' Название поля (для payload запроса на сайт). '
        self.value: str = value
        ' Значение поля (для payload запроса на сайт). '
        self.value_range_limit: int | None = value_range_limit
        ' Value spread limit. '

class GameCategoryInstruction:
    """
    Подкласс, описывающий информацию о странице инструкии по продаже/покупке в категории.

    :param id: ID инструкции.
    :type id: `str`

    :param text: Текст инструкции.
    :type text: `str`
    """

    def __init__(self, id: str, text: str):
        self.id: str = id
        ' Instruction ID. '
        self.text: str = text
        ' Instruction text. '

class GameCategoryInstructionPageInfo:
    """
    Подкласс, описывающий инструкцию по продаже/покупке в категории.

    :param start_cursor: Курсор начала страницы.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Имеет ли предыдущую страницу.
    :type has_previous_page: `bool`

    :param has_next_page: Имеет ли следующую страницу.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class GameCategoryInstructionList:
    """
    Класс, описывающий страницу инструкций по продаже/покупке в категории.

    :param instructions: Инструкции страницы.
    :type instructions: `list[playerokapi.types.GameCategoryInstruction]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.GameCategoryInstructionPageInfo`

    :param total_count: Всего инструкций.
    :type total_count: `int`
    """

    def __init__(self, instructions: list[GameCategoryInstruction], page_info: GameCategoryInstructionPageInfo, total_count: int):
        self.instructions: list[GameCategoryInstruction] = instructions
        ' Page Conventions. '
        self.page_info: GameCategoryInstructionPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total инструкций. '

class GameCategory:
    """
    Объект категории игры/приложения.

    :param id: ID категории.
    :type id: `str`

    :param slug: Имя страницы категории.
    :type slug: `str`

    :param name: Название категории.
    :type name: `str`

    :param category_id: ID родительской категории.
    :type category_id: `str` or `None`

    :param game_id: ID игры категории.
    :type game_id: `str` or `None`

    :param obtaining: Тип получения.
    :type obtaining: `str` or `None` or `None`

    :param options: Опции категории.
    :type options: `list[playerokapi.types.GameCategoryOption]` or `None`

    :param props: Пропорции категории.
    :type props: `playerokapi.types.GameCategoryProps` or `None`

    :param no_comment_from_buyer: Без комментария от покупателя?
    :type no_comment_from_buyer: `bool` or `None`

    :param instruction_for_buyer: Инструкция для покупателя.
    :type instruction_for_buyer: `str` or `None`

    :param instruction_for_seller: Инструкция для продавца.
    :type instruction_for_seller: `str` or `None`

    :param use_custom_obtaining: Используется ли кастомное получение.
    :type use_custom_obtaining: `bool`

    :param auto_confirm_period: Период авто-подтверждения сделки этой категории.
    :type auto_confirm_period: `playerokapi.enums.GameCategoryAutoConfirmPeriods` or `None`

    :param auto_moderation_mode: Включена ли автоматическая модерация.
    :type auto_moderation_mode: `bool` or `None`

    :param agreements: Соглашения покупателя.
    :type agreements: `list[playerokapi.types.GameCategoryAgreement]` or `None`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float` or `None`
    """

    def __init__(self, id: str, slug: str, name: str, category_id: str | None, game_id: str | None, obtaining: str | None, options: list[GameCategoryOption] | None, props: GameCategoryProps | None, no_comment_from_buyer: bool | None, instruction_for_buyer: str | None, instruction_for_seller: str | None, use_custom_obtaining: bool, auto_confirm_period: GameCategoryAutoConfirmPeriods | None, auto_moderation_mode: bool | None, agreements: list[GameCategoryAgreement] | None, fee_multiplier: float | None):
        self.id: str = id
        ' Category ID. '
        self.slug: str = slug
        ' Category page name. '
        self.name: str = name
        ' Category name. '
        self.category_id: str | None = category_id
        ' Parent category ID. '
        self.game_id: str | None = game_id
        ' Category game ID. '
        self.obtaining: str | None = obtaining
        ' Receipt type. '
        self.options: list[GameCategoryOption] | None = options
        ' Category Options. '
        self.props: str | None = props
        ' Category proportions. '
        self.no_comment_from_buyer: bool | None = no_comment_from_buyer
        ' No comment from buyer? '
        self.instruction_for_buyer: str | None = instruction_for_buyer
        " Buyer's instructions. "
        self.instruction_for_seller: str | None = instruction_for_seller
        ' Instructions for the seller. '
        self.use_custom_obtaining: bool = use_custom_obtaining
        ' Is custom receiving used?. '
        self.auto_confirm_period: GameCategoryAutoConfirmPeriods | None = auto_confirm_period
        ' Период авто-подтверждения сделки этой категории. '
        self.auto_moderation_mode: bool | None = auto_moderation_mode
        ' Is automatic moderation enabled?. '
        self.agreements: list[GameCategoryAgreement] | None = agreements
        ' Buyer Agreements. '
        self.fee_multiplier: float | None = fee_multiplier
        ' Commission multiplier. '

class Game:
    """
    Объект игры/приложения.

    :param id: ID игры/приложения.
    :type id: `str`

    :param slug: Имя страницы игры/приложения.
    :type slug: `str`

    :param name: Название игры/приложения.
    :type name: `str`

    :param type: Тип: игра или приложение.
    :type type: `playerokapi.enums.GameTypes`

    :param logo: Лого игры/приложения.
    :type logo: `playerokapi.types.FileObject`

    :param banner: Баннер игры/приложения.
    :type banner: `FileObject`

    :param categories: Список категорий игры/приложения.
    :type categories: `list[playerokapi.types.GameCategory]`

    :param created_at: Дата создания.
    :type created_at: `str`
    """

    def __init__(self, id: str, slug: str, name: str, type: GameTypes, logo: FileObject, banner: FileObject, categories: list[GameCategory], created_at: str):
        self.id: str = id
        ' ID игры/приложения. '
        self.slug: str = slug
        ' Имя страницы игры/приложения. '
        self.name: str = name
        ' Название игры/приложения. '
        self.type: GameTypes = type
        ' Тип: игра или приложение. '
        self.logo: FileObject = logo
        ' Лого игры/приложения. '
        self.banner: FileObject = banner
        ' Баннер игры/приложения. '
        self.categories: list[GameCategory] = categories
        ' Список категорий игры/приложения. '
        self.created_at: str = created_at
        ' Creation date. '

class GameProfile:
    """
    Профиль игры/приложения.

    :param id: ID игры/приложения.
    :type id: `str`

    :param slug: Имя страницы игры/приложения.
    :type slug: `str`

    :param name: Название игры/приложения.
    :type name: `str`

    :param type: Тип: игра или приложение.
    :type type: `playerokapi.types.GameTypes`

    :param logo: Лого игры/приложения.
    :type logo: `playerokapi.types.FileObject`
    """

    def __init__(self, id: str, slug: str, name: str, type: GameTypes, logo: FileObject):
        self.id: str = id
        ' ID игры/приложения. '
        self.slug: str = slug
        ' Имя страницы игры/приложения. '
        self.name: str = name
        ' Название игры/приложения. '
        self.type: GameTypes = id
        ' Тип: игра или приложение. '
        self.logo: FileObject = logo
        ' Лого игры/приложения. '

class GamePageInfo:
    """
    Подкласс, описывающий информацию о странице игр.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class GameList:
    """
    Класс, описывающий страницу игр.

    :param games: Игры/приложения страницы.
    :type games: `list[playerokapi.types.Game]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Всего игр.
    :type total_count: `int`
    """

    def __init__(self, games: list[Game], page_info: GamePageInfo, total_count: int):
        self.games: list[Game] = games
        ' Игры/приложения страницы. '
        self.page_info: ChatPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total игр. '

class ItemPriorityStatusPriceRange:
    """
    Подкласс, описывающий ценовой диапазон предмета, подходящего для опред. статуса приоритета.

    :param min: Минимальная цена предмета.
    :type min: `int`

    :param max: Максимальная цена предмета.
    :type max: `int`
    """

    def __init__(self, min: int, max: str):
        self.min: int = min
        ' Минимальная цена предмета (в рублях). '
        self.max: int = max
        ' Максимальная цена предмета (в рублях). '

class ItemPriorityStatus:
    """
    Класс, описывающий статус приоритета предмета.

    :param id: ID статуса приоритета.
    :type id: `str`

    :param price: Цена статуса (в рублях).
    :type price: `int`

    :param name: Название статуса.
    :type name: `str`

    :param type: Тип статуса.
    :type type: `playerokapi.enums.PriorityTypes`

    :param period: Длительность статуса (в днях).
    :type period: `str`

    :param price_range: Ценовой диапазон предмета статуса.
    :type price_range: `playerokapi.types.ItemPriorityStatusPriceRange`
    """

    def __init__(self, id: str, price: int, name: str, type: PriorityTypes, period: int, price_range: ItemPriorityStatusPriceRange):
        self.id: str = id
        ' Priority Status ID. '
        self.price: int = price
        ' Цена статуса (в рублях). '
        self.name: str = name
        ' Status name. '
        self.type: PriorityTypes = type
        ' Status type. '
        self.period: int = period
        ' Длительность статуса (в днях). '
        self.price_range: ItemPriorityStatusPriceRange = price_range
        ' Status Item Price Range. '

class ItemLog:
    """
    Подкласс, описывающий лог действия с предметом.
    
    :param id: Logo ID.
    :type id: `str`
    
    :param event: Log event.
    :type event: `playerokapi.enums.ItemLogEvents`
    
    :param created_at: Creation date лога.
    :type created_at: `str`
    
    :param user: Profile пользователя, совершившего лог.
    :type user: `playerokapi.types.UserProfile`
    """

    def __init__(self, id: str, event: ItemLogEvents, created_at: str, user: UserProfile):
        self.id: str = id
        ' Logo ID. '
        self.event: ItemLogEvents = event
        ' Log event. '
        self.created_at: str = created_at
        ' Creation date лога. '
        self.user: UserProfile = user
        ' Profile пользователя, совершившего лог. '

class Item:
    """
    Объект предмета.

    :param id: ID предмета.
    :type id: `str`

    :param name: Название предмета.
    :type name: `str`

    :param description: Описание предмета.
    :type description: `str`

    :param status: Статус предмета.
    :type status: `playerokapi.enums.ItemStatuses`

    :param obtaining_type: Способ получения.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

    :param price: Цена предмета.
    :type price: `int`

    :param raw_price: Цена без учёта скидки.
    :type raw_price: `int`

    :param priority_position: Приоритетная позиция.
    :type priority_position: `int`

    :param attachments: Файлы-приложения.
    :type attachments: `list[playerokapi.types.FileObject]`

    :param attributes: Аттрибуты предмета.
    :type attributes: `dict`

    :param category: Категория игры предмета.
    :type category: `playerokapi.types.GameCategory`

    :param comment: Комментарий предмета.
    :type comment: `str` or `None`

    :param data_fields: Поля данных предмета.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float`

    :param game: Профиль игры предмета.
    :type game: `playerokapi.types.GameProfile`

    :param seller_type: Тип продавца.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param slug: Имя страницы предмета.
    :type slug: `str`

    :param user: Профиль продавца.
    :type user: `playerokapi.types.UserProfile`
    """

    def __init__(self, id: str, slug: str, name: str, description: str, obtaining_type: GameCategoryObtainingType | None, price: int, raw_price: int, priority_position: int, attachments: list[FileObject], attributes: dict, category: GameCategory, comment: str | None, data_fields: list[GameCategoryDataField] | None, fee_multiplier: float, game: GameProfile, seller_type: UserTypes, status: ItemStatuses, user: UserProfile):
        self.id: str = id
        ' Item ID. '
        self.slug: str = slug
        ' Item Page Name. '
        self.name: str = name
        ' Title of the subject. '
        self.description: str = description
        ' Item Description. '
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        ' Method of obtaining. '
        self.price: int = price
        ' Price the item. '
        self.raw_price: int = raw_price
        ' Price without discount. '
        self.priority_position: int = priority_position
        ' Priority position. '
        self.attachments: list[FileObject] = attachments
        ' Файлы-приложения. '
        self.attributes: dict = attributes
        ' Subject Attributes. '
        self.category: GameCategory = category
        ' Item game category. '
        self.comment: str | None = comment
        ' Item comment. '
        self.data_fields: list[GameCategoryDataField] | None = data_fields
        ' Item Data Fields. '
        self.fee_multiplier: float = fee_multiplier
        ' Commission multiplier. '
        self.game: GameProfile = game
        ' Item Game Profile. '
        self.seller_type: UserTypes = seller_type
        ' Seller type. '
        self.slug: str = slug
        ' Item Page Name. '
        self.status: ItemStatuses = status
        ' Subject status. '
        self.user: UserProfile = user
        ' Seller Profile. '

class MyItem:
    """
    Объект своего предмета.

    :param id: ID предмета.
    :type id: `str`

    :param slug: Имя страницы предмета.
    :type slug: `str`

    :param name: Название предмета.
    :type name: `str`

    :param description: Описание предмета.
    :type description: `str`

    :param status: Статус предмета.
    :type status: `playerokapi.enums.ItemStatuses`

    :param obtaining_type: Способ получения.
    :type obtaining_type: `playerokapi.types.GameCategoryObtainingType` or `None`

    :param price: Цена предмета.
    :type price: `int`

    :param prev_price: Предыдущая цена.
    :type prev_price: `int`

    :param raw_price: Цена без учёта скидки.
    :type raw_price: `int`

    :param priority_position: Приоритетная позиция.
    :type priority_position: `int`

    :param attachments: Файлы-приложения.
    :type attachments: `list[playerokapi.types.FileObject]`

    :param attributes: Аттрибуты предмета.
    :type attributes: `dict`

    :param category: Категория игры предмета.
    :type category: `playerokapi.types.GameCategory`

    :param comment: Комментарий предмета.
    :type comment: `str` or `None`

    :param data_fields: Поля данных предмета.
    :type data_fields: `list[playerokapi.types.GameCategoryDataField]` or `None`

    :param fee_multiplier: Множитель комиссии.
    :type fee_multiplier: `float`

    :param prev_fee_multiplier: Предыдущий множитель комиссии.
    :type prev_fee_multiplier: `float`

    :param seller_notified_about_fee_change: Оповещён ли продавец о смене комиссии.
    :type seller_notified_about_fee_change: `bool`

    :param game: Профиль игры предмета.
    :type game: `playerokapi.types.GameProfile`

    :param seller_type: Тип продавца.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param user: Профиль продавца.
    :type user: `playerokapi.types.UserProfile`

    :param buyer: Профиль продавца.
    :type user: `playerokapi.types.UserProfile`

    :param priority: Статус приоритета предмета.
    :type priority: `playerokapi.types.PriorityTypes`

    :param priority_price: Цены статуса приоритета.
    :type priority_price: `int`

    :param sequence: Позиция предмета в таблице товаров пользователей.
    :type sequence: `int` or `None`

    :param status_expiration_date: Дата истечения статуса приоритета.
    :type status_expiration_date: `str` or `None`

    :param status_description: Описание статуса приоритета.
    :type status_description: `str` or `None`

    :param status_payment: Платёж статуса (транзакция).
    :type status_payment: `playerokapi.types.Transaction` or `None`

    :param views_counter: Количество просмотров предмета.
    :type views_counter: `int`

    :param is_editable: Можно ли редактировать товар.
    :type is_editable: `bool`

    :param approval_date: Дата публикации товара.
    :type approval_date: `str` or `None`

    :param deleted_at: Дата удаления товара.
    :type deleted_at: `str` or `None`

    :param updated_at: Дата последнего обновления товара.
    :type updated_at: `str` or `None`

    :param created_at: Дата создания товара.
    :type created_at: `str` or `None`
    """

    def __init__(self, id: str, slug: str, name: str, description: str, obtaining_type: GameCategoryObtainingType | None, price: int, raw_price: int, priority_position: int, attachments: list[FileObject], attributes: dict, buyer: UserProfile, category: GameCategory, comment: str | None, data_fields: list[GameCategoryDataField] | None, fee_multiplier: float, game: GameProfile, seller_type: UserTypes, status: ItemStatuses, user: UserProfile, prev_price: int, prev_fee_multiplier: float, seller_notified_about_fee_change: bool, priority: PriorityTypes, priority_price: int, sequence: int | None, status_expiration_date: str | None, status_description: str | None, status_payment: Transaction | None, views_counter: int, is_editable: bool, approval_date: str | None, deleted_at: str | None, updated_at: str | None, created_at: str | None):
        self.id: str = id
        ' Item ID. '
        self.slug: str = slug
        ' Item Page Name. '
        self.name: str = name
        ' Title of the subject. '
        self.status: ItemStatuses = status
        ' Subject status. '
        self.description: str = description
        ' Item Description. '
        self.obtaining_type: GameCategoryObtainingType | None = obtaining_type
        ' Method of obtaining. '
        self.price: int = price
        ' Price the item. '
        self.prev_price: int = prev_price
        ' Previous price. '
        self.raw_price: int = raw_price
        ' Price without discount. '
        self.priority_position: int = priority_position
        ' Priority position. '
        self.attachments: list[FileObject] = attachments
        ' Файлы-приложения. '
        self.attributes: dict = attributes
        ' Subject Attributes. '
        self.category: GameCategory = category
        ' Item game category. '
        self.comment: str | None = comment
        ' Item comment. '
        self.data_fields: list[GameCategoryDataField] | None = data_fields
        ' Item Data Fields. '
        self.fee_multiplier: float = fee_multiplier
        ' Commission multiplier. '
        self.prev_fee_multiplier: float = prev_fee_multiplier
        ' Previous commission multiplier. '
        self.seller_notified_about_fee_change: bool = seller_notified_about_fee_change
        ' Is the seller notified of the commission change?. '
        self.game: GameProfile = game
        ' Item Game Profile. '
        self.seller_type: UserTypes = seller_type
        ' Seller type. '
        self.user: UserProfile = user
        ' Seller Profile. '
        self.buyer: UserProfile = buyer
        ' Профиль покупателя предмета (если продан). '
        self.priority: PriorityTypes = priority
        ' Item Priority Status. '
        self.priority_price: int = priority_price
        ' Priority status prices. '
        self.sequence: int | None = sequence
        ' Position предмета в таблице items пользователей. '
        self.status_expiration_date: str | None = status_expiration_date
        ' Status expiration date приоритета. '
        self.status_description: str | None = status_description
        ' Description of priority status. '
        self.status_payment: str | None = status_payment
        ' Платёж статуса (транзакция). '
        self.views_counter: int = views_counter
        ' Number of item views. '
        self.is_editable: bool = is_editable
        ' Is it possible to edit a product?. '
        self.approval_date: str | None = approval_date
        ' Product publication date. '
        self.deleted_at: str | None = deleted_at
        ' Product removal date. '
        self.updated_at: str | None = updated_at
        ' Product last updated date. '
        self.created_at: str | None = created_at
        ' Creation date товара. '

class ItemProfile:
    """
    Profile предмета.

    :param id: Item ID.
    :type id: `str`

    :param slug: Item Page Name.
    :type slug: `str`

    :param priority: Item priority.
    :type priority: `playerokapi.enums.PriorityTypes`

    :param status: Subject status.
    :type status: `playerokapi.enums.ItemStatuses`

    :param name: Title of the subject.
    :type name: `str`

    :param price: Price the item.
    :type price: `int`

    :param raw_price: Price without discount.
    :type raw_price: `int`

    :param seller_type: Seller type.
    :type seller_type: `playerokapi.enums.UserTypes`

    :param attachment: Файл-приложение.
    :type attachment: `playerokapi.types.FileObject`

    :param user: Seller Profile.
    :type user: `playerokapi.types.UserProfile`

    :param approval_date: Date of approvals.
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

    def __init__(self, id: str, slug: str, priority: PriorityTypes, status: ItemStatuses, name: str, price: int, raw_price: int, seller_type: UserTypes, attachment: FileObject, user: UserProfile, approval_date: str, priority_position: int, views_counter: int | None, fee_multiplier: float, created_at: str):
        self.id: str = id
        ' Item ID. '
        self.slug: str = slug
        ' Item Page Name. '
        self.priority: PriorityTypes = priority
        ' Item priority. '
        self.status: ItemStatuses = status
        ' Subject status. '
        self.name: str = name
        ' Title of the subject. '
        self.price: int = price
        ' Price the item. '
        self.raw_price: int = raw_price
        ' Price without discount. '
        self.seller_type: UserTypes = seller_type
        ' Seller type. '
        self.attachment: FileObject = attachment
        ' Файл-приложение. '
        self.user: UserProfile = user
        ' Seller Profile. '
        self.approval_date: str = approval_date
        ' Date of approvals. '
        self.priority_position: int = priority_position
        ' Priority position. '
        self.views_counter: int | None = views_counter
        ' Number of views. '
        self.fee_multiplier: float = fee_multiplier
        ' Commission multiplier. '
        self.created_at: str = created_at
        ' Creation date. '

class ItemProfilePageInfo:
    """
    Подкласс, описывающий информацию о странице items.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class ItemProfileList:
    """
    Профиль страницы предметов.

    :param items: Предметы страницы.
    :type items: `list[playerokapi.types.Item]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.ItemProfilePageInfo`

    :param total_count: Всего предметов.
    :type total_count: `int`
    """

    def __init__(self, items: list[ItemProfile], page_info: ItemProfilePageInfo, total_count: int):
        self.items: list[ItemProfile] = items
        ' Items страницы. '
        self.page_info: ItemProfilePageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total items. '

class SBPBankMember:
    """
    Объект членов СБП банка.

    :param id: ID.
    :type id: `str`

    :param name: Name.
    :type name: `str`

    :param icon: URL icons.
    :type icon: `str`
    """

    def __init__(self, id: str, name: str, icon: str):
        self.id: str = id
        ' ID. '
        self.name: str = name
        ' Name. '
        self.icon: str = icon
        ' URL icons. '

class TransactionPaymentMethod:
    """
    Платёжный метод транзакции.

    :param id: ID метода.
    :type id: `playerokapi.types.TransactionPaymentMethodIds`

    :param name: Название метода.
    :type name: `str`

    :param fee: Комиссия метода.
    :type fee: `int`

    :param provider_id: ID провайдера транзакции.
    :type provider_id: `playerokapi.types.TransactionProviderIds`

    :param account: Аккаунт метода (?).
    :type account: `AccountProfile` or `None`

    :param props: Параметры провайдера транзакции.
    :type props: `playerokapi.types.TransactionProviderProps`

    :param limits: Лимиты провайдера транзакции.
    :type limits: `playerokapi.types.TransactionProviderLimits`
    """

    def __init__(self, id: TransactionPaymentMethodIds, name: str, fee: int, provider_id: TransactionProviderIds, account: AccountProfile | None, props: TransactionProviderProps, limits: TransactionProviderLimits):
        self.id: TransactionPaymentMethodIds = id
        ' Method ID. '
        self.name: str = name
        ' Method name. '
        self.fee: int = fee
        ' Commission method. '
        self.provider_id: TransactionProviderIds = provider_id
        ' Transaction provider ID. '
        self.account: AccountProfile | None = account
        ' Аккаунт метода (?). '
        self.props: TransactionProviderProps = props
        ' Transaction Provider Options. '
        self.limits: TransactionProviderLimits = limits
        ' Transaction Provider Limits. '

class TransactionProviderLimitRange:
    """
    Диапозон лимитов провайдера транзакции.

    :param min: Минимальная сумма (в рублях).
    :type min: `int`

    :param max: Максимальная сумма (в рублях).
    :type max: `int`
    """

    def __init__(self, min: int, max: int):
        self.min: int = min
        ' Минимальная сумма (в рублях). '
        self.max: int = max
        ' Максимальная сумма (в рублях). '

class TransactionProviderLimits:
    """
    Transaction Provider Limits.

    :param incoming: For replenishment.
    :type incoming: `playerokapi.types.TransactionProviderLimitRange`

    :param outgoing: For conclusion.
    :type outgoing: `playerokapi.types.TransactionProviderLimitRange`
    """

    def __init__(self, incoming: TransactionProviderLimitRange, outgoing: TransactionProviderLimitRange):
        self.incoming: TransactionProviderLimitRange = incoming
        ' For replenishment. '
        self.outgoing: TransactionProviderLimitRange = outgoing
        ' For conclusion. '

class TransactionProviderRequiredUserData:
    """
    Required user data провайдера транзакции.

    :param email: Is it necessary to indicate EMail??
    :type email: `bool`

    :param phone_number: Is it necessary to provide a phone number??
    :type phone_number: `bool`

    :param erip_account_number: Is it mandatory to specify ERIP account number?
    :type erip_account_number: `bool` or `None`
    """

    def __init__(self, email: bool, phone_number: bool, erip_account_number: bool | None):
        self.email: bool = email
        ' Is it necessary to indicate EMail?? '
        self.phone_number: bool = phone_number
        ' Is it necessary to provide a phone number?? '
        self.erip_account_number: bool | None = erip_account_number
        ' Is it mandatory to specify ERIP account number? '

class TransactionProviderProps:
    """
    Transaction Provider Options.

    :param required_user_data: Required user data.
    :type required_user_data: `playerokapi.types.TransactionProviderRequiredUserData`

    :param tooltip: Clue.
    :type tooltip: `str` or `None`
    """

    def __init__(self, required_user_data: TransactionProviderRequiredUserData, tooltip: str | None):
        self.required_user_data: TransactionProviderRequiredUserData = required_user_data
        ' Required user data. '
        self.tooltip: str | None = tooltip
        ' Clue. '

class TransactionProvider:
    """
    Объект провайдера транзакции.

    :param id: ID провайдера.
    :type id: `playerokapi.enums.TransactionProviderIds`

    :param name: Название провайдера.
    :type name: `str`

    :param fee: Комиссия провайдера.
    :type fee: `int`

    :param min_fee_amount: Минимальная комиссия.
    :type min_fee_amount: `int` or `None`

    :param description: Описание провайдера.
    :type description: `str` or `None`

    :param account: Аккаунт провайдера (?).
    :type account: `playerokapi.types.AccountProfile` or `None`

    :param props: Параметры провайдера.
    :type props: `playerokapi.types.TransactionProviderProps`

    :param limits: Лимиты провайдера.
    :type limits: `playerokapi.types.TransactionProviderLimits`

    :param payment_methods: Платёжные методы.
    :type payment_methods: `list` of `playerokapi.types.TransactionPaymentMethod`
    """

    def __init__(self, id: TransactionProviderIds, name: str, fee: int, min_fee_amount: int | None, description: str | None, account: AccountProfile | None, props: TransactionProviderProps, limits: TransactionProviderLimits, payment_methods: list[TransactionPaymentMethod]):
        self.id: TransactionProviderIds = id
        ' Provider ID. '
        self.name: str = name
        ' Name провайдера. '
        self.fee: int = fee
        ' Provider commission. '
        self.min_fee_amount: int | None = min_fee_amount
        ' Minimum commission. '
        self.description: str | None = description
        ' Provider Description. '
        self.account: AccountProfile | None = account
        ' Аккаунт провайдера (?). '
        self.props: TransactionProviderProps = props
        ' Provider settings. '
        self.limits: TransactionProviderLimits = limits
        ' Provider limits. '
        self.payment_methods: list[TransactionPaymentMethod] = payment_methods
        ' Payment methods. '

class Transaction:
    """
    Объект транзакции.

    :param id: ID транзакции.
    :type id: `str`

    :param operation: Тип выполненной операции.
    :type operation: `playerokapi.enums.TransactionOperations`

    :param direction: Направление транзакции.
    :type direction: `playerokapi.enums.TransactionDirections`

    :param provider_id: ID платёжного провайдера.
    :type provider_id: `playerokapi.enums.TransactionProviderIds`

    :param provider: Объект провайдера транзакции.
    :type provider: `playerokapi.types.TransactionProvider`

    :param user: Объект пользователя-совершателя транзакции.
    :type user: `playerokapi.types.UserProfile`

    :param creator: Объект пользователя-создателя транзакции.
    :type creator: `playerokapi.types.UserProfile` or `None`

    :param status: Статус обработки транзакции.
    :type status: `playerokapi.enums.TransactionStatuses`

    :param status_description: Описание статуса.
    :type status_description: `str` or `None`

    :param status_expiration_date: Дата истечения статуса.
    :type status_expiration_date: `str` or `None`

    :param value: Сумма транзакции.
    :type value: `int`

    :param fee: Комиссия транзакции.
    :type fee: `int`

    :param created_at: Дата создания транзакции.
    :type created_at: `str`

    :param verified_at: Дата подтверждения транзакции.
    :type verified_at: `str` or `None`

    :param verified_by: Объект пользователя, подтвердившего транзакцию.
    :type verified_by: `playerokapi.types.UserProfile` or `None`

    :param completed_at: Дата выполнения транзакции.
    :type completed_at: `str` or `None`

    :param completed_by: Объект пользователя, выполнившего транзакцию.
    :type completed_by: `playerokapi.types.UserProfile` or `None`

    :param payment_method_id: ID способа оплаты.
    :type payment_method_id: `str` or `None`

    :param is_suspicious: Подозрительная ли транзакция.
    :type is_suspicious: `bool` or `None`

    :param sbp_bank_name: Название банка СБП (если транзакция была совершена с помощью СБП).
    :type sbp_bank_name: `str` or `None`
    """

    def __init__(self, id: str, operation: TransactionOperations, direction: TransactionDirections, provider_id: TransactionProviderIds, provider: TransactionProvider, user: UserProfile, creator: UserProfile, status: TransactionStatuses, status_description: str | None, status_expiration_date: str | None, value: int, fee: int, created_at: str, verified_at: str | None, verified_by: UserProfile | None, completed_at: str | None, completed_by: UserProfile | None, payment_method_id: str | None, is_suspicious: bool | None, sbp_bank_name: str | None):
        self.id: str = id
        ' Transaction ID. '
        self.operation: TransactionOperations = operation
        ' Type of operation performed. '
        self.direction: TransactionDirections = direction
        ' Transaction direction. '
        self.provider_id: TransactionProviderIds = provider_id
        ' Payment provider ID. '
        self.provider: TransactionProvider = provider
        ' Transaction Provider Object. '
        self.user: UserProfile = user
        ' Объект пользователя-совершателя транзакции. '
        self.creator: UserProfile | None = creator
        ' Объект пользователя-создателя транзакции. '
        self.status: TransactionStatuses = status
        ' Transaction processing status. '
        self.status_description: str | None = status_description
        ' Description of status. '
        self.status_expiration_date: str | None = status_expiration_date
        ' Status expiration date. '
        self.value: int = value
        ' Transaction amount. '
        self.fee: int = fee
        ' Transaction fee. '
        self.created_at: str = created_at
        ' Creation date транзакции. '
        self.verified_at: str | None = verified_at
        ' Transaction confirmation date. '
        self.verified_by: UserProfile | None = verified_by
        ' Объект пользователя, подтвердившего транзакцию. '
        self.completed_at: str | None = completed_at
        ' Transaction date. '
        self.completed_by: UserProfile | None = completed_by
        ' Объект пользователя, выполнившего транзакцию. '
        self.payment_method_id: str | None = payment_method_id
        ' Method ID оплаты. '
        self.is_suspicious: bool | None = is_suspicious
        ' Is the transaction suspicious?. '
        self.sbp_bank_name: str | None = sbp_bank_name
        ' Название банка СБП (если транзакция была совершена с помощью СБП). '

class TransactionPageInfo:
    """
    Подкласс, описывающий информацию о странице транзакций.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class TransactionList:
    """
    Класс, описывающий страницу сообщений чата.

    :param transactions: Транзакции страницы.
    :type transactions: `list[playerokapi.types.Transaction]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.TransactionPageInfo`

    :param total_count: Всего транзакций на странице.
    :type total_count: `int`
    """

    def __init__(self, transactions: list[Transaction], page_info: TransactionPageInfo, total_count: int):
        self.transactions: list[Transaction] = transactions
        ' Page Transactions. '
        self.page_info: TransactionPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total транзакций on странице. '

class UserBankCard:
    """
    Объект банковской карты пользователя.

    :param id: ID card.
    :type id: `str`

    :param card_first_six: First six digits of the card.
    :type card_first_six: `str`

    :param card_last_four: Last four digits of the card.
    :type card_last_four: `str`

    :param card_type: Bank card type.
    :type card_type: `playerokapi.enums.BankCardTypes`

    :param is_chosen: Is this card selected as default??
    :type is_chosen: `bool`
    """

    def __init__(self, id: str, card_first_six: str, card_last_four: str, card_type: BankCardTypes, is_chosen: bool):
        self.id: str = id
        ' ID card. '
        self.card_first_six: str = card_first_six
        ' First six digits of the card. '
        self.card_last_four: str = card_last_four
        ' Last four digits of the card. '
        self.card_type: BankCardTypes = card_type
        ' Bank card type. '
        self.is_chosen: bool = is_chosen
        ' Is this card selected as default?? '

class UserBankCardPageInfo:
    """
    Подкласс, описывающий информацию о странице банковских карт пользователя.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class UserBankCardList:
    """
    Класс, описывающий страницу банковских карт пользователя.

    :param bank_cards: Банковские карты страницы.
    :type bank_cards: `list[playerokapi.types.UserBankCard]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.UserBankCardPageInfo`

    :param total_count: Всего банковских карт на странице.
    :type total_count: `int`
    """

    def __init__(self, bank_cards: list[UserBankCard], page_info: UserBankCardPageInfo, total_count: int):
        self.bank_cards: list[UserBankCard] = bank_cards
        ' Bank cards page. '
        self.page_info: UserBankCardPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total банковских карт on странице. '

class Moderator:

    def __init__(self):
        pass

class TemporaryAttachmentUploadOutput:
    """
    Выходные данные для загрузки временного вложения
    (приложенное к сообщению изображение).

    :param id: ID данных.
    :type id: `str`

    :param url: URL изображения.
    :type url: `str`

    :param chat_id: ID чата, куда отправляется изображение.
    :type chat_id: `str`

    :param client_attachment_id: ID файла-приложения клиента.
    :type client_attachment_id: `str`

    :param expires_at: Дата истечения.
    :type expires_at: `str`
    """

    def __init__(self, id: str, url: str, chat_id: str, client_attachment_id: str, expires_at: str):
        self.id: str = id
        ' Data ID. '
        self.url: str = id
        ' Image URL. '
        self.chat_id: str = id
        ' Chat ID, куда отправляется изображение. '
        self.client_attachment_id: str = id
        ' ID applications the client. '
        self.expires_at: str = id
        ' Expiration date. '

class ChatMessageButton:
    """
    Объект кнопки сообщения.

    :param type: Button type.
    :type type: `playerokapi.types.ChatMessageButtonTypes`

    :param url: Button URL.
    :type url: `str` or None

    :param text: Button text.
    :type text: `str`
    """

    def __init__(self, type: ChatMessageButtonTypes, url: str | None, text: str):
        self.type: ChatMessageButtonTypes = type
        ' Button type. '
        self.url: str | None = url
        ' Button URL. '
        self.text: str = text
        ' Button text. '

class ChatMessage:
    """
    Класс, описывающий сообщение в чате.

    :param id: ID сообщения.
    :type id: `str`

    :param text: Текст сообщения.
    :type text: `str`

    :param created_at: Дата создания сообщения.
    :type created_at: `str`

    :param deleted_at: Дата удаления сообщения.
    :type deleted_at: `str` or `None`

    :param is_read: Прочитано ли сообщение.
    :type is_read: `bool`

    :param is_suspicious: Подозрительное ли сообщение.
    :type is_suspicious: `bool`

    :param is_bulk_messaging: Массовая ли это рассылка.
    :type is_bulk_messaging: `bool`

    :param game: Игра, к которой относится сообщение.
    :type game: `str` or `None`

    :param file: Файл, прикреплённый к сообщению.
    :type file: `playerokapi.types.FileObject` or `None`

    :param user: Пользователь, который отправил сообщение.
    :type user: `playerokapi.types.UserProfile`

    :param deal: Сделка, к которой относится сообщение.
    :type deal: `playerokapi.types.Deal` or `None`

    :param item: Предмет, к которому относится сообщение (обычно передаётся только сама сделка в переменную deal).
    :type item: `playerokapi.types.Item` or `None`

    :param transaction: Транзакция сообщения.
    :type transaction: `playerokapi.types.Transaction` or `None`

    :param moderator: Модератор сообщения.
    :type moderator: `playerokapi.types.Moderator`

    :param event_by_user: Ивент от пользователя.
    :type event_by_user: `playerokapi.types.UserProfile` or `None`

    :param event_to_user: Ивент для пользователя.
    :type event_to_user: `playerokapi.types.UserProfile` or `None`

    :param is_auto_response: Авто-ответ ли это.
    :type is_auto_response: `bool`

    :param event: Ивент сообщения.
    :type event: `playerokapi.types.Event` or `None`

    :param buttons: Кнопки сообщения.
    :type buttons: `list[playerokapi.types.MessageButton]`
    """

    def __init__(self, id: str, text: str, created_at: str, deleted_at: str | None, is_read: bool, is_suspicious: bool, is_bulk_messaging: bool, game: Game | None, file: FileObject | None, user: UserProfile, deal: ItemDeal | None, item: ItemProfile | None, transaction: Transaction | None, moderator: Moderator | None, event_by_user: UserProfile | None, event_to_user: UserProfile | None, is_auto_response: bool, event: Event | None, buttons: list[ChatMessageButton]):
        self.id: str = id
        ' Message ID. '
        self.text: str = text
        ' Message text. '
        self.created_at: str = created_at
        ' Creation date сообщения. '
        self.deleted_at: str | None = deleted_at
        ' Date the message was deleted. '
        self.is_read: bool = is_read
        ' Has the message been read?. '
        self.is_suspicious: bool = is_suspicious
        ' Is the message suspicious?. '
        self.is_bulk_messaging: bool = is_bulk_messaging
        ' Is this a mass mailing?. '
        self.game: Game | None = game
        ' A game, к которой относится сообщение. '
        self.file: FileObject | None = file
        ' Файл, прикреплённый к сообщению. '
        self.user: UserProfile = user
        ' Пользователь, который отправил сообщение. '
        self.deal: ItemDeal | None = deal
        ' Сделка, к которой относится сообщение. '
        self.item: ItemProfile | None = item
        ' Предмет, к которому относится сообщение (обычно передаётся только сама сделка в переменную deal). '
        self.transaction: Transaction | None = transaction
        ' Message transaction. '
        self.moderator: Moderator = moderator
        ' Moderator сообщения. '
        self.event_by_user: UserProfile | None = event_by_user
        ' User event. '
        self.event_to_user: UserProfile | None = event_to_user
        ' User event. '
        self.is_auto_response: bool = is_auto_response
        ' Авто-ответ ли это. '
        self.event: Event | None = event
        ' Event messages. '
        self.buttons: list[ChatMessageButton] = buttons
        ' Message Buttons. '

class ChatMessagePageInfo:
    """
    Подкласс, описывающий информацию о странице сообщений.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class ChatMessageList:
    """
    Класс, описывающий страницу сообщений чата.

    :param messages: Сообщения страницы.
    :type messages: `list[playerokapi.types.ChatMessage]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.ChatMessagePageInfo`

    :param total_count: Всего сообщений в чате.
    :type total_count: `int`
    """

    def __init__(self, messages: list[ChatMessage], page_info: ChatMessagePageInfo, total_count: int):
        self.messages: list[ChatMessage] = messages
        ' Page Posts. '
        self.page_info: ChatMessagePageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total сообщений в чате. '

class Chat:
    """
    Объект чата.

    :param id: ID чата.
    :type id: `str`

    :param type: Тип чата.
    :type type: `playerokapi.enums.ChatTypes`

    :param status: Статус чата.
    :type status: `playerokapi.enums.ChatStatuses` or `None`

    :param unread_messages_counter: Количество непрочитанных сообщений.
    :type unread_messages_counter: `int`

    :param bookmarked: В закладках ли чат.
    :type bookmarked: `bool` or `None`

    :param is_texting_allowed: Разрешено ли писать в чат.
    :type is_texting_allowed: `bool` or `None`

    :param owner: Владелец чата (только если это чат с ботом).
    :type owner: `bool` or `None`

    :param deals: Сделки в чате.
    :type deals: `list[playerokapi.types.ItemDeal]` or `None`

    :param last_message: Объект последнего сообщения в чате
    :type last_message: `playerokapi.types.ChatMessage` or `None`

    :param users: Участники чата.
    :type users: `list[UserProfile]`

    :param started_at: Дата начала диалога.
    :type started_at: `str` or `None`

    :param finished_at: Дата завершения диалога.
    :type finished_at: `str` or `None`
    """

    def __init__(self, id: str, type: ChatTypes, status: ChatStatuses | None, unread_messages_counter: int, bookmarked: bool | None, is_texting_allowed: bool | None, owner: UserProfile | None, deals: list[ItemDeal] | None, started_at: str | None, finished_at: str | None, last_message: ChatMessage | None, users: list[UserProfile]):
        self.id: str = id
        ' Chat ID. '
        self.type: ChatTypes = type
        ' Chat type. '
        self.status: ChatStatuses | None = status
        ' Chat status. '
        self.unread_messages_counter: int = unread_messages_counter
        ' Number of unread messages. '
        self.bookmarked: bool | None = bookmarked
        ' I bookmarked chat. '
        self.is_texting_allowed: bool | None = is_texting_allowed
        ' Is it allowed to write in chat?. '
        self.owner: UserProfile = owner
        ' Chat owner. '
        self.deals: list[ItemDeal] | None = deals
        ' Transactions in chat. '
        self.last_message: ChatMessage | None = last_message
        ' Last chat message object. '
        self.users: list[UserProfile] = users
        ' Chat participants. '
        self.started_at: str | None = started_at
        ' Dialogue start date. '
        self.finished_at: str | None = finished_at
        ' Dialogue end date. '

class ChatPageInfo:
    """
    Подкласс, описывающий информацию о странице чатов.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class ChatList:
    """
    Класс, описывающий страницу чатов.

    :param chats: Чаты страницы.
    :type chats: `list[playerokapi.types.Chat]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.ChatPageInfo`

    :param total_count: Всего чатов.
    :type total_count: `int`
    """

    def __init__(self, chats: list[Chat], page_info: ChatPageInfo, total_count: int):
        self.chats: list[Chat] = chats
        ' Chats pages. '
        self.page_info: ChatPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total чатов. '

class Review:
    """
    Объект отзыва.

    :param id: Review ID.
    :type id: `str`

    :param status: Review status.
    :type status: `playerokapi.enums.ReviewStatuses`

    :param text: Review text.
    :type text: `str` or `None`

    :param rating: Rating отзыва.
    :type rating: `int`

    :param created_at: Creation date отзыва.
    :type created_at: `str`

    :param updated_at: Review modification date.
    :type updated_at: `str`

    :param deal: Сделка, связанная с отзывом.
    :type deal: `Deal`

    :param creator: Review Creator Profile.
    :type creator: `UserProfile`

    :param moderator: Moderator, обработавший отзыв.
    :type moderator: `Moderator` or `None`

    :param user: Seller Profile, к которому относится отзыв.
    :type user: `UserProfile`
    """

    def __init__(self, id: str, status: ReviewStatuses, text: str | None, rating: int, created_at: str, updated_at: str, deal: ItemDeal, creator: UserProfile, moderator: Moderator | None, user: UserProfile):
        self.id: str = id
        ' Review ID. '
        self.status: ReviewStatuses = status
        ' Review status. '
        self.text: str | None = text
        ' Review text. '
        self.rating: int = rating
        ' Rating отзыва. '
        self.created_at: str = created_at
        ' Creation date отзыва. '
        self.updated_at: str = updated_at
        ' Review modification date. '
        self.deal: ItemDeal = deal
        ' Сделка, связанная с отзывом. '
        self.creator: UserProfile = creator
        ' Review Creator Profile. '
        self.moderator: Moderator | None = moderator
        ' Moderator, обработавший отзыв. '
        self.user: UserProfile = user
        ' Seller Profile, к которому относится отзыв. '

class ReviewPageInfo:
    """
    Подкласс, описывающий информацию о странице отзывов.

    :param start_cursor: Top of page cursor.
    :type start_cursor: `str`

    :param end_cursor: Курсок конца страницы.
    :type end_cursor: `str`

    :param has_previous_page: Does the previous page.
    :type has_previous_page: `bool`

    :param has_next_page: Does the next page.
    :type has_next_page: `bool`
    """

    def __init__(self, start_cursor: str, end_cursor: str, has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        ' Top of page cursor. '
        self.end_cursor: str = end_cursor
        ' End of page cursor. '
        self.has_previous_page: bool = has_previous_page
        ' Does the previous page. '
        self.has_next_page: bool = has_next_page
        ' Does the next page. '

class ReviewList:
    """
    Класс, описывающий страницу отзывов.

    :param reviews: Отзывы страницы.
    :type reviews: `list[playerokapi.types.Review]`

    :param page_info: Информация о странице.
    :type page_info: `playerokapi.types.ReviewPageInfo`

    :param total_count: Всего отзывов.
    :type total_count: `int`
    """

    def __init__(self, reviews: list[Review], page_info: ReviewPageInfo, total_count: int):
        self.reviews: list[Review] = reviews
        ' Reviews страницы. '
        self.page_info: ReviewPageInfo = page_info
        ' Page information. '
        self.total_count: int = total_count
        ' Total отзывов. '