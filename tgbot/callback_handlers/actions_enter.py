from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from settings import Settings as sett

from .. import templates as templ
from .. import callback_datas as calls
from .. import states as states
from ..helpful import throw_float_message
from .navigation import *


router = Router()


@router.callback_query(F.data == "enter_token")
async def callback_enter_token(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.SettingsStates.waiting_for_token)
    config = sett.get("config")
    golden_key = config["playerok"]["api"]["token"] or "❌ Not set"
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_auth_float_text(f"🔐 Enter a new <b>token</b> for your account ↓\n・ Current: <code>{golden_key}</code>"), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
    )


@router.callback_query(F.data == "enter_user_agent")
async def callback_enter_user_agent(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.SettingsStates.waiting_for_user_agent)
    config = sett.get("config")
    user_agent = config["playerok"]["api"]["user_agent"] or "❌ Not set"
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_auth_float_text(f"🎩 Enter a new <b>User Agent</b> for your browser ↓\n・ Current: <code>{user_agent}</code>"), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
    )


@router.callback_query(F.data == "enter_proxy")
async def callback_enter_proxy(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.SettingsStates.waiting_for_proxy)
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not set"
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_conn_float_text(f"🌐 Enter a new <b>proxy</b> (format: user:pass@ip:port or ip:port) ↓\n・ Current: <code>{proxy}</code>"), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
    )


@router.callback_query(F.data == "enter_requests_timeout")
async def callback_enter_requests_timeout(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.SettingsStates.waiting_for_requests_timeout)
    config = sett.get("config")
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not set"
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_conn_float_text(f"🛜 Enter a new <b>request timeout</b> (in seconds) ↓\n・ Current: <code>{requests_timeout}</code>"), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
    )


@router.callback_query(F.data == "enter_watermark_value")
async def callback_enter_watermark_value(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.SettingsStates.waiting_for_watermark_value)
    config = sett.get("config")
    watermark_value = config["playerok"]["watermark"]["value"] or "❌ Not set"
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_other_float_text(f"✍️©️ Enter a new <b>message watermark</b> ↓\n・ Current: <code>{watermark_value}</code>"), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="other").pack())
    )


@router.callback_query(F.data == "enter_new_included_restore_item_keyphrases")
async def callback_enter_new_included_restore_item_keyphrases(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.RestoreItemsStates.waiting_for_new_included_restore_item_keyphrases)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_new_restore_included_float_text(f"🔑 Enter <b>keyphrases</b> for the item name to include in auto-restore (comma-separated, e.g. \"samp account, with all data\") ↓"), 
        reply_markup=templ.back_kb(calls.IncludedRestoreItemsPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_new_excluded_restore_item_keyphrases")
async def callback_enter_new_excluded_restore_item_keyphrases(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.RestoreItemsStates.waiting_for_new_excluded_restore_item_keyphrases)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_new_restore_excluded_float_text(f"🔑 Enter <b>keyphrases</b> for the item name to exclude from auto-restore (comma-separated, e.g. \"samp account, with all data\") ↓"), 
        reply_markup=templ.back_kb(calls.ExcludedRestoreItemsPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_auto_bump_items_interval")
async def callback_enter_auto_bump_items_interval(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.set_state(states.BumpItemsStates.waiting_for_bump_items_interval)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_bump_float_text(f"⏲️ Enter the <b>item bump interval</b> ↓"), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="bump").pack())
    )


@router.callback_query(F.data == "enter_new_included_bump_item_keyphrases")
async def callback_enter_new_included_bump_item_keyphrases(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.BumpItemsStates.waiting_for_new_included_bump_item_keyphrases)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_new_bump_included_float_text(f"🔑 Enter <b>keyphrases</b> for the item name to include in auto-bump (comma-separated, e.g. \"samp account, with all data\") ↓"), 
        reply_markup=templ.back_kb(calls.IncludedBumpItemsPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_new_excluded_bump_item_keyphrases")
async def callback_enter_new_excluded_bump_item_keyphrases(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.BumpItemsStates.waiting_for_new_excluded_bump_item_keyphrases)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_new_bump_excluded_float_text(f"🔑 Enter <b>keyphrases</b> for the item name to exclude from auto-bump (comma-separated, e.g. \"samp account, with all data\") ↓"), 
        reply_markup=templ.back_kb(calls.ExcludedBumpItemsPagination(page=last_page).pack())
    )
        

