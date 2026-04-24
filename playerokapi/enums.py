from enum import Enum

class EventTypes(Enum):
    """Event Types."""
    CHAT_INITIALIZED = 0
    'Chat has been initialized.'
    NEW_MESSAGE = 1
    'New chat message.'
    NEW_DEAL = 2
    'Создана новая сделка (когда покупатель оплатил товар).'
    NEW_REVIEW = 3
    'New review from buyer.'
    DEAL_CONFIRMED = 4
    'Сделка подтверждена (покупатель подтвердил получение предмета).'
    DEAL_CONFIRMED_AUTOMATICALLY = 5
    'Сделка подтверждена автоматически (если покупатель долго не выходит на связь).'
    DEAL_ROLLED_BACK = 6
    'The seller issued a refund.'
    DEAL_HAS_PROBLEM = 7
    'The user reported a problem with the transaction.'
    DEAL_PROBLEM_RESOLVED = 8
    'Transaction problem resolved.'
    DEAL_STATUS_CHANGED = 9
    'Transaction status changed.'
    ITEM_PAID = 10
    'The user paid for the item.'
    ITEM_SENT = 11
    'Предмет отправлен (продавец подтвердил выполнение сделки).'

class ItemLogEvents(Enum):
    """Item log events."""
    PAID = 0
    'The seller confirmed the completion of the transaction.'
    SENT = 1
    'Transaction item shipped.'
    DEAL_CONFIRMED = 2
    'Deal confirmed.'
    DEAL_ROLLED_BACK = 3
    'Deal returned.'
    PROBLEM_REPORTED = 4
    'Отправлена жалоба (создана проблема).'
    PROBLEM_RESOLVED = 5
    'Problem solved.'

class TransactionOperations(Enum):
    """Transaction operations."""
    DEPOSIT = 0
    'Replenishment.'
    BUY = 1
    'Payment for goods.'
    SELL = 2
    'Sale of goods.'
    ITEM_DEFAULT_PRIORITY = 3
    'Pay for free priority.'
    ITEM_PREMIUM_PRIORITY = 4
    'Premium priority payment.'
    WITHDRAW = 5
    'Pay.'
    MANUAL_BALANCE_INCREASE = 6
    'Accrual on баланс аккаунта.'
    MANUAL_BALANCE_DECREASE = 7
    'Write-off from account balance.'
    REFERRAL_BONUS = 8
    'Приглашение друга (реферал).'
    STEAM_DEPOSIT = 9
    'Payment for Steam replenishment.'

class TransactionDirections(Enum):
    """Transaction operations."""
    IN = 0
    'Accrual.'
    OUT = 1
    'Magazine.'

class TransactionStatuses(Enum):
    """Transaction statuses."""
    PENDING = 0
    'В ожидании (транзакция оплачена, но деньги за неё ещё не поступили на баланс).'
    PROCESSING = 1
    'In the freeze.'
    CONFIRMED = 2
    'Transaction deal confirmed.'
    ROLLED_BACK = 3
    'Return on transaction transaction.'
    FAILED = 4
    'Transaction error.'

class TransactionPaymentMethodIds(Enum):
    """ID of transaction methods."""
    MIR = 0
    'Using MIR bank cards.'
    VISA_MASTERCARD = 1
    'С помощью банковских карт VISA/Mastercard.'
    ERIP = 2
    'Using ERIP.'

class TransactionProviderDirections(Enum):
    """Transaction Provider Directions."""
    IN = 0
    'Replenishment.'
    OUT = 1
    'Conclusion.'

class TransactionProviderIds(Enum):
    """Transaction providers ID."""
    LOCAL = 0
    'Using your account balance.'
    SBP = 1
    'Using SBP.'
    BANK_CARD_RU = 2
    'Using a Russian bank card.'
    BANK_CARD_BY = 3
    'Using a Belarusian bank card.'
    BANK_CARD = 4
    'Using a foreign bank card.'
    YMONEY = 5
    'With the help of YuMoney.'
    USDT = 6
    'Криптовалюта USDT (TRC20).'
    PENDING_INCOME = 7
    'Replenishment из замороженных средств.'

