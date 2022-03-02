#include <stdio.h>

int main()
{
    /**
    * Example 1
    */
    int a = 10;
    int b = ++a;
    printf("a: %d, b: %d\n", a, b);//a = 11, b = 11
    a = 10;
    int c = a++;
    printf("a: %d, c: %d\n", a, c);//a = 11, c = 10

    
    /**
    * Example 2
    */
    int f = 10;
    int d = 5;
    f += ++d;
    printf("f: %d, d: %d\n", f, d);//f = 16, d = 6

    
    /**
    * Example 3
    */
    a = 5;
    b = 10;
    if (++a == 5 & ++b == 11)
    {
        printf("%s\n", "Condition is True");
    }
    printf("a: %d, b: %d\n", a, b);//a = 6, b = 11

    
    /**
    * Example 4
    */
    a = 5;
    b = 10;
    if (++a == 5 && ++b == 11)
    {
        printf("%s\n", "Condition is True");
    }
    printf("a: %d, b: %d\n", a, b);//a = 6, b = 10

    return 0;
}
