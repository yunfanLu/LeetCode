/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    if (head == NULL){
        return NULL;
    }

    struct ListNode *p,
                    *q,
                    *r;
    p = head;
    while(p -> next != NULL){
        p = p -> next;
    }
    q = head;
    while(q != p){
        r = q -> next;
        q -> next = p -> next;
        p -> next = q;
        q = r;
    }
    return p;
}