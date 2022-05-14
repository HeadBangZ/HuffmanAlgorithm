def createEmptyPQ():
    """Returns an empty list"""
    return []

def minHeapify(arr, i):
    """Make sure the heap follow the rules of a min heap"""
    heapsize = len(arr) - 1
    smallest = i
    left = leftChild(i)
    right = rightChild(i)

    if left <= heapsize and arr[left] < arr[i]:
        smallest = left
    else:
        smallest = i
    if right <= heapsize and arr[right] < arr[smallest]:
        smallest = right

    # need this condition to ensure recursive call stops when parent-child swap reach the bottom.
    if smallest != i:
        # swapping smallest element with the current element
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, smallest)

def extractMin(arr):
    """Extracts the smallest value from the heap"""
    heapsize = len(arr) - 1
    if heapsize < 0:
        return
    element = arr[0]
    arr[0] = arr[heapsize]
    arr.pop()
    minHeapify(arr, 0)
    return element

def insert(arr, element):
    """Inserts key into the heap"""
    heapsize = len(arr)
    i = heapsize
    arr.append(element)
    while i > 0 and arr[parentIndex(i)] > arr[i]:
        arr[parentIndex(i)], arr[i] = arr[i], arr[parentIndex(i)]
        i = parentIndex(i)

# idx = index
def leftChild(idx):
    """Finds the left child"""
    return (2 * idx) + 1

def rightChild(idx):
    """Finds the right child"""
    return (2 * idx) + 2

def parentIndex(idx):
    """Finds the parent of the index"""
    return (idx - 1) // 2