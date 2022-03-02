from openpyxl import load_workbook


bd = load_workbook('database.xlsx')
stickers_page = bd['Stickers']

stickers = {}

for row in range(2, stickers_page.max_row + 1):
    keyword = stickers_page.cell(row=row, column=1).value
    sticker_id = stickers_page.cell(row=row, column=2).value
    stickers[keyword] = sticker_id


if __name__ == '__main__':
    print(stickers)
    