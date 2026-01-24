#include <bits/stdc++.h>
using namespace std;

class node {
public:
    int data;
    node* next;
    
    node(int value) {
        data = value;
        next = NULL;
    }
};

// Insert at start
void insert_at_start(node* &head, int val_to_insert) {
    // defining new node and adding value into that new node
    node* node_to_insert = new node(val_to_insert);
    
    // if there is no element in the CLL then directly insert
    if (head == NULL) {
        head = node_to_insert;
        node_to_insert->next = head;  // making it circular
        return;
    }
    
    // else i.e. if we already have elements in the linked list then
    node* ptr = head;
    while (ptr->next != head) {  // traverse to the last node
        ptr = ptr->next;
    }
    ptr->next = node_to_insert;        // in the last node put the address of new node because it
    node_to_insert->next = head;       // in the new node add address of the previous first node
    head = node_to_insert;             // point the head to the new inserted node
    
    return;
}

// Insert at end
void insert_at_end(node* &head, int val_to_insert) {
    // defining new node and adding value into that new node
    node* node_to_insert = new node(val_to_insert);
    
    // if there is no element in the CLL then directly insert
    if (head == NULL) {
        head = node_to_insert;
        node_to_insert->next = head;  // making it circular
        return;
    }
    
    // else i.e. if we already have elements in the linked list then
    // traversing untill we reach the end of the linked list
    // then insert at end by changing links
    node* ptr = head;
    while (ptr->next != head) {
        ptr = ptr->next;
    }
    ptr->next = node_to_insert;
    node_to_insert->next = head;  // making it circular
    
    return;
}

// Display function
void display(node* &head) {
    // If there is no element in the CLL then nothing to print
    if (head == NULL) {
        cout << "No elements to the circular linked list" << endl;
        return;
    }
    
    // Else if there are elements present in the CLL then print those
    node* ptr = head;
    do {
        cout << ptr->data << " -> ";
        ptr = ptr->next;
    } while (ptr != head);
    
    cout << "(back to head)" << endl;
}

int main() {
    // Creating initially since the CLL is empty, here CLL is pointing to nothing
    node* head = NULL;
    
    // Testing insert at start
    cout << "Inserting at start:" << endl;
    insert_at_start(head, 5);
    insert_at_start(head, 4);
    insert_at_start(head, 3);
    insert_at_start(head, 2);
    insert_at_start(head, 1);
    display(head);
    
    cout << "\nInserting at end:" << endl;
    insert_at_end(head, 6);
    insert_at_end(head, 7);
    insert_at_end(head, 8);
    display(head);
    
    return 0;
}
