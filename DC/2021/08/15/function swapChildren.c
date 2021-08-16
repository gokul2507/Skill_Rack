#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *left, *right; 
};

struct Node *root;

struct Node* createNode(int data)
{
    struct Node *newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void insertNode(struct Node *node, int rootData, int data, char pos)
{
    if(node != NULL)
    {
        if(node->data == rootData)
        {
            if(pos == 'l' && node->left == NULL)
            {
                node->left = createNode(data);
            }
            else if(pos == 'r' && node->right == NULL)
            {
                node->right = createNode(data);
            }
            else
            {
                printf("Left & Right Nodes are already present\n");
            }
            return;
        }
        insertNode(node->left, rootData, data, pos);
        insertNode(node->right, rootData, data, pos);
    }
}

void printPreorder(struct Node *root)
{
    if(root == NULL)
    {
        return;
    }
    printf("%d ", root->data);
    printPreorder(root->left);
    printPreorder(root->right);
}
 
void swapChildren(struct Node *root, int X)
{
if(root==NULL){
    return;
}
else{
    if(root->left && root->right && root->data==X){
        struct Node *temp=root->left;
        root->left=root->right;
        root->right=temp;
    }
    swapChildren(root->left,X);
    swapChildren(root->right,X);
}
}

int main()
{
    int N, rootData, data;
    char pos;
    scanf("%d", &N);
    scanf("%d", &rootData);
    root = createNode(rootData);
    for(int ctr = 2; ctr <= N; ctr++)
    {
        scanf("\n%d %d %c", &rootData, &data, &pos);
        insertNode(root, rootData, data, tolower(pos));
    }
    int X;
    scanf("%d", &X);
    printf("Before Swap: ");
    printPreorder(root);
    swapChildren(root, X);
    printf("\nAfter Swap: ");
    printPreorder(root);
    return 0;
}