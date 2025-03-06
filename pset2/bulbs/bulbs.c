#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    //get text from user
    string text = get_string("Text: ");

    //convert text to decimal
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        int decimal = text[i];

        int binary[] = {0, 0, 0, 0, 0, 0, 0, 0};

        int j = 0;

        //convert decimal to binary
        while (decimal > 0)
        {
            binary[j] = decimal % 2;
            decimal = decimal / 2;
            j++;
        }

        //reverse converted value to give the correct binary value
        for (int k = BITS_IN_BYTE - 1; k >= 0; k--)
        {
            print_bulb(binary[k]);
        }
        printf("\n");
    }

}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
