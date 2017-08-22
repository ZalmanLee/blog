Title:排序：插入排序（python）
Date:2016-06-25 1:40
Tags:python,algorithm
Slug:python_insert_sort

排序：插入排序（python）
####################

    #!python
    def insert_sort(array):
        for i in xrange(1, len(array)):
            x = array[i]
            while i and array[i-1] < x:
                array[i] = array[i-1]
                i = i - 1
            array[i] = x
        return array

    print insert_sort([2, 9, 4, 6, 7])