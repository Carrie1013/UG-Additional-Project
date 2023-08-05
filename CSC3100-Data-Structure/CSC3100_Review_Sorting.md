# CSC3100_Review_SortingAlgorithm

### Sorting problem

Input: a sequence of n numbers
Output: a permutation (reordering) of input such that $a_1'<=a_2'<=...<=a_n'$

- Stored in <span style='color:red'>arrays</span>
- The numbers are referred as <span style='color:red'>keys</span>
- Associated with additional information
- Several ways to solve

### QuickSort (complexity)

<span style='color:blue'>Average</span> running time is $O(NlogN)$

<span style='color:blue'>Worst case</span> performance is $O(N^2)$ (but very unlikely)

### Deterministic & Randomized

<span style='color:blue'>Deterministic</span>: All previously learnt algorithms are deterministic. $\rightarrow$ The running cost is the same

<span style='color:blue'>Randomized</span>: We include one more basic operation: *radom(x, y)* $\rightarrow$ The running cost is a random variable

### QuickSort (divide-and-conquer)

##### High level idea (assume elements are distinct)

Pivot: Randomly pick an element, denoted as the pivot, and partition the remaining elements to three parts: <span style='color:blue'>pivot</span>, <span style='color:blue'>left part</span> (smaller than pivot), <span style='color:blue'>right part</span> (larger than pivot)

For the left part and right part: repeat the above process if the number of elements is larger than 1

### QuickSort (implementation)

```Java
// Algorithm: quicksort(arr, left, right)
if left >= right
  return
pivot <-- RANDOM(left, right) // randomly select pivot from [left,right]
pivotNewposition = partition(arr, left, right, pivot)
quicksort(arr, left, pivotNewposition - 1)
quicksort(arr, pivotNewposition + 1, right)
  
// Algorithm: partition(arr, left, right, pivot)
pivotVal = arr[pivot] //record the pivot data
arr[right] ↔ arr[pivot] //swap the pivot data and the last data
nextsmallpos = left//record the next position to put data smaller than pivotVal 
for j from left to right-1
	if arr[j] < pivotVal 
    arr[nextsmallpos] ↔ arr[j] 
    nextsmallpos++
arr[nextsmallpos] ↔ arr[right] 
return nextsmallpos
```

### MergeSort & Quicksort (both Divide-and-Conquer)

- When MergeSort executes the <span style='color:blue'>merge</span> operation
  - Requires an additional array to do the merge operation
  - Needs to do additional data copy: copy to additional array and then copy back to the input array
- When QuickSort executes the <span style='color:blue'>partition</span> operation 
  - Operates on the same array
  - No additional space required

- Quicksort is typically <span style='color:blue'>2-3 times faster</span> than MergeSort even though they have the <span style='color:blue'>same</span> (expected) time complexity $O(n·logn)$ 

### QuickSort (a good way)

- Set the pivot to the median among the first, center and last elements
- Exchange the second last element with the pivot
- Set i at the second element
- Set j at the third last element
- While i is on the left of j, move i right, skipping over elements that are smaller than the pivot
- Move j left, skipping over elements that are larger than the pivot
- When i and j have stopped, i is pointing at a large element and j at a small element
- If i is to the left of j, swap A [i] with A [j] and continue
- When i>j, swap the pivot element with the element at i
- All elements to the left of pivot are smaller than pivot, and all elements to the right of pivot are larger than pivot
- What to do when some elements are equal to pivot?

```Java
// QuickSort
private static int median3(int[] a, int left, int right) { 
  int center = (left + right) / 2;
  if (a[center] < a[left])
    swap (a, left, center); 
  if (a[right] < a[left])
    swap (a, left, right); 
  if (a[right] < a[center])
    swap (a, center, right);
// Place pivot at position right - 1
  swap (a, center, right - 1);
  return a[right - 1]; 
}
/* Main quicksort routine */
private static void quicksort(int[] a, int left, int right) { 
  if (left + CUTOFF <= right) {
    int pivot = median3(a, left, right);
		// Begin partitioning
    int i = left+1, j = right - 2; 
    while (true) {
      while (a[i] < pivot) {i++;} 
      while (a[j] > pivot) {j--;}
      if (i >= j) break; // i meets j
    	swap (a, i, j);
    }
    swap (a, i, right - 1); // Restore pivot 
    quicksort(a, left, i - 1); // Sort small elements 
    quicksort(a, i + 1, right); // Sort large elements
  } else
    insertionSort(a, left, right);
}
```

