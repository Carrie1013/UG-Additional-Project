# CSC3100_Review_Tree

## Tree, binary tree

### Tree

##### Definition

A tree is a finite set of one or more nodes such that

◦ Each node stores an <span style='color:blue'>element</span>
◦ There is a specially node called the <span style='color:blue'>root</span>
◦ The remaining nodes are partitioned into $n\geq0$ disjoint sets $T_1,...,T_n$ where each of these sets is a tree
◦ We call $T_1,...,T_n$  the <span style='color:blue'>subtrees</span> of the root
◦ A tree with N nodes has one root, and $N-1$ edges
◦ Every node in the tree is the root of some subtree (<span style='color:blue'>recursive definition</span>)

**Parent**: Node A is the parent of B if B is the root of the left or right sub-tree of A
**Left (Right) Child**: Node B is the left (right) child of node A if A is the parent of B
**Sibling**: Node B and node C are siblings if they have the same parent
**Leaf**: A node is called a leaf if it has no children
**A path from node $n_1$ to $n_k$**: A sequence of nodes $n_1, n_2, ..., n_k$ such that $n_i$ is the parent of $n_{i+1}$ for $1\leq i<k$
**Length of a path**: The number of edges on the path, namely $k-1$. Notice that in a tree, there is <span style='color:blue'>exactly one path from the root to each node</span>.
**Depth of a node $n_i$**: the length of the unique path from the root to $n_i$, the root is at depth 0.
**Height of a node $n_i$**: the length of the longest path from $n_i$ to a leaf, all leaves are at height 0. 

##### Application 

◦ Unix file system
◦ HR system
◦ Java data types



### Binary Tree

**Full binary tree**: A binary tree where all the nodes have either **two or no** children
**Complete binary tree**: A binary tree where all the levels are completely filled except possibly the lowest one, which is filled from the **left** ![image-20220328175314886](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220328175314886.png)



### Binary tree ADT

##### <span style='color:blue'>Operations：</span>

**Create(bintree)**: creates an empty binary tree
**Boolean IsEmpty(bintree)**: if bintree is empty return TRUE else FALSE
**MakeBT(bintree1,element,bintree2)**: return a binary tree whose left subtree is **bintree1** and right subtree is **bintree2**, and whose root node contains the data **element**
**Lchild(bintree)**: if bintree is empty return error else return the left subtree of bintree
**Rchild(bintree)**: if bintree is empty return error else return the right subtree of bintree
**Data(bintree)**: if bintree is empty return error else return the element data stored in the root node of bintree



### Binary tree design

**<span style='color:purple'>Using pointers</span>**: More intuitive solution.

For each node <span style='color:red'>node</span>, we maintain:
· <span style='color:red'>node.</span><span style='color:blue'>parent</span>: store the **address** its parent
· <span style='color:red'>node.</span><span style='color:blue'>leftchild</span>: store the address of its left child
· <span style='color:red'>node.</span><span style='color:blue'>rightchild</span>: store the address of its right child
· <span style='color:red'>node.</span><span style='color:blue'>element</span>: store the values

##### Implementation

```java
// Create(bintree)
bintree = NULL
// isEmpty(bintree)
return bintree == NULL
// MakeBT(bintree1, element, bintree2)
rootNode <- allocate new memory
rootNode.element = element
rootNode.parent = NULL
rootNode.leftchild = bintree1
rootNode.rightchild = bintree2
if bintree1 != NULL
  bintree1.parent = rootNode
if bintree2 != NULL
  bintree2.parent = rootNode
return rootNode
// Lchild(bintree)
if bintree == NULL
  error "empty tree"
return bintree.leftchild
// Rchild(bintree)
if bintree == NULL
  error "empty tree"
return bintree.rightchild
// Data(bintree)
if bintree == NULL
  error "empty tree"
return bintree.element 
```

**<span style='color:purple'>Using array</span>**: Need more complicated design, and cannot efficiently handle all operations (thus will omit its implementations for each operation)  Will be used for **heap**, a special type of complete binary tree.

##### An array representation

◦ Generalize to all binary trees
◦ Efficient for complete binary trees
◦ But inefficient for skewed binary trees 
◦ Inefficient to implement the ADT

Given a <span style='color:blue'>complete binary tree</span> with $n$ nodes, for any $i^{th}$ node, $1\leq i\leq n$
· parent($i$) is $\lfloor\frac{i}{2}\rfloor$
· leftChild($i$) is at $2i$ if $2i\leq n$. Otherwise, $i$ has no left child
· rightChild($i$) is at $2i$ + 1 if $2i+1\leq n$; otherwise, $i$ has no right child



### Traversal of binary trees

**Preorder** (depth-first)
 ◦ Visit the node
 ◦ Traverse the left subtree in preorder 
 ◦ Traverse the right subtree in preorder

![image-20220328202432653](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220328202432653.png)

**Inorder**
 ◦ Traverse the left subtree in inorder 
 ◦ Visit the node
 ◦ Traverse the right subtree in inorder

- **Implementation**

  ```java
  INORDER-TREE-WALK(x)
  	if x != NIL
  		then INORDER-TREE-WALK(left[x])
  				print key[x] 
      		INORDER-TREE-WALK (right[x])
  ```

**Postorder**
 ◦ Traverse the left subtree in postorder 
 ◦ Traverse the right subtree in postorder 
 ◦ Visit the node

![image-20220328202743819](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220328202743819.png)

![image-20220328203545362](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220328203545362.png)

**Running time**: $\Theta(n)$, where $n$ is the size of the tree rooted at $x$.

### Reconstruction of binary trees

Reconstruction of Binary Tree from its **preorder** and **Inorder** sequences

Example: Given the following sequences, find the corresponding binary tree:
	inorder: DCEBAUZTXY
	preorder: ABCDEXZUTY

But: A binary tree may not be uniquely defined by its preorder and postorder sequences, Example: 
	preorder: ABC
	postorder: CBA



## Binary search tree

### Binary search tree

**Property**: 
BST is a tree such that for each node T, the key values in its left subtree are smaller than the key value of T, the key values in its right subtree are larger than the key value of T.

**Many applications due to its ordered structure**： 

◦ Useful for indexing and multi-level indexing
◦ Helpful in maintaining a sorted stream of data
◦ Helpful to implement various searching algorithms and data structures (e.g., TreeMap, TreeSet, Priority queue)

### Operatioins on BST

#### - Support many dynamic set operations

◦ searchKey, findMin, findMax, predecessor, successor, insert, delete
◦ Running time of basic operations on BST
		◦ On average: $\Theta(logn)$ $\Rightarrow$ The expected height of the tree is $logn$
		◦ In the worst case: $\Theta(n)$ $\Rightarrow$ The tree is a linear chain of n nodes

#### - Searching for a key

Given a pointer to the root of a tree and a key k: 
◦ Return a pointer to a node with key k if one exists, otherwise return NIL

```java
// find(x, k)
if x = NIL or k = key[x]
  then return x
if k < key[x]
  then return find(left[x], k)
  else return find(right[x], k)
```

Running Time: $O(h)$, $h$ is the height of the tree

#### - Finding the Minimum

Goal: find the minimun value in a BST:
◦ Following left child pointers from the root, until a NIL is encountered.

```java
// findMin(x)
while left[x] != NIL
  do x <- left[x]
return x
```

Running Time: $O(h)$, $h$ is the height of tree.

#### - Finding successor

<span style='color:red'>Def</span>: successor (x ) = y, such that key [y] is the smallest key > key [x]

**Case1**: right(x) is non-empty
· successor(x) = the minimum in right(x)
**Case2**: right(x) is empty
· go **up** the tree until the current node is a left child, successor (x) is the parent of the current node.
· if you cannot go further (and you **reached the root**): x is the <span style='color:blue'>largest</span> element.

```java
// successor(x)
if right[x] != NIL
  then return findMin(right [x])
y ← p[x]
while y != NIL and x = right[y]
  do x ← y
    y ← p[y]
return y
```

Running time: $O(h)$, $h$ is the height of the tree.

#### - Finding predecessor 

<span style='color:red'>Def</span>: predecessor (x ) = y, such that key [y] is the biggest key < key [x]

**Case1**: left(x) is non empty
· predecessor (x) = the maximum in left (x)
**Case2**: left(x) is empty
· go **up** the tree until the current node is a right child: predecessor (x) is the parent of the current node
· if you cannot go further (and you **reached the root**): x is the <span style='color:blue'>smallest</span> element

#### - Insertion

Goal: Insert value $v$ into a binary search tree

 Find the position and insert as a leaf:
◦ If key[x] < v move to the right child of x, else move to the left child of x 
◦ When x is NIL, we found the correct position
◦ If v < key[y] insert the new node as y’s left child, else insert it as y’s right child
◦ Beginning at the root, go down the tree and maintain:  
		Pointer x : traces the downward path (current node)
  	  Pointer y : parent of x (“trailing pointer” )

```java
y ← NIL 
x ← root[T] 
while x ≠ NIL
  do y ← x
    if key[z] < key[x]
      then x ← left[x]
      else x ← right[x] 
p[z]←y
if y = NIL
  then root[T] ← z
  else if key[z] < key[y]
    then left[y] ← z 
    else right[y] ← z
```

Running time: $O(h)$

#### - Deletion

Goal: Delete a given node z from a binary search tree
Idea:
◦ Case 1: z has no children
	· Delete z by making the parent of z point to NIL
◦ Case 2: z has one child
    · Delete z by making the parent of z point to z’s child, instead of to z, and link the parent 	     	  with the new child
◦ Case 3: z has two children
	· Find z’s successor y (the leftmost node in z’s right subtree)
	· y has either no child or one right child (but no left child), why? 
	· Delete y from the tree (via Case 1 or 2)
	· Replace z’s key and satellite data with y’s

```java
if left[z] = NIL or right[z] = NIL
  then y ← z   								//z has one child
  else y ← TREE-SUCCESSOR(z)  //z has 2 children
if left[y] != NIL
  then x ← left[y]
  else x ← right[y]
if x != NIL
  then p[x] ← p[y]
if p[y] = NIL
  then root[T] ← x 
  else if y = left[p[y]]
    then left[p[y]] ← x
    else right[p[y]] ← x 
if y != z
  then key[z] ← key[y]
  	copy y’s satellite data into z
return y
```

Running time: $O(h)$

#### - Summary

![image-20220328234512083](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220328234512083.png)

### Comparison between BST and linked list

![image-20220329004850366](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329004850366.png)

##### Exercise 1: Countleaves

```java
//To count the number of leaf nodes
int Mytree::count_leaf(TreeNode* p){
  if (p == NULL)
    return 0;
  else if ((p->left == NULL) && (p->right == NULL))
    return 1; 
  else
    return count_leaf(p->left) + count_leaf(p->right); 
}
```

##### Exercise 2: Delete the node with two children

A bit complicated if we want to delete a NON-LEAF NODE with TWO children
1.Locate the node
2.Find the rightmost node in its left subtree
3.Or find the leftmost node in its right subtree
4.Use the key of the node to 1 replace its key
5.Delete the node

##### Exercise 4: 

![image-20220329010039645](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329010039645.png)

##### Exercise 5: 

![image-20220329010120871](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329010120871.png)

![image-20220329010138285](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329010138285.png)

## AVL_tree

### Motivation

All BST operations are $O(d)$, where d is the tree depth, where $logn\leq d\leq n-1$, thus they take at most $O(N)$ time and at least $O(logn)$ time.
The best case: A complete binary tree
The worse case: All nodes from a chain

Want a complete tree after every operation 
◦ A **complete binary tree** has height of $O( log n)$ 
◦ The tree is full except possibly in the lower right
◦ This is expensive, for example, insert 2 in the tree on the left and then rebuild as a complete tree

Solution: we relax the condition a little bit $\Rightarrow$ **balanced BST**

Unless keys appear in just the right order, imbalance will occur on the updated BST
◦ In fact, **the order of keys** defines the **structure of the tree**

Many algorithms exist for keeping binary search trees **balanced**
◦ <span style='color:blue'>AVL trees</span>
◦ <span style='color:blue'>Red-black trees</span>
◦ Splay trees and other self-adjusting trees 
◦ B-trees and other multiway search trees

### Formal definition

**Definition**: An AVL tree is a self-balancing BST s.t.
◦ For every node in the tree, the **height** of the **left subtree** differs from the height of the **right subtree** by **at most 1**.  Balance factor of a node: <span style='color:blue'>height(left subtree) - height(right subtree)</span>

If at any time they differ by more than one, **rebalancing** is done to restore this property

<span style='color:blue'>Balance condition</span>: balance factor of every node is between -1 and 1

#### - AVL tree properties

- Structural properties：
  ◦ Binary tree property (same as for BST)
  ◦ Order property (same as for BST)
  ◦ Balance condition: balance factor of every node is between -1 and 1
  where **balance(node) = height(node.left) – height(node.right)**

