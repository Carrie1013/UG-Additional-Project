# CSC3100_Review_Basic

## Insertion sort & Merge sort

### Insertion sort (for small number of elements)

```pseudocode
InsertSort(A)
for j=2 to A.length 
	key = A[j] 
	// insert A[j] into sorted sequence A[1,...,j-1]
	i = j-1 
	while i > 0 and A[i] > key
		A[i+1] = A[i]
	A[i+1] = key
```

**Loop invariant**: in each iteration, the array $A[1, ..., j-1]$ is sorted

Help us prove the correctness of the algorithm
• Initialization: true before the begin of loop.  $A[1]$ only one element
• Maintenance: if true before an iteration, then also true after it. $A[j-1]\leq A[j]\leq A[j+1]$
• Termination: when the loop stops, the algorithm is correct. $A[1,..,j-1]$ is sorted $j=n$
Similar to the mathematical induction 数学归纳法

 Random-access machine **(RAM) model**
• Sequential and no concurrent operations
• Operations taking a constant amount of time:
• E.g., arithmetic, data movement, conditions, function all, etc.

##### The running time of insertion sort

$T(n)=c_1n+c_2(n-1)+c_4(n-1)+c_5\sum_{j=2}^nt_j+c_6\sum_{j=1}^n(t_j-1)+c_7\sum_{j=2}^n(t_j-1)+c_8(n-1)$

**Best case**: array is sorted ($t_j=1$). $T(n)=(c_1+c_2+c_4+c_5+c_8)n-(c_2+c_4+c_5+c_8)$
**Worst case**: array is in reverse order ($t_j=j$). $T(n)=(\frac{c_5}{2}+\frac{c_6}{2}+\frac{c_7}{2})n^2+(c_1+c_2+c_4+\frac{c_5}{2}-\frac{c_6}{2}-\frac{c_7}{2}+c_8)n-(c_2+c_4+c_5+c_8)$.

#### - Recursion

Characteristics of a recursive definition
• It has a stopping point (base case) 例如：array size 小于等于1
• It recursively evaluates an expression involving a variable n  from a higher value to a lower value of n 
• Base case must be reached

### Merge sort (divide and conquer)

```pseudocode
MergeSort(A, p, r) // p start, r end.
if p < r
	then q = int((p + r) / 2)
		MergeSort(A, p, q)
		MergeSort(A, q+1, r)
		Merge(A, p, q, r)
```

![image-20220329201342085](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329201342085.png)

#### - Implementation of merge sort

```java
public static void Main(int[] a){
  int[] tmpArray = new int[a.length];
  mergeSort(a, tmpArray, 0, a.length-1)
}
private static void mergeSort(int[] a, int[] tmpArray, int left, int right){
  if (left < right){
    int center = (left + right)/2;
    mergeSort(a, tmpArray, left, center);
    mergeSort(a, tmpArray, center+1, right);
    merge(a, tmpArray, left, center+1, right)
  }
}
private static void merge(int[] a,int[] tmpArray,int leftPos,int rightPos,int rightEnd){
  int leftEnd = rightPos - 1,
  tmpPos = leftPos;
  int numElements = rightEnd - leftPos + 1;
  while (leftPos <= leftEnd && rightPos <= rightEnd)
    if (a[leftPos] <= a[rightPos])
      tmpArray[tmpPos++] = a[leftPos++];
  	else
      tmpArray[tmpPos++] = a[rightPos++];
  while (leftPos <= leftEnd)
    tmpArray[tmpPos++] = a[leftPos++];
  while (rightPos <= rightEnd)
    tmpArray[tmpPos++] = a[rightPos++];
  for (int i=0; i < numElements; i++, rightEnd--)
    a[rightEnd] = tmpArray[rightEnd];
}
```

#### - Analyzing merge sort

Suppose N is a power of 2

$T(n)=\begin{cases}c, \text{ if }n=1\\2T(\frac{n}{2})+cn,\text{ if }n>1\end{cases}$
$T(1)=C$
$T(N)=2T(\frac{N}{2})+CN$
$\frac{T(N)}{N}=\frac{T(\frac{N}{2})}{\frac{N}{2}}+C=...=\frac{T(1)}{1}+ClogN$
$T(N)=CNlogN+CN=O(NlogN)$

## Asymptotic notations

#### Basic Operations in Pseudocode

Arithmetic operations
Assigning a value to a variable
Indexing into an array / accessing value of objects/structs
Calling a method
Returning from a method
Comparison

![image-20220329211500418](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329211500418.png)





## Complexity analysis with recursion and divide and conquer

### Master Theorem (Big-Oh version)

 Let $g(n)$ be the running cost depending on the input size $n$, and we have its recurrence:

◦ $g(1)=O(1)$

◦$g(n)\leq a·g(\frac{n}{b})+O(n^\lambda)$

With $a,b,\lambda$ to be constants such that $a\geq1,b>1,\lambda\geq0$. Then,

◦ If $log_ba<\lambda,g(n)=O(n^\lambda)$ 
◦ If $log_ba=\lambda,g(n)=O(n^\lambda·logn)$
◦ If $log_ba>\lambda,g(n)=O(n^{log_ba})$  

Limitations: cannot be applied to cases like:
◦ $g(n)\leq a·g(n-1)+c$

