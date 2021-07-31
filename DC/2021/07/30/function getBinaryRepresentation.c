#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int val;
    struct Node *prev, *next;
};
 
struct Node* getBinaryRepresentation(int x)
{   
    int a[101],l=0;
    while(x>0){
        a[l++]=x%2;
        x/=2;
    }
    struct Node *head=NULL,*tail=NULL;
    for(int i=l-1;i>=0;i--){
        struct Node *n=(struct Node *)malloc(sizeof(struct Node *));
        n->prev=NULL;
        n->next=NULL;
        n->val=a[i];
        if(head==NULL){
            head=n;
            tail=n;
        }
        else{
            n->prev=tail;
            tail->next=n;
            tail=tail->next;
        }
    }
    return head;   
    
}

void display(struct Node *head)
{
    struct Node *ptr = head;
    while(ptr != NULL)
    {
        printf("%d ", ptr->val);
        ptr = ptr->next;
    }
}

void displayReverse(struct Node *head)
{
    struct Node *ptr = head, *prev;
    while(ptr != NULL)
    {
        prev = ptr;
        ptr = ptr->next;
    }
    ptr = prev;
    while(ptr != NULL)
    {
        printf("%d ", ptr->val);
        ptr = ptr->prev;
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    struct Node *head = getBinaryRepresentation(N);
    printf("DLL: ");
    display(head);
    printf("\nReverse DLL: ");
    displayReverse(head);
    return 0;
}