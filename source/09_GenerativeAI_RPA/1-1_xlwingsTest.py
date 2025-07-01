import xlwings as xw

# 현재 열린 엑셀 파일 데이터 가져옴
wb = xw.apps.active.books.active
sheet = wb.sheets.active
print('데이터 가져와 연산 수행')
b1 = sheet.range('B1').value
b2 = sheet.range('B2').value
# b1-b2값을 'B3'셀에 넣기
sheet.range('B3').value = b1-b2
print("연산결과 쓰기 완료")
