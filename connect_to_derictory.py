from openpyxl import load_workbook


def insert_users(user_id=None, name=None, sex=None, grade=None):
    row = users_page.max_row + 1
    stickers_page.cell(row=row, column=1).value = user_id
    stickers_page.cell(row=row, column=2).value = name
    stickers_page.cell(row=row, column=3).value = sex
    stickers_page.cell(row=row, column=4).value = grade
    bd.save(database_filename)
    users[user_id] = user_id
    replies[keyword] = reply_text


def insert_sticker(keyword=None, sticker_id=None, reply_text=None):
    row = stickers_page.max_row + 1
    stickers_page.cell(row=row, column=1).value = keyword
    stickers_page.cell(row=row, column=2).value = sticker_id
    stickers_page.cell(row=row, column=3).value = reply_text
    bd.save(database_filename)
    stickers[keyword] = sticker_id
    replies[keyword] = reply_text


def in_database(user: int) -> bool:
    """
    Возвращает True, если id пользователя есть в БД
    """
    for row in range(2, users_page.max_row + 1):
        if user == users_page.cell(row=row, column=1).value:
            return True
        return False


database_filename = 'database.xlsx'
bd = load_workbook(database_filename)
stickers_page = bd['Stickers']
users_page = bd['Users']

users = {}
stickers = {}
replies = {}

for row in range(2, stickers_page.max_row + 1):
    keyword = stickers_page.cell(row=row, column=1).value
    sticker_id = stickers_page.cell(row=row, column=2).value
    reply_text = stickers_page.cell(row=row, column=3).value
    stickers[keyword] = sticker_id
    replies[keyword] = reply_text
