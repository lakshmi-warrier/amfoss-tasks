#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float to_dollar[] = {25, 10, 5, 1};   //array to store each corresponding values in dollars
    float owe = get_float("O hai! How much change is owed?\n");

    while(owe < 0)
        owe = get_float("Try again, How much change is owed?\n");

    int coinNums = 0;
    
    owe = owe*100; //converting to cents
    int cents = round(owe); //to get rid of all the irrelevent digits that joins along a float
    for(int i=0; i<4; i++)
    {
        while(cents >= to_dollar[i])
        {
            coinNums ++;
            cents -= to_dollar[i];
        }
    }
     printf("%i", coinNums);
}