### Worst case partitioning

- One region has one element and the other has n – 1 elements
- Maximally unbalanced

Recurrence:  $q=1$
$T(n) = T(1)+T(n-1)+n$
$T(1)=\Theta(1)$
<span style='color:blue'>$T(n)=T(n-1)+n=n +(\sum_{k=1}^nk)-1=\Theta(n)+\Theta(n^2)=\Theta(n^2)$</span>

### Best case partitioning

- Partitioning produces two regions of size $\frac{n}{2}$

Recurrence: $q=\frac{n}{2}$
$T(n)=2T(\frac{n}{2})+\Theta(n)$
<span style='color:blue'>$T(n)=\Theta(nlogn)$</span>

### Case between worst and best

$Q(n)=Q(\frac{9n}{10})+Q(\frac{n}{10})+n$

- Using the recursion tree:
  Longest path: $Q(n)\leq n\sum_{i=0}^{log_{\frac{10}{9}}n}1=n(log_{\frac{10}{9}}n+1)=c_2n·logn$
  Shortest path: $Q(n)\geq n\sum_{i=0}^{log_{10}n}1=n(log_{10}n+1)=c_1n·logn$

Thus, <span style='color:blue'>$Q(n)=\Theta(n·logn)$</span>

### Comparison of sorting algorithms

![image-20220327181946246](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220327181946246.png)

<span style='color:blue'>Stability</span>: A sorting algorithm is said to be stable, if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. Selection Sort: 5，1，2，1* => 1*，1，2，5

### How fast can we sort

Theorem: Any comparison-based sorting algorithms will take $\Omega(n·logn)$ time.

Consider a <span style='color:red'>decision tree</span> that describes the sorting:

- A node represents a key comparison
- An edge indicates the result of the comparison (yes or no). We assume that all keys are distinct

![image-20220327193305303](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220327193305303.png)

### Complexity analysis (optional)

Lec11 p28

### Comparison-based sorting algorithms --- ShellSort

Afteraphase,withanincrementhk,A[i]<=A[i+hk]. All elements spaced hk apart are sorted (insertion sort)![image-20220327201154665](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220327201154665.png)

```java
// ShellSort with {1,2,4,8,...,n/2}
public static void shellSort(int[] a) { 
  int j;
  for (int gap = a.length/2; gap > 0; gap /=2) 
    for (int i = gap; i < a.length; i++) {
      int tmp = a[i];
      for (j = i; j >= gap && tmp < a[j-gap]; j-= gap)
        a[j] = a[j-gap]; 
      a[j] = tmp;
    } 
}
```

##### Analysis of ShellSort （based on insertion sort）

It is very hard (average-case is a long-standing open problem)

Results depend on the **selection of** an **increment** sequence 

<span style='color:blue'>Theorem</span>: The **worst-case** running time of Shellsort, using some increment, is <span style='color:blue'>$\Theta(N^2)$</span>

<span style='color:blue'>Proof</span> (for some cases): 

​	Put the largest $\frac{N}{2}$ numbers in the even position. e.g., 4,12,1,10,3,11,2,9
​	Using the increments {..., 8,4,2,1}
​	Before the last sort, the $\frac{N}{2}$ Largest numbers are still in the even positions. eg., 
​	1,9,2,10,3,11,4,12
​	The numbers of inversions is 1+2+...+$\frac{(N-1)}{2}$ =$\Theta(N^2)$

### Non-comparison-based sorting algorithms

#### CountingSorting

**Idea**: suppose the values are integers in [0, m-1]

**Steps**
◦ Start with m empty buckets numbered 0 to m-1 
◦ Scan the list and place element s[i] in bucket s[i] 
◦ Output the buckets in order

- Will need <span style='color:blue'>an array of buckets</span>, and the values in the list to be sorted will be the indexes to the buckets 
- No comparisons will be necessary

