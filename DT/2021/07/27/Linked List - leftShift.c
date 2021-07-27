#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int val;
    struct Node *next;
};
struct Node *head = NULL, *tail = NULL;

void append(int val)
{
    struct Node *newNode = malloc(sizeof(struct Node*));
    newNode->val = val;
    newNode->next = NULL;
    if(head == NULL)
    {
        head = tail = newNode;
    }
    else
    {
        tail->next = newNode;
        tail = newNode;
    }
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

struct Node* getNode(struct Node *head, int N)
{
    int ctr = 1;
    struct Node *ptr = head;
    while(ctr < N)
    {
        ptr = ptr->next;
        ctr++;
    }
    return ptr;
}
 
struct Node* leftShift(struct Node *head, int x)
{
      struct Node *temp=head;
    struct Node *end=NULL;
    int len=0;
    while(temp){
        end=temp;
        temp=temp->next;
        len++;
    }
    temp=end;
    x=x%len;
    while(x--){
        temp->next=head;
        temp=temp->next;
        head=head->next;
        temp->next=NULL;
    }
    return head;
}
int main()
{
    int totalNodes, val, X;
    scanf("%d", &totalNodes);
    for(int ctr = 1; ctr <= totalNodes; ctr++)
    {
        scanf("%d", &val);
        append(val);
    }
    scanf("%d", &X);
    struct Node *ptr = getNode(head, (X%totalNodes)+1);
    struct Node *revisedHead = leftShift(head, X);
    if(revisedHead != ptr)
    {
        printf("List is not left shifted properly");
    }
    printf("Singly Linked List: ");
    display(revisedHead);
    return 0;
}