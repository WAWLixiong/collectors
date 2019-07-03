#已排序的序列处理
# insort是insort_right的别名，另外还有insort_left
# bisect是bisect_right的别名，另外还有bisect_left
from collections import deque

import bisect


#二分查找
#日常项目中用于维护需要维持顺序的序列

# inter_list = []
inter_list = deque()

bisect.insort(inter_list,3)
bisect.insort(inter_list,1)
bisect.insort(inter_list,6)
bisect.insort(inter_list,3)
print(inter_list)

print(bisect.bisect(inter_list,3))
