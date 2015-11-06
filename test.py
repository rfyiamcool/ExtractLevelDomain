import ExtractLevelDomain
filter = ExtractLevelDomain.ExtractLevelDomain()
print filter.level
print filter.parse_url('http://dmp.301.xiaorui.cc/redirect/xiaorui.cc')
print filter.parse_url_level('http://dmp.301.xiaorui.cc/redirect/xiaorui.cc',level=2)
filter.set_level(1)
print filter.parse_url_level('http://dmp.301.xiaorui.cc/redirect/xiaorui.cc',level=1)
print filter.level
