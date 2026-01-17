from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from settings import Settings as sett

from .. import templates as templ
from .. import callback_datas as calls
from .. import states
from ..helpful import throw_float_message


router = Router()


@router.message(states.BumpItemsStates.waiting_for_day_max_sequence, F.text)
async def handler_waiting_for_day_max_sequence(message: types.Message, state: FSMContext):
    try: 
        await state.set_state(None)
        if not message.text.strip().isdigit():
            raise Exception("❌ Value is too short")

        day_max_sequence = int(message.text.strip())
        config = sett.get("config")
        config["playerok"]["auto_bump_items"]["day_max_sequence"] = day_max_sequence
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_bump_float_text(f"✅ <b>Maximum item position during day</b> was successfully changed to <b>{day_max_sequence}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="bump").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_bump_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="bump").pack())
        )


@router.message(states.BumpItemsStates.waiting_for_night_max_sequence, F.text)
async def handler_waiting_for_night_max_sequence(message: types.Message, state: FSMContext):
    try: 
        await state.set_state(None)
        if not message.text.strip().isdigit():
            raise Exception("❌ You must enter a numeric value")

        night_max_sequence = int(message.text.strip())
        config = sett.get("config")
        config["playerok"]["auto_bump_items"]["night_max_sequence"] = night_max_sequence
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_bump_float_text(f"✅ <b>Maximum item position during night</b> was successfully changed to <b>{night_max_sequence}</b>"),
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="bump").pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_bump_float_text(e), 
            reply_markup=templ.back_kb(calls.SettingsNavigation(to="bump").pack())
        )


@router.message(states.BumpItemsStates.waiting_for_new_included_bump_item_keyphrases, F.text)
async def handler_waiting_for_new_included_bump_item_keyphrases(message: types.Message, state: FSMContext):
    try: 
        await state.set_state(None)
        if len(message.text.strip()) <= 0:
            raise Exception("❌ Value is too short")
        
        keyphrases = [phrase.strip() for phrase in message.text.strip().split(",") if len(phrase.strip()) > 0]
        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["included"].append(keyphrases)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_included_float_text(f"✅ Item with keyphrases <code>{'</code>, <code>'.join(keyphrases)}</code> was successfully included in bump"),
            reply_markup=templ.back_kb(calls.IncludedBumpItemsPagination(page=last_page).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_included_float_text(e), 
            reply_markup=templ.back_kb(calls.IncludedBumpItemsPagination(page=last_page).pack())
        )


@router.message(
    states.BumpItemsStates.waiting_for_new_included_bump_items_keyphrases_file, 
    F.document.file_name.lower().endswith('.txt')
)
async def handler_waiting_for_new_included_bump_items_keyphrases_file(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        file = await message.bot.get_file(message.document.file_id)
        downloaded_file = await message.bot.download_file(file.file_path)
        file_content = downloaded_file.read().decode('utf-8')

        keyphrases_list = []
        for line in file_content.splitlines():
            line = line.strip()
            if len(line) > 0:
                keyphrases = [phrase.strip() for phrase in line.split(",") if len(phrase.strip()) > 0]
                if len(keyphrases) > 0:
                    keyphrases_list.append(keyphrases)

        if len(keyphrases_list) <= 0:
            raise Exception("❌ File does not contain valid keyphrases")

        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["included"].extend(keyphrases_list)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_included_float_text(f"✅ Successfully included <b>{len(keyphrases_list)}</b> items from file in bump"),
            reply_markup=templ.back_kb(calls.IncludedBumpItemsPagination(page=last_page).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_included_float_text(e), 
            reply_markup=templ.back_kb(calls.IncludedBumpItemsPagination(page=last_page).pack())
        )


@router.message(states.BumpItemsStates.waiting_for_new_excluded_bump_item_keyphrases, F.text)
async def handler_waiting_for_new_excluded_bump_item_keyphrases(message: types.Message, state: FSMContext):
    try: 
        await state.set_state(None)
        if len(message.text.strip()) <= 0:
            raise Exception("❌ Value is too short")
        
        keyphrases = [phrase.strip() for phrase in message.text.strip().split(",") if len(phrase.strip()) > 0]
        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["excluded"].append(keyphrases)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_excluded_float_text(f"✅ Item with keyphrases <code>{'</code>, <code>'.join(keyphrases)}</code> was successfully added to exclusions for bump"),
            reply_markup=templ.back_kb(calls.ExcludedBumpItemsPagination(page=last_page).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_excluded_float_text(e), 
            reply_markup=templ.back_kb(calls.ExcludedBumpItemsPagination(page=last_page).pack())
        )


@router.message(
    states.BumpItemsStates.waiting_for_new_excluded_bump_items_keyphrases_file, 
    F.document.file_name.lower().endswith('.txt')
)
async def handler_waiting_for_new_excluded_bump_items_keyphrases_file(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        file = await message.bot.get_file(message.document.file_id)
        downloaded_file = await message.bot.download_file(file.file_path)
        file_content = downloaded_file.read().decode('utf-8')

        keyphrases_list = []
        for line in file_content.splitlines():
            line = line.strip()
            if len(line) > 0:
                keyphrases = [phrase.strip() for phrase in line.split(",") if len(phrase.strip()) > 0]
                if len(keyphrases) > 0:
                    keyphrases_list.append(keyphrases)

        if len(keyphrases_list) <= 0:
            raise Exception("❌ File does not contain valid keyphrases")

        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["excluded"].extend(keyphrases_list)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_excluded_float_text(f"✅ Successfully added <b>{len(keyphrases_list)}</b> items from file to exclusions for bump"),
            reply_markup=templ.back_kb(calls.ExcludedBumpItemsPagination(page=last_page).pack())
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_excluded_float_text(e), 
            reply_markup=templ.back_kb(calls.ExcludedBumpItemsPagination(page=last_page).pack())
        )