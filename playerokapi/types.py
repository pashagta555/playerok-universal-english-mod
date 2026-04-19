Here is the translation of the text to English, keeping the code unchanged:

```
from __future__ import annotations
from typing import List, Optional

class ChatMessage:
    def __init__(self, id: str, text: str, created_at: str, updated_at: str):
        self.id: str = id
        """ ID сообщения. """
        self.text: str = text
        """ Текст сообщения. """
        self.created_at: str = created_at
        """ Дата создания сообщения. """
        self.updated_at: str = updated_at
        """ Дата изменения сообщения. """

class Chat:
    def __init__(self, id: str, type: str, status: Optional[str], unread_messages_counter: int,
                 bookmarked: bool, is_texting_allowed: bool, owner: Optional[UserProfile], deals: List[ItemDeal],
                 started_at: str, finished_at: str, last_message: ChatMessage, users: List[UserProfile]):
        self.id: str = id
        """ ID чата. """
        self.type: str = type
        """ Тип чата. """
        self.status: Optional[str] = status
        """ Статус чата. """
        self.unread_messages_counter: int = unread_messages_counter
        """ Количество непрочитанных сообщений. """
        self.bookmarked: bool = bookmarked
        """ В закладках ли чат. """
        self.is_texting_allowed: bool = is_texting_allowed
        """ Разрешено ли писать в чат. """
        self.owner: Optional[UserProfile] = owner
        """ Владелец чата (только если это чат с ботом). """
        self.deals: List[ItemDeal] = deals
        """ Сделки в чате. """
        self.last_message: ChatMessage = last_message
        """ Объект последнего сообщения в чате. """
        self.users: List[UserProfile] = users
        """ Участники чата. """
        self.started_at: str = started_at
        """ Дата начала диалога. """
        self.finished_at: str = finished_at
        """ Дата завершения диалога. """

class ChatPageInfo:
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Курсор начала страницы. """
        self.end_cursor: str = end_cursor
        """ Курсор конца страницы. """
        self.has_previous_page: bool = has_previous_page
        """ Имеет ли предыдущую страницу. """
        self.has_next_page: bool = has_next_page
        """ Имеет ли следующую страницу. """

class ChatList:
    def __init__(self, chats: List[Chat], page_info: ChatPageInfo,
                 total_count: int):
        self.chats: List[Chat] = chats
        """ Чаты страницы. """
        self.page_info: ChatPageInfo = page_info
        """ Информация о странице. """
        self.total_count: int = total_count
        """ Всего чатов. """

class Review:
    def __init__(self, id: str, status: str, text: Optional[str], rating: int,
                 created_at: str, updated_at: str, deal: ItemDeal, creator: UserProfile,
                 moderator: Optional[UserProfile], user: UserProfile):
        self.id: str = id
        """ ID отзыва. """
        self.status: str = status
        """ Статус отзыва. """
        self.text: Optional[str] = text
        """ Текст отзыва. """
        self.rating: int = rating
        """ Рейтинг отзыва. """
        self.created_at: str = created_at
        """ Дата создания отзыва. """
        self.updated_at: str = updated_at
        """ Дата изменения отзыва. """
        self.deal: ItemDeal = deal
        """ Сделка, связанная с отзывом. """
        self.creator: UserProfile = creator
        """ Профиль создателя отзыва. """
        self.moderator: Optional[UserProfile] = moderator
        """ Модератор, обработавший отзыв. """
        self.user: UserProfile = user
        """ Профиль продавца, к которому относится отзыв. """

class ReviewPageInfo:
    def __init__(self, start_cursor: str, end_cursor: str,
                 has_previous_page: bool, has_next_page: bool):
        self.start_cursor: str = start_cursor
        """ Курсор начала страницы. """
        self.end_cursor: str = end_cursor
        """ Курсор конца страницы. """
        self.has_previous_page: bool = has_previous_page
        """ Имеет ли предыдущую страницу. """
        self.has_next_page: bool = has_next_page
        """ Имеет ли следующую страницу. """

class ReviewList:
    def __init__(self, reviews: List[Review], page_info: ReviewPageInfo,
                 total_count: int):
        self.reviews: List[Review] = reviews
        """ Отзывы страницы. """
        self.page_info: ReviewPageInfo = page_info
        """ Информация о странице. """
        self.total_count: int = total_count
        """ Всего отзывов. """

class UserProfile:
    pass

class ItemDeal:
    pass

class ChatStatuses:
    pass

class ReviewStatuses:
    pass

class ModerationLevel:
    pass
```

