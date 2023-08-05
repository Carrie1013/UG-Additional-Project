# CSC3100_Heap

#####  Priority queue operations

◦ insert
◦ deleteMin
◦ create
◦ isEmpty

##### Possibilities for the implementation

◦ Singly linked list
Insert at the front in O(1)
Delete minimum in O(N)

◦ Sorted array
Insert in O(N)
Delete minimum in O(N)

◦ Binary heap
Insert in O(logN)
Delete minimum in O(logN)
Two properties: structure property & heap order property

### Binary heap

(A) Structure property
◦ A heap is a complete binary tree
◦ A complete binary tree of height h has between $2^h$ And $2^{h+1}$
◦ The height of a complete binary tree = $\lfloor logN \rfloor$
(B) Heap order property
◦ The value at any node should be smaller than (or equal to) all of its descendants (guarantee that the node with the <span style='color:blue'>minimum value is at the root</span>)

##### Class skeleton for elements

```java
class ElementType { 
  int priority;
  String data;
  public ElementType(int priority, String data) { 
    this.priority = priority;
    this.data = data; 
  }
  public boolean isHigherPriorityThan(ElementType e) {
    return priority < e.priority; 
  }
}
```

##### Definition and constructor of priority queue

```java
public class BinaryHeap {
  private int currentSize; // Number of elements in heap 
  private ElementType arr[ ]; // The heap array
  public BinaryHeap (int capacity) { 
    currentSize = 0;
    arr = new ElementType[capacity + 1]; 
  }
}
```

##### Binary heap: insert

 To insert an element X,
 ◦ Create a hole in the next available location
 ◦ If X can be placed in the hole without violating heap order, insertion is complete
 ◦ Otherwise slide the element that is in the hole’s parent node into the hole, i.e., bubbling the hole up towards the root
 ◦ Continue this process until X can be placed in the hole (a percolating up process)

The worst case running time is <span style='color:blue'>O(logN)</span>: the new element is percolating up all the way to the root

```java
public void insert(ElementType x) throws Exception { 
  if (isFull())
    throw new Exception("Overflow");
  // Percolate up
  int hole = ++currentSize;
  while(hole > 1 && x.isHigherPriorityThan(arr[hole/2])) {
    arr[hole] = array[hole / 2];
    hole /= 2;
  }
  arr[hole] = x;
}
```

##### Binary heap: deleteMin

 ◦ The element at the root (position 1) is to be removed, and a hole is created
 ◦ Fill the root with the last node X
 ◦ Percolate X down (switch X with smaller child) until heap order property satisfied
 ◦ Note that:
 	◦ Some node may have only one child (be careful when coding!) 
	 ◦ Worst case running time is O (log N)

```java
// deleteMin
public String deleteMin() { 
  if (isEmpty())
    return null;
  String data = arr[1].data; 
  arr[1] = arr[currentSize--];
  percolateDown(1);
  return data; 
}
// percolateDown
private void percolateDown(int hole) { 
  int child;
  ElementType tmp = arr[hole]; 
  while (hole * 2 <= currentSize) {
    child = hole * 2;
    if (child != currentSize &&
        arr[child +1].isHigherPriorityThan(arr[child]))
    		child++;
    if (arr[child].isHigherPriorityThan(tmp))
      	arr[hole] = array[child];
    else
      break;
    hole = child;
  }
  arr[hole] = tmp; 
}
```

### Complexity analysis

During insertion/deletion, the worst-case time complexity depends linearly to the height/depth of the heap
◦ The height/depth of heap is 𝑂(log 𝑛)
◦ The heap insertion: 𝑂(log 𝑛)
◦ The heap deletion: 𝑂(log 𝑛)

### Binary heap construction

A naive algorithm to build heap is to repeatedly insert nodes one by one, which completes in O(nlogn) time

A faster algorithm to build the binary heap:
◦ N successive appends at the end of the array, each taking O(1), so the tree is unordered
◦ For (i = $\frac{N}{2}$, i>0; i--): percolateDown(i)

### Variants of heap

##### Min-heap

◦ The key present at the root node must be less than or equal among the keys present at all of its children
◦ The same property must be recursively true for all sub-trees

##### Max-heap

◦ The key present at the root node must be larger than or equal among the keys present at all of its children
◦ The same property must be recursively true for all sub-trees

### HeapSort

Sorting using a max-heap
◦ To sort an array arr, we first create a max-heap H with a capacity of arr.length+1
◦ Then, we repeatedly delete from the max-heap until the max-heap becomes empty