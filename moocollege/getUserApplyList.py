import requests
import openpyxl

authorization = 'your_authorization',
baggage = 'your_baggage',
cookie = 'your_cookie'


url = 'https://cc.moocollege.com/api/web/user/getUserApplyList'

proxy = {
    'http': 'http://your_proxy_ip:your_proxy_port',
    'https': 'https://your_proxy_ip:your_proxy_port'
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
    "Authorization" : authorization,
    "Baggage" : baggage,
    "Cookie" : cookie,
    'Content-Type': 'application/json',
    'Origin': 'https://cc.moocollege.com',
    'Referer': 'https://cc.moocollege.com//',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0'
}

try:
    workbook = openpyxl.load_workbook("data.xlsx")
except FileNotFoundError:
    workbook = openpyxl.Workbook()

worksheet = workbook.active

worksheet.append(['ID', 'ID Card Name', 'Academy', 'Email', 'Login Phone Number', 'Major', 'Labels', 'School', 'Belong School', 'Login Name', 'Status', 'Create Time'])


for pageNum in range(1, 50): # Modify based on total quantity
    payload = {"pageNum": pageNum, "pageSize": 20, "tag": ""}
    response = requests.post(url=url, headers=headers, json=payload)
    data = response.json()

    print(data)
    list_data = data['data']['list']
    
    print(list_data)
    
    for item in list_data:
        row_data = [
            item['id'],
            item['idcardName'],
            item['academy'],
            item['email'],
            item['loginPhoneNumber'],
            item['major'],
            item['labels'],
            item['school'],
            item['belongSchool'],
            item['loginName'],
            item['status'],
            item['createTime']
        ]
        worksheet.append(row_data)

    workbook.save("data.xlsx")

print("Completed!")
