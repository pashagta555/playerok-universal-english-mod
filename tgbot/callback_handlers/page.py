Here is the translation of the code into English:

```
from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .. import templates as templ
from .. import callback_datas as calls
from ..helpful import throw_float_message


router = Router()


@router.callback_query(calls.CustomCommandPage.filter())
async def callback_custom_command_page(callback: CallbackQuery, callback_data: calls.CustomCommandPage, state: FSMContext):
    await state.set_state(None)
    
    command = callback_data.command
    await state.update_data(custom_command=command)
    
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    
    await throw_float_message(
        state=state,
        message=callback.message,
        text=templ.settings_comm_page_text(command),
        reply_markup=templ.settings_comm_page_kb(command, last_page),
        callback=callback
    )


@router.callback_query(calls.AutoDeliveryPage.filter())
async def callback_auto_delivery_page(callback: CallbackQuery, callback_data: calls.AutoDeliveryPage, state: FSMContext):
    await state.set_state(None)
    
    index = callback_data.index
    await state.update_data(auto_delivery_index=index)
    
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    
    await throw_float_message(
        state=state,
        message=callback.message,
        text=templ.settings_deliv_page_text(index),
        reply_markup=templ.settings_deliv_page_kb(index, last_page),
        callback=callback
    )
    

@router.callback_query(calls.MessagePage.filter())
async def callback_message_page(callback: CallbackQuery, callback_data: calls.MessagePage, state: FSMContext):
    await state.set_state(None)
    
    message_id = callback_data.message_id
    await state.update_data(message_id=message_id)
    
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    
    await throw_float_message(
        state=state,
        message=callback.message,
        text=templ.settings_mess_page_text(message_id),
        reply_markup=templ.settings_mess_page_kb(message_id, last_page),
        callback=callback
    )


@router.callback_query(calls.ModulePage.filter())
async def callback_module_page(callback: CallbackQuery, callback_data: calls.ModulePage, state: FSMContext):
    await state.set_state(None)
    
    module_uuid = callback_data.uuid
    await state.update_data(module_uuid=module_uuid)
    
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    
    await throw_float_message(
        state=state,
        message=callback.message,
        text=templ.module_page_text(module_uuid),
        reply_markup=templ.module_page_kb(module_uuid, last_page),
        callback=callback
    )
```

This code defines four functions for handling different types of callback queries in an AIogram bot. The functions are decorated with the `@router.callback_query()` decorator and filter out specific types of callback queries using the `filter()` method.

Each function takes three arguments: `callback`, which is a `CallbackQuery` object representing the incoming callback query; `callback_data`, which contains data related to the callback query; and `state`, which is an instance of `FSMContext` that allows you to store and retrieve data associated with the conversation state.

