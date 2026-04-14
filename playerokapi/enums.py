from enum import Enum


class EventTypes(Enum):
    """Types events."""

    CHAT_INITIALIZED = 0
    """Chat initialized."""
    NEW_MESSAGE = 1
    """New message V chat."""
    NEW_DEAL = 2
    """Created new deal (When buyer paid product)."""
    NEW_REVIEW = 3
    """New review from buyer."""
    DEAL_CONFIRMED = 4
    """Deal confirmed (buyer confirmed receiving subject)."""
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    """Deal confirmed automatically (If buyer for a long time Not comes out on connection)."""
    DEAL_ROLLED_BACK = 6
    """Salesman issued return deals."""
    DEAL_HAS_PROBLEM = 7
    """User reported O problem V deal."""
    DEAL_PROBLEM_RESOLVED = 8
    """Problem V deal resolved."""
    DEAL_STATUS_CHANGED = 9
    """Status deals changed."""
    ITEM_PAID = 10
    """User paid item."""
    ITEM_SENT = 11
    """Item sent (seller confirmed execution deals)."""


class ItemLogEvents(Enum):
    """Events lairs subject."""

    PAID = 0
    """Salesman confirmed execution deals."""
    SENT = 1
    """Product deals sent."""
    DEAL_CONFIRMED = 2
    """Deal confirmed."""
    DEAL_ROLLED_BACK = 3
    """Deal returned."""
    PROBLEM_REPORTED = 4
    """Sent complaint (created problem)."""
    PROBLEM_RESOLVED = 5
    """Problem resolved."""


class TransactionOperations(Enum):
    """Operations transactions."""

    DEPOSIT = 0
    """Replenishment."""
    BUY = 1
    """Payment goods."""
    SELL = 2
    """Sale goods."""
    ITEM_DEFAULT_PRIORITY = 3
    """Payment free priority."""
    ITEM_PREMIUM_PRIORITY = 4
    """Payment premium priority."""
    WITHDRAW = 5
    """Pay."""
    MANUAL_BALANCE_INCREASE = 6
    """Accrual on balance account."""
    MANUAL_BALANCE_DECREASE = 7
    """Write-off With balance account."""
    REFERRAL_BONUS = 8
    """Invitation friend (referral)."""
    STEAM_DEPOSIT = 9
    """Payment replenishment Steam."""


class TransactionDirections(Enum):
    """Operations transactions."""

    IN = 0
    """Accrual."""
    OUT = 1
    """Write-off."""


class TransactionStatuses(Enum):
    """Statuses transactions."""

    PENDING = 0
    """IN waiting (transaction paid, But money for her more Not arrived on balance)."""
    PROCESSING = 1
    """IN freezing."""
    CONFIRMED = 2
    """Deal transactions confirmed."""
    ROLLED_BACK = 3
    """Return By deal transactions."""
    FAILED = 4
    """Error transactions."""


class TransactionPaymentMethodIds(Enum):
    """ID methods transactions."""

    MIR = 0
    """WITH with help banking kart WORLD."""
    VISA_MASTERCARD = 1
    """WITH with help banking kart VISA/Mastercard."""
    ERIP = 2
    """WITH with help ERIP."""


class TransactionProviderDirections(Enum):
    """Directions providers transactions."""

    IN = 0
    """Replenishment."""
    OUT = 1
    """Conclusion."""


class TransactionProviderIds(Enum):
    """ID providers transactions."""

    LOCAL = 0
    """WITH with help balance account."""
    SBP = 1
    """WITH with help SBP."""
    BANK_CARD_RU = 2
    """WITH with help banking cards Russia."""
    BANK_CARD_BY = 3
    """WITH with help banking cards Belarus."""
    BANK_CARD = 4
    """WITH with help foreign banking cards."""
    YMONEY = 5
    """WITH with help YuMoney."""
    USDT = 6
    """Cryptocurrency USDT (TRC20)."""
    PENDING_INCOME = 7
    """Replenishment from frozen funds."""