class BankCardTypes(Enum):
    """Types of bank cards."""
    MIR = 0
    'Bank card MIR.'
    VISA = 1
    'VISA bank card.'
    MASTERCARD = 2
    'Mastercard bank card.'

class ItemDealStatuses(Enum):
    """Transaction states."""
    PAID = 0
    'The deal is paid.'
    PENDING = 1
    'Transaction pending shipment of goods.'
    SENT = 2
    'The seller confirmed the completion of the transaction.'
    CONFIRMED = 3
    'Deal confirmed.'
    CONFIRMED_AUTOMATICALLY = 4
    'Deal confirmed автоматически.'
    ROLLED_BACK = 5
    'Deal returned.'

class ItemDealDirections(Enum):
    """Transaction directions."""
    IN = 0
    'Purchase.'
    OUT = 1
    'Sale.'

class GameTypes(Enum):
    """Types of games."""
    GAME = 0
    'A game.'
    APPLICATION = 1
    'Application.'

class UserTypes(Enum):
    """User Types."""
    USER = 0
    'Regular user.'
    MODERATOR = 1
    'Moderator.'
    BOT = 2
    'Bot.'

class ChatTypes(Enum):
    """Types of chats."""
    PM = 0
    'Приватный чат (диалог с пользователем).'
    NOTIFICATIONS = 1
    'Chat notifications.'
    SUPPORT = 2
    'Support chat.'

class ChatStatuses(Enum):
    """Chat statuses."""
    NEW = 0
    'Новый чат (в нём нет ни единого прочитанного сообщения).'
    FINISHED = 1
    'Чат доступен, в нём сейчас можно переписываться.'

class ChatMessageButtonTypes(Enum):
    """Types of Message Buttons."""
    REDIRECT = 0
    'Перенаправляет on ссылку.'
    LOTTERY = 1
    'Перенаправляет на розыгрыш/акцию.'

class ItemStatuses(Enum):
    """Статусы items."""
    PENDING_APPROVAL = 0
    'Ожидает принятия (на проверке модерацией).'
    PENDING_MODERATION = 1
    'Awaiting moderation review of changes.'
    APPROVED = 2
    'Активный (принятый модерацией).'
    DECLINED = 3
    'Rejected.'
    BLOCKED = 4
    'Locked.'
    EXPIRED = 5
    'Wanted.'
    SOLD = 6
    'Sold.'
    DRAFT = 7
    'Черновик (если предмет не выставлен на продажу).'

class ReviewStatuses(Enum):
    """Review statuses."""
    APPROVED = 0
    'Active.'
    DELETED = 1
    'Remote.'

class SortDirections(Enum):
    """Types of sorting."""
    DESC = 0
    'Descending.'
    ASC = 1
    'Ascending.'

class PriorityTypes(Enum):
    """Types of Priorities."""
    DEFAULT = 0
    'Standard priority.'
    PREMIUM = 1
    'Premium priority.'

class GameCategoryAgreementIconTypes(Enum):
    """Types of buyer agreement icons in a specific category."""
    RESTRICTION = 0
    'Limitation.'
    CONFIRMATION = 0
    'Confirmation.'

class GameCategoryOptionTypes(Enum):
    """Category Option Types."""
    SELECTOR = 0
    'Type selection.'
    SWITCH = 1
    'Switch.'

class GameCategoryDataFieldTypes(Enum):
    """Types of game category data fields."""
    ITEM_DATA = 0
    'Item Data.'
    OBTAINING_DATA = 1
    'Получаемые данные (после покупки предмета).'

class GameCategoryDataFieldInputTypes(Enum):
    """Types of input fields with game category data."""
    INPUT = 0
    'Вводимое значение (вводится покупателем при оформлении предмета).'

class GameCategoryAutoConfirmPeriods(Enum):
    """Automatic transaction confirmation periods in the game category."""
    SEVEN_DEYS = 0
    'seven days.'

class GameCategoryInstructionTypes(Enum):
    """Types of Category Instructions."""
    FOR_SELLER = 0
    'For the seller.'
    FOR_BUYER = 1
    'For the buyer.'