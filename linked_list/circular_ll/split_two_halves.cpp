#include <bits/stdc++.h>
using namespace std;

// Split two halves
node* split_two_halves(node* &head) {
    // pointer at first node of CLL
    node* ptr = head;
    
    // calculating length of CLL
    int L = length(head);
    
    // checking if length is even or odd
    if (L % 2 == 0) 
    {
        for (int count = 1; count <= (L/2 - 1); count++) 
        {
            ptr = ptr->next;
        }
    }
    else 
    {
        for (int count = 1; count <= (L/2); count++) 
        {
            ptr = ptr->next;
        }
    }
    
    node* head_second_half = ptr->next;
    
    // making first half circular LL
    ptr->next = head;
    
    // making second half circular LL
    node* ptr2 = head_second_half;
    while (ptr2->next != head) 
    {  // traversing pointer to the end of CLL
        ptr2 = ptr2->next;
    }
    ptr2->next = head_second_half;
    
    return head_second_half;
}