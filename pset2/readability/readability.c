#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

//New function
int get_index(string s);
int main(void)
{

    //Ask user for text
    string text = get_string("Text: ");
    int index = get_index(text);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
}

int get_index(string s)
{
    //TODO
    int letters = 0, sentences = 0, words = 0;

    for (int i = 0; i < strlen(s); i++)
    {
        char ch = s[i];

        //If it is an alphabet
        if (isalpha(ch))
        {
            letters++;
        }

        //If there is a space
        if (isspace(ch))
        {
            words++;
        }

        //If there is a '.' or a '!' or a '?'. It is a sentence
        if (ch == '.' || ch == '!' || ch == '?')
        {
            sentences++;
        }
    }
    words++;

    float L = (letters * 100.0f) / words;
    float S = (sentences * 100.0f) / words;

    //Coleman-Liau's index
    return round(0.0588 * L - 0.296 * S - 15.8);
}