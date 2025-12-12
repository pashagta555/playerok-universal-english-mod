from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.exceptions import TelegramAPIError

from . import templates as templ


async def do_auth(message: Message, state: FSMContext) -> Message | None:
    """
    Starts bot authorization process (requests password specified in config).

    :param message: Source message.
    :type message: `aiogram.types.Message`

    :param state: Source state.
    :type state: `aiogram.fsm.context.FSMContext`
    """
    from . import states
    
    await state.set_state(states.SystemStates.waiting_for_password)
    return await throw_float_message(
        state=state,
        message=message,
        text=templ.sign_text('🔑 Enter the password key you specified in the bot config ↓\n\n<span class="tg-spoiler">If you forgot it, you can view it directly in the config at path bot_settings/config.json, parameter password in section telegram.bot</span>'),
        reply_markup=templ.destroy_kb()
    )


async def throw_float_message(state: FSMContext, message: Message, text: str, 
                              reply_markup: InlineKeyboardMarkup = None,
                              callback: CallbackQuery = None,
                              send: bool = False) -> Message | None:
    """
    Changes floating message (changes text of accented message) or parent bot message passed in `message` argument.\n
    If accented message not found, or this message is a command, sends new accented message.

    :param state: Bot state.
    :type state: `aiogram.fsm.context.FSMContext`
    
    :param message: Message object passed to handler.
    :type message: `aiogram.types.Message`

    :param text: Message text.
    :type text: `str`

    :param reply_markup: Message keyboard, _optional_.
    :type reply_markup: `aiogram.types.InlineKeyboardMarkup`

    :param callback: Handler CallbackQuery, for empty AnswerCallbackQuery response, _optional_.
    :type callback: `aiogram.types.CallbackQuery` or `None`

    :param send: Whether to send new accented message, _optional_.
    :type send: `bool`
    """
    from .telegrambot import get_telegram_bot
    try:
        bot = get_telegram_bot().bot
        data = await state.get_data()
        accent_message_id = message.message_id
        if message.from_user and message.from_user.id != bot.id:
            accent_message_id = data.get("accent_message_id")
        mess = None
        new_mess_cond = False

        if not send:
            if message.text is not None:
                new_mess_cond = message.from_user.id != bot.id and message.text.startswith('/')

            if accent_message_id is not None and not new_mess_cond:
                try:
                    if message.from_user.id != bot.id: 
                        await bot.delete_message(message.chat.id, message.message_id)
                    mess = await bot.edit_message_text(
                        text=text, 
                        reply_markup=reply_markup, 
                        chat_id=message.chat.id, 
                        message_id=accent_message_id, 
                        parse_mode="HTML"
                    )
                except TelegramAPIError as e:
                    if "message to edit not found" in e.message.lower():
                        accent_message_id = None
                    elif "message is not modified" in e.message.lower():
                        await bot.answer_callback_query(
                            callback_query_id=callback.id, 
                            show_alert=False, 
                            cache_time=0
                        )
                        pass
                    elif "query is too old" in e.message.lower():
                        return
                    else:
                        raise e
        if callback:
            await bot.answer_callback_query(
                callback_query_id=callback.id, 
                show_alert=False, 
                cache_time=0
            )
        if accent_message_id is None or new_mess_cond or send:
            mess = await bot.send_message(
                chat_id=message.chat.id, 
                text=text, 
                reply_markup=reply_markup, 
                parse_mode="HTML"
            )
    except Exception as e:
        try:
            mess = await bot.edit_message_text(
                chat_id=message.chat.id, 
                reply_markup=templ.destroy_kb(),
                text=templ.error_text(e), 
                message_id=accent_message_id, 
                parse_mode="HTML"
            )
        except Exception as e:
            mess = await bot.send_message(
                chat_id=message.chat.id, 
                reply_markup=templ.destroy_kb(),
                text=templ.error_text(e), 
                parse_mode="HTML"
            )
    finally:
        if mess: await state.update_data(accent_message_id=mess.message_id)
    return mess