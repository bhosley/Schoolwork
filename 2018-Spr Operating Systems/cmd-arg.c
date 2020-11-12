/* main() with command-line arguments          */
/* converts a command-line argument to integer */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
   int i, times;

   printf("The command line has %d arguments (in addition to the command itself):\n", argc - 1);
   for (i = 1; i < argc; i++)
      printf("   argv[%d] points to string \"%s\"\n", i, argv[i]);
	
   if (argc != 3 || (times = atoi(argv[1])) < 1) { // atoi() converts a string to an integer
      printf("Usage: %s positive-number name\n", argv[0]);
      printf("(That is, use two arguments only.)\n");
   }
   else {
      printf("After converting to integer, repeat %d times:\n", times);
      for (i = 0; i < times; i++)
         printf("   %s\n", argv[2]);
   }
}