```java
// Algorithm CountingSort(S) <--values in S are between 0 and m-1-->
for j <-- 0 to m-1 do // initialize m buckets 
  b[j] <-- 0
for i <-- 0 to n-1 do // place elements in their appropriate buckets 
  b[S[i]] <-- b[S[i]] + 1
i <-- 0
for j <-- 0 to m-1 do // place elements in buckets
  for r <-- 1 to b[j] do // back in S 
    S[i] <-- j
    i <-- i+1
```

**Problem**: 
How to process the case that the minimum value in the input sequence of integers is very large?
How to process the case that the values in the sequence vary greatly (i.e., 1, 10, 101, 1000, 100001) ?

#### BucketSorting

**Assumption**: The input is generated by a random process that distributes elements uniformly over [0, 1).

**Idea** 
◦ Divide [0, 1) into n equal-sized buckets
◦ Distribute the n input values into the buckets
◦ Sort each bucket (e.g., using QuickSort)
◦ Go through the buckets in order, listing elements in each one

```java
// Bucket-Sort(A, n) <--totally Theta(n)-->
for i <-- 1 to n // O(n)
  do insert A[i] into list B[nA[i]]
for i <-- 0 to n-1 // Theta(n)
  do sort list B[i] with quicksort sort
concatenate lists B[0], B[1], ..., B[n-1] together in order // O(n)
return the concatenated lists
```

BucketSort is not efficient if m is large

##### <span style='color:blue'>Stable sort</span>

**Definition**: A stable sorting algorithm is one that preserves the original relative order of elements with equal key.![image-20220327222858761](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220327222858761.png)

Suppose we sort some 2-digit integers：
	Phase 1: Stable sort by the right digit (the least significant digit)
	Phase 2: Stable sort by the left digit (the second least significant digit)

#### RadixSorting

**Idea**: 
Apply stable bucket sort on each digit (from Least Significant Digit to Most Significant Digit)

**A** **complication**:
◦ Just keeping the count is not enough 
◦ Need to keep the actual elements
◦ Use a queue for each digit

```java
// item is the type: {0,...,10d-1},
// i.e., the type of d-digit integers void radixsort(item A[], int n, int d) 
{
   int i;
   for (i=0; i<d; i++)
      bucketsort(A, n, i);
}
// To extract d-th digit of x
int digit(item x, int d)
{
   int i;
   for (i=0; i<d; i++)
      x /= 10; // integer division
   return x%10;
}
void bucketsort(item A[], int n, int d)
// stable-sort according to d-th digit
{
   int i, j;
   Queue *C = new Queue[10];
   for (i=0; i<10; i++) C[i].makeEmpty();
   for (i=0; i<n; i++)
      C[digit(A[i],d)].EnQueue(A[i]);
   for (i=0, j=0; i<10; i++)
      while (!C[i].empty())
      { // copy values from queues to A[]
         C[i].DeQueue(A[j]);
         j++; 
      }
}
```

##### Inductive proof that RadixSort works

**Keys**: k-digit numbers, base B

**Claim**: after $i^{th}$ BucketSort, the least significant $i$ digits are sorted	
◦ Base case: $i=0$, 0 digits are sorted.
 ◦ Inductive step: Assume for i, prove for i+1
		Consider two numbers: **X, Y**. Say $X_i$ is ith digit of **X**:
			 Xi+1 < Yi+1 then i+1th BucketSort will put them in order
			 Xi+1 > Yi+1 , same thing
			 Xi+1 = Yi+1 , order depends on last i digits. Induction hypothesis says already sorted 
				for these digits because BucketSort is **stable**	 

##### Worst-case time complexity

- Assume k digits, each digit comes from {0,...,M-1}
- For each digit,
   ◦ O(M) time to initialize M queues,
   ◦ O(n) time to distribute n numbers into M queues
- Total time = $O(k(M+n))$
- When k is constant and $M = O(n)$, we can make RadixSort run in linear time, i.e., $O(n)$

Since RadixSort is faster than QuickSort, why is QuickSort still preferable in many cases?
◦ Although RadixSort runs in Θ(n) while QuickSort Θ(n lg n), QuickSort has much smaller
	**constant factor c**
◦ RadixSort requires **extra memory**, whereas QuickSort works in place

### A summary of 10 classic sorting algorithms

![image-20220327225201774](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220327225201774.png)