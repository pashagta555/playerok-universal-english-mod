from ..enums import EventTypes
from .. import types
import time

class BaseEvent:
    """
    Базовый класс события.

    :param event_type: Event type.
    :type event_type: `PlayerokAPI.enums.EventTypes`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, event_type: EventTypes, chat: types.Chat):
        self.type = event_type
        ' Event type. '
        self.chat = chat
        ' Объект чата, в котором произошло событие. '
        self.time = time.time()
        ' Event time. '

class ChatInitializedEvent(BaseEvent):
    """
    Класс события: обнаружен чат при первом запросе Runner'а.

    :param chat: Detected chat object.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, chat: types.Chat):
        super(ChatInitializedEvent, self).__init__(EventTypes.CHAT_INITIALIZED, chat)
        self.chat: types.Chat = chat
        ' Detected chat object. '

class NewMessageEvent(BaseEvent):
    """
    Класс события: новое сообщение в чате.

    :param message: Received message object.
    :type message: `PlayerokAPI.types.ChatMessage`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, message: types.ChatMessage, chat: types.Chat):
        super(NewMessageEvent, self).__init__(EventTypes.NEW_MESSAGE, chat)
        self.message: types.ChatMessage = message
        ' Received message object. '

class NewDealEvent(BaseEvent):
    """
    Класс события: новая созданная сделка (когда покупатель оплатил предмет).

    :param deal: Объект новой сделки.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewDealEvent, self).__init__(EventTypes.NEW_DEAL, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class NewReviewEvent(BaseEvent):
    """
    Класс события: новый отзыв от покупателя.

    :param deal: Object of transaction с отзывом.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewReviewEvent, self).__init__(EventTypes.NEW_REVIEW, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class DealConfirmedEvent(BaseEvent):
    """
    Класс события: покупатель подтвердил сделку.

    :param deal: Object of transaction.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealConfirmedEvent, self).__init__(EventTypes.DEAL_CONFIRMED, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class DealRolledBackEvent(BaseEvent):
    """
    Класс события: продавец вернул средства за сделку.

    :param deal: Object of transaction.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealRolledBackEvent, self).__init__(EventTypes.DEAL_ROLLED_BACK, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class DealHasProblemEvent(BaseEvent):
    """
    Класс события: кто-то сообщил о проблеме в сделке.

    :param deal: Object of transaction.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealHasProblemEvent, self).__init__(EventTypes.DEAL_HAS_PROBLEM, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class DealProblemResolvedEvent(BaseEvent):
    """
    Класс события: проблема в сделке решена.

    :param deal: Object of transaction.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealProblemResolvedEvent, self).__init__(EventTypes.DEAL_PROBLEM_RESOLVED, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class DealStatusChangedEvent(BaseEvent):
    """
    Класс события: статус сделки изменён.

    :param deal: Object of transaction.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealStatusChangedEvent, self).__init__(EventTypes.DEAL_STATUS_CHANGED, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class ItemPaidEvent(BaseEvent):
    """
    Класс события: предмет оплачен.

    :param deal: Object of transaction.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemPaidEvent, self).__init__(EventTypes.ITEM_PAID, chat)
        self.deal: types.ItemDeal = deal
        ' Object of transaction. '

class ItemSentEvent(BaseEvent):
    """
    Класс события: предмет отправлен покупателю.

    :param deal: Object of transaction.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Объект чата, в котором произошло событие.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemSentEvent, self).__init__(EventTypes.ITEM_SENT, chat)
        self.deal: types.ItemDeal = deal
        ' Transaction Object. '