import re
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from settings import Settings as sett

from .. import templates as templ
from .. import states
from .. import callback_datas as calls
from ..helpful import throw_float_message

from utils import (
    is_token_valid,
    is_user_agent_valid,
    is_proxy_valid, 
    is_proxy_working
)


router = Router()


@router.message(states.SettingsStates.waiting_for_token, F.text)
async def handler_waiting_for_token(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        token = message.text
        
        if not is_token_valid(token):
            raise Exception("❌ Incorrect format token. Example: eyJhbGciOiJIUzI1NiIsInR5cCI1IkpXVCJ9")

        config = sett.get("config")
        config["playerok"]["api"]["token"] = token
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(f"✅ <b>Token</b> was successfully changed on <b>{token}</b>"),
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
        
        user_agent = message.text
        
        if not is_user_agent_valid(user_agent):
            raise Exception("❌ Incorrect format User Agent. Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36")

        config = sett.get("config")
        config["playerok"]["api"]["user_agent"] = user_agent
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(f"✅ <b>User Agent</b> was successfully changed on <b>{user_agent}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="auth").pack())
        )


@router.message(states.SettingsStates.waiting_for_pl_proxy, F.text)
async def handler_waiting_for_pl_proxy(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        proxy = message.text
        
        if len(proxy) <= 3:
            raise Exception("❌ Too much short meaning")
        if not is_proxy_valid(proxy):
            raise Exception("❌ Incorrect format proxy. Correct format: user:pass@ip:port or ip:port")
        if not is_proxy_working(proxy):
            raise Exception("❌ Specified you proxy Not works. No connections To playerok.com")

        config = sett.get("config")
        config["playerok"]["api"]["proxy"] = proxy
        sett.set("config", config)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(f"✅ <b>Proxy For Playerok</b> was successfully changed on <b>{proxy}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="conn").pack())
        )


@router.message(states.SettingsStates.waiting_for_tg_proxy, F.text)
async def handler_waiting_for_tg_proxy(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        proxy = message.text
        
        if len(proxy) <= 3:
            raise Exception("❌ Too much short meaning")
        if not is_proxy_valid(proxy):
            raise Exception("❌ Incorrect format proxy. Correct format: user:pass@ip:port or ip:port")
        if not is_proxy_working(proxy, "https://api.telegram.org/"):
            raise Exception("❌ Specified you proxy Not works. No connections To api.telegram.org")

        config = sett.get("config")
        config["telegram"]["api"]["proxy"] = proxy
        sett.set("config", config)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_auth_float_text(f"✅ <b>Proxy For Telegram</b> was successfully changed on <b>{proxy}</b>"),
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
        
        timeout = message.text
        
        if not timeout.isdigit():
            raise Exception("❌ You should enter numeric meaning")       
        if int(timeout) < 0:
            raise Exception("❌ Too much low meaning")

        config = sett.get("config")
        config["playerok"]["api"]["requests_timeout"] = int(timeout)
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_conn_float_text(f"✅ <b>Time-out requests</b> was successfully changed on <b>{timeout}</b>"),
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
        
        delay = message.text
        
        if not delay.isdigit():
            raise Exception("❌ You should enter numeric meaning")
        if int(delay) < 0:
            raise Exception("❌ Too much low meaning")

        config = sett.get("config")
        config["playerok"]["api"]["listener_requests_delay"] = int(delay)
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_conn_float_text(f"✅ <b>Periodicity requests</b> was successful changed on <b>{delay}</b>"),
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
        
        chat_input = message.text
        
        if len(chat_input) < 0:
            raise Exception("❌ Too much low meaning")
        
        if chat_input.isdigit(): 
            chat_id = "-100" + str(chat_input).replace("-100", "")
        else: 
            chat_id = "@" + str(chat_input).replace("@", "")
        
        config = sett.get("config")
        config["playerok"]["tg_logging"]["chat_id"] = chat_id
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_logger_float_text(f"✅ <b>ID chat For lairs</b> was successfully changed on <b>{chat_id}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="logger").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_logger_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="logger").pack())
        )


@router.message(states.SettingsStates.waiting_for_auto_withdrawal_interval, F.text)
async def handler_waiting_for_auto_withdrawal_interval(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        interval = message.text
        
        if not interval.isdigit():
            raise Exception("❌ You should enter numeric meaning")
        if int(interval) <= 1:
            raise Exception("❌ Too much low meaning")
        
        interval_int = int(interval)

        config = sett.get("config")
        config["playerok"]["auto_withdrawal"]["interval"] = interval_int
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_withdrawal_float_text(f"✅ <b>Interval output</b> was successfully changed on <b>{interval_int}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_withdrawal_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
        )


@router.message(states.SettingsStates.waiting_for_sbp_bank_phone_number, F.text)
async def handler_waiting_for_sbp_bank_phone_number(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        data = await state.get_data()
        sbp_bank_id = data.get("sbp_bank_id")
        
        phone_number = message.text
        
        if not phone_number.isdigit():
            raise Exception("❌ You indicated incorrect number phone")
        if len(phone_number) < 4:
            raise Exception("❌ Too much short meaning")
        
        if phone_number.startswith("8"):
            phone_number = phone_number.replace("8", "+7", 1)

        config = sett.get("config")
        config["playerok"]["auto_withdrawal"]["credentials_type"] = "sbp"
        config["playerok"]["auto_withdrawal"]["sbp_bank_id"] = sbp_bank_id
        config["playerok"]["auto_withdrawal"]["sbp_phone_number"] = phone_number.strip()
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_withdrawal_sbp_float_text(f"✅ <b>Data output</b> were successfully changed on <b>{phone_number} (SBP)</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_withdrawal_sbp_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
        )


@router.message(states.SettingsStates.waiting_for_usdt_address, F.text)
async def handler_waiting_for_usdt_address(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        address = message.text
        
        if len(address) <= 10:
            raise Exception("❌ Too much short meaning")

        config = sett.get("config")
        config["playerok"]["auto_withdrawal"]["credentials_type"] = "usdt"
        config["playerok"]["auto_withdrawal"]["usdt_address"] = address
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_withdrawal_float_text(f"✅ <b>Data output</b> were successfully changed on <b>{address} (USDT TRC20)</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_withdrawal_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="withdrawal").pack())
        )
            

@router.message(states.SettingsStates.waiting_for_watermark_value, F.text)
async def handler_waiting_for_watermark_value(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        watermark = message.text

        if len(watermark) <= 0 or len(watermark) >= 150:
            raise Exception("❌ Too much short or long meaning")

        config = sett.get("config")
        config["playerok"]["watermark"]["value"] = watermark
        sett.set("config", config)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_other_float_text(f"✅ <b>Water sign messages</b> was successfully changed on <b>{watermark}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="other").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_other_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="other").pack())
        )
            

@router.message(states.SettingsStates.waiting_for_logs_max_file_size, F.text)
async def handler_waiting_for_logs_max_file_size(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        max_size = message.text
        
        if not max_size.isdigit():
            raise Exception("❌ You should enter numeric meaning")
        if int(max_size) <= 0:
            raise Exception("❌ Too much low meaning")
        
        max_size_int = int(max_size)

        config = sett.get("config")
        config["logs"]["max_file_size"] = max_size_int
        sett.set("config", config)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.logs_float_text(f"✅ <b>Maximum size file lairs</b> was successfully changed on <b>{max_size_int} MB</b>"),
            reply_markup=templ.back_kb(calls.MenuNavigation(to="logs").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.logs_float_text(e), 
            reply_markup=templ.back_kb(calls.MenuNavigation(to="logs").pack())
        )