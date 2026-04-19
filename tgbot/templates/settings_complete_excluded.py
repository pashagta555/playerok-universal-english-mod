I'll translate the text to English, keeping the code unchanged. Here are the translations:

1. `settings_complete_excluded_text()`:
```python
def settings_complete_excluded_text():
    excluded_complete_deals = sett.get("auto_complete_deals").get("excluded")
    txt = textwrap.dedent(f"""
        <b>☑️➖ Excluded</b>

        Total of <b>{len(excluded_complete_deals)}</b> excluded items:
    """)
    return txt
```

2. `settings_complete_excluded_kb(page=0)`:
```python
def settings_complete_excluded_kb(page=0):
    excluded_complete_deals: list[list] = sett.get("auto_complete_deals").get("excluded")
    
    rows = []
    items_per_page = 7
    total_pages = math.ceil(len(excluded_complete_deals) / items_per_page)
    total_pages = total_pages if total_pages > 0 else 1

    if page < 0: page = 0
    elif page >= total_pages: page = total_pages - 1

    start_offset = page * items_per_page
    end_offset = start_offset + items_per_page

    for keyphrases in list(excluded_complete_deals)[start_offset:end_offset]:
        keyphrases_frmtd = ", ".join(keyphrases) or "❌ Not specified"
        rows.append([
            InlineKeyboardButton(text=f"{keyphrases_frmtd}", callback_data="123"),
            InlineKeyboardButton(text=f"🗑️", callback_data=calls.DeleteExcludedCompleteDeal(index=excluded_complete_deals.index(keyphrases)).pack()),
        ])

    if total_pages > 1:
        buttons_row = []
        btn_back = InlineKeyboardButton(text="←", callback_data=calls.ExcludedCompleteDealsPagination(page=page-1).pack()) if page > 0 else InlineKeyboardButton(text="🛑", callback_data="123")
        buttons_row.append(btn_back)
        
        btn_pages = InlineKeyboardButton(text=f"{page+1}/{total_pages}", callback_data="enter_messages_page")
        buttons_row.append(btn_pages)

        btn_next = InlineKeyboardButton(text="→", callback_data=calls.ExcludedCompleteDealsPagination(page=page+1).pack()) if page < total_pages - 1 else InlineKeyboardButton(text="🛑", callback_data="123")
        buttons_row.append(btn_next)
        rows.append(buttons_row)

    rows.append([
        InlineKeyboardButton(text="➕ Add", callback_data="enter_new_excluded_complete_deal_keyphrases"),
        InlineKeyboardButton(text="➕📄 Add many", callback_data="send_new_excluded_complete_deals_keyphrases_file"),
    ])
    rows.append([
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="complete").pack()),
    ])

    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb
```

3. `settings_complete_excluded_float_text(placeholder: str)`:
```python
def settings_complete_excluded_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>☑️➖ Excluded</b>
        \n{placeholder}
    """)
    return txt
```

4. `settings_new_complete_excluded_float_text(placeholder: str)`:
```python
def settings_new_complete_excluded_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>☑️➖ Adding excluded item</b>
        \n{placeholder}
    """)
    return txt
```

Note that I've translated the text to English, but kept the code unchanged. If you have any further requests or questions, feel free to ask!

