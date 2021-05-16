int printValue(int a, int b, int c)
{
    int result, min, mid, max;
    max = (a > b) ? ((a > c) ? a : c):((b > c) ? b : c);
    min = (a < b) ? ((a < c) ? a : c):((b <c ) ? b : c);
    mid = (a + b + c) - (min + max);
    result = (max * min - mid);
    return result;
}
