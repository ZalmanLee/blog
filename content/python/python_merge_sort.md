Title:排序：归并排序（python）
Date:2016-06-26 0:50
Tags:python,algorithm
Slug:python_merge_sort

排序：归并排序（python）
####################

```python preset=mypreset lineno=True
def merge(l1, l2):
    l = []
    while len(l1) and len(l2):
        if l1[0] < l2[0]:
            l.append(l1[0])
            l1 = l1[1:]
        else:
            l.append(l2[0])
            l2 = l2[1:]
    return l+l1+l2


def merge_sort(array):
    mid = int(len(array)/2)
    if len(array) <= 1:
        return array
    else:
        return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


print merge_sort([3,4,2,6,8,0,2])
```