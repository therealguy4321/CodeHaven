// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//declare variables
unsigned int word_count = 0;
unsigned int hash_value;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    hash_value = hash(word);
    node *cursor = table[hash_value];

    //go through the linked list
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor -> word) == 0)
        {
            return true;
        }
        cursor = cursor -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long total = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        total += tolower(word[i]);
    }
    return total % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //open dictionary
    FILE *file = fopen(dictionary, "r");

    //if return value = NULL
    if (file == NULL)
    {
        printf("Unable to open %s\n", dictionary);
        return false;
    }

    //declare a variable called word
    char word[LENGTH + 1];

    //scan dictionary for strings up till EOF
    while (fscanf(file, "%s", word) != EOF)
    {
        //allocate memory for new node
        node *n = malloc(sizeof(node));

        //if malloc returns NULL, return false
        if (n == NULL)
        {
            return false;
        }

        //copy word into node
        strcpy(n -> word, word);

        //use hash function
        hash_value = hash(word);

        //check if head is pointing to NULL
        if (table[hash_value] == NULL)
        {
            //point n to NULL
            n -> next = NULL;
        }
        else
        {
            //point n to first node of the linked list
            n -> next = table[hash_value];
        }
        //point the header to n
        table[hash_value] = n;
        word_count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_count;
}

void freenode(node *n)
{
    if (n -> next != NULL)
    {
        freenode(n -> next);
    }
    free(n);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            freenode(table[i]);
        }
    }
    return true;
}
