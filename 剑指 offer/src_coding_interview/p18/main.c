/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteNode(struct ListNode* head, int val){
    struct ListNode *node = head;
    if(node == NULL){
    	return node;
    }
    if(node -> val == val){
    	head = node -> next;
    	free(node);
    	node = NULL;
    	return head;
    }
    while((node -> next != NULL) && (node -> next -> val != val)){
    	node = node -> next;
    }
    if(node -> next == NULL){
    	return head;
    }
    struct ListNode *tmp = node -> next;
    node -> next = node -> next -> next;
    free(tmp);
    tmp = NULL;
    return headl
}