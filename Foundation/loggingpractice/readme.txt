基本元素说明:
Logger: 用于输出的日志的总对象
Handlers: 用来指定log的输出方式
Formatters: 设置日志信息的结构和内容格式, 默认的时间格式为%Y-%m-%d %H:%M:%S
Filter: 过滤器, 用来过滤的输出内容

常用函数:
logger = logging.getLogger('django')
logger.setLevel(lel)
logger.addFilter(filter)、logger.removeFilter(filter)
logger.addHandler(handler)、logger.removeHandler(handler)
logger.log("debug", "This is a bug")

























