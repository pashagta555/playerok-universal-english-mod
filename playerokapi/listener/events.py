from ..enums import EventTypes
from .. import types
import time


class BaseEvent:
    """
    Base event class.

    :param event_type: Type of event.
    :type event_type: `PlayerokAPI.enums.EventTypes`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, event_type: EventTypes, chat: types.Chat):
        self.type = event_type
        """ Type of event. """
        self.chat = chat
        """ Chat object in which the event occurred. """
        self.time = time.time()
        """ Time of the event. """


class ChatInitializedEvent(BaseEvent):
    """
    Event class: chat detected during the first Runner request.

    :param chat: Detected chat object.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, chat: types.Chat):
        super(ChatInitializedEvent, self).__init__(
            EventTypes.CHAT_INITIALIZED, chat
        )
        self.chat: types.Chat = chat
        """ Detected chat object. """


class NewMessageEvent(BaseEvent):
    """
    Event class: new message in the chat.

    :param message: Received message object.
    :type message: `PlayerokAPI.types.ChatMessage`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, message: types.ChatMessage, chat: types.Chat):
        super(NewMessageEvent, self).__init__(EventTypes.NEW_MESSAGE, chat)
        self.message: types.ChatMessage = message
        """ Received message object. """


class NewDealEvent(BaseEvent):
    """
    Event class: new deal created (when the buyer has paid for the item).

    :param deal: New deal object.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewDealEvent, self).__init__(EventTypes.NEW_DEAL, chat)
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class NewReviewEvent(BaseEvent):
    """
    Event class: new review from the buyer.

    :param deal: Deal object with the review.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewReviewEvent, self).__init__(EventTypes.NEW_REVIEW, chat)
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class DealConfirmedEvent(BaseEvent):
    """
    Event class: the buyer confirmed the deal.

    :param deal: Deal object.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealConfirmedEvent, self).__init__(EventTypes.DEAL_CONFIRMED, chat)
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class DealRolledBackEvent(BaseEvent):
    """
    Event class: the seller refunded the deal.

    :param deal: Deal object.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealRolledBackEvent, self).__init__(EventTypes.DEAL_ROLLED_BACK, chat)
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class DealHasProblemEvent(BaseEvent):
    """
    Event class: someone reported a problem with the deal.

    :param deal: Deal object.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealHasProblemEvent, self).__init__(EventTypes.DEAL_HAS_PROBLEM, chat)
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class DealProblemResolvedEvent(BaseEvent):
    """
    Event class: the problem in the deal has been resolved.

    :param deal: Deal object.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealProblemResolvedEvent, self).__init__(
            EventTypes.DEAL_PROBLEM_RESOLVED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class DealStatusChangedEvent(BaseEvent):
    """
    Event class: deal status changed.

    :param deal: Deal object.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealStatusChangedEvent, self).__init__(
            EventTypes.DEAL_STATUS_CHANGED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class ItemPaidEvent(BaseEvent):
    """
    Event class: item has been paid for.

    :param deal: Deal object.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemPaidEvent, self).__init__(EventTypes.ITEM_PAID, chat)
        self.deal: types.ItemDeal = deal
        """ Deal object. """


class ItemSentEvent(BaseEvent):
    """
    Event class: item has been sent to the buyer.

    :param deal: Deal object.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemSentEvent, self).__init__(EventTypes.ITEM_SENT, chat)
        self.deal: types.ItemDeal = deal
        """ Deal object. """