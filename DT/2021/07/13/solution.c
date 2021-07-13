#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int val;
    struct Node *next;
};
struct Node *head = NULL, *tail = NULL;
struct Node* deleteNodesAtEvenPositions(struct Node *head)
{
    struct Node* x=head;
    while(x){
        if(x->next){
            x->next=x->next->next;
            x=x->next;
        }
        else{
            break;
        }
    }
    return head;
}
void append(int val)
{
    struct Node newNode = malloc(sizeof(struct Node));
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

int main()
{
    int totalNodes, val;
    scanf("%d", &totalNodes);
    for(int ctr = 1; ctr <= totalNodes; ctr++)
    {
        scanf("%d", &val);
        append(val);
    }
    head = deleteNodesAtEvenPositions(head);
    printf("Revised Singly Linked List: ");
    display(head);
    return 0;
}