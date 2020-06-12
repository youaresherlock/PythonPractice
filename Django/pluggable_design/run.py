# 启动文件

import setting  # 将配置文件导进来
import importlib  # 将这个模块导入


def run(content):
    # 循环settings配置文件里的类的模块列表
    '''
    FUNC_LIST  = [
    'msg_bag.phone.Phone',
    'msg_bag.qq.QQ',
    'msg_bag.wechat.Wechat',
    '''
    for func in setting.FUNC_LIST:
        # 将每一个字符串拿出来，然后根据.切割，从末尾切割一个
        model, class_name = func.rsplit('.', maxsplit=1)
        print(model)  # msg_bag.phone \ msg_bag.qq \ msg_bag.wechat
        print(class_name)  # Phone \ QQ \ Wechat

        # 利用importlib模块
        mod = importlib.import_module(model)
        '''
         等同于 
         from msg_bag import phone
         from msg_bag import qq
         from msg_bag import wechat
        '''

        # 通过反射class_name是不是mod的类，然后取值赋给class_obj
        class_obj = getattr(mod, class_name)

        # 通过类去调用对象的绑定方法，将类自己传给send_msg
        class_obj.send_msg(class_obj, content)


run('开开心心')