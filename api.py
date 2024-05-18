import requests  # 导入发送 HTTP 请求的库
import random  # 导入生成随机数的库
import json  # 导入处理 JSON 数据的库
import os  # 导入操作文件系统的库
import sys  # 导入操作系统参数的库
from hashlib import md5  # 导入 MD5 哈希函数


# 检查命令行参数是否正确
if len(sys.argv) != 2:
    print("usage: python {} <image>".format(sys.argv[0]))
    exit(-1)

file_name = sys.argv[1]  # 获取图片文件名

endpoint = 'http://api.fanyi.baidu.com'  # 百度翻译 API 地址
path = '/api/trans/sdk/picture'  # 图片翻译 API 路径
url = endpoint + path  # 拼接完整的请求 URL

#常用语言：auto自动识别；zh中文；en英语；jp日语；这里以日语翻译中文为例
from_lang = 'jp'  # 原始语言
to_lang = 'zh'  # 目标语言

# 设置应用程序 ID 和密钥
app_id = ''
app_key = ''

# 定义设备 ID 和 MAC 地址
cuid = 'APICUID'
mac = 'mac'

# 生成 MD5 哈希值的函数
def get_md5(string, encoding='utf-8'):
    return md5(string.encode(encoding)).hexdigest()

# 计算文件的 MD5 哈希值
def get_file_md5(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        return md5(data).hexdigest()

# 生成随机数和签名
salt = random.randint(32768, 65536)
sign = get_md5(app_id + get_file_md5(file_name) + str(salt) + cuid + mac + app_key)

# 构建请求参数
payload = {'from': from_lang, 'to': to_lang, 'appid': app_id, 'salt': salt, 'sign': sign, 'cuid': cuid, 'mac': mac}
image = {'image': (os.path.basename(file_name), open(file_name, 'rb'), "multipart/form-data")}

# 发送请求
response = requests.post(url, params=payload, files=image)
result = response.json()  # 解析响应结果为 JSON 格式

# 打印响应结果
# print(json.dumps(result, indent=4, ensure_ascii=False))


# 直接访问字典中的键来获取所需的信息
sum_dst = result['data']['sumDst']
chinese_content = sum_dst.strip('“”')  # 去除双引号

# 保留历史记录方便查看
print(chinese_content)