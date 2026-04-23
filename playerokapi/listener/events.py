from ..enums import EventTypes 
from ..import types 
import time 


class BaseEvent :
    'Base event class.\n\n    :param event_type: Event type.\n    :type event_type: `PlayerokAPI.enums.EventTypes`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,event_type :EventTypes ,chat :types .Chat ):
        self .type =event_type 
        'Event type.'
        self .chat =chat 
        'The chat object in which the event occurred.'
        self .time =time .time ()
        'Event time.'


class ChatInitializedEvent (BaseEvent ):
    "Event class: Chat detected on Runner's first request.\n\n    :param chat: The detected chat object.\n    :type chat: `PlayerokAPI.types.Chat`"

    def __init__ (self ,chat :types .Chat ):
        super (ChatInitializedEvent ,self ).__init__ (
        EventTypes .CHAT_INITIALIZED ,chat 
        )
        self .chat :types .Chat =chat 
        'The object of the detected chat.'


class NewMessageEvent (BaseEvent ):
    'Event class: new message in chat.\n\n    :param message: Object of the received message.\n    :type message: `PlayerokAPI.types.ChatMessage`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,message :types .ChatMessage ,chat :types .Chat ):
        super (NewMessageEvent ,self ).__init__ (EventTypes .NEW_MESSAGE ,chat )
        self .message :types .ChatMessage =message 
        'The object of the received message.'


class NewDealEvent (BaseEvent ):
    'Event class: New deal created (when the Buyer paid for the Item).\n\n    :param deal: New deal object.\n    :type deal: `PlayerokAPI.types.ItemDeal`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (NewDealEvent ,self ).__init__ (EventTypes .NEW_DEAL ,chat )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class NewReviewEvent (BaseEvent ):
    'Event class: new review from a customer.\n\n    :param deal: Deal object with review.\n    :type deal: `PlayerokAPI.types.ItemDeal`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (NewReviewEvent ,self ).__init__ (EventTypes .NEW_REVIEW ,chat )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class DealConfirmedEvent (BaseEvent ):
    'Event class: Buyer confirmed the deal.\n\n    :param deal: The deal object.\n    :type deal: `PlayerokAPI.types.ItemDeal`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealConfirmedEvent ,self ).__init__ (EventTypes .DEAL_CONFIRMED ,chat )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class DealRolledBackEvent (BaseEvent ):
    'Event class: the seller has returned funds for the transaction.\n\n    :param deal: The deal object.\n    :type deal: `PlayerokAPI.types.ItemDeal`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealRolledBackEvent ,self ).__init__ (EventTypes .DEAL_ROLLED_BACK ,chat )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class DealHasProblemEvent (BaseEvent ):
    'Event class: Someone reported a problem with the transaction.\n\n    :param deal: The deal object.\n    :type deal: `PlayerokAPI.types.ItemDeal`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealHasProblemEvent ,self ).__init__ (EventTypes .DEAL_HAS_PROBLEM ,chat )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class DealProblemResolvedEvent (BaseEvent ):
    'Event class: transaction problem resolved.\n\n    :param deal: The deal object.\n    :type deal: `PlayerokAPI.types.ItemDeal`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealProblemResolvedEvent ,self ).__init__ (
        EventTypes .DEAL_PROBLEM_RESOLVED ,chat 
        )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class DealStatusChangedEvent (BaseEvent ):
    'Event class: Status of the deal changed.\n\n    :param deal: The deal object.\n    :type deal: `PlayerokAPI.types.ItemDeal`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (DealStatusChangedEvent ,self ).__init__ (
        EventTypes .DEAL_STATUS_CHANGED ,chat 
        )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class ItemPaidEvent (BaseEvent ):
    'Event class: Item paid.\n\n    :param deal: The deal object.\n    :type deal: `PlayerokAPI.types.Item`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (ItemPaidEvent ,self ).__init__ (EventTypes .ITEM_PAID ,chat )
        self .deal :types .ItemDeal =deal 
        'deal object.'


class ItemSentEvent (BaseEvent ):
    'Event class: Item sent to buyer.\n\n    :param deal: The deal object.\n    :type deal: `PlayerokAPI.types.Item`\n\n    :param chat: The chat object in which the event occurred.\n    :type chat: `PlayerokAPI.types.Chat`'

    def __init__ (self ,deal :types .ItemDeal ,chat :types .Chat ):
        super (ItemSentEvent ,self ).__init__ (EventTypes .ITEM_SENT ,chat )
        self .deal :types .ItemDeal =deal 
        'Transaction object.'