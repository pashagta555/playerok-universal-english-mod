Here is the translation of the text to English, keeping the code unchanged:

```
from enum import Enum


class EventTypes(Enum):
    """Event types."""

    CHAT_INITIALIZED = 0
    """Chat initialized."""
    NEW_MESSAGE = 1
    """New message in chat."""
    NEW_DEAL = 2
    """A new deal (when buyer pays for the item)."""
    NEW_REVIEW = 3
    """A new review from a buyer."""
    DEAL_CONFIRMED = 4
    """Deal confirmed (buyer confirms receipt of item)."""
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    """Deal confirmed automatically (if buyer is unresponsive for a long time)."""
    DEAL_ROLLED_BACK = 6
    """Seller rolls back the deal."""
    DEAL_HAS_PROBLEM = 7
    """User reports a problem with the deal."""
    DEAL_PROBLEM_RESOLVED = 8
    """Problem with the deal resolved."""
    DEAL_STATUS_CHANGED = 9
    """Deal status changed."""
    ITEM_PAID = 10
    """Buyer paid for item."""
    ITEM_SENT = 11
    """Item sent (seller confirms completion of deal)."""


class ItemLogEvents(Enum):
    """Item log events."""

    PAID = 0
    """Seller confirmed payment."""
    SENT = 1
    """Item was shipped."""
    DEAL_CONFIRMED = 2
    """Deal confirmed."""
    DEAL_ROLLED_BACK = 3
    """Deal rolled back."""
    PROBLEM_REPORTED = 4
    """Problem reported (created a problem)."""
    PROBLEM_RESOLVED = 5
    """Problem resolved."""


class TransactionOperations(Enum):
    """Transaction operations."""

    DEPOSIT = 0
    """Deposit."""
    BUY = 1
    """Buy."""
    SELL = 2
    """Sell."""
    ITEM_DEFAULT_PRIORITY = 3
    """Default priority for item."""
    ITEM_PREMIUM_PRIORITY = 4
    """Premium priority for item."""
    WITHDRAW = 5
    """Withdrawal."""
    MANUAL_BALANCE_INCREASE = 6
    """Manual balance increase."""
    MANUAL_BALANCE_DECREASE = 7
    """Manual balance decrease."""
    REFERRAL_BONUS = 8
    """Referral bonus."""
    STEAM_DEPOSIT = 9
    """Steam deposit."""


class TransactionDirections(Enum):
    """Transaction directions."""

    IN = 0
    """In (deposit)."""
    OUT = 1
    """Out (withdrawal)."""


class TransactionStatuses(Enum):
    """Transaction statuses."""

    PENDING = 0
    """Pending (transaction paid, but funds have not yet been added to balance)."""
    PROCESSING = 1
    """Processing."""
    CONFIRMED = 2
    """Confirmed."""
    ROLLED_BACK = 3
    """Rolled back (deal was cancelled or failed)."""
    FAILED = 4
    """Failed."""


class TransactionPaymentMethodIds(Enum):
    """Transaction payment method IDs."""

    MIR = 0
    """MIR payment method."""
    VISA_MASTERCARD = 1
    """Visa/Mastercard payment method."""
    ERIP = 2
    """ERIP payment method."""


class TransactionProviderDirections(Enum):
    """Transaction provider directions."""

    IN = 0
    """In (deposit)."""
    OUT = 1
    """Out (withdrawal)."""


class TransactionProviderIds(Enum):
    """Transaction provider IDs."""

    LOCAL = 0
    """Local provider."""
    SBP = 1
    """SBP provider."""
    BANK_CARD_RU = 2
    """Bank card Russia provider."""
    BANK_CARD_BY = 3
    """Bank card Belarus provider."""
    BANK_CARD = 4
    """International bank card provider."""
    YMONEY = 5
    """Yandex Money provider."""
    USDT = 6
    """USDT (TRC20) cryptocurrency."""
    PENDING_INCOME = 7
    """Pending income."""


class BankCardTypes(Enum):
    """Bank card types."""

    MIR = 0
    """MIR bank card."""
    VISA = 1
    """Visa bank card."""
    MASTERCARD = 2
    """Mastercard bank card."""


class ItemDealStatuses(Enum):
    """Item deal statuses."""

    PAID = 0
    """Paid (deal is confirmed)."""
    PENDING = 1
    """Pending (waiting for item to be sent)."""
    SENT = 2
    """Sent (seller confirms delivery)."""
    CONFIRMED = 3
    """Confirmed (buyer confirms receipt of item)."""
    CONFIRMED_AUTOMATICALLY = 4
    """Confirmed automatically."""
    ROLLED_BACK = 5
    """Rolled back (deal was cancelled or failed)."""


class ItemDealDirections(Enum):
    """Item deal directions."""

    IN = 0
    """In (purchase)."""
    OUT = 1
    """Out (sale)."""


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
    """New (no unread messages)."""
    FINISHED = 1
    """Finished (chat is available for writing)."""


class ChatMessageButtonTypes(Enum):
    """Chat message button types."""

    # TODO: Complete all chat message button types
    REDIRECT = 0
    """Redirects to link."""
    LOTTERY = 1
    """Redirects to lottery/offer."""


class ItemStatuses(Enum):
    """Item statuses."""

    PENDING_APPROVAL = 0
    """Pending approval (waiting for moderator review)."""
    PENDING_MODERATION = 1
    """Pending moderation (awaiting changes review)."""
    APPROVED = 2
    """Approved (item is active and available)."""
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
    """Approved."""
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
    """Game category agreement icon types."""

    # TODO: Complete all game category agreement icon types
    RESTRICTION = 0
    """Restriction."""
    CONFIRMATION = 0
    """Confirmation."""


class GameCategoryOptionTypes(Enum):
    """Game category option types."""

    # TODO: Complete all game category option types
    SELECTOR = 0
    """Selector."""
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

    # TODO: Complete all game category data field input types
    INPUT = 0
    """Input value (inputted by buyer during item purchase)."""


class GameCategoryAutoConfirmPeriods(Enum):
    """Game category auto-confirm periods."""

    # TODO: Complete all game category auto-confirm periods
    SEVEN_DAYS = 0
    """Seven days."""
```
Please note that I left the TODO comments in place as they were, and did not complete them. If you would like me to complete the translations for the remaining TODO comments, please let me know!

