from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from settings import Settings as set

from .. import templates as templ
from .. import states
from .. import callback_datas as calls
from ..helpful import throw_float_message


router = Router()


@router.message(states.AutoDeliveriesStates.waiting_for_page, F.text)
async def handler_waiting_for_auto_deliveries_page(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        if not message.text.isdigit():
            raise Exception('❌ You must enter a numeric value')
        
        page = int(message.text) - 1
        await state.update_data(last_page=page)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_delivs_float_text(f"📃 Enter the page number to go to:"),
            reply_markup=templ.settings_delivs_kb(page)
        )
    except Exception as e:
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_delivs_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
        )


@router.message(states.AutoDeliveryStates.waiting_for_new_auto_delivery_keyphrases, F.text)
async def handler_waiting_for_new_auto_delivery_keyphrases(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        
        if len(message.text) <= 0:
            raise Exception('❌ Value too short')
        
        keyphrases = [phrase.strip() for phrase in message.text.split(",")]
        
        await state.update_data(new_auto_delivery_keyphrases=keyphrases)
        await state.set_state(states.AutoDeliveryStates.waiting_for_auto_delivery_piece)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_float_text(f"🛒 Select <b>auto-delivery type</b>:"),
            reply_markup=templ.settings_new_deliv_piece_kb(last_page)
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
        )
        

@router.message(states.AutoDeliveryStates.waiting_for_new_auto_delivery_message, F.text)
async def handler_waiting_for_new_auto_delivery_message(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        
        if len(message.text) <= 0:
            raise Exception('❌ Value too short')

        await state.update_data(new_auto_delivery_message=message.text)
        
        keyphrases = data.get("new_auto_delivery_keyphrases")
        phrases = "</code>, <code>".join(keyphrases)
        msg = message.text
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_float_text(
                f"✔️ Confirm <b>adding auto-issue</b>:"
                f"\n<b>· Key phrases:</b> <code>{phrases}</code>"
                f"\n<b>· Issue type:</b> Message"
                f"\n<b>· Message:</b> {msg}"
            ),
            reply_markup=templ.confirm_kb(
                confirm_cb="add_new_auto_delivery", 
                cancel_cb=calls.AutoDeliveriesPagination(page=last_page).pack()
            )
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
        )
        

@router.message(states.AutoDeliveryStates.waiting_for_new_auto_delivery_goods, F.text | F.document)
async def handler_waiting_for_new_auto_delivery_goods(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        
        if message.text:
            if len(message.text.strip()) == 0:
                raise Exception('❌ Value too short')

            goods = [g.strip() for g in message.text.splitlines() if g.strip()]
        elif message.document:
            file = await message.bot.get_file(message.document.file_id)
            file_bytes = await message.bot.download_file(file.file_path)
            content = file_bytes.read().decode("utf-8", errors="ignore")

            if len(content.strip()) == 0:
                raise Exception('❌ File is empty')

            goods = [g.strip() for g in content.splitlines() if g.strip()]
        else:
            raise Exception('❌ Send text or file')
        
        if not goods:
            raise Exception('❌ Failed to retrieve products')
        
        await state.update_data(new_auto_delivery_goods=goods)
        
        keyphrases = data.get("new_auto_delivery_keyphrases")
        phrases = "</code>, <code>".join(keyphrases)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_float_text(
                f"✔️ Confirm <b>adding auto-issue</b>:"
                f"\n<b>· Key phrases:</b> <code>{phrases}</code>"
                f"\n<b>· Issue type:</b> Piece"
                f"\n<b>· Goods:</b> {len(goods)} pcs."
            ),
            reply_markup=templ.confirm_kb(
                confirm_cb="add_new_auto_delivery", 
                cancel_cb=calls.AutoDeliveriesPagination(page=last_page).pack()
            )
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveriesPagination(page=last_page).pack())
        )


@router.message(states.AutoDeliveryStates.waiting_for_auto_delivery_keyphrases, F.text)
async def handler_waiting_for_auto_delivery_keyphrases(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        data = await state.get_data()
        index = data.get("auto_delivery_index")

        if len(message.text) <= 0:
            raise Exception('❌ Value too short')
        
        auto_deliveries = sett.get("auto_deliveries")
        keyphrases = [phrase.strip() for phrase in message.text.split(",")]
        auto_deliveries[index]["keyphrases"] = keyphrases
        sett.set("auto_deliveries", auto_deliveries)
        
        keyphrases_str = "</code>, <code>".join(keyphrases)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_deliv_page_float_text(f"✅ <b>Keyphrases</b> were successfully changed to: <code>{keyphrases_str}</code>"),
            reply_markup=templ.back_kb(calls.AutoDeliveryPage(index=index).pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_deliv_page_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveryPage(index=index).pack())
        )


@router.message(states.AutoDeliveryStates.waiting_for_auto_delivery_message, F.text)
async def handler_waiting_for_auto_delivery_message(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        data = await state.get_data()
        index = data.get("auto_delivery_index")
        
        if len(message.text) <= 0:
            raise Exception('❌ Text is too short')
        
        auto_deliveries = sett.get("auto_deliveries")
        auto_deliveries[index]["message"] = message.text.splitlines()
        sett.set("auto_deliveries", auto_deliveries)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_deliv_page_float_text(f"✅ <b>Auto-delivery message</b> was successfully changed to: <blockquote>{message.text}</blockquote>"),
            reply_markup=templ.back_kb(calls.AutoDeliveryPage(index=index).pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_deliv_page_float_text(e), 
            reply_markup=templ.back_kb(calls.AutoDeliveryPage(index=index).pack())
        )


@router.message(states.AutoDeliveryStates.waiting_for_auto_delivery_goods_add, F.text | F.document)
async def handler_waiting_for_auto_delivery_goods_add(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        
        data = await state.get_data()
        last_page = data.get("last_page", 0)
        index = data.get("auto_delivery_index")
        
        if message.text:
            if len(message.text.strip()) == 0:
                raise Exception('❌ Value too short')

            goods = [g.strip() for g in message.text.splitlines() if g.strip()]
        elif message.document:
            file = await message.bot.get_file(message.document.file_id)
            file_bytes = await message.bot.download_file(file.file_path)
            content = file_bytes.read().decode("utf-8", errors="ignore")

            if len(content.strip()) == 0:
                raise Exception('❌ File is empty')

            goods = [g.strip() for g in content.splitlines() if g.strip()]
        else:
            raise Exception('❌ Send text or file')
        
        if not goods:
            raise Exception('❌ Failed to retrieve products')
        
        auto_deliveries = sett.get("auto_deliveries")
        auto_deliveries[index]["goods"].extend(goods)
        sett.set("auto_deliveries", auto_deliveries)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_goods_float_text(
                f"✅ <b>{len(goods)} products</b> successfully added to auto-issue"
            ),
            reply_markup=templ.back_kb(calls.DelivGoodsPagination(page=last_page).pack())
        )
    except Exception as e:
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_deliv_goods_float_text(e), 
            reply_markup=templ.back_kb(calls.DelivGoodsPagination(page=last_page).pack())
        )