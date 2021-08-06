#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int val;
    struct Node *next;
};

struct Node *head1 = NULL, *tail1 = NULL, *head2 = NULL, *tail2 = NULL;

void appendFirstList(int val)
{
    struct Node *newNode = malloc(sizeof *newNode);
    newNode->val = val;
    newNode->next = NULL;
    if(head1 == NULL)
    {
        head1 = tail1 = newNode;
    }
    else
    {
        tail1->next = newNode;
        tail1 = newNode;
    }
}

void appendSecondList(int val)
{
    struct Node *newNode = malloc(sizeof *newNode);
    newNode->val = val;
    newNode->next = NULL;
    if(head2 == NULL)
    {
        head2 = tail2 = newNode;
    }
    else
    {
        tail2->next = newNode;
        tail2 = newNode;
    }
}

struct Node* getNode(struct Node *head, int K)
{
    int ctr = 1;
    struct Node *ptr = head;
    while(ctr < K)
    {
        ptr = ptr->next;
        ctr++;
    }
    return ptr;
}

void display(struct Node *head)
{
    if(head == NULL)
    {
        printf("-1");
        return;
    }
    struct Node *ptr = head;
    while(ptr != NULL)
    {
        printf("%d ", ptr->val);
        ptr = ptr->next;
    }
}
 
struct Node * insertLinkedList(struct Node *h1, struct Node * h2,  int k){
    struct Node *a=getNode(h1,k),*b=a->next;
    a->next=h2;
    tail2->next=b;
    return h1;
}

int main()
{
    int totalNodes1, totalNodes2, val;
    scanf("%d", &totalNodes1);
    for(int ctr = 1; ctr <= totalNodes1; ctr++)
    {
        scanf("%d", &val);
        appendFirstList(val);
    }
    scanf("%d", &totalNodes2);
    for(int ctr = 1; ctr <= totalNodes2; ctr++)
    {
        scanf("%d", &val);
        appendSecondList(val);
    }
    int K;
    scanf("%d", &K);
    if(K > totalNodes1)
    {
        printf("K not in boundary");
    }
    struct Node *kThNode = getNode(head1, K), *kThNodeNext = kThNode->next;
    struct Node *head = insertLinkedList(head1, head2, K);
    if(kThNode->next != head2 || tail2->next != kThNodeNext)
    {
        printf("Linked List not inserted properly");
    }
    printf("Linked List:\n");
    display(head);
    return 0;
}

