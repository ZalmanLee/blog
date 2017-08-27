Title:排序：冒泡排序（python）
Date:2016-06-24 9:35
Tags:python,algorithm
Slug:python_bubble_sort

排序：冒泡排序（python）
####################

```python preset=mypreset lineno=True
def bubble_sort(array):
    for i in xrange(1,len(array)):
        for j in xrange(0, len(array) - i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
print bubble_sort([1,4,3,5,7,8,0])
```