from ..enums import EventTypes
from .. import types
import time


class BaseEvent:
    """
    Base event class.

    :param event_type: Event type.
    :type event_type: `PlayerokAPI.enums.EventTypes`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, event_type: EventTypes, chat: types.Chat):
        self.type = event_type
        """ Event type. """
        self.chat = chat
        """ The chat object in which the event occurred. """
        self.time = time.time()
        """ Event time. """


class ChatInitializedEvent(BaseEvent):
    """
    Event class: Chat detected on Runner's first request.

    :param chat: The detected chat object.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, chat: types.Chat):
        super(ChatInitializedEvent, self).__init__(
            EventTypes.CHAT_INITIALIZED, chat
        )
        self.chat: types.Chat = chat
        """ Object of the detected chat. """


class NewMessageEvent(BaseEvent):
    """
    Event class: new chat message.

    :param message: Object of the received message.
    :type message: `PlayerokAPI.types.ChatMessage`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, message: types.ChatMessage, chat: types.Chat):
        super(NewMessageEvent, self).__init__(EventTypes.NEW_MESSAGE, chat)
        self.message: types.ChatMessage = message
        """ Object of the received message. """


class NewDealEvent(BaseEvent):
    """
    Event class: new transaction created (when the buyer paid for the item).

    :param deal: New deal object.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewDealEvent, self).__init__(EventTypes.NEW_DEAL, chat)
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class NewReviewEvent(BaseEvent):
    """
    Event class: new review from a customer.

    :param deal: Deal object with review.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewReviewEvent, self).__init__(EventTypes.NEW_REVIEW, chat)
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class DealConfirmedEvent(BaseEvent):
    """
    Event class: the buyer confirmed the transaction.

    :param deal: Object of the deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealConfirmedEvent, self).__init__(EventTypes.DEAL_CONFIRMED, chat)
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class DealRolledBackEvent(BaseEvent):
    """
    Event class: the seller has returned funds for the transaction.

    :param deal: Object of the deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealRolledBackEvent, self).__init__(EventTypes.DEAL_ROLLED_BACK, chat)
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class DealHasProblemEvent(BaseEvent):
    """
    Event class: Someone reported a problem with the transaction.

    :param deal: Object of the deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealHasProblemEvent, self).__init__(EventTypes.DEAL_HAS_PROBLEM, chat)
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class DealProblemResolvedEvent(BaseEvent):
    """
    Event class: transaction problem resolved.

    :param deal: Object of the deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealProblemResolvedEvent, self).__init__(
            EventTypes.DEAL_PROBLEM_RESOLVED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class DealStatusChangedEvent(BaseEvent):
    """
    Event class: transaction status changed.

    :param deal: Object of the deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealStatusChangedEvent, self).__init__(
            EventTypes.DEAL_STATUS_CHANGED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class ItemPaidEvent(BaseEvent):
    """
    Event class: item paid for.

    :param deal: Object of the deal.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemPaidEvent, self).__init__(EventTypes.ITEM_PAID, chat)
        self.deal: types.ItemDeal = deal
        """ Object of transaction. """


class ItemSentEvent(BaseEvent):
    """
    Event Class: The item has been shipped to the buyer.

    :param deal: Object of the deal.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: The chat object in which the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemSentEvent, self).__init__(EventTypes.ITEM_SENT, chat)
        self.deal: types.ItemDeal = deal
        """ Transaction Object. """