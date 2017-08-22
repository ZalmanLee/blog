Title:排序：选择排序（python）
Date:2016-06-25 23:52
Tags:python,algorithm
Slug:python_select_sort

排序：选择排序（python）
####################

	#!python
    def select_sort(array):
        for i in xrange(0,len(array)):
            max = array[i]
            max_idx = i
            for j in xrange(i+1,len(array)):
                if max < array[j]:
                    max = array[j]
                    max_idx = j
            array[i],array[max_idx] = array[max_idx],array[i]
        return array

    print select_sort([3,6,8,1,4,7,4,0])