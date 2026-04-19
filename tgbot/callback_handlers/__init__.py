The provided text is already in English, so there's nothing to translate. It appears to be Python code for an AIogram bot, which is a popular Telegram bot framework. The code defines a new router instance and includes several other routers into it. 

Here's the original code again:

```
from aiogram import Router

from .navigation import router as navigation_router
from .pagination import router as pagination_router
from .page import router as page_router

from .actions_enter import router as actions_enter_router
from .actions_switch import router as actions_switch_router
from .actions_other import router as actions_other_router
from .actions_confirm import router as actions_confirm_router


router = Router()
router.include_routers(
    navigation_router,
    pagination_router,
    page_router,
    actions_enter_router,
    actions_switch_router,
    actions_other_router,
    actions_confirm_router
)
```