@router.callback_query(F.data == "enter_custom_commands_page")
async def callback_enter_custom_commands_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.CustomCommandsStates.waiting_for_page)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_comms_float_text(f"📃 Enter a page number to navigate ↓"), 
        reply_markup=templ.back_kb(calls.CustomCommandsPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_new_custom_command")
async def callback_enter_new_custom_command(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.CustomCommandsStates.waiting_for_new_custom_command)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_new_comm_float_text(f"⌨️ Enter a <b>new command</b> (e.g. <code>!test</code>) ↓"), 
        reply_markup=templ.back_kb(calls.CustomCommandsPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_custom_command_answer")
async def callback_enter_custom_command_answer(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        custom_commands = sett.get("custom_commands")
        custom_command = data.get("custom_command")
        if not custom_command:
            raise Exception("❌ Custom command was not found, please restart the process from the beginning")
        
        await state.set_state(states.CustomCommandsStates.waiting_for_custom_command_answer)
        custom_command_answer = "\n".join(custom_commands[custom_command]) or "❌ Not set"
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_comm_page_float_text(f"💬 Enter a new <b>reply text</b> for command <code>{custom_command}</code> ↓\n・ Current: <blockquote>{custom_command_answer}</blockquote>"), 
            reply_markup=templ.back_kb(calls.CustomCommandPage(command=custom_command).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_comm_page_float_text(e), 
            reply_markup=templ.back_kb(calls.CustomCommandsPagination(page=last_page).pack())
        )


@router.callback_query(F.data == "enter_auto_deliveries_page")
async def callback_enter_auto_deliveries_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.AutoDeliveriesStates.waiting_for_page)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_delivs_float_text(f"📃 Enter a page number to navigate ↓"), 
        reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_new_auto_delivery_keyphrases")
async def callback_enter_new_auto_delivery_keyphrases(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.AutoDeliveriesStates.waiting_for_new_auto_delivery_keyphrases)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_new_deliv_float_text(f"🔑 Enter <b>keyphrases</b> for the item name to add auto-delivery to (comma-separated, e.g. \"telegram subscribers, auto-delivery\") ↓"), 
        reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_auto_delivery_keyphrases")
async def callback_enter_auto_delivery_keyphrases(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        auto_delivery_index = data.get("auto_delivery_index")
        if auto_delivery_index is None:
            raise Exception("❌ Auto-delivery was not found, please restart the process from the beginning")
        
        await state.set_state(states.AutoDeliveriesStates.waiting_for_auto_delivery_keyphrases)
        auto_deliveries = sett.get("auto_deliveries")
        auto_delivery_message = "</code>, <code>".join(auto_deliveries[auto_delivery_index]["keyphrases"]) or "❌ Not set"
        
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_deliv_page_float_text(f"🔑 Enter new <b>keyphrases</b> for the item name (comma-separated)\n・ Current: <code>{auto_delivery_message}</code>"), 
            reply_markup=templ.back_kb(calls.AutoDeliveryPage(index=auto_delivery_index).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_deliv_page_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
        )


@router.callback_query(F.data == "enter_auto_delivery_message")
async def callback_enter_auto_delivery_message(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        auto_delivery_index = data.get("auto_delivery_index")
        if auto_delivery_index is None:
            raise Exception("❌ Auto-delivery was not found, please restart the process from the beginning")
        
        await state.set_state(states.AutoDeliveriesStates.waiting_for_auto_delivery_message)
        auto_deliveries = sett.get("auto_deliveries")
        auto_delivery_message = "\n".join(auto_deliveries[auto_delivery_index]["message"]) or "❌ Not set"
        
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_deliv_page_float_text(f"💬 Enter a new <b>message</b> after purchase\n・ Current: <blockquote>{auto_delivery_message}</blockquote>"), 
            reply_markup=templ.back_kb(calls.AutoDeliveryPage(index=auto_delivery_index).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_deliv_page_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
        )


@router.callback_query(F.data == "enter_auto_withdrawal_interval")
async def callback_enter_auto_withdrawal_interval(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)

    config = sett.get("config")
    interval = config["playerok"]["auto_withdrawal"]["interval"]

    await state.set_state(states.SettingsStates.waiting_for_auto_withdrawal_interval)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_withdrawal_float_text(
            f"⏱️ Enter a new <b>withdrawal interval</b> (in seconds) ↓"
            f"\n・ Current: <code>{interval}</code>"
        ), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
    )


@router.callback_query(F.data == "enter_usdt_address")
async def callback_enter_usdt_address(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)

    await state.set_state(states.SettingsStates.waiting_for_usdt_address)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_withdrawal_usdt_float_text(
            f"💲 Enter the <b>wallet address</b> for USDT (TRC20) ↓"
        ), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
    )


@router.callback_query(F.data == "enter_messages_page")
async def callback_enter_messages_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_page = data.get("last_page", 0)
    await state.set_state(states.MessagesStates.waiting_for_page)
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_mess_float_text(f"📃 Enter a page number to navigate ↓"), 
        reply_markup=templ.back_kb(calls.MessagesPagination(page=last_page).pack())
    )


@router.callback_query(F.data == "enter_message_text")
async def callback_enter_message_text(callback: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        message_id = data.get("message_id")
        if not message_id:
            raise Exception("❌ Message ID was not found, please restart the process from the beginning")
        
        await state.set_state(states.MessagesStates.waiting_for_message_text)
        messages = sett.get("messages")
        mess_text = "\n".join(messages[message_id]["text"]) or "❌ Not set"
        
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_mess_float_text(f"💬 Enter a new <b>message text</b> <code>{message_id}</code> ↓\n・ Current: <blockquote>{mess_text}</blockquote>"), 
            reply_markup=templ.back_kb(calls.MessagesPagination(page=last_page).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state, 
            message=callback.message, 
            text=templ.settings_mess_float_text(e), 
            reply_markup=templ.back_kb(calls.MessagesPagination(page=last_page).pack())
        )


@router.callback_query(F.data == "enter_tg_logging_chat_id")
async def callback_enter_tg_logging_chat_id(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.SettingsStates.waiting_for_tg_logging_chat_id)
    config = sett.get("config")
    tg_logging_chat_id = config["playerok"]["tg_logging"]["chat_id"] or "✔️ Your chat with the bot"
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.settings_logger_float_text(f"💬 Enter a new <b>log chat ID</b> (you can provide a numeric ID or a username) ↓\n・ Current: <code>{tg_logging_chat_id}</code>"), 
        reply_markup=templ.back_kb(calls.SettingsNavigation(to="logger").pack())
    )


@router.callback_query(F.data == "enter_logs_max_file_size")
async def callback_enter_logs_max_file_size(callback: CallbackQuery, state: FSMContext):
    await state.set_state(states.SettingsStates.waiting_for_logs_max_file_size)
    config = sett.get("config")
    max_file_size = config["logs"]["max_file_size"] or "❌ Not set"
    await throw_float_message(
        state=state, 
        message=callback.message, 
        text=templ.logs_float_text(
            f"📄 Enter a new <b>maximum log file size</b> (in megabytes) ↓"
            f"\n・ Current: <b>{max_file_size} MB</b>"
        ), 
        reply_markup=templ.back_kb(calls.MenuNavigation(to="logs").pack())
    )