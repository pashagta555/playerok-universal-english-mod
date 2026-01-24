from enum import Enum


class EventTypes(Enum):
    """Event types."""

    CHAT_INITIALIZED = 0
    """Chat initialized."""
    NEW_MESSAGE = 1
    """New message in chat."""
    NEW_DEAL = 2
    """New deal created (when buyer paid for the item)."""
    NEW_REVIEW = 3
    """New review from buyer."""
    DEAL_CONFIRMED = 4
    """Deal confirmed (buyer confirmed receipt of item)."""
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    """Deal confirmed automatically (if buyer doesn't respond for a long time)."""
    DEAL_ROLLED_BACK = 6
    """Seller issued a refund for the deal."""
    DEAL_HAS_PROBLEM = 7
    """User reported a problem in the deal."""
    DEAL_PROBLEM_RESOLVED = 8
    """Problem in deal resolved."""
    DEAL_STATUS_CHANGED = 9
    """Deal status changed."""
    ITEM_PAID = 10
    """User paid for item."""
    ITEM_SENT = 11
    """Item sent (seller confirmed deal completion)."""


class ItemLogEvents(Enum):
    """Item log events."""

    PAID = 0
    """Seller confirmed deal completion."""
    SENT = 1
    """Deal item sent."""
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
    """Item payment."""
    SELL = 2
    """Item sale."""
    ITEM_DEFAULT_PRIORITY = 3
    """Free priority payment."""
    ITEM_PREMIUM_PRIORITY = 4
    """Premium priority payment."""
    WITHDRAW = 5
    """Withdrawal."""
    MANUAL_BALANCE_INCREASE = 6
    """Manual balance increase."""
    MANUAL_BALANCE_DECREASE = 7
    """Manual balance decrease."""
    REFERRAL_BONUS = 8
    """Referral bonus (friend invitation)."""
    STEAM_DEPOSIT = 9
    """Steam deposit payment."""


class TransactionDirections(Enum):
    """Transaction operations."""

    IN = 0
    """Credit."""
    OUT = 1
    """Debit."""


class TransactionStatuses(Enum):
    """Transaction statuses."""

    PENDING = 0
    """Pending (transaction paid, but funds haven't been credited to balance yet)."""
    PROCESSING = 1
    """Frozen."""
    CONFIRMED = 2
    """Transaction deal confirmed."""
    ROLLED_BACK = 3
    """Transaction deal refund."""
    FAILED = 4
    """Transaction error."""


class TransactionPaymentMethodIds(Enum):
    """Transaction method IDs."""

    MIR = 0
    """Using MIR bank cards."""
    VISA_MASTERCARD = 1
    """Using VISA/Mastercard bank cards."""
    ERIP = 2
    """Using ERIP."""


class TransactionProviderDirections(Enum):
    """Transaction provider directions."""

    IN = 0
    """Deposit."""
    OUT = 1
    """Withdrawal."""


class TransactionProviderIds(Enum):
    """Transaction provider IDs."""

    LOCAL = 0
    """Using account balance."""
    SBP = 1
    """Using SBP."""
    BANK_CARD_RU = 2
    """Using Russian bank card."""
    BANK_CARD_BY = 3
    """Using Belarusian bank card."""
    BANK_CARD = 4
    """Using foreign bank card."""
    YMONEY = 5
    """Using YooMoney."""
    USDT = 6
    """USDT cryptocurrency (TRC20)."""
    PENDING_INCOME = 7
    """Deposit from frozen funds."""


class BankCardTypes(Enum):
    """Bank card types."""

    MIR = 0
    """MIR bank card."""
    VISA = 1
    """VISA bank card."""
    MASTERCARD = 2
    """Mastercard bank card."""


class ItemDealStatuses(Enum):
    """Deal statuses."""

    PAID = 0
    """Deal paid."""
    PENDING = 1
    """Deal pending item shipment."""
    SENT = 2
    """Seller confirmed deal completion."""
    CONFIRMED = 3
    """Deal confirmed."""
    ROLLED_BACK = 4
    """Deal refunded."""


class ItemDealDirections(Enum):
    """Deal directions."""

    IN = 0
    """Purchase."""
    OUT = 1
    """Sale."""


class GameTypes(Enum):
    """Game types."""

    GAME = 0
    """Game."""
    APPLICATION = 1
    """Application."""


class UserTypes(Enum):
    """User types."""

    USER = 0
    """Regular user."""
    MODERATOR = 1
    """Moderator."""
    BOT = 2
    """Bot."""


class ChatTypes(Enum):
    """Chat types."""

    PM = 0
    """Private chat (dialog with user)."""
    NOTIFICATIONS = 1
    """Notifications chat."""
    SUPPORT = 2
    """Support chat."""


class ChatStatuses(Enum):
    """Chat statuses."""

    NEW = 0
    """New chat (no read messages in it)."""
    FINISHED = 1
    """Chat available, can message now."""


class ChatMessageButtonTypes(Enum):
    """Message button types."""

    # TODO: Complete all message button types
    REDIRECT = 0
    """Redirects to link."""
    LOTTERY = 1
    """Redirects to lottery/promotion."""


class ItemStatuses(Enum):
    """Item statuses."""

    PENDING_APPROVAL = 0
    """Pending approval (under moderation review)."""
    PENDING_MODERATION = 1
    """Pending moderation review of changes."""
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
    """Draft (if item is not listed for sale)."""


class ReviewStatuses(Enum):
    """Review statuses."""

    APPROVED = 0
    """Active."""
    DELETED = 1
    """Deleted."""


class SortDirections(Enum):
    """Sort types."""

    DESC = 0
    """Descending."""
    ASC = 1
    """Ascending."""


class PriorityTypes(Enum):
    """Priority types."""

    DEFAULT = 0
    """Standard priority."""
    PREMIUM = 1
    """Premium priority."""


class GameCategoryAgreementIconTypes(Enum):
    """Buyer agreement icon types in a specific category."""

    # TODO: Complete all agreement icon types
    RESTRICTION = 0
    """Restriction."""
    CONFIRMATION = 0
    """Confirmation."""


class GameCategoryOptionTypes(Enum):
    """Category option types."""

    # TODO: Complete all category option types
    SELECTOR = 0
    """Type selection."""
    SWITCH = 1
    """Switch."""


class GameCategoryDataFieldTypes(Enum):
    """Game category data field types."""

    ITEM_DATA = 0
    """Item data."""
    OBTAINING_DATA = 1
    """Obtaining data (after purchasing item)."""


class GameCategoryDataFieldInputTypes(Enum):
    """Game category data field input types."""

    # TODO: Complete all data field input types
    INPUT = 0
    """Input value (entered by buyer when ordering item)."""


class GameCategoryAutoConfirmPeriods(Enum):
    """Auto-confirm deal periods in game category."""

    # TODO: Complete all auto-confirm periods
    SEVEN_DEYS = 0
    """Seven days."""


class GameCategoryInstructionTypes(Enum):
    """Category instruction types."""

    FOR_SELLER = 0
    """For seller."""
    FOR_BUYER = 1
    """For buyer."""
