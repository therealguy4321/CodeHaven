#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //check that argument count = 2
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //open file for reading
    FILE *input_file = fopen(argv[1], "r");

    //check that the input_file provided in arg is valid
    if (input_file == NULL)
    {
        printf("Could not open file");
        return 2;
    }

    FILE *output_file = NULL;

    BYTE buffer[512];
    char filename[8];
    int counter = 0;
    while (fread(buffer, sizeof(BYTE), 512, input_file) == 512)
    {
        // checks if start of img in buffer
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if start of img and first image i.e. counter == 0
            // then begins writing a new image
            if (counter == 0)
            {
                sprintf(filename, "%03i.jpg", counter);
                output_file = fopen(filename, "w");
                fwrite(&buffer, sizeof(BYTE), 512, output_file);
                counter ++;
            }

            // if start of img but not first image then
            // closes the image and begins writing new image
            else if (counter > 0)
            {
                fclose(output_file);
                sprintf(filename, "%03i.jpg", counter);
                output_file = fopen(filename, "w");
                fwrite(&buffer, sizeof(BYTE), 512, output_file);
                counter ++;
            }
        }

        // if not start of new img
        // then it keeps on writing the image
        else if (counter > 0)
        {
            fwrite(&buffer, sizeof(BYTE), 512, output_file);
        }

    }

    // Close file
    fclose(input_file);
    fclose(output_file);

    return 0;
}