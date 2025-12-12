from ..enums import EventTypes
from .. import types
import time


class BaseEvent:
    """
    Base event class.

    :param event_type: Event type.
    :type event_type: `PlayerokAPI.enums.EventTypes`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, event_type: EventTypes, chat_obj: types.Chat):
        self.type = event_type
        """ Event type. """
        self.chat = chat_obj
        """ Chat object where event occurred. """
        self.time = time.time()
        """ Event time. """


class ChatInitializedEvent(BaseEvent):
    """
    Event class: chat detected on first Runner request.

    :param chat_obj: Detected chat object.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, chat_obj: types.Chat):
        super(ChatInitializedEvent, self).__init__(
            EventTypes.CHAT_INITIALIZED, chat_obj
        )
        self.chat: types.Chat = chat_obj
        """ Detected chat object. """


class NewMessageEvent(BaseEvent):
    """
    Event class: new message in chat.

    :param message_obj: Received message object.
    :type message_obj: `PlayerokAPI.types.ChatMessage`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, message_obj: types.ChatMessage, chat_obj: types.Chat):
        super(NewMessageEvent, self).__init__(EventTypes.NEW_MESSAGE, chat_obj)
        self.message: types.ChatMessage = message_obj
        """ Received message object. """


class NewDealEvent(BaseEvent):
    """
    Event class: new deal created (when buyer paid for item).

    :param deal_obj: New deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(NewDealEvent, self).__init__(EventTypes.NEW_DEAL, chat_obj)
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class NewReviewEvent(BaseEvent):
    """
    Event class: new review from buyer.

    :param deal_obj: Deal object with review.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(NewReviewEvent, self).__init__(EventTypes.NEW_REVIEW, chat_obj)
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class DealConfirmedEvent(BaseEvent):
    """
    Event class: buyer confirmed deal.

    :param deal_obj: Deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(DealConfirmedEvent, self).__init__(EventTypes.DEAL_CONFIRMED, chat_obj)
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class DealRolledBackEvent(BaseEvent):
    """
    Event class: seller refunded deal.

    :param deal_obj: Deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(DealRolledBackEvent, self).__init__(EventTypes.DEAL_ROLLED_BACK, chat_obj)
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class DealHasProblemEvent(BaseEvent):
    """
    Event class: someone reported a problem in deal.

    :param deal_obj: Deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(DealHasProblemEvent, self).__init__(EventTypes.DEAL_HAS_PROBLEM, chat_obj)
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class DealProblemResolvedEvent(BaseEvent):
    """
    Event class: deal problem resolved.

    :param deal_obj: Deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(DealProblemResolvedEvent, self).__init__(
            EventTypes.DEAL_PROBLEM_RESOLVED, chat_obj
        )
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class DealStatusChangedEvent(BaseEvent):
    """
    Event class: deal status changed.

    :param deal_obj: Deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(DealStatusChangedEvent, self).__init__(
            EventTypes.DEAL_STATUS_CHANGED, chat_obj
        )
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class ItemPaidEvent(BaseEvent):
    """
    Event class: item paid.

    :param deal_obj: Deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(ItemPaidEvent, self).__init__(EventTypes.ITEM_PAID, chat_obj)
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """


class ItemSentEvent(BaseEvent):
    """
    Event class: item sent to buyer.

    :param deal_obj: Deal object.
    :type deal_obj: `PlayerokAPI.types.ItemDeal`

    :param chat_obj: Chat object where event occurred.
    :type chat_obj: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal_obj: types.ItemDeal, chat_obj: types.Chat):
        super(ItemSentEvent, self).__init__(EventTypes.ITEM_SENT, chat_obj)
        self.deal: types.ItemDeal = deal_obj
        """ Deal object. """