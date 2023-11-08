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
  <li>1 <= n <= 10<sup>4</sup></li>
  <li>0 <= left.length <= n + 1</li>
  <li>0 <= left[i] <= n</li>
  <li>0 <= right.length <= n + 1</li>
  <li>0 <= right[i] <= n</li>
   <li>1 <= left.length + right.length <= n + 1</li>
   <li>All values of left and right are unique, and each value can appear only in one of the two arrays.</li>
</ul>
</p>
</div>
<strong>Example 1:</strong> 
<strong>Input:</strong>  n = 4, left = [4,3], right = [0,1] <br>
<img src="https://assets.leetcode.com/uploads/2020/06/17/ants.jpg" >
<strong>Output:</strong> 4<br>
<strong>Explanation:</strong><br>
In the image above:<br>
-The ant at index 0 is named A and going to the right.<br>
-The ant at index 1 is named B and going to the right.<br>
-The ant at index 3 is named C and going to the left.<br>
-The ant at index 4 is named D and going to the left.<br>
The last moment when an ant was on the plank is t = 4 seconds. After that, it falls immediately out of the plank. (i.e., We can say that at t = 4.0000000001, there are no ants on the plank).<br>
<strong>Example 2:</strong><br>
<strong>Input:</strong> n = 7, left = [], right = [0,1,2,3,4,5,6,7]<br>
<img src="https://assets.leetcode.com/uploads/2020/06/17/ants2.jpg" >
<strong> Output: </strong>7<br>
<strong>Explanation:</strong> All ants are going to the right, the ant at index 0 needs 7 seconds to fall.<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/blob/November-2023/04-11-2023.py">Click Here</a></Strong>
 <br>

<h2>DAY_5</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/find-the-winner-of-an-array-game/description/">Link</a></p>
<div>
<p>
<strong>1535</strong>Find the Winner of an Array Game.
Given an integer array arr of distinct integers and an integer k.
   A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
Return the integer which will win the game.
It is guaranteed that there will be a winner of the game.
<br>
<strong>Constraints:</strong>
<ul>
  <li>2 <= arr.length <= 10<sup>5</sup></li>
  <li>1 <= arr[i] <= 10<sup>6</sup></li>
  <li>0 <= left[i] <= n</li>
  <li>arr contains distinct integers.</li>
  <li>1 <= k <= 10<sup>9</sup></li>
</ul>
</p>
</div>
 <strong>Example 1:</strong> 
<strong>Input:</strong> arr = [2,1,3,5,4,6,7], k = 2<br>
<strong>Output:</strong> 5<br>
<strong>Explanation:</strong><br>
Round |       arr       | winner | win_count <br>
  1   | [2,1,3,5,4,6,7] | 2      | 1 <br>
  2   | [2,3,5,4,6,7,1] | 3      | 1 <br>
  3   | [3,5,4,6,7,1,2] | 5      | 1 <br>
  4   | [5,4,6,7,1,2,3] | 5      | 2 <br>
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/blob/November-2023/05-11-2023.py">Click Here</a></Strong><br>

<h2>DAY_6</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06">Link</a></p>
<strong>1845.</strong>Seat Reservation Manager.
<div>
 <p>Design a system that manages the reservation state of n seats that are numbered from 1 to n.</p>
 <p>Implement the SeatManager class:</p>
 <ul>
  <li>SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.</li>
  <li>int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.</li>
  <li>void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.</li>
 </ul>
 <br>
<strong>Constraints:</strong>
 <ul>
  <li>1 <= n <= 10<sup>5</sup></li>
   <li>1 <= seatNumber <= n</li>
    <li>For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
</li>
    <li>For each call to unreserve, it is guaranteed that seatNumber will be reserved.</li>
    <li>At most 10 <sup>5</sup> calls in total will be made to reserve and unreserve.</li>
 </ul>
</div>
 <strong>Example 1:</strong> 
<strong>Input:</strong> ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]<br>
<strong>Output:</strong> [null, 1, 2, null, 2, 3, 4, 5, null]<br>
<strong>Explanation:</strong><br>
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.<br>
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.<br>
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.<br>
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].<br>
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.<br>
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.<br>
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.<br>
seatManager.reserve();    // The only available seat is seat 5, so return 5.<br>
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/commit/ce640610d0205c14fbd84e02fa4588d7be803875">Click Here</a></Strong><br>

<h2>DAY_7</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/">Link</a></p>
<strong>1921.</strong>Eliminate Maximum Number of Monsters.
<div>
 <p>You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.</p>
 <p>The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.</p>
 <p>You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge. The weapon is fully charged at the very start.</p>
 <p>You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon</p>
 <p>Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.</p>
 <strong>Constraints:</strong>
 <ul>
  <li> n == dist.length == speed.length</li>
  <li>1 <= n <= 10 <sup>5</sup> </li>
   <li>1 <= dist[i], speed[i] <= 10 <sup>5</sup> </li>
 </ul>
</div>
<strong>Example 1:</strong><br>
<strong>Input:</strong>dist = [1,3,4], speed = [1,1,1]<br>
<strong>Output:</strong> 3<br>
<strong>Explanation:</strong><br>
In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.<br>
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.<br>
After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.<br>
All 3 monsters can be eliminated.<br>
<strong>Example 2:</strong><br>
<strong>Input:</strong>dist = [1,1,2,3], speed = [1,1,1,1]<br>
<strong>Output:</strong> 1<br>
<strong>Explanation:</strong><br>
In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.<br>
After a minute, the distances of the monsters are [X,0,1,2], so you lose.<br>
You can only eliminate 1 monster.<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/commit/fb748bd710bf49c20c826d969a07a05901051a0f">Click Here</a></Strong><br>

<h2>DAY_8</h2>
<p>Problem Discription-<a href="https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description/">Link</a></p>
<strong>2849.</strong>Determine if a Cell Is Reachable at a Given Time.
<div><p>You are given four integers sx, sy, fx, fy, and a non-negative integer t.</p>
 <p>In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.</p>
<p>Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.</p>
<p>A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.</p>

 <strong>Constraints:</strong>
 <ul>
  <li> 1 <= sx, sy, fx, fy <= 10<sup>9</sup></li>
  <li>0 <= t <= 10<sup>9</sup> </li>
  </ul>
</div>
<strong>Example 1:</strong><br>
<strong>Input:</strong>sx = 2, sy = 4, fx = 7, fy = 7, t = 6<br>
<strong>Output:</strong> True<br>
 <img src="https://assets.leetcode.com/uploads/2023/08/05/example2.svg" >
<strong>Explanation:</strong><br>
Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above. 
After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.<br>
<strong>Example 2:</strong><br>
<strong>Input:</strong>sx = 3, sy = 1, fx = 7, fy = 3, t = 3<br>
<strong>Output:</strong> False<br>
<img src="https://assets.leetcode.com/uploads/2023/08/05/example1.svg" >
<strong>Explanation:</strong><br>
 <p>Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.</p>
<br>
<Strong>Solution Link:  <a href="https://github.com/BVARUNTEJA/LeetCode-POD/blob/November-2023/08-11-2023.py">Click Here</a></Strong><br>
