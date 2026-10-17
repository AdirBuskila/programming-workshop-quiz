//Auxiliary function - checks whether all elements of L1 are in L2
int List1_elements_in_List2(Item* L1, Item* L2)
{
    Item* ptr1 = L1, * ptr2 = L2;
    int found;

    /* whether L2 is not shorter L1*/
    while (ptr1 && ptr2)
    {
        ptr1 = ptr1->next;
        ptr2 = ptr2->next;
    }
    if (ptr1 && !ptr2)
        return 0;
    /*---------------------------------*/
    /* searching each element of L1 in L2 */
    ptr1 = L1;
    while (ptr1)
    {
        found = 0;
        ptr2 = L2;
        while (ptr2)
        {
            if (ptr1->data == ptr2->data)
            {
                found = 1;
                break;
            }
            ptr2 = ptr2->next;
        } // while (ptr2)
        if (!found)
            return 0;
        ptr1 = ptr1->next;
    } // while (ptr1)
    /*---------------------------------*/
    return 1;
}

//Auxiliary function
void insert_in_head(int x, Item **pl)
{
    Item *temp = (Item *)malloc(sizeof(Item));
    temp->data = x;
    temp->next = *pl;
    *pl = temp;
}

Item *lists_with_given_elements(Item** A, int n, Item* L)
{
    int i;
    Item *ind_list = NULL;
    for (i = n - 1; i >= 0; i--)
        if (List1_elements_in_List2(L, A[i]))
            insert_in_head(i, &ind_list);
    return ind_list;
}
