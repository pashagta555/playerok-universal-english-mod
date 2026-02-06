from enum import Enum


class EventTypes(Enum):
    """Types of events."""

    CHAT_INITIALIZED = 0
    """Chat initialized."""
    NEW_MESSAGE = 1
    """New message in the chat."""
    NEW_DEAL = 2
    """New deal created (when the buyer has paid for the item)."""
    NEW_REVIEW = 3
    """New review from the buyer."""
    DEAL_CONFIRMED = 4
    """Deal confirmed (the buyer confirmed receiving the item)."""
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    """Deal confirmed automatically (if the buyer does not respond for a long time)."""
    DEAL_ROLLED_BACK = 6
    """Seller has refunded the deal."""
    DEAL_HAS_PROBLEM = 7
    """User reported a problem with the deal."""
    DEAL_PROBLEM_RESOLVED = 8
    """Problem with the deal has been resolved."""
    DEAL_STATUS_CHANGED = 9
    """Deal status changed."""
    ITEM_PAID = 10
    """User paid for the item."""
    ITEM_SENT = 11
    """Item sent (the seller confirmed fulfillment of the deal)."""


class ItemLogEvents(Enum):
    """Item log events."""

    PAID = 0
    """Seller confirmed completion of the deal."""
    SENT = 1
    """Deal item has been sent."""
    DEAL_CONFIRMED = 2
    """Deal confirmed."""
    DEAL_ROLLED_BACK = 3
    """Deal refunded."""
    PROBLEM_REPORTED = 4
    """Complaint sent (problem created)."""
    PROBLEM_RESOLVED = 5
    """Problem resolved."""


class TransactionOperations(Enum):
    """Transaction operations."""

    DEPOSIT = 0
    """Deposit."""
    BUY = 1
    """Item purchase."""
    SELL = 2
    """Item sale."""
    ITEM_DEFAULT_PRIORITY = 3
    """Payment for free priority."""
    ITEM_PREMIUM_PRIORITY = 4
    """Payment for premium priority."""
    WITHDRAW = 5
    """Payout."""
    MANUAL_BALANCE_INCREASE = 6
    """Manual account balance increase."""
    MANUAL_BALANCE_DECREASE = 7
    """Manual account balance decrease."""
    REFERRAL_BONUS = 8
    """Referral bonus."""
    STEAM_DEPOSIT = 9
    """Payment for Steam top-up."""


class TransactionDirections(Enum):
    """Directions of transactions."""

    IN = 0
    """Incoming."""
    OUT = 1
    """Outgoing."""


class TransactionStatuses(Enum):
    """Transaction statuses."""

    PENDING = 0
    """Pending (transaction is paid, but funds have not yet been credited)."""
    PROCESSING = 1
    """Frozen."""
    CONFIRMED = 2
    """Transaction deal confirmed."""
    ROLLED_BACK = 3
    """Refund for the transaction deal."""
    FAILED = 4
    """Transaction error."""


class TransactionPaymentMethodIds(Enum):
    """IDs of transaction payment methods."""

    MIR = 0
    """Using MIR bank cards."""
    VISA_MASTERCARD = 1
    """Using VISA/Mastercard bank cards."""
    ERIP = 2
    """Using ERIP."""


class TransactionProviderDirections(Enum):
    """Directions of transaction providers."""

    IN = 0
    """Deposit."""
    OUT = 1
    """Withdrawal."""


class TransactionProviderIds(Enum):
    """IDs of transaction providers."""

    LOCAL = 0
    """Using the account balance."""
    SBP = 1
    """Using SBP."""
    BANK_CARD_RU = 2
    """Using a Russian bank card."""
    BANK_CARD_BY = 3
    """Using a Belarusian bank card."""
    BANK_CARD = 4
    """Using a foreign bank card."""
    YMONEY = 5
    """Using YooMoney."""
    USDT = 6
    """USDT cryptocurrency (TRC20)."""
    PENDING_INCOME = 7
    """Deposit from frozen funds."""


class BankCardTypes(Enum):
    """Types of bank cards."""

    MIR = 0
    """MIR bank card."""
    VISA = 1
    """VISA bank card."""
    MASTERCARD = 2
    """Mastercard bank card."""


class ItemDealStatuses(Enum):
    """Deal statuses."""

    PAID = 0
    """Deal is paid."""
    PENDING = 1
    """Deal is waiting for the item to be sent."""
    SENT = 2
    """Seller confirmed completion of the deal."""
    CONFIRMED = 3
    """Deal confirmed."""
    CONFIRMED_AUTOMATICALLY = 4
    """Deal confirmed automatically."""
    ROLLED_BACK = 5
    """Deal refunded."""


class ItemDealDirections(Enum):
    """Deal directions."""

    IN = 0
    """Purchase."""
    OUT = 1
    """Sale."""


class GameTypes(Enum):
    """Types of games."""

    GAME = 0
    """Game."""
    APPLICATION = 1
    """Application."""


class UserTypes(Enum):
    """Types of users."""

    USER = 0
    """Regular user."""
    MODERATOR = 1
    """Moderator."""
    BOT = 2
    """Bot."""


class ChatTypes(Enum):
    """Types of chats."""

    PM = 0
    """Private chat (dialog with a user)."""
    NOTIFICATIONS = 1
    """Notifications chat."""
    SUPPORT = 2
    """Support chat."""


class ChatStatuses(Enum):
    """Chat statuses."""

    NEW = 0
    """New chat (no messages have been read yet)."""
    FINISHED = 1
    """Chat is available and can be used for messaging."""


class ChatMessageButtonTypes(Enum):
    """Types of message buttons."""

    # TODO: Add all message button types
    REDIRECT = 0
    """Redirects to a link."""
    LOTTERY = 1
    """Redirects to a giveaway/promotion."""


class ItemStatuses(Enum):
    """Item statuses."""

    PENDING_APPROVAL = 0
    """Awaiting approval (under moderation review)."""
    PENDING_MODERATION = 1
    """Waiting for changes to be checked by moderation."""
    APPROVED = 2
    """Active (approved by moderation)."""
    DECLINED = 3
    """Declined."""
    BLOCKED = 4
    """Blocked."""
    EXPIRED = 5
    """Expired."""
    SOLD = 6
    """Sold."""
    DRAFT = 7
    """Draft (item is not listed for sale)."""


class ReviewStatuses(Enum):
    """Review statuses."""

    APPROVED = 0
    """Active."""
    DELETED = 1
    """Deleted."""


class SortDirections(Enum):
    """Sort directions."""

    DESC = 0
    """Descending."""
    ASC = 1
    """Ascending."""


class PriorityTypes(Enum):
    """Types of priorities."""

    DEFAULT = 0
    """Standard priority."""
    PREMIUM = 1
    """Premium priority."""


class GameCategoryAgreementIconTypes(Enum):
    """Types of buyer agreement icons for a specific category."""

    # TODO: Add all agreement icon types
    RESTRICTION = 0
    """Restriction."""
    CONFIRMATION = 0
    """Confirmation."""


class GameCategoryOptionTypes(Enum):
    """Types of category options."""

    # TODO: Add all category option types
    SELECTOR = 0
    """Type selector."""
    SWITCH = 1
    """Toggle switch."""


class GameCategoryDataFieldTypes(Enum):
    """Types of data fields for a game category."""

    ITEM_DATA = 0
    """Item data."""
    OBTAINING_DATA = 1
    """Obtained data (after purchasing the item)."""


class GameCategoryDataFieldInputTypes(Enum):
    """Types of input data fields for a game category."""

    # TODO: Add all types of input data fields
    INPUT = 0
    """Input value (entered by the buyer when placing an order)."""


class GameCategoryAutoConfirmPeriods(Enum):
    """Auto-confirmation periods for deals in a game category."""

    # TODO: Add all auto-confirmation periods
    SEVEN_DEYS = 0
    """Seven days."""


class GameCategoryInstructionTypes(Enum):
    """Types of category instructions."""

    FOR_SELLER = 0
    """For the seller."""
    FOR_BUYER = 1
    """For the buyer."""
