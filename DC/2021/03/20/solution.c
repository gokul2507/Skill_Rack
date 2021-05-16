struct Node* deleteThirdNode(struct Node *head)
{
    head->next->next=head->next->next->next;
    return head;
}
