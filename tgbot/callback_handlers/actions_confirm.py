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


@router.callback_query(F.data == "confirm_bump_items")
async def callback_confirm_bump_items(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await throw_float_message(
        state=state,
        message=callback.message, 
        text=templ.events_float_text("⬆️✔️ Confirm <b>item bumping</b> ↓"), 
        reply_markup=templ.confirm_kb("bump_items", calls.MenuNavigation(to="events").pack())
    )


@router.callback_query(F.data == "confirm_withdrawal")
async def callback_confirm_withdrawal(callback: CallbackQuery, state: FSMContext):
    await state.set_state(None)
    await throw_float_message(
        state=state,
        message=callback.message, 
        text=templ.events_float_text("💸✔️ Confirm <b>fund withdrawal</b> ↓"), 
        reply_markup=templ.confirm_kb("request_withdrawal", calls.MenuNavigation(to="events").pack())
    )