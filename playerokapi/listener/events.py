from ..enums import EventTypes 
from ..import types 
import time 


class BaseEvent :
    "Basic event class.

    :param event_type: Type of event.
    :type event_type: PlayerokAPI.enums.EventTypes

    :param chat: Chat object where the event occurred.
    :type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,event_type :EventTypes ,chat :types .Chat ):
        self .type =event_type 
        "Event type."
        self .chat =chat 
        "Event object where the event occurred."
        self .time =time .time ()
        "Event time."


class ChatInitializedEvent (BaseEvent ):
    "Class event: a chat is found on the first Runner query.

    :param chat: Chat object discovered.
    :type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,chat :types .Chat ):
        super (ChatInitializedEvent ,self ).__init__ (
        EventTypes .CHAT_INITIALIZED ,chat 
        )
        self .chat :types .Chat =chat 
        "Detected chat object."


class NewMessageEvent (BaseEvent ):
    "Event class: new message in the chat.

:param message: Object of received message.
:type message: PlayerokAPI.types.ChatMessage

:param chat: Object of the chat where the event occurred.
:type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,message :types .ChatMessage ,chat :types .Chat ):
        super (NewMessageEvent ,self ).__init__ (EventTypes .NEW_MESSAGE ,chat )
        self .message :types .ChatMessage =message 
        "Received message object."


class NewDealEvent (BaseEvent ):
    "Event class: new created deal (when the buyer paid for the item).

:param deal: Object of a new deal.
:type deal: PlayerokAPI.types.ItemDeal

:param chat: Object of the chat where the event occurred.
:type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (NewDealEvent ,self ).__init__ (EventTypes .NEW_DEAL ,chat )
        self .deal :types .ItemDeal =deal 
        "Transaction object."


class NewReviewEvent (BaseEvent ):
    "Event class: new customer review.

:param deal: Deal object with a review.
:type deal: PlayerokAPI.types.ItemDeal

:param chat: Chat object where the event occurred.
:type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (NewReviewEvent ,self ).__init__ (EventTypes .NEW_REVIEW ,chat )
        self .deal :types .ItemDeal =deal 
        "Transaction object."


class DealConfirmedEvent (BaseEvent ):
    "Event class: customer confirmed the deal.

:param deal: Deal object.
:type deal: PlayerokAPI.types.ItemDeal

:param chat: Chat object where the event occurred.
:type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealConfirmedEvent ,self ).__init__ (EventTypes .DEAL_CONFIRMED ,chat )
        self .deal :types .ItemDeal =deal 
        "Transaction object."


class DealRolledBackEvent (BaseEvent ):
    "Event class: seller returned funds for the transaction.

:param deal: Deal object.
:type deal: PlayerokAPI.types.ItemDeal

:param chat: Chat object where the event occurred.
:type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealRolledBackEvent ,self ).__init__ (EventTypes .DEAL_ROLLED_BACK ,chat )
        self .deal :types .ItemDeal =deal 
        "Transaction object."


class DealHasProblemEvent (BaseEvent ):
    "Event class: someone reported a problem in the deal.

:param deal: Deal object.
:type deal: `PlayerokAPI.types.ItemDeal`

:param chat: Chat object where the event occurred.
:type chat: `PlayerokAPI.types.Chat`"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealHasProblemEvent ,self ).__init__ (EventTypes .DEAL_HAS_PROBLEM ,chat )
        self .deal :types .ItemDeal =deal 
        "Transaction object."


class DealProblemResolvedEvent (BaseEvent ):
    "Event class: the problem in the deal is resolved.

:param deal: Object of a deal.
:type deal: `PlayerokAPI.types.ItemDeal`

:param chat: Object of a chat where the event occurred.
:type chat: `PlayerokAPI.types.Chat`"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealProblemResolvedEvent ,self ).__init__ (
        EventTypes .DEAL_PROBLEM_RESOLVED ,chat 
        )
        self .deal :types .ItemDeal =deal 
        "Transaction Object."


class DealStatusChangedEvent (BaseEvent ):
    "Event class: deal status changed.

:param deal: Deal object.
:type deal: PlayerokAPI.types.ItemDeal

:param chat: Chat object where the event occurred.
:type chat: PlayerokAPI.types.Chat"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealStatusChangedEvent ,self ).__init__ (
        EventTypes .DEAL_STATUS_CHANGED ,chat 
        )
        self .deal :types .ItemDeal =deal 
        "Transaction object."


class ItemPaidEvent (BaseEvent ):
    "Event class: item paid.

:param deal: Deal object.
:type deal: `PlayerokAPI.types.Item`

:param chat: Chat object where the event occurred.
:type chat: `PlayerokAPI.types.Chat`"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (ItemPaidEvent ,self ).__init__ (EventTypes .ITEM_PAID ,chat )
        self .deal :types .ItemDeal =deal 
        "Transaction object."


class ItemSentEvent (BaseEvent ):
    "Event class: item sent to customer.

:param deal: Deal object.
:type deal: `PlayerokAPI.types.Item`

:param chat: Chat object where the event occurred.
:type chat: `PlayerokAPI.types.Chat`"

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (ItemSentEvent ,self ).__init__ (EventTypes .ITEM_SENT ,chat )
        self .deal :types .ItemDeal =deal 
        "Object of Transaction."