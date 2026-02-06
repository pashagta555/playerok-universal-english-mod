from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from settings import Settings as sett

from .. import templates as templ
from .. import states
from .. import callback_datas as calls
from ..helpful import throw_float_message


router = Router()


@router.message(states.CustomCommandsStates.waiting_for_page, F.text)
async def handler_waiting_for_custom_commands_page(message: types.Message, state: FSMContext):
    try: 
        await state.set_state(None)
        if not message.text.strip().isdigit():
            raise Exception("❌ You must enter a numeric value")
        
        await state.update_data(last_page=int(message.text.strip())-1)
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_comms_text(),
            reply_markup=templ.settings_comms_kb(page=int(message.text)-1)
        )
    except Exception as e:
        data = await state.get_data()
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_comms_float_text(e), 
            reply_markup=templ.back_kb(calls.CustomCommandsPagination(page=data.get("last_page", 0)).pack())
        )
        
        
@router.message(states.CustomCommandsStates.waiting_for_new_custom_command, F.text)
async def handler_waiting_for_new_custom_command(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if len(message.text.strip()) <= 0 or len(message.text.strip()) >= 32:
            raise Exception("❌ The command is too short or too long")

        data = await state.get_data()
        await state.update_data(new_custom_command=message.text.strip())
        await state.set_state(states.CustomCommandsStates.waiting_for_new_custom_command_answer)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_comm_float_text(f"💬 Enter <b>a reply for the command</b> <code>{message.text.strip()}</code> ↓"),
            reply_markup=templ.back_kb(calls.CustomCommandsPagination(page=data.get("last_page", 0)).pack())
        )
    except Exception as e:
        data = await state.get_data()
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_comm_float_text(e), 
            reply_markup=templ.back_kb(calls.CustomCommandsPagination(page=data.get("last_page", 0)).pack())
        )
        
        
@router.message(states.CustomCommandsStates.waiting_for_new_custom_command_answer, F.text)
async def handler_waiting_for_new_custom_command_answer(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if len(message.text.strip()) <= 0:
            raise Exception("❌ The reply is too short")

        data = await state.get_data()
        await state.update_data(new_custom_command_answer=message.text.strip())
        
        cmd = data.get("new_custom_command")
        answr = message.text.strip()

        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_comm_float_text(
                f"✔️ Confirm <b>adding a new command:</b>"
                f"\n<b>· Command:</b> {cmd}"
                f"\n<b>· Reply:</b> <blockquote>{answr}</blockquote>"
            ),
            reply_markup=templ.confirm_kb(confirm_cb="add_new_custom_command", cancel_cb=calls.CustomCommandsPagination(page=data.get("last_page", 0)).pack())
        )
    except Exception as e:
        data = await state.get_data()
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_new_comm_float_text(e), 
            reply_markup=templ.back_kb(calls.CustomCommandsPagination(page=data.get("last_page", 0)).pack())
        )


@router.message(states.CustomCommandsStates.waiting_for_custom_command_answer, F.text)
async def handler_waiting_for_custom_command_answer(message: types.Message, state: FSMContext):
    try:
        await state.set_state(None)
        if len(message.text.strip()) <= 0:
            raise Exception("❌ The text is too short")

        data = await state.get_data()
        custom_commands = sett.get("custom_commands")
        custom_commands[data["custom_command"]] = message.text.strip().split('\n')
        sett.set("custom_commands", custom_commands)
        
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_comm_page_float_text(f"✅ <b>The reply text</b> for the command <code>{data['custom_command']}</code> has been successfully changed to: <blockquote>{message.text.strip()}</blockquote>"),
            reply_markup=templ.back_kb(calls.CustomCommandPage(command=data["custom_command"]).pack())
        )
    except Exception as e:
        data = await state.get_data()
        await throw_float_message(
            state=state,
            message=message,
            text=templ.settings_comm_page_float_text(e), 
            reply_markup=templ.back_kb(calls.CustomCommandPage(command=data["custom_command"]).pack())
        )