# ExtractLevelDomain
通过URL抽取各层各级的域名(一级域名,二级域名....) .  这模块本来是用来分析日志及数据分析的.

# Install Document:

pypi install
```
pip install ExtractLevelDomain
```

source install
```
git clone https://github.com/rfyiamcool/ExtractLevelDomain.git
cd ExtractLevelDomain
python setup.py install
```

# Usage Document:

```
import ExtractLevelDomain
filter = ExtractLevelDomain.ExtractLevelDomain()

#普通抽取域名,默认是最多匹配
print filter.parse_url('http://dmp.301.xiaorui.cc/redirect/xiaorui.cc')

#parse_url_level可以控制level级,可接收的参数两种参数 1 2 3 或"*"
print filter.parse_url_level('http://dmp.301.xiaorui.cc/redirect/xiaorui.cc',level=2)

#set_level设置level级别
filter.set_level(1)

print filter.parse_url_level('http://dmp.301.xiaorui.cc/redirect/xiaorui.cc',level=1)

#现实Level级别
print filter.level
```
