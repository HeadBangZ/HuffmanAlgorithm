from Element import Element
import PQHeap

def huffman_tree(frequencies):
    pq = PQHeap.createEmptyPQ()
    for i, f in enumerate(frequencies):
        PQHeap.insert(pq, Element(f, i))
    while len(pq) > 1:
        x = PQHeap.extractMin(pq)
        y = PQHeap.extractMin(pq)
        z = Element(x.key + y.key, [x.data, y.data])
        z.left = x
        z.right = y
        PQHeap.insert(pq, z)
    return pq[0]

def inorder(root, val, codes):
    if root is not None:
        if not root.left and not root.right:
            codes[root.data] = val
        if root.left:
            inorder(root.left, val + "0", codes)
        if root.right:
            inorder(root.right, val + "1", codes)
    return codes