#include <cs50.h>
#include <stdio.h>
#include <math.h>

long long cardNumber = 0;
int main(void)

//get card number
{
    do
    {
        printf("input card number here: ");
        cardNumber = get_long_long();
    }
    while(cardNumber <= 0);

    long long cardLength = floor(log10(labs(cardNumber))) + 1;

    long long cardDigits[cardLength];

    for (int i = (cardLength - 1); i >= 0; i--)
    {

        cardDigits[i] = cardNumber % 10;
        cardNumber = floor(cardNumber / 10);
    }

    long long doubleDigit[cardLength];

    for (int j = (cardLength - 2), l = 0; j >= 0; j -= 2, l++)

    {
        doubleDigit[l] = cardDigits[j] * 2;
    }

    int multSum = 0;

    for (int m = 0; m <= ((cardLength - 2) / 2); m++)

    {
        if(doubleDigit[m] > 9)
        {
            multSum = multSum + ((floor(doubleDigit[m] / 10 )) + (doubleDigit[m] % 10));
        }
        else
        {
            multSum = multSum + doubleDigit[m];
        }
    }

    int nonMultSum = 0;

    for (int k = cardLength - 1; k >= 0; k -= 2)
    {
        int nonDoubleDigit = cardDigits[k];
        nonMultSum = nonMultSum + nonDoubleDigit;
    }

    if ((multSum + nonMultSum) % 10 == 0)
    {
        switch(cardDigits[0])
        {
            case 3:
                if(cardDigits[1] == 4 || cardDigits[1] == 7)
                {
                    printf("AMEX\n");
                }
                break;

            case 4:
                printf("VISA\n");
                break;

            case 5:
                if (cardDigits[1] == 1 || cardDigits[1] == 2 || cardDigits[1] == 3 || cardDigits[1] == 4 || cardDigits[1] == 5)
                {
                    printf("MASTERCARD\n");
                }
                break;
        }
    }
    else
    
    {
        printf("INVALID\n");
    }

    return 0;
}