#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    // TODO: Prompt for end size
    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold
    int current = start;
    int years = 0;
    while (current < end)
    {
        current = round(current + (current / 3) - (current / 4));
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i \n", years);
}
