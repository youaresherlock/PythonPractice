"""
group: 访问每个独立的子组
groups: 获取一个包含所有匹配子组的元组
"""
import re


match_object = re.match(r'(\w\w\w)-(\d\d\d)', 'abc-123')
print(match_object.group(), match_object.groups(), match_object.group(1))
