import os # oprtating system

def read_file(filename):
    products=[]
    with open(filename, 'r', encoding='utf-8') as f: # 打開檔案
        for line in f:
            if '商品, 價格' in line: # 忽略商品價個的if 寫法
                continue # 跳出這次的回圈, 繼續同個迴圈的下個迴圈
            name, price = line.strip().split(',') #換行(strip)+切割(split),
            products.append([name, price])
    return products
 
# 讓使用者輸入
def user_input(products):
    while True:        
        name = input("請輸入商品名稱: ")
        if name == 'q':
            break
        price = input("請輸入商品價格: ")
        products.append([name, price])
        print(products)
        return products

# 印出所有購買紀錄 
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: #打開檔案
        f.write('商品, 價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')  #寫入檔案

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # 尋找檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file(filename)
    else:
        print("找不到檔案")

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
