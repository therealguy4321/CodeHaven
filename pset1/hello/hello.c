#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompts user for name
    string name = get_string("What's your name? ");

    //prints out given name
    printf("Hello, %s\n", name);
}