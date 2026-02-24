from enum import Enum


class EventTypes(Enum):
    """Event types."""

    CHAT_INITIALIZED = 0
    """Chat initialized."""
    NEW_MESSAGE = 1
    """New message in chat."""
    NEW_DEAL = 2
    """New deal created (buyer paid for item)."""
    NEW_REVIEW = 3
    """New review from buyer."""
    DEAL_CONFIRMED = 4
    """Deal confirmed (buyer confirmed item receipt)."""
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    """Deal confirmed automatically (if buyer is unresponsive)."""
    DEAL_ROLLED_BACK = 6
    """Seller issued a refund."""
    DEAL_HAS_PROBLEM = 7
    """User reported a problem with the deal."""
    DEAL_PROBLEM_RESOLVED = 8
    """Deal problem resolved."""
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
    """Referral bonus."""
    STEAM_DEPOSIT = 9
    """Steam deposit payment."""


class TransactionDirections(Enum):
    """Transaction directions."""

    IN = 0
    """Credit."""
    OUT = 1
    """Debit."""


class TransactionStatuses(Enum):
    """Transaction statuses."""

    PENDING = 0
    """Pending (transaction paid but funds not yet on balance)."""
    PROCESSING = 1
    """On hold."""
    CONFIRMED = 2
    """Transaction deal confirmed."""
    ROLLED_BACK = 3
    """Transaction deal refunded."""
    FAILED = 4
    """Transaction failed."""


class TransactionPaymentMethodIds(Enum):
    """Transaction method IDs."""

    MIR = 0
    """MIR bank cards."""
    VISA_MASTERCARD = 1
    """VISA/Mastercard bank cards."""
    ERIP = 2
    """ERIP."""


class TransactionProviderDirections(Enum):
    """Transaction provider directions."""

    IN = 0
    """Deposit."""
    OUT = 1
    """Withdrawal."""


class TransactionProviderIds(Enum):
    """Transaction provider IDs."""

    LOCAL = 0
    """Account balance."""
    SBP = 1
    """SBP."""
    BANK_CARD_RU = 2
    """Russian bank card."""
    BANK_CARD_BY = 3
    """Belarus bank card."""
    BANK_CARD = 4
    """Foreign bank card."""
    YMONEY = 5
    """YooMoney."""
    USDT = 6
    """USDT (TRC20) cryptocurrency."""
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
    """Seller confirmed completion."""
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
    """Private chat (direct with user)."""
    NOTIFICATIONS = 1
    """Notifications chat."""
    SUPPORT = 2
    """Support chat."""


class ChatStatuses(Enum):
    """Chat statuses."""

    NEW = 0
    """New chat (no messages read yet)."""
    FINISHED = 1
    """Chat available, messaging allowed."""


class ChatMessageButtonTypes(Enum):
    """Message button types."""

    # TODO: Add all message button types
    REDIRECT = 0
    """Redirects to a link."""
    LOTTERY = 1
    """Redirects to lottery/promotion."""


class ItemStatuses(Enum):
    """Item statuses."""

    PENDING_APPROVAL = 0
    """Pending approval (under moderation)."""
    PENDING_MODERATION = 1
    """Pending moderation review."""
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
    """Draft (item not listed for sale)."""


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
    """Priority types."""

    DEFAULT = 0
    """Default priority."""
    PREMIUM = 1
    """Premium priority."""


class GameCategoryAgreementIconTypes(Enum):
    """Buyer agreement icon types for a category."""

    # TODO: Add all agreement icon types
    RESTRICTION = 0
    """Restriction."""
    CONFIRMATION = 0
    """Confirmation."""


class GameCategoryOptionTypes(Enum):
    """Category option types."""

    # TODO: Add all category option types
    SELECTOR = 0
    """Type selector."""
    SWITCH = 1
    """Switch."""


class GameCategoryDataFieldTypes(Enum):
    """Game category data field types."""

    ITEM_DATA = 0
    """Item data."""
    OBTAINING_DATA = 1
    """Obtaining data (after item purchase)."""


class GameCategoryDataFieldInputTypes(Enum):
    """Game category data field input types."""

    # TODO: Add all data field input types
    INPUT = 0
    """Input value (entered by buyer when ordering item)."""


class GameCategoryAutoConfirmPeriods(Enum):
    """Auto-confirm periods for game category deals."""

    # TODO: Add all auto-confirm periods
    SEVEN_DEYS = 0
    """Seven days."""


class GameCategoryInstructionTypes(Enum):
    """Category instruction types."""

    FOR_SELLER = 0
    """For seller."""
    FOR_BUYER = 1
    """For buyer."""
