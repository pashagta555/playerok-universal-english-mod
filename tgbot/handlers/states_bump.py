Here is the translation of the provided Python code to English:

```
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from settings import Settings as sett

from .. import templates as templ
from .. import callback_datas as calls
from .. import states
from ..helpful import throw_float_message


router = Router()


@router.message(states.BumpItemsStates.waiting_for_bump_items_interval, F.text)
async def handler_waiting_for_bump_items_interval(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)

        if not message.text.isdigit():
            raise Exception("❌ You should enter a numeric value")
        if int(message.text) <= 0:
            raise Exception("❌ Too low value")

        interval = int(message.text)

        config = sett.get("config")
        config["playerok"]["auto_bump_items"]["interval"] = interval
        sett.set("config", config)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_bump_float_text(f"✅ The interval for bumping items has been successfully changed to <b>{interval}</b>"),
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

        if len(message.text) <= 0:
            raise Exception("❌ Too short value")

        keyphrases = [phrase.strip() for phrase in message.text.split(",") if phrase.strip()]

        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["included"].append(keyphrases)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_included_float_text(f"✅ The item with key phrases <code>{'</code>, <code>'.join(keyphrases)}</code> has been successfully included in bumping"),
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
                keyphrases = [phrase.strip() for phrase in line.split(",") if phrase.strip()]
                if len(keyphrases) > 0:
                    keyphrases_list.append(keyphrases)

        if len(keyphrases_list) <= 0:
            raise Exception("❌ The file does not contain valid key phrases")

        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["included"].extend(keyphrases_list)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_included_float_text(f"✅ Successfully included <b>{len(keyphrases_list)}</b> items from the file in bumping"),
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

        if len(message.text) <= 0:
            raise Exception("❌ Too short value")

        keyphrases = [phrase.strip() for phrase in message.text.split(",") if phrase.strip()]

        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["excluded"].append(keyphrases)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_excluded_float_text(f"✅ The item with key phrases <code>{'</code>, <code>'.join(keyphrases)}</code> has been successfully added to the exclusions for bumping"),
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
                keyphrases = [phrase.strip() for phrase in line.split(",") if phrase.strip()]
                if len(keyphrases) > 0:
                    keyphrases_list.append(keyphrases)

        if len(keyphrases_list) <= 0:
            raise Exception("❌ The file does not contain valid key phrases")

        auto_bump_items = sett.get("auto_bump_items")
        auto_bump_items["excluded"].extend(keyphrases_list)
        sett.set("auto_bump_items", auto_bump_items)

        data = await state.get_data()
        last_page = data.get("last_page", 0)

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_bump_excluded_float_text(f"✅ Successfully added <b>{len(keyphrases_list)}</b> items from the file to the exclusions for bumping"),
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
```

The provided Python code is used to handle messages in an AIogram bot. The `handler_waiting_for_bump_items_interval`, `handler_waiting_for_new_included_bump_item_keyphrases`, `handler_waiting_for_new_excluded_bump_item_keyphrases`, and other handlers are responsible for processing different types of messages, such as integer values for setting an interval for bumping items or text values for adding key phrases to included or excluded lists. The code also includes error handling using the `try`-`except` block to handle any exceptions that may occur during message processing.

The translation from Russian to English is provided below:

* ❌ You should enter a numeric value
* ❌ Too low value
* ✅ The item with key phrases <code>{'</code>, <code>'.join(keyphrases)}</code> has been successfully included in bumping
* ✅ Successfully included <b>{len(keyphrases_list)}</b> items from the file in bumping
* ✅ The item with key phrases <code>{'</code>, <code>'.join(keyphrases)}</code> has been successfully added to the exclusions for bumping
* ✅ Successfully added <b>{len(keyphrases_list)}</b> items from the file to the exclusions for bumping

