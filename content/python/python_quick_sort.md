Title:排序：快速排序（python）
Date:2016-06-24 4:59
Tags:python,algorithm
Slug:python_quick_sort

排序：快速排序（python）
####################

    #!python
    def quick_sort(array):
        if len(array) <= 1:
            return array
        leftArr = []
        rightArr = []
        val = array.pop()
        for x in array:
            if x < val:
                leftArr.append(x)
            else:
                rightArr.append(x)
        return quick_sort(leftArr) + [val] + quick_sort(rightArr)

    nums = [4,1,5,6,8,2]
    print quick_sort(nums)