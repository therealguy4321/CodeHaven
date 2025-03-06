#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("height: ");

    }

    while (h < 1 || h > 8);

    //For each row
    for (int i = 0; i < h; i++)
    {
        //For each column
        for (int j = 0; j < h; j++)
        {
            if (i + j < h - 1)

            {
                printf(" ");
            }
            else
                //Print a brick
            {
                printf("#");
            }
        }



        //Move to the next row
        printf("\n");
    }


}