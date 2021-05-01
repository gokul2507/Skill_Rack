int findMinimum(int arr[], int len)
{
    int index, min = arr[0];
    for(index = 0; index < len; index++)
    {
        if(arr[index] < min)
        {
            min = arr[index];
        }
    }
    return min;
}
