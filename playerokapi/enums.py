from enum import Enum


class EventTypes(Enum):
    """Event types."""

    CHAT_INITIALIZED = 0
    """Chat initialized."""
    NEW_MESSAGE = 1
    """New message in chat."""
    NEW_DEAL = 2
    """New deal (buyer paid for the item)."""
    NEW_REVIEW = 3
    """New review from the buyer."""
    DEAL_CONFIRMED = 4
    """Deal confirmed (buyer confirmed receipt)."""
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    """Deal auto-confirmed (buyer did not respond in time)."""
    DEAL_ROLLED_BACK = 6
    """Seller refunded the deal."""
    DEAL_HAS_PROBLEM = 7
    """User reported a problem with the deal."""
    DEAL_PROBLEM_RESOLVED = 8
    """Problem with the deal resolved."""
    DEAL_STATUS_CHANGED = 9
    """Deal status changed."""
    ITEM_PAID = 10
    """User paid for the item."""
    ITEM_SENT = 11
    """Item sent (seller confirmed completion)."""


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
    """Complaint filed (problem created)."""
    PROBLEM_RESOLVED = 5
    """Problem resolved."""


class TransactionOperations(Enum):
    """Transaction operations."""

    DEPOSIT = 0
    """Top-up."""
    BUY = 1
    """Purchase payment."""
    SELL = 2
    """Sale."""
    ITEM_DEFAULT_PRIORITY = 3
    """Free priority fee."""
    ITEM_PREMIUM_PRIORITY = 4
    """Premium priority fee."""
    WITHDRAW = 5
    """Withdrawal."""
    MANUAL_BALANCE_INCREASE = 6
    """Manual balance credit."""
    MANUAL_BALANCE_DECREASE = 7
    """Manual balance debit."""
    REFERRAL_BONUS = 8
    """Referral bonus."""
    STEAM_DEPOSIT = 9
    """Steam top-up payment."""


class TransactionDirections(Enum):
    """Transaction direction."""

    IN = 0
    """Incoming."""
    OUT = 1
    """Outgoing."""


class TransactionStatuses(Enum):
    """Transaction statuses."""

    PENDING = 0
    """Pending (paid but not yet credited)."""
    PROCESSING = 1
    """On hold."""
    CONFIRMED = 2
    """Confirmed."""
    ROLLED_BACK = 3
    """Refunded."""
    FAILED = 4
    """Failed."""


class TransactionPaymentMethodIds(Enum):
    """Transaction payment method IDs."""

    MIR = 0
    """MIR cards."""
    VISA_MASTERCARD = 1
    """VISA/Mastercard."""
    ERIP = 2
    """ERIP."""


class TransactionProviderDirections(Enum):
    """Transaction provider direction."""

    IN = 0
    """Deposit."""
    OUT = 1
    """Withdrawal."""


class TransactionProviderIds(Enum):
    """Transaction provider IDs."""

    LOCAL = 0
    """Account balance."""
    SBP = 1
    """SBP (Fast Payments)."""
    BANK_CARD_RU = 2
    """Russian bank card."""
    BANK_CARD_BY = 3
    """Belarus bank card."""
    BANK_CARD = 4
    """Foreign bank card."""
    YMONEY = 5
    """YooMoney."""
    USDT = 6
    """USDT (TRC20)."""
    PENDING_INCOME = 7
    """Credit from frozen funds."""


class BankCardTypes(Enum):
    """Bank card types."""

    MIR = 0
    """MIR."""
    VISA = 1
    """VISA."""
    MASTERCARD = 2
    """Mastercard."""


class ItemDealStatuses(Enum):
    """Item deal status."""

    PAID = 0
    """Paid."""
    PENDING = 1
    """Awaiting delivery."""
    SENT = 2
    """Seller confirmed completion."""
    CONFIRMED = 3
    """Confirmed."""
    CONFIRMED_AUTOMATICALLY = 4
    """Auto-confirmed."""
    ROLLED_BACK = 5
    """Refunded."""


class ItemDealDirections(Enum):
    """Deal direction."""

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
    """Private chat."""
    NOTIFICATIONS = 1
    """Notifications chat."""
    SUPPORT = 2
    """Support chat."""


class ChatStatuses(Enum):
    """Chat statuses."""

    NEW = 0
    """New (no read messages)."""
    FINISHED = 1
    """Active chat."""


class ChatMessageButtonTypes(Enum):
    """Chat message button types."""

    # TODO: Доделать все типы кнопок сообщения
    REDIRECT = 0
    """Opens a link."""
    LOTTERY = 1
    """Opens a promo/lottery."""


class ItemStatuses(Enum):
    """Item statuses."""

    PENDING_APPROVAL = 0
    """Pending moderation."""
    PENDING_MODERATION = 1
    """Edit pending moderation."""
    APPROVED = 2
    """Active (approved)."""
    DECLINED = 3
    """Declined."""
    BLOCKED = 4
    """Blocked."""
    EXPIRED = 5
    """Expired."""
    SOLD = 6
    """Sold."""
    DRAFT = 7
    """Draft (not listed)."""


class ReviewStatuses(Enum):
    """Review statuses."""

    APPROVED = 0
    """Active."""
    DELETED = 1
    """Deleted."""


class SortDirections(Enum):
    """Sort direction."""

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
    """Buyer agreement icon types in a category."""

    # TODO: Доделать все типы иконок соглашений
    RESTRICTION = 0
    """Restriction."""
    CONFIRMATION = 0
    """Confirmation."""


class GameCategoryOptionTypes(Enum):
    """Category option types."""

    # TODO: Доделать все типы опций категории
    SELECTOR = 0
    """Selector."""
    SWITCH = 1
    """Toggle."""


class GameCategoryDataFieldTypes(Enum):
    """Game category data field types."""

    ITEM_DATA = 0
    """Item data."""
    OBTAINING_DATA = 1
    """Data received after purchase."""


class GameCategoryDataFieldInputTypes(Enum):
    """Game category data field input types."""

    # TODO: Доделать все типы вводимых дата-полей
    INPUT = 0
    """Value entered by buyer at checkout."""


class GameCategoryAutoConfirmPeriods(Enum):
    """Auto-confirm periods for a game category."""

    # TODO: Доделать все периоды авто-подтверждения
    SEVEN_DEYS = 0
    """Seven days."""


class GameCategoryInstructionTypes(Enum):
    """Category instruction types."""

    FOR_SELLER = 0
    """For seller."""
    FOR_BUYER = 1
    """For buyer."""
