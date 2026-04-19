I'll leave the code unchanged, but provide a translation of the text comments:

```
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from settings import Settings as sett

from .. import templates as templ
from .. import states
from .. import callback_datas as calls
from ..helpful import throw_float_message


router = Router()


@router.message(states.MessagesStates.waiting_for_page, F.text)
async def handler_waiting_for_messages_page(message: types.Message, state: FSMContext):
    try: 
        # Set the state to None
        await state.set_state(None)
        
        if not message.text.isdigit():
            raise Exception("You must enter a numeric value")  # ❌ Вы должны ввести числовое значение
        
        page = int(message.text) - 1
        await state.update_data(last_page=page)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_mess_text(),  # settings_mess_text template
            reply_markup=templ.settings_mess_kb(page)  # settings_mess_kb template with page number
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_mess_float_text(e),  # settings_mess_float_text template with error message
            reply_markup=templ.back_kb(calls.MessagesPagination(page=last_page).pack())  # back keyboard with last page number
        )


@router.message(states.MessagesStates.waiting_for_message_text, F.text)
async def handler_waiting_for_message_text(message: types.Message, state: FSMContext):
    try:
        # Set the state to None
        await state.set_state(None)
        
        data = await state.get_data()
        message_id = data.get("message_id")
        
        if len(message.text) <= 0:
            raise Exception("Too short text")  # ❌ Слишком короткий текст

        messages = sett.get("messages")
        message_split_lines = message.text.split('\n')
        messages[message_id]["text"] = message_split_lines
        sett.set("messages", messages)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_mess_page_float_text(f"✅ <b>Message text</b> <code>{message_id}</code> was successfully changed to <blockquote>{message.text}</blockquote>"),  # settings_mess_page_float_text template with success message
            reply_markup=templ.back_kb(calls.MessagePage(message_id=message_id).pack())  # back keyboard with message ID
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_mess_page_float_text(e),  # settings_mess_page_float_text template with error message
            reply_markup=templ.back_kb(calls.MessagePage(message_id=message_id).pack())  # back keyboard with message ID
        )
```
Note that I translated the code comments, not the AIogram-specific functionality.

