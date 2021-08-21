#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *prev, *next;
};

struct Node *head=NULL, *tail=NULL;

void append(int data)
{
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = data;
    if(head == NULL)
    {
        head = tail = newNode;
    }
    else
    {
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
    tail->next = head;
    head->prev = tail;
}

void display(struct Node *head)
{
    struct Node *ptr = head;
    while(ptr->next != head)
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf("%d", ptr->data);
}

void displayReverse(struct Node *head)
{
    struct Node *ptr = head->next, *prev = head, *tail;
    while(ptr != head)
    {
        prev = ptr;
        ptr = ptr->next;
    }
    ptr = prev;
    tail = prev;
    do
    {
        printf("%d ", ptr->data);
        ptr = ptr->prev;
    }
    while(ptr != tail);
}

struct Node* getNode(struct Node *head, int N)
{
    if(N <= 0)
    {
        return NULL;
    }
    int ctr = 1;
    struct Node *ptr = head;
    while(ctr < N)
    {
        ptr = ptr->next;
        ctr++;
    }
    return ptr;
}
 
struct Node* deleteAtMiddle(struct Node *head)
{
    if(head->next==head){
        free(head);
        return NULL;
    }
    else{
        struct Node *t=head;
        int l=0;
        while(t->next!=head){
            l++;
            t=t->next;
        }
        t=getNode(head,l/2);
        struct Node *m=t->next;
        t->next->next->prev=t;
        t->next=t->next->next;
        free(m);
        return head;
    }
}

int main()
{
    int totalNodes, data;
    scanf("%d", &totalNodes);
    for(int ctr = 1; ctr <= totalNodes; ctr++)
    {
        scanf("%d", &data);
        append(data);
    }

    struct Node *mid = getNode(head, (totalNodes+1)/2);
    struct Node *midPrev = mid->prev, *midNext = mid->next;

    struct Node *ptr = deleteAtMiddle(head);

    if(ptr == NULL)
    {
        printf("CDLL:\nList is empty");
        return;
    }

    if((midPrev->next != midNext) || (midNext->prev != midPrev))
    {
        printf("Middle Node not deleted properly in CDLL\n");
    }
    printf("CDLL:\n");
    display(ptr);
    printf("\n");
    displayReverse(ptr);
    return 0;
}