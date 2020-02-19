/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* reversePrint(struct ListNode* head, int* returnSize){
    int i,
        len,
        tmp;
    len = 0;
    struct ListNode* node = head;
    while(node != NULL){
        node = node -> next;
        len ++;
    }
    // printf("%d\n", len);
    int *ans = (int *)malloc(len * sizeof(int));
    
    i = 0;
    node = head;
    while (i < len){
        ans[i] = node -> val;
        // printf("%d\n", ans[i]);
        i ++;
        node = node -> next;
    }

    for(i = 0; i < len / 2; i ++){
        tmp = ans[i];
        ans[i] = ans[len - i - 1];
        ans[len - i - 1] = tmp;
    }
    // for(i =0; i < len; i ++){
    //     printf("%d ", ans[i]);
    // }
    (* returnSize) = len;
    return ans;
}