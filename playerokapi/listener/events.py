from ..enums import EventTypes
from .. import types
import time


class BaseEvent:
    """
    Base Class events.

    :param event_type: Type events.
    :type event_type: `PlayerokAPI.enums.EventTypes`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, event_type: EventTypes, chat: types.Chat):
        self.type = event_type
        """ Type events. """
        self.chat = chat
        """ Object chat, V which happened event. """
        self.time = time.time()
        """ Time events. """


class ChatInitializedEvent(BaseEvent):
    """
    Class events: discovered chat at first request Runner'A.

    :param chat: Object discovered chat.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, chat: types.Chat):
        super(ChatInitializedEvent, self).__init__(
            EventTypes.CHAT_INITIALIZED, chat
        )
        self.chat: types.Chat = chat
        """ Object discovered chat. """


class NewMessageEvent(BaseEvent):
    """
    Class events: new message V chat.

    :param message: Object received messages.
    :type message: `PlayerokAPI.types.ChatMessage`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, message: types.ChatMessage, chat: types.Chat):
        super(NewMessageEvent, self).__init__(EventTypes.NEW_MESSAGE, chat)
        self.message: types.ChatMessage = message
        """ Object received messages. """


class NewDealEvent(BaseEvent):
    """
    Class events: new created deal (When buyer paid item).

    :param deal: Object new deals.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewDealEvent, self).__init__(EventTypes.NEW_DEAL, chat)
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class NewReviewEvent(BaseEvent):
    """
    Class events: new review from buyer.

    :param deal: Object deals With review.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewReviewEvent, self).__init__(EventTypes.NEW_REVIEW, chat)
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class DealConfirmedEvent(BaseEvent):
    """
    Class events: buyer confirmed deal.

    :param deal: Object deals.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealConfirmedEvent, self).__init__(EventTypes.DEAL_CONFIRMED, chat)
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class DealRolledBackEvent(BaseEvent):
    """
    Class events: salesman returned funds for deal.

    :param deal: Object deals.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealRolledBackEvent, self).__init__(EventTypes.DEAL_ROLLED_BACK, chat)
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class DealHasProblemEvent(BaseEvent):
    """
    Class events: Who-That reported O problem V deal.

    :param deal: Object deals.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealHasProblemEvent, self).__init__(EventTypes.DEAL_HAS_PROBLEM, chat)
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class DealProblemResolvedEvent(BaseEvent):
    """
    Class events: problem V deal resolved.

    :param deal: Object deals.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealProblemResolvedEvent, self).__init__(
            EventTypes.DEAL_PROBLEM_RESOLVED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class DealStatusChangedEvent(BaseEvent):
    """
    Class events: status deals changed.

    :param deal: Object deals.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealStatusChangedEvent, self).__init__(
            EventTypes.DEAL_STATUS_CHANGED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class ItemPaidEvent(BaseEvent):
    """
    Class events: item paid.

    :param deal: Object deals.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemPaidEvent, self).__init__(EventTypes.ITEM_PAID, chat)
        self.deal: types.ItemDeal = deal
        """ Object deals. """


class ItemSentEvent(BaseEvent):
    """
    Class events: item sent to the buyer.

    :param deal: Object deals.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Object chat, V which happened event.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemSentEvent, self).__init__(EventTypes.ITEM_SENT, chat)
        self.deal: types.ItemDeal = deal
        """ Object Transactions. """