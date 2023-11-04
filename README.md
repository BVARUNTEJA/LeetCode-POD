<h1>November</h1>
<h2>DAY_1</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/find-mode-in-binary-search-tree/description/?envType=daily-question&envId=2023-11-01">Link</a></p>
<div>
<p>
<strong>501</strong>.Find Mode in Binary Search Tree
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
<br>
Assume a BST is defined as follows:
<br>
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
<br>
<br>
<strong>Constraints:</strong>
<p>The number of nodes in the tree is in the range [1, 104].</p>
<p>10<sup>-5</sup> <= Node.val <= 10<sup>5</sup></p>
</p>
</div>
Example 1:
Input: root = [1,null,2,2]
<img src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" >
Output: [2]<br>
Example 2:
Input: root = [0]<br>
Output: [0]
<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/commit/46ad8412cb070df5b0ff27ef777a2c81dac6bd01">Click Here</a></Strong>
<br>
 
<h2>DAY_2</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2023-11-02">Link</a></p>
<div>
<p>
<strong>2265.</strong>.Count Nodes Equal to Average of Subtree
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
<br>
Note:
<br>
1.The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.<br>
2.A subtree of root is a tree consisting of root and all of its descendants.
<br>
<br>
<strong>Constraints:</strong>
<p>The number of nodes in the tree is in the range [1, 1000]. </p>
<p> 0 <= Node.val <= 1000</p>
</p>
</div>
Example 1:
Input: root = [4,8,5,0,1,null,6]
<img src="https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png" >
Output: 5<br>
Explanation: <br>
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.<br>
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.<br>
For the node with value 0: The average of its subtree is 0 / 1 = 0.<br>
For the node with value 1: The average of its subtree is 1 / 1 = 1.<br>
For the node with value 6: The average of its subtree is 6 / 1 = 6.<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/blob/November-2023/02-11-2023.py">Click Here</a></Strong>
 <br>
  
<h2>DAY_3</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=daily-question&envId=2023-11-03">Link</a></p>
<strong>1441.</strong>.Build an Array With Stack Operations.<br>

You are given an integer array target and an integer n.<br>
You have an empty stack with the two following operations:<br>
"Push": pushes an integer to the top of the stack.<br>
"Pop": removes the integer on the top of the stack.<br>
You also have a stream of the integers in the range [1, n].<br>
Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:<br>

If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.<br>
If the stack is not empty, pop the integer at the top of the stack.<br>
If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.<br>
Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.<br>

 

Example 1:<br>

Input: target = [1,3], n = 3<br>
Output: ["Push","Push","Pop","Push"]<br>
Explanation: Initially the stack s is empty. The last element is the top of the stack.<br>
Read 1 from the stream and push it to the stack. s = [1].<br>
Read 2 from the stream and push it to the stack. s = [1,2].<br>
Pop the integer on the top of the stack. s = [1].<br>
Read 3 from the stream and push it to the stack. s = [1,3].<br>

Example 2:<br>
Input: target = [1,2,3], n = 3<br>
Output: ["Push","Push","Push"]<br>
Explanation: Initially the stack s is empty. The last element is the top of the stack.<br>
Read 1 from the stream and push it to the stack. s = [1].<br>
Read 2 from the stream and push it to the stack. s = [1,2].<br>
Read 3 from the stream and push it to the stack. s = [1,2,3].<br>

Example 3:<br>
Input: target = [1,2], n = 4<br>
Output: ["Push","Push"]<br>
Explanation: Initially the stack s is empty. The last element is the top of the stack.<br>
Read 1 from the stream and push it to the stack. s = [1].<br>
Read 2 from the stream and push it to the stack. s = [1,2].<br>
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.<br>
The answers that read integer 3 from the stream are not accepted.<br>

<strong>Constraints:</strong>
<ul>
  <li>1 <= target.length <= 100</li>
  <li>1 <= n <= 100</li>
  <li>1 <= target[i] <= n</li>
  <li>target is strictly increasing.</li>
</ul>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/blob/November-2023/03-11-2023.py">Click Here</a></Strong>
 <br>
 <h2>DAY_2</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2023-11-02">Link</a></p>
<div>
<p>
<strong>2265.</strong>.Count Nodes Equal to Average of Subtree
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
<br>
Note:
<br>
1.The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.<br>
2.A subtree of root is a tree consisting of root and all of its descendants.
<br>
<br>
<strong>Constraints:</strong>
<p>The number of nodes in the tree is in the range [1, 1000]. </p>
<p> 0 <= Node.val <= 1000</p>
</p>
</div>
Example 1:
Input: root = [4,8,5,0,1,null,6]
<img src="https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png" >
Output: 5<br>
Explanation: <br>
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.<br>
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.<br>
For the node with value 0: The average of its subtree is 0 / 1 = 0.<br>
For the node with value 1: The average of its subtree is 1 / 1 = 1.<br>
For the node with value 6: The average of its subtree is 6 / 1 = 6.<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/blob/November-2023/02-11-2023.py">Click Here</a></Strong>
 <br>
<h2>DAY_2</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2023-11-02">Link</a></p>
<div>
<p>
<strong>2265.</strong>.Count Nodes Equal to Average of Subtree
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
<br>
Note:
<br>
1.The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.<br>
2.A subtree of root is a tree consisting of root and all of its descendants.
<br>
<br>
<strong>Constraints:</strong>
<p>The number of nodes in the tree is in the range [1, 1000]. </p>
<p> 0 <= Node.val <= 1000</p>
</p>
</div>
Example 1:
Input: root = [4,8,5,0,1,null,6]
<img src="https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png" >
Output: 5<br>
Explanation: <br>
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.<br>
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.<br>
For the node with value 0: The average of its subtree is 0 / 1 = 0.<br>
For the node with value 1: The average of its subtree is 1 / 1 = 1.<br>
For the node with value 6: The average of its subtree is 6 / 1 = 6.<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/blob/November-2023/02-11-2023.py">Click Here</a></Strong>
 <br>
 
<h2>DAY_4</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/">Link</a></p>
<div>
<p>
<strong>1503</strong> Last Moment Before All Ants Fall Out of a Plank.
We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.

When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time.

When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank.
<br>
<strong>Constraints:</strong>
<ul>
  <li>1 <= n <= 10<sub>4</sub></li>
  <li>0 <= left.length <= n + 1</li>
  <li>0 <= left[i] <= n</li>
  <li>0 <= right.length <= n + 1</li>
  <li>0 <= right[i] <= n</li>
   <li>1 <= left.length + right.length <= n + 1</li>
   <li>All values of left and right are unique, and each value can appear only in one of the two arrays.</li>
</ul>
</p>
</div>
Example 1:
Input: n = 4, left = [4,3], right = [0,1] <br>
<img src="https://assets.leetcode.com/uploads/2020/06/17/ants.jpg" >
Output: 4<br>
Explanation: <br>
In the image above:<br>
-The ant at index 0 is named A and going to the right.<br>
-The ant at index 1 is named B and going to the right.<br>
-The ant at index 3 is named C and going to the left.<br>
-The ant at index 4 is named D and going to the left.<br>
The last moment when an ant was on the plank is t = 4 seconds. After that, it falls immediately out of the plank. (i.e., We can say that at t = 4.0000000001, there are no ants on the plank).<br>
<Strong>Solution Link:  <a href="">Click Here</a></Strong>
 <br>


