#!usr/bin/python
# -*- coding:utf8 -*-

a = {"bobby1": {"company": "imooc"},
     "bobby2": {"company": "imooc2"}}

# clear 清空所有项Remove all items from D
# a.clear()
# print(a)

# copy 返回浅拷贝
new_dict = a.copy()
new_dict["bobby1"]["company"] = "imooc3"
print(new_dict, a)

# 深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict["bobby1"]["company"] = "imooc3"
print(new_dict, a)

# fromkeys
new_list = ["bobby1", "bobby2"]
new_dict = dict.fromkeys(new_list, {"company": "imooc"})
print(new_dict)

# get
value = new_dict.get("bobby1", {})

for key, value in new_dict.items():
    print(new_dict)

default_value = new_dict.setdefault("bobby", "imooc")
print(default_value)

# update()
# new_dict.update({"bobby": "imooc"})
# new_dict.update(bobby="imooc", bobby1="imooc")
# new_dict.update([("bobby", "imooc")])























