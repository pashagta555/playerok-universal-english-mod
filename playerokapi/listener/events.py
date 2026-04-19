The text is in Russian, so I'll translate it to English while keeping the code unchanged:

```
from ..enums import EventTypes
from .. import types
import time


class BaseEvent:
    """
    Basic event class.

    :param event_type: Type of event.
    :type event_type: `PlayerokAPI.enums.EventTypes`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, event_type: EventTypes, chat: types.Chat):
        self.type = event_type
        """ Type of event. """
        self.chat = chat
        """ Chat object where the event occurred. """
        self.time = time.time()
        """ Time of the event. """


class ChatInitializedEvent(BaseEvent):
    """
    Class event: chat is initialized when runner makes first request.

    :param chat: Object of detected chat.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, chat: types.Chat):
        super(ChatInitializedEvent, self).__init__(
            EventTypes.CHAT_INITIALIZED, chat
        )
        self.chat: types.Chat = chat
        """ Object of detected chat. """


class NewMessageEvent(BaseEvent):
    """
    Class event: new message in chat.

    :param message: Object of received message.
    :type message: `PlayerokAPI.types.ChatMessage`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, message: types.ChatMessage, chat: types.Chat):
        super(NewMessageEvent, self).__init__(EventTypes.NEW_MESSAGE, chat)
        self.message: types.ChatMessage = message
        """ Object of received message. """


class NewDealEvent(BaseEvent):
    """
    Class event: new deal created (when buyer paid for item).

    :param deal: Object of new deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewDealEvent, self).__init__(EventTypes.NEW_DEAL, chat)
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class NewReviewEvent(BaseEvent):
    """
    Class event: new review from buyer.

    :param deal: Object of deal with review.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(NewReviewEvent, self).__init__(EventTypes.NEW_REVIEW, chat)
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class DealConfirmedEvent(BaseEvent):
    """
    Class event: buyer confirmed the deal.

    :param deal: Object of deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealConfirmedEvent, self).__init__(EventTypes.DEAL_CONFIRMED, chat)
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class DealRolledBackEvent(BaseEvent):
    """
    Class event: seller rolled back the deal.

    :param deal: Object of deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealRolledBackEvent, self).__init__(EventTypes.DEAL_ROLLED_BACK, chat)
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class DealHasProblemEvent(BaseEvent):
    """
    Class event: someone reported a problem with the deal.

    :param deal: Object of deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealHasProblemEvent, self).__init__(EventTypes.DEAL_HAS_PROBLEM, chat)
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class DealProblemResolvedEvent(BaseEvent):
    """
    Class event: problem with the deal is resolved.

    :param deal: Object of deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealProblemResolvedEvent, self).__init__(
            EventTypes.DEAL_PROBLEM_RESOLVED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class DealStatusChangedEvent(BaseEvent):
    """
    Class event: status of the deal changed.

    :param deal: Object of deal.
    :type deal: `PlayerokAPI.types.ItemDeal`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(DealStatusChangedEvent, self).__init__(
            EventTypes.DEAL_STATUS_CHANGED, chat
        )
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class ItemPaidEvent(BaseEvent):
    """
    Class event: item is paid for.

    :param deal: Object of deal.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemPaidEvent, self).__init__(EventTypes.ITEM_PAID, chat)
        self.deal: types.ItemDeal = deal
        """ Object of deal. """


class ItemSentEvent(BaseEvent):
    """
    Class event: item is sent to buyer.

    :param deal: Object of deal.
    :type deal: `PlayerokAPI.types.Item`

    :param chat: Chat object where the event occurred.
    :type chat: `PlayerokAPI.types.Chat`
    """

    def __init__(self, deal: types.ItemDeal, chat: types.Chat):
        super(ItemSentEvent, self).__init__(EventTypes.ITEM_SENT, chat)
        self.deal: types.ItemDeal = deal
        """ Object of deal. """
```

