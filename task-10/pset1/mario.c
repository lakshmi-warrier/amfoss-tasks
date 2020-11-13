#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    while(true)
    {
        n = get_int("Height: ");
        if((n<=23)&&(n>=0)) break;
    }

    for (int i = 1; i < n; i = i + 1)
    {
      for (int j = 0; j < n-i; ++j)
          printf(" ");

      for (int k = 0; k <= i; ++k)
          printf("#");

      printf("\n");
    }

}