class BankCardTypes(Enum):
    """Types banking kart."""

    MIR = 0
    """Banking map WORLD."""
    VISA = 1
    """Banking map VISA."""
    MASTERCARD = 2
    """Banking map Mastercard."""


class ItemDealStatuses(Enum):
    """States deals."""

    PAID = 0
    """Deal paid."""
    PENDING = 1
    """Deal V waiting sending goods."""
    SENT = 2
    """Salesman confirmed execution deals."""
    CONFIRMED = 3
    """Deal confirmed."""
    CONFIRMED_AUTOMATICALLY = 4
    """Deal confirmed automatically."""
    ROLLED_BACK = 5
    """Deal returned."""


class ItemDealDirections(Enum):
    """Directions deals."""

    IN = 0
    """Purchase."""
    OUT = 1
    """Sale."""


class GameTypes(Enum):
    """Types games."""

    GAME = 0
    """Game."""
    APPLICATION = 1
    """Application."""


class UserTypes(Enum):
    """Types users."""

    USER = 0
    """Ordinary user."""
    MODERATOR = 1
    """Moderator."""
    BOT = 2
    """Bot."""


class ChatTypes(Enum):
    """Types chats."""

    PM = 0
    """Private chat (dialogue With user)."""
    NOTIFICATIONS = 1
    """Chat notifications."""
    SUPPORT = 2
    """Chat support."""


class ChatStatuses(Enum):
    """Statuses chats."""

    NEW = 0
    """New chat (V him No neither single read messages)."""
    FINISHED = 1
    """Chat available, V him Now Can correspond."""


class ChatMessageButtonTypes(Enum):
    """Types buttons messages."""

    # TODO: Finish All types buttons messages
    REDIRECT = 0
    """Redirects on link."""
    LOTTERY = 1
    """Redirects on draw/share."""


class ItemStatuses(Enum):
    """Statuses items."""

    PENDING_APPROVAL = 0
    """Waiting adoption (on verification moderation)."""
    PENDING_MODERATION = 1
    """Waiting checks changes moderation."""
    APPROVED = 2
    """Active (accepted moderation)."""
    DECLINED = 3
    """Rejected."""
    BLOCKED = 4
    """Locked."""
    EXPIRED = 5
    """Expired."""
    SOLD = 6
    """Sold."""
    DRAFT = 7
    """Draft (If item Not exhibited on sale)."""


class ReviewStatuses(Enum):
    """Statuses reviews."""

    APPROVED = 0
    """Active."""
    DELETED = 1
    """Remote."""


class SortDirections(Enum):
    """Types sorting."""

    DESC = 0
    """By descending."""
    ASC = 1
    """By increasing."""


class PriorityTypes(Enum):
    """Types priorities."""

    DEFAULT = 0
    """Standard priority."""
    PREMIUM = 1
    """Premium priority."""


class GameCategoryAgreementIconTypes(Enum):
    """Types icons agreements buyer V certain categories."""

    # TODO: Finish All types icons agreements
    RESTRICTION = 0
    """Limitation."""
    CONFIRMATION = 0
    """Confirmation."""


class GameCategoryOptionTypes(Enum):
    """Types options categories."""

    # TODO: Finish All types options categories
    SELECTOR = 0
    """Choice type."""
    SWITCH = 1
    """Switch."""


class GameCategoryDataFieldTypes(Enum):
    """Types fields With data categories games."""

    ITEM_DATA = 0
    """Data subject."""
    OBTAINING_DATA = 1
    """Received data (after purchases subject)."""


class GameCategoryDataFieldInputTypes(Enum):
    """Types entered fields With data categories games."""

    # TODO: Finish All types entered date-fields
    INPUT = 0
    """Input meaning (introduced buyer at registration subject)."""


class GameCategoryAutoConfirmPeriods(Enum):
    """Periods automatic confirmation deals V categories games."""

    # TODO: Finish All periods auto-confirmation
    SEVEN_DEYS = 0
    """Seven days."""


class GameCategoryInstructionTypes(Enum):
    """Types instructions categories."""

    FOR_SELLER = 0
    """For seller."""
    FOR_BUYER = 1
    """For buyer."""
