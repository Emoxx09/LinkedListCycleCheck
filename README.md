## Linked Lists
A linked list is a sequence of data structures, which are connected together via links. Linked List is a sequence of links which contains items. Each link contains a connection to another link. Linked list is the second most-used data structure after array.

In the real world, this data structure has helped many practical real-world processes such as handling queues. It is a tool that has greatly brought ease in the lives of people. This is why it is important that as programmers, we ensure that our linked lists work as intended.

## The Problem
In most cases, unfortunately, linked lists don't go as planned. They may contain accidental nodes, perform overly lengthy traversals or even become structurally illogical at scale.

One of the famous problems that programmers deal with linked lists is the presence of cycles. In many cases, the presence of a cycle can make or break a system. Hence, it is important that as programmers, we check for their presence.

## Cycle Detection in Linked Lists
Now, let us discuss the "how" part. Let us see the inner workings of how one can approach cycle detection in linked lists. Below are a series of illustrations and codes. For this, we will use Python, a known functional programming language.


<img src="https://github.com/KMontebon/LinkedListCycleCheck/blob/main/Pictures/1.png?raw=true" width="300">

To move forward, we must firstly create our vital classes which include our Node, and the LinkedList itself. Under LinkedList, we have two utility functions; setHead() which sets the head of our linked list, and printLL() which  prints the contents of our linked list.
  
<br>
<img src="https://github.com/KMontebon/LinkedListCycleCheck/blob/main/Pictures/2.png?raw=true" width="400">
  
Here, we created a function named checkCycle. As you've guessed, this function checks the presence of a cycle in a linked list by having two separate pointers; one that traverses in increments of 2 and one in only increments of 1. As these pointers traverse the linked list, the function can spot a cycle when both pointers direct to the same node. See illustration below for better understanding.

<img src="https://github.com/KMontebon/LinkedListCycleCheck/blob/main/Pictures/6.png?raw=true" width="600">

<br>
Finally, let's test our function. First we created a linked list that has a cycle in it. This should be able to detect that there is a cycle since the last node, n4, has its next node set to n1, the head of the linked list.

<img src="https://github.com/KMontebon/LinkedListCycleCheck/blob/main/Pictures/3.png?raw=true" width="400">
  
Then we created a linked list that has no cycle in it to see if it can still detect so.

<img src="https://github.com/KMontebon/LinkedListCycleCheck/blob/main/Pictures/4.png?raw=true" width="400">

And as expected, both produced True and False, respectively.

<img src="https://github.com/KMontebon/LinkedListCycleCheck/blob/main/Pictures/5.png?raw=true" width="300">

This is one way to solve the problem of cycles in linked lists. I'm sure there are other ways to do so and maybe they're even better. But for now, that's it for me.
If you want to test the program, please see the file attached or visit this link: jdoodle.com/ia/oHM
Thank you for reading!
