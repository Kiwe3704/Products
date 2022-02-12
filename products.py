#讀取檔案
products=[]
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        name, price = line.strip().split(',') #換行(strip)+切割(split),
        products.append([name, price])
print(products)


while True:
  name = input("請輸入商品名稱: ")
  if name == 'q':
      break
  price = input("請輸入商品價格: ")
  products.append([name, price])
print(products)
 
for p in products:
     print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f: #打開檔案
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')  #寫入檔案
