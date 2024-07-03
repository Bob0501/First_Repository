#十大基本排序算法综合（升序）
#1. 选择排序
'''
选择排序(Selection sort)是不稳定的排序方法,
每一次从待排序的数据元素中选出最小(或最大)的一个元素，
存放在序列的起始位置，直到全部待排序的数据元素排完。
'''
def SelectionSort(lists):
    for i in range(len(lists)-1):
        mini=i
        for j in range(i+1,len(lists)):
            if lists[j]<lists[mini]:
                mini=j
        lists[mini],lists[i]=lists[i],lists[mini]
    return lists
def SelectionSort1(lists):
    for i in range(len(lists)-1):
        mini=i
        for j in range(i+1,len(lists)):
            if lists[j]<lists[mini]:
                mini=j
        if mini!=i:
            lists[mini],lists[i]=lists[i],lists[mini]
    return lists
#2. 冒泡排序
'''
冒泡排序（BubbleSort）
重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。
'''
def BubbleSort(lists):
    for i in range(len(lists)-1):
        for j in range(len(lists)-i-1):
            if lists[j]>lists[j+1]:
                lists[j],lists[j+1]=lists[j+1],lists[j]
    return lists
def BubbleSort1(lists):
    i=0;flag=True
    while i<len(lists)-1 and flag:
        flag=False
        for j in range(len(lists)-i-1):
            if lists[j]>lists[j+1]:
                lists[j],lists[j+1]=lists[j+1],lists[j]
                flag=True
        i+=1
    return lists
#3. 快速排序
'''
快速排序(Quicksort)是对冒泡排序的一种改进。
通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，
以此达到整个数据变成有序序列。
'''
def QuickSort(lists,left,right):
    if left>=right:
        return lists
    key=lists[left];low=left;high=right
    while left<right:
        while left<right and lists[right]>=key:
            right-=1
        lists[left]=lists[right]
        while left<right and lists[left]<=key:
            left+=1
        lists[right]=lists[left]
        lists[left]=key
    QuickSort(lists, low, left-1)
    QuickSort(lists, left+1, high)
    return lists
def QuickSort1(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot] 
    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]
    return QuickSort1(left) + [pivot] + QuickSort1(right)
def QuickSort2(nums, left, right):
    def partition(nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot #nums[right] = pivot 亦可
        return left  #return right 亦可
    if left < right:
        pivotIndex = partition(nums, left, right)
        QuickSort2(nums, left, pivotIndex - 1)
        QuickSort2(nums, pivotIndex + 1, right)
    return nums
def QuickSort3(lists):
    if len(lists)<=1:
        return lists
    key=lists[0];left=0;right=len(lists)-1
    while left<right:
        while left<right and lists[right]>=key:
            right-=1
        lists[left]=lists[right]
        while left<right and lists[left]<=key:
            left+=1
        lists[right]=lists[left]
        lists[left]=key
    lists=QuickSort3(lists[:left])+lists[left:]
    lists=lists[:left+1]+QuickSort3(lists[left+1:])
    return lists
#4. 插入排序
'''
插入排序(InsertionSort)
每步将一个待排序的纪录，
按其关键码值的大小插入前面已经排序的文件中适当位置上，
直到全部插入完为止。
'''
def InsertionSort(lists):
    for i in range(len(lists)):
        num=lists[i];k=i
        for j in range(i-1,-1,-1):
            if lists[j]>num:
                lists[j+1]=lists[j]
                k=j
        lists[k]=num
    return lists
def InsertionSort1(lists):
    for i in range(1,len(lists)):
        for j in range(i,0,-1):
            if lists[j]<lists[j-1]:
                lists[j],lists[j-1]=lists[j-1],lists[j]
            else:
                break
    return lists
def InsertionSort2(lists):
    for i in range(1,len(lists)):
        num=lists[i];j=i-1
        while j>=0 and lists[j]>num:
            lists[j+1]=lists[j]
            j-=1
        lists[j+1]=num
    return lists
'''
def InsertionSort_N_(lists):
    #利用更快速的查找算法找到插入位置
'''
#5. 希尔排序
def ShellSort(arr):
    gap=len(arr) // 2
    while gap>0:
        for i in range(gap,len(arr)):
            for j in range(i,gap-1,-gap):
                if arr[j]<arr[j-gap]:
                    arr[j]=arr[j-gap]
        gap//=2
    return arr
def shellSort1(nums):
    lens = len(nums)
    gap = 1  
    while gap < lens // 3:
        gap=gap*3+1
    while gap > 0:
        for i in range(gap, lens):
            cur, preIndex = nums[i], i - gap
            while preIndex >= 0 and cur < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex]
                preIndex -= gap
            nums[preIndex + gap] = cur
        gap //= 3
    return nums
