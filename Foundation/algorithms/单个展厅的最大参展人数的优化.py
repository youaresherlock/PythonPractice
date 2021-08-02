#!/usr/bin/python# -*- coding:utf-8 -*-import timeimport randomimport functoolsfrom typing import Listdef log_time_for_n_step(steps: int) -> "a decorator simple factory":    """    装饰器工厂函数，计算不同执行steps次的执行时间    :param steps: 需要执行的steps    :return:    """    if not Solution.cache:        for i in range(1):            nums = [random.randint(1, 10 ** 5) for _ in range(random.randint(1, 10 ** 5))]            cnt = random.randint(0, 10 ** 10)            Solution.cache[i] = (nums, cnt)    def decorator(f: "builtin function or method"):        """        :param f: callable object        :return: a same callable object like f        """        @functools.wraps(f)        def inner(self):            start = time.time()            for j in range(steps):                nums_input, cnt_input = Solution.cache[j]                result = f(self, nums_input, cnt_input)                print(f"final limit in {f.__name__}: {result}")            end = time.time()            print(f"run time in {f.__name__}: {end - start}")        return inner    return decoratorclass Solution:    cache = dict()    def __init__(self):        self.sorted_set_nums = None        self.counter = None        """        key value         value表示nums中 >= key的个数        """        self.mapping = None        """        min 表示limit可能的最小值        max 表示limit可能的最大值        limit 表示limit的确定值        """        self.limit_mapping = {            'min': 0,            'max': 0,            'limit': None        }    def init(self, nums_input: List[int]):        """        O(n)复杂度初始化实例变量        :param nums_input:        :return:        """        self.counter = [-1] * (max(nums_input) + 1)        self.sorted_set_nums = sorted(set(nums_input))        self.mapping = dict.fromkeys(self.sorted_set_nums, 0)        sorted_num = sorted(nums_input)        before_num = 0        before_numbers = 0        current_numbers = 0        for index, value in enumerate(sorted_num):            if before_num != value:                before_numbers = current_numbers                before_num = value            current_numbers += value            self.mapping[value] += 1            self.counter[value] = before_numbers        count = 0        length = len(nums_input)        for key, value in self.mapping.items():            self.mapping[key] = length - count            count += value    @staticmethod    def check_limit(nums_input: List[int], cnt_input: int) -> bool:        """        判断是否要限制参展人数        :param nums_input:        :param cnt_input:        :return:        """        count = sum(nums_input)        return count > cnt_input    def compute_number(self, limit: int) -> int:        """        给定limit,计算参展总人数        :param limit: 当前的每个展厅参展限制人数limit        :return: people count when the limit shows like that        """        if self.counter[limit] != -1:            people_count = self.counter[limit] + self.mapping[limit] * limit            return people_count        count = 0        for key, value in self.mapping.items():            if key > limit:                count = key                break        return self.counter[count] + self.mapping[count] * limit    def find_limit(self, cnt_input) -> int:        """        找到合适的limit        :param cnt_input:        :return:        """        if self.limit_mapping['limit']:            return self.limit_mapping['limit']        index = self.limit_mapping['min'] + 1        while index <= self.limit_mapping['max']:            if self.compute_number(index) <= cnt_input:                self.limit_mapping['min'] = index                index += 1            else:                break        return self.limit_mapping['min']    def binary_search(self, cnt_input: int):        """        使用二分查找合适的limit范围        :param cnt_input:        :return:        """        left, right = 0, max(self.sorted_set_nums)        while left <= right:            mid = left + (right - left) // 2            people = self.compute_number(mid)            if people < cnt_input:                self.limit_mapping['limit'] = mid                left = mid + 1            if people == cnt_input:                self.limit_mapping['limit'] = mid                break            if people > cnt_input:                right = mid - 1@log_time_for_n_step(1)def manage_tourists(self, nums_input: List[int], cnt_input: int) -> int:    """    未优化前，只做了快速查询某个limit限制下所有的参展人数是多少,复杂度O(1)    总体时间复杂度O(n)    :param nums_input:    :param cnt_input:    :return:    """    if not self.check_limit(nums_input, cnt_input):        return -1    self.init(nums_input)    for item in self.sorted_set_nums:        """        先找出min, max的可能的值，然后去逐个查找        """        people = self.compute_number(item)        if people < cnt_input:            self.limit_mapping['min'] = item        if people == cnt_input:            self.limit_mapping['limit'] = item        if people > cnt_input:            self.limit_mapping['max'] = item - 1            break    print('limit_mapping:', self.limit_mapping)    return self.find_limit(cnt_input)@log_time_for_n_step(1)def manage_tourists_optimization(self, nums_input: List[int], cnt_input: int) -> int:    """    优化后    快速查询某个limit限制下所有的参展人数是多少,复杂度O(1)    快速使用二分查找limit可能的范围    总体时间复杂度 O(log2^n)    :param nums_input:    :param cnt_input:    :return:    """    if not self.check_limit(nums_input, cnt_input):        return -1    self.init(nums_input)    self.binary_search(cnt_input)    print('limit_mapping:', self.limit_mapping)    return self.limit_mapping['limit']def init():    setattr(Solution, manage_tourists.__name__, manage_tourists)    setattr(Solution, manage_tourists_optimization.__name__, manage_tourists_optimization)if __name__ == '__main__':    # nums = [1, 4, 2, 5, 5, 1, 6]    # cnt = 13    init()    solution = Solution()    solution.manage_tourists()    solution = Solution()    solution.manage_tourists_optimization()