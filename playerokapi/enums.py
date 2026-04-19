from enum import Enum 


class EventTypes (Enum ):
    "Types of Events."

    CHAT_INITIALIZED =0 
    "Chat initialized."
    NEW_MESSAGE =1 
    "New message in chat."
    NEW_DEAL =2 
    "A new deal has been created (when the buyer paid for the product)."
    NEW_REVIEW =3 
    "New customer review."
    DEAL_CONFIRMED =4 
    "The deal is confirmed (the buyer confirmed receipt of the item)."
    DEAL_CONFIRMED_AUTOMATICALLY =5 
    "The deal is confirmed automatically (if the buyer does not exit for a long time)."
    DEAL_ROLLED_BACK =6 
    "The seller has processed the return."
    DEAL_HAS_PROBLEM =7 
    "User reported an issue with the deal."
    DEAL_PROBLEM_RESOLVED =8 
    "The problem in the deal is solved."
    DEAL_STATUS_CHANGED =9 
    "The deal status has been changed."
    ITEM_PAID =10 
    "The user paid for the item."
    ITEM_SENT =11 
    "The item has been sent (the seller confirmed the transaction)."


class ItemLogEvents (Enum ):
    "Events of the item's logs."

    PAID =0 
    "The seller confirmed the transaction."
    SENT =1 
    "Transaction item has been sent."
    DEAL_CONFIRMED =2 
    "The deal is confirmed."
    DEAL_ROLLED_BACK =3 
    "The deal is returned."
    PROBLEM_REPORTED =4 
    "A complaint has been filed (a problem has been created)."
    PROBLEM_RESOLVED =5 
    "The problem is solved."


class TransactionOperations (Enum ):
    "Operations Transactions."

    DEPOSIT =0 
    "Replenishment."
    BUY =1 
    "Payment of goods."
    SELL =2 
    "Sale of goods."
    ITEM_DEFAULT_PRIORITY =3 
    "Payment for free priority."
    ITEM_PREMIUM_PRIORITY =4 
    "Payment of premium priority."
    WITHDRAW =5 
    "Payment."
    MANUAL_BALANCE_INCREASE =6 
    "Posting to account balance."
    MANUAL_BALANCE_DECREASE =7 
    "Cancellation of account balance."
    REFERRAL_BONUS =8 
    "Invitation to a friend (referral)."
    STEAM_DEPOSIT =9 
    "Payment of Steam refill."


class TransactionDirections (Enum ):
    "Operations transactions."

    IN =0 
    "Assessment."
    OUT =1 
    "Cancellation."


class TransactionStatuses (Enum ):
    "Transaction statuses."

    PENDING =0 
    "In anticipation (transaction is paid for, but money has not yet been credited to the account)."
    PROCESSING =1 
    "In frost."
    CONFIRMED =2 
    "Transaction deal is confirmed."
    ROLLED_BACK =3 
    "Return of transaction deal."
    FAILED =4 
    "Transaction error."


class TransactionPaymentMethodIds (Enum ):
    "Methods of Transaction Identification."

    MIR =0 
    "With the help of bank cards MIR."
    VISA_MASTERCARD =1 
    "With the help of bank cards VISA/Mastercard."
    ERIP =2 
    "Using ERP."


class TransactionProviderDirections (Enum ):
    "Transaction provider directions."

    IN =0 
    "Replenishment."
    OUT =1 
    "Output."


class TransactionProviderIds (Enum ):
    "ID providers of transaction."

    LOCAL =0 
    "With the help of account balance."
    SBP =1 
    "With the help of SBP."
    BANK_CARD_RU =2 
    "With the help of Russia's bank card."
    BANK_CARD_BY =3 
    "With the help of Belarusian bank card."
    BANK_CARD =4 
    "With foreign bank card."
    YMONEY =5 
    "Using Yandex Money."
    USDT =6 
    "Cryptocurrency USDT (TRC20)."
    PENDING_INCOME =7 
    "Replenishment from frozen funds."


class BankCardTypes (Enum ):
    "Types of Bank Cards."

    MIR =0 
    "Banking card MIR."
    VISA =1 
    "Banking card Visa."
    MASTERCARD =2 
    "Banking card Mastercard."


class ItemDealStatuses (Enum ):
    "Deal Status."

    PAID =0 
    "Deal paid."
    PENDING =1 
    "Deal awaiting shipment of goods."
    SENT =2 
    "The seller confirmed the deal completion."
    CONFIRMED =3 
    "The deal is confirmed."
    CONFIRMED_AUTOMATICALLY =4 
    "Deal confirmed automatically."
    ROLLED_BACK =5 
    "The deal is returned."


class ItemDealDirections (Enum ):
    "Directions of the deal."

    IN =0 
    "Purchase."
    OUT =1 
    "Sale."


class GameTypes (Enum ):
    "Types of games."

    GAME =0 
    "Game."
    APPLICATION =1 
    "Application."


class UserTypes (Enum ):
    "Types of Users."

    USER =0 
    "Average user."
    MODERATOR =1 
    "Moderator."
    BOT =2 
    "Bot."


class ChatTypes (Enum ):
    "Types of chats."

    PM =0 
    "Private chat (dialog with the user)."
    NOTIFICATIONS =1 
    "Notifications chat."
    SUPPORT =2 
    "Support Chat."


class ChatStatuses (Enum ):
    "Chat statuses."

    NEW =0 
    "New chat (there is not a single read message in it)."
    FINISHED =1 
    "Chat is available, in it you can now write."


class ChatMessageButtonTypes (Enum ):
    "Types of message buttons."

    # TODO: Finish all types of message buttons
    REDIRECT =0 
    "Redirects to the link."
    LOTTERY =1 
    "Redirects to a raffle/action."


class ItemStatuses (Enum ):
    "Item statuses."

    PENDING_APPROVAL =0 
    "Awaits adoption (under moderation check)."
    PENDING_MODERATION =1 
    "Awaits verification of changes by moderation."
    APPROVED =2 
    "Active (moderated)."
    DECLINED =3 
    "Rejected."
    BLOCKED =4 
    "Locked."
    EXPIRED =5 
    "Expiring."
    SOLD =6 
    "Sold."
    DRAFT =7 
    "Draft (if the item is not put up for sale)."


class ReviewStatuses (Enum ):
    "Review statuses."

    APPROVED =0 
    "Active."
    DELETED =1 
    "Remote."


class SortDirections (Enum ):
    "Types of sorting."

    DESC =0 
    "By decreasing."
    ASC =1 
    "In ascending order."


class PriorityTypes (Enum ):
    "Types of Priorities."

    DEFAULT =0 
    "Standard priority."
    PREMIUM =1 
    "Premium priority."


class GameCategoryAgreementIconTypes (Enum ):
    "Types of icons of agreement for a customer in a specific category."

    To Do: Finish all types of icon agreements.
    RESTRICTION =0 
    "Limitation."
    CONFIRMATION =0 
    "Confirmation."


class GameCategoryOptionTypes (Enum ):
    "Types of category options."

    # TODO: Finish all types of options for category
    SELECTOR =0 
    "Choice type."
    SWITCH =1 
    "Switcher."


class GameCategoryDataFieldTypes (Enum ):
    "Types of fields with data category game."

    ITEM_DATA =0 
    "Data subjects."
    OBTAINING_DATA =1 
    "Received data (after purchasing the item)."


class GameCategoryDataFieldInputTypes (Enum ):
    "Types of input fields with data categories for a game."

    To Do: Finish all types of input date fields
    INPUT =0 
    "Entered value (entered by the customer when ordering an item)."


class GameCategoryAutoConfirmPeriods (Enum ):
    "Periods of automatic deal confirmation in the game category."

    # TODO: Complete all auto-authentication periods
    SEVEN_DEYS =0 
    "Seven days."


class GameCategoryInstructionTypes (Enum ):
    "Types of instructions in category."

    FOR_SELLER =0 
    "For the seller."
    FOR_BUYER =1 
    "For the buyer."