#6. 归并排序
'''
归并排序(MergeSort)
是建立在归并操作上的一种有效，稳定的排序算法，
该算法是采用分治法(Divide and Conquer)的一个非常典型的应用。
将已有序的子序列合并，得到完全有序的序列;即先使每个子序列有序，
再使子序列段间有序。
'''
def MergeSort(arr):
    if len(arr) == 1:
        return arr
    def merge(left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        result += right
        return result
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(MergeSort(left), MergeSort(right))
#7. 基数排序
'''
'''
def LSD_RadixSort(arr):
    x=len(str(max(arr)));mod=10
    for i in range(x):
        buskets=[[] for k in range(mod)]
        for j in arr:
            buskets[j//(10**i)%mod].append(j)
        arr=[num for busket in buskets for num in busket]
    return arr
def MSD_RadixSort(arr):
    def radix_sort(lists,index):
        if index<0:
            return lists
        buskets=[[] for k in range(10)]
        for j in lists:
            buskets[j//(10**index)%10].append(j)
        for i in range(10):
            buskets[i]=radix_sort(buskets[i],index-1)
        res=[num for busket in buskets for num in busket]
        return res
    x=len(str(max(arr)))
    res=radix_sort(arr,x)
    return res
#8. 计数排序
def CountingSort(nums):
    minn=min(nums);maxn=max(nums)
    bucket=[0 for i in range(minn,(maxn+1))]
    for num in nums:
        bucket[num-minn]+=1
    i=0
    for j in range(len(bucket)):
        while bucket[j]>0:
            nums[i]=j
            bucket[j]-=1
            i+=1
    return nums
#9. 堆排序
def BigRoot_HeapSort(nums):
    def adjustHeap(nums, i, size):
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        largest = i 
        if lchild < size and nums[lchild] > nums[largest]: 
            largest = lchild 
        if rchild < size and nums[rchild] > nums[largest]: 
            largest = rchild 
        if largest != i: 
            nums[largest], nums[i] = nums[i], nums[largest] 
            adjustHeap(nums, largest, size)
    def builtHeap(nums, size):
        for i in range(len(nums)//2,-1,-1):
            adjustHeap(nums, i, size) 
    size = len(nums)
    builtHeap(nums, size) 
    for i in range(len(nums),-1,-1): 
        nums[0], nums[i] = nums[i], nums[0] 
        adjustHeap(nums, 0, i) 
    return nums
#10.桶排序
def BucketSort(the_list):
    all_list = [0 for i in range(100)]
    last_list = []
    for v in the_list:
        all_list[v] = 1 if all_list[v]==0 else all_list[v]+1
    for i,t_v in enumerate(all_list):
        if t_v != 0:
            for j in range(t_v):
                last_list.append(i)
    return last_list
def bucketSort(nums, defaultBucketSize = 5):
    maxVal, minVal = max(nums), min(nums)
    bucketSize = defaultBucketSize  # 如果没有指定桶的大小，则默认为5
    bucketCount = (maxVal - minVal) // bucketSize + 1  # 数据分为 bucketCount 组
    buckets = []  # 二维桶
    for i in range(bucketCount):
        buckets.append([])
    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)
    nums.clear()  # 清空 nums
    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:
        bucket.sort()
        nums.extend(bucket)    # 将排序好的桶依次放入到 nums 中
    return nums