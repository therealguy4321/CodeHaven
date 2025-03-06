#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int column = 0; column < height; column++)
    {
        for (int row = 0; row < width; row++)

        {
            //to get the average rgb values of each pixel and balance them out
            int rgbt = round((image[column][row].rgbtBlue + image[column][row].rgbtGreen + image[column][row].rgbtRed) / 3.0);
            image[column][row].rgbtBlue = image[column][row].rgbtGreen = image[column][row].rgbtRed = rgbt;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int column = 0; column < height; column++)
    {
        for (int row = 0; row < width; row++)

        {
            //implementing the sepia algorithms
            int sepiaBlue = round(.272 * image[column][row].rgbtRed + .534 * image[column][row].rgbtGreen + .131 *
                                  image[column][row].rgbtBlue);
            int sepiaGreen = round(.349 * image[column][row].rgbtRed + .686 * image[column][row].rgbtGreen + .168 *
                                   image[column][row].rgbtBlue);
            int sepiaRed = round(.393 * image[column][row].rgbtRed + .769 * image[column][row].rgbtGreen + .189 *
                                 image[column][row].rgbtBlue);

            image[column][row].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
            image[column][row].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[column][row].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int column = 0; column < height; column++)
    {
        for (int row = 0; row < width / 2; row++)

        {
            //to create a temp variable and swap pixels horizontally
            RGBTRIPLE tmp[height][width];
            tmp[column][row] = image[column][row];
            image[column][row] = image[column][width - (row + 1)];
            image[column][width - (row + 1)] = tmp[column][row];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    //create copy of image
    RGBTRIPLE tmp[height][width];

    for (int column = 0; column < height; column++)
    {
        for (int row = 0; row < width; row++)
        {
            float sumBlue = 0;
            float sumGreen = 0;
            float sumRed = 0;
            float counter = 0;

            //to find the boundary of the image
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)

                {
                    //to prevent working with invalid pixels
                    if (column + x < 0 || column + x > height - 1)
                    {
                        continue;
                    }

                    if (row + y < 0 || row + y > width - 1)
                    {
                        continue;
                    }

                    //sum of the rgb values of the neighbouring pixels
                    sumBlue += image[column + x][row + y].rgbtBlue;
                    sumGreen += image[column + x][row + y].rgbtGreen;
                    sumRed += image[column + x][row + y].rgbtRed;
                    counter++;
                }
            }

            //average of the sum of rgb values
            tmp[column][row].rgbtBlue = round(sumBlue / counter);
            tmp[column][row].rgbtGreen = round(sumGreen / counter);
            tmp[column][row].rgbtRed = round(sumRed / counter);
        }
    }

    for (int column = 0; column < height; column++)
    {
        for (int row = 0; row < width; row++)
        {
            //replacing original rgb values with averaged ones
            image[column][row].rgbtBlue = tmp[column][row].rgbtBlue;
            image[column][row].rgbtGreen = tmp[column][row].rgbtGreen;
            image[column][row].rgbtRed = tmp[column][row].rgbtRed;
        }

    }

    return;
}