- The worst-case depth is $O(logn)$
  ◦ All operations depend on the depth of the tree
  ◦ Find, insertion, and deletion can be completed in O(logn), where n is the number of nodes in the tree

#### - Height of binary search tree

**Theorem 1**: Given a balanced binary search tree $T$ of $n$ nodes, the height, or equivalently the depth, of $T$ is $O(logn)$.
**Proof**: Let $f(h)$ be the minimum number of nodes of a balanced binary search tree of height h. Then, it is easy to verify that $f(1) = 2,f (2) = 4$.
	For any $h\geq3$, we have that $f(h)=f(h-1)+f(h-2)+1$
	When $h$ is even number: $f(h)>f(h-1)+f(h-2)>2f(h-2)>4f(h-4)>...>2^{\frac{h}{2}-1}f(2)=2^{\frac{h}{2}}$
	When $h$ is odd number: $f(h)>f(h-1)>...>2^{\frac{h-1}{2}}$
	Therefore, given a balanced BST of $n$ nodes of height $h$, we have: $n>2^{\frac{h-1}{2}}\Rightarrow h<2log_2n+1\Rightarrow h=O(logn)$ 



### Insertion, rebalance strategies, deletion

#### - Insertion on AVL tree

- Insertion at the leaf (as **for all BST**) may cause unbalance
  ◦ Only nodes on the path from insertion point to root node have possibly changed in height
  ◦ After the insertion, go back up to the root node by node, updating heights
  ◦ If a new balance factor is 2 or –2, rebalance tree by rotation around the node

- General steps of insertion:
   ◦ Search for the element
   ◦ If it is not there, insert it in its place

- Rebalance strategies:
  ◦ <span style='color:blue'>Rotation</span> allows us to change the structure without violating the BST property

- ##### There are 4 cases:

  - <span style='color:blue'>Outside</span>b cases (require **single rotation**):
    ◦ Left-left: insertion into <span style='color:blue'>left</span> subtree of <span style='color:blue'>left</span> child
    ◦ Right-right: Insertion into <span style='color:blue'>right</span> subtree of <span style='color:blue'>right</span> child  
    ◦ (These two cases are symmetry)
  - <span style='color:blue'>Inside</span> cases (require **double rotation**) :
     ◦ Left-right: insertion into <span style='color:blue'>left</span> subtree of <span style='color:blue'>right</span> child  
     ◦ Right-left: insertion into <span style='color:blue'>right</span> subtree of <span style='color:blue'>left </span>child  
     ◦ (These two cases are symmetry)

- AVL tree: resolving imbalance issue:
  ![image-20220329100432625](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329100432625.png)



#### - Left(right) imbalance [and right(left) imbalance by symmetry]

![image-20220329103933801](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329103933801.png)

![image-20220329103949657](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329103949657.png)



#### - Rebalance implementation

![image-20220329101036475](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329101036475.png)

![image-20220329101056638](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329101056638.png)

![image-20220329101110245](/Users/qiaochufeng/Library/Application Support/typora-user-images/image-20220329101110245.png)

#### - Deletion on AVL-tree

 Similar but more complex than insertion
◦ Rotations and double rotations needed to rebalance重新平衡所需的旋转和双旋转
◦ Imbalance may propagate upward so that many rotations may be needed不平衡可能向上传播，因此可能需要多次旋转

- General steps (a recursive algorithm)
  ◦ Search downward for node
  ◦ Delete node (may replace it by its successor) 
  ◦ Unwind, correcting heights as we go
  ◦      If imbalance #1, 
  ◦           single rotate 
  ◦      If imbalance #2,
  ◦           double rotate

#### - Pros and cons of AVL trees

- ##### Arguments for AVL trees:

1. Search is $O(log n)$ since AVL trees are always balanced 
2. Insertion and deletions are also $O(logn)$ 
3. The height balancing adds no more than a constant factor to the speed of insertion 高度平衡只需要增加插入速度的一个常数因素

- ##### Arguments against using AVL trees:

1. Difficult to program & debug; more space for balance factor
2. Asymptotically faster but rebalancing costs time 渐近更快但重新平衡需要时间
3. Most large searches are done in database systems on disk and use other structures (e.g., B-trees) 大多数大型搜索在磁盘上的数据库系统中完成并使用其他结构

​		 			 		