import re
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from settings import Settings as sett

from .. import templates as templ
from .. import states
from .. import callback_datas as calls
from ..helpful import throw_float_message


router = Router()


def is_eng_str(str: str):
    pattern = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~ ]+$'
    return bool(re.match(pattern, str))


@router.message(states.SettingsStates.waiting_for_token, F.text)
async def handler_waiting_for_token(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if len(message.text.strip()) <= 3 or len(message.text.strip()) >= 500:
            raise Exception("❌ Too short or too long value")

        config = sett.get("config")
        config["playerok"]["api"]["token"] = message.text.strip()
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(f"✅ <b>Token</b> was successfully changed to <b>{message.text.strip()}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
        )


@router.message(states.SettingsStates.waiting_for_user_agent, F.text)
async def handler_waiting_for_user_agent(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if len(message.text.strip()) <= 3:
            raise Exception("❌ Value is too short")

        config = sett.get("config")
        config["playerok"]["api"]["user_agent"] = message.text.strip()
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(f"✅ <b>user_agent</b> was successfully changed to <b>{message.text.strip()}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
        )


@router.message(states.SettingsStates.waiting_for_proxy, F.text)
async def handler_waiting_for_proxy(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if len(message.text.strip()) <= 3:
            raise Exception("❌ Value is too short")
        if not is_eng_str(message.text.strip()):
            raise Exception("❌ Invalid proxy")

        config = sett.get("config")
        config["playerok"]["api"]["proxy"] = message.text.strip()
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(f"✅ <b>Proxy</b> was successfully changed to <b>{message.text.strip()}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )


@router.message(states.SettingsStates.waiting_for_requests_timeout, F.text)
async def handler_waiting_for_requests_timeout(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if not message.text.strip().isdigit():
            raise Exception("❌ You must enter a numeric value")       
        if int(message.text.strip()) < 0:
            raise Exception("❌ Value is too low")

        config = sett.get("config")
        config["playerok"]["api"]["requests_timeout"] = int(message.text.strip())
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_conn_float_text(f"✅ <b>Request timeout</b> was successfully changed to <b>{message.text.strip()}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_conn_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )


@router.message(states.SettingsStates.waiting_for_listener_requests_delay, F.text)
async def handler_waiting_for_listener_requests_delay(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if not message.text.strip().isdigit():
            raise Exception("❌ You must enter a numeric value")
        if int(message.text.strip()) < 0:
            raise Exception("❌ Value is too low")

        config = sett.get("config")
        config["playerok"]["api"]["listener_requests_delay"] = int(message.text.strip())
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_conn_float_text(f"✅ <b>Request frequency</b> was successfully changed to <b>{message.text.strip()}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_conn_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )


@router.message(states.SettingsStates.waiting_for_tg_logging_chat_id, F.text)
async def handler_waiting_for_tg_logging_chat_id(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None) 
        if len(message.text.strip()) < 0:
            raise Exception("❌ Value is too low")
        
        if message.text.strip().isdigit(): 
            chat_id = "-100" + str(message.text.strip()).replace("-100", "")
        else: 
            chat_id = "@" + str(message.text.strip()).replace("@", "")
        
        config = sett.get("config")
        config["playerok"]["tg_logging"]["chat_id"] = chat_id
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_logger_float_text(f"✅ <b>Chat ID for logs</b> was successfully changed to <b>{chat_id}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="logger").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_logger_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="logger").pack())
        )
            

@router.message(states.SettingsStates.waiting_for_watermark_value, F.text)
async def handler_waiting_for_watermark_value(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        data = await state.get_data()
        if len(message.text.strip()) <= 0 or len(message.text.strip()) >= 150:
            raise Exception("❌ Too short or too long value")

        config = sett.get("config")
        config["playerok"]["watermark"]["value"] = message.text.strip()
        sett.set("config", config)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_other_float_text(f"✅ <b>Message watermark</b> was successfully changed to <b>{message.text.strip()}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="other").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_other_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="other").pack())
        )
