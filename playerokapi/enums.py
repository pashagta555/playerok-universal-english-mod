from enum import Enum


class EventTypes(Enum):
    """Event types."""

    CHAT_INITIALIZED = 0
    """Chat has been initialized."""
    NEW_MESSAGE = 1
    """New message in chat."""
    NEW_DEAL = 2
    """A new transaction was created (when the buyer paid for the goods)."""
    NEW_REVIEW = 3
    """New review from buyer."""
    DEAL_CONFIRMED = 4
    """Transaction confirmed (buyer confirms receipt of item)."""
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    """The transaction is confirmed automatically (if the buyer does not contact for a long time)."""
    DEAL_ROLLED_BACK = 6
    """The seller has issued a refund."""
    DEAL_HAS_PROBLEM = 7
    """The user reported a problem with the transaction."""
    DEAL_PROBLEM_RESOLVED = 8
    """The problem in the transaction has been resolved."""
    DEAL_STATUS_CHANGED = 9
    """The transaction status has been changed."""
    ITEM_PAID = 10
    """The user paid for the item."""
    ITEM_SENT = 11
    """The item has been sent (the seller has confirmed the completion of the transaction)."""


class ItemLogEvents(Enum):
    """Item log events."""

    PAID = 0
    """The seller confirmed the completion of the transaction."""
    SENT = 1
    """The transaction item has been sent."""
    DEAL_CONFIRMED = 2
    """The transaction is confirmed."""
    DEAL_ROLLED_BACK = 3
    """The transaction has been returned."""
    PROBLEM_REPORTED = 4
    """A complaint has been sent (a problem has been created)."""
    PROBLEM_RESOLVED = 5
    """Problem solved."""


class TransactionOperations(Enum):
    """Transaction operations."""

    DEPOSIT = 0
    """Replenishment."""
    BUY = 1
    """Payment for goods."""
    SELL = 2
    """Selling goods."""
    ITEM_DEFAULT_PRIORITY = 3
    """Pay for free priority."""
    ITEM_PREMIUM_PRIORITY = 4
    """Premium priority payment."""
    WITHDRAW = 5
    """Pay."""
    MANUAL_BALANCE_INCREASE = 6
    """Credit to account balance."""
    MANUAL_BALANCE_DECREASE = 7
    """Debiting from your account balance."""
    REFERRAL_BONUS = 8
    """Invite a friend (referral)."""
    STEAM_DEPOSIT = 9
    """Payment for Steam replenishment."""


class TransactionDirections(Enum):
    """Transaction operations."""

    IN = 0
    """Accrual."""
    OUT = 1
    """Write-off."""


class TransactionStatuses(Enum):
    """Transaction statuses."""

    PENDING = 0
    """Pending (the transaction has been paid, but the money for it has not yet been credited to the balance)."""
    PROCESSING = 1
    """Frozen."""
    CONFIRMED = 2
    """The transaction transaction is confirmed."""
    ROLLED_BACK = 3
    """Return on transaction transaction."""
    FAILED = 4
    """Transaction error."""


class TransactionPaymentMethodIds(Enum):
    """ID of transaction methods."""

    MIR = 0
    """Using MIR bank cards."""
    VISA_MASTERCARD = 1
    """Using VISA/Mastercard bank cards."""
    ERIP = 2
    """With the help of ERIP."""


class TransactionProviderDirections(Enum):
    """Transaction provider directions."""

    IN = 0
    """Replenishment."""
    OUT = 1
    """Conclusion."""


class TransactionProviderIds(Enum):
    """ID of transaction providers."""

    LOCAL = 0
    """Using your account balance."""
    SBP = 1
    """Using SBP."""
    BANK_CARD_RU = 2
    """Using a Russian bank card."""
    BANK_CARD_BY = 3
    """Using a Belarusian bank card."""
    BANK_CARD = 4
    """Using a foreign bank card."""
    YMONEY = 5
    """With the help of YuMoney."""
    USDT = 6
    """Cryptocurrency USDT (TRC20)."""
    PENDING_INCOME = 7
    """Replenishment from frozen funds."""


class BankCardTypes(Enum):
    """Types of bank cards."""

    MIR = 0
    """Bank card MIR."""
    VISA = 1
    """VISA bank card."""
    MASTERCARD = 2
    """Mastercard bank card."""


class ItemDealStatuses(Enum):
    """Transaction status."""

    PAID = 0
    """The transaction has been paid."""
    PENDING = 1
    """Transaction pending shipment of goods."""
    SENT = 2
    """The seller confirmed the completion of the transaction."""
    CONFIRMED = 3
    """The transaction is confirmed."""
    CONFIRMED_AUTOMATICALLY = 4
    """The transaction was confirmed automatically."""
    ROLLED_BACK = 5
    """The transaction has been returned."""


class ItemDealDirections(Enum):
    """Transaction directions."""

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
    """User types."""

    USER = 0
    """Regular user."""
    MODERATOR = 1
    """Moderator."""
    BOT = 2
    """Bot."""


class ChatTypes(Enum):
    """Types of chats."""

    PM = 0
    """Private chat (dialogue with the user)."""
    NOTIFICATIONS = 1
    """Chat notifications."""
    SUPPORT = 2
    """Support chat."""


class ChatStatuses(Enum):
    """Chat statuses."""

    NEW = 0
    """New chat (there are no read messages in it)."""
    FINISHED = 1
    """The chat is available, you can chat in it now."""


class ChatMessageButtonTypes(Enum):
    """Types of message buttons."""

    # TODO: Доделать все типы кнопок сообщения
    REDIRECT = 0
    """Redirects to a link."""
    LOTTERY = 1
    """Redirects to a draw/promotion."""


class ItemStatuses(Enum):
    """Item statuses."""

    PENDING_APPROVAL = 0
    """Awaiting acceptance (under moderation)."""
    PENDING_MODERATION = 1
    """Waiting for changes to be reviewed by moderation."""
    APPROVED = 2
    """Active (accepted by moderation)."""
    DECLINED = 3
    """Rejected."""
    BLOCKED = 4
    """Locked."""
    EXPIRED = 5
    """Expired."""
    SOLD = 6
    """Sold."""
    DRAFT = 7
    """Draft (if the item is not for sale)."""


class ReviewStatuses(Enum):
    """Review statuses."""

    APPROVED = 0
    """Active."""
    DELETED = 1
    """Remote."""


class SortDirections(Enum):
    """Sorting types."""

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
    """Types of buyer agreement icons in a specific category."""

    # TODO: Доделать все типы иконок соглашений
    RESTRICTION = 0
    """Limitation."""
    CONFIRMATION = 0
    """Confirmation."""


class GameCategoryOptionTypes(Enum):
    """Category option types."""

    # TODO: Доделать все типы опций категории
    SELECTOR = 0
    """Select type."""
    SWITCH = 1
    """Switch."""


class GameCategoryDataFieldTypes(Enum):
    """Types of game category data fields."""

    ITEM_DATA = 0
    """Item data."""
    OBTAINING_DATA = 1
    """Received data (after purchasing an item)."""


class GameCategoryDataFieldInputTypes(Enum):
    """Types of input fields with game category data."""

    # TODO: Доделать все типы вводимых дата-полей
    INPUT = 0
    """Entered value (entered by the buyer when checking out the item)."""


class GameCategoryAutoConfirmPeriods(Enum):
    """Periods for automatic confirmation of transactions in the game category."""

    # TODO: Доделать все периоды авто-подтверждения
    SEVEN_DEYS = 0
    """Seven days."""


class GameCategoryInstructionTypes(Enum):
    """Types of category instructions."""

    FOR_SELLER = 0
    """For the seller."""
    FOR_BUYER = 1
    """For the buyer."""
