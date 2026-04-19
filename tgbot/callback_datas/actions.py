The provided text is already in English, as it appears to be a Python code defining various classes for callback data handling in the AIogram library. Therefore, I won't translate it, but rather keep the code unchanged:

```
from aiogram.filters.callback_data import CallbackData


class RememberUsername(CallbackData, prefix="rech"):
    name: str
    do: str

class RememberDealId(CallbackData, prefix="rede"):
    de_id: str
    do: str


class DeleteIncludedRestoreItem(CallbackData, prefix="delinre"):
    index: int

class DeleteExcludedRestoreItem(CCallbackData, prefix="delexre"):
    index: int


class DeleteIncludedCompleteDeal(CallbackData, prefix="delinco"):
    index: int

class DeleteExcludedCompleteDeal(CallbackData, prefix="delexco"):
    index: int


class DeleteIncludedBumpItem(CallbackData, prefix="delinbu"):
    index: int

class DeleteExcludedBumpItem(CCallbackData, prefix="delexbu"):
    index: int


class SelectBankCard(CallbackData, prefix="sebaca"):
    id: str

class SelectSbpBank(CCallbackData, prefix="sesbp"):
    id: str


class SendLogsFile(CCallbackData, prefix="selogs"):
    lines: int


class SetNewDelivPiece(CCallbackData, prefix="sepiece"):
    val: bool

class DeleteDelivGood(CallbackData, prefix="delgod"):
    index: int
```

