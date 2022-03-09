from openpyxl import load_workbook


bd = load_workbook('database.xlsx')
stickers_page = bd['Stickers']

stickers = {}
replies = {}

for row in range(2, stickers_page.max_row + 1):
    keyword = stickers_page.cell(row=row, column=1).value
    sticker_id = stickers_page.cell(row=row, column=2).value
    replies[keyword] = stickers_page.cell(row=row, column=3).value
    print(keyword, ':', sticker_id)
    stickers[keyword] = sticker_id
