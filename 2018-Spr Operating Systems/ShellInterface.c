/*
 * Author: Brandon Hosley, bhosl2, bhosl2@uis.edu
 * Compile using the GCC program.
 * Description: This program emulates a Shell OS 
 *  
 * The two main functions it serves is as a wrapper to evoke
 * a number of functions borrowed from the Linux operating system.
 * it does so in a manner that will allow additional functionaility
 * to be added trivially.
 * Second, the program demonstrates usage of the fork() functionality
 * of a unix system to create new processes, the new processes will
 * execute the desired function before closing itself.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_CMD_LENGTH 80  // the max length of characters for each command

const char ACCEPTABLE_CALLS[6][6] = {"cal","date","ls","ps","pwd","who"};

int isAcceptableCommand(char s[])
{
    for(int i=0; i<(sizeof(ACCEPTABLE_CALLS)); i++)
    {
        if(strcmp(ACCEPTABLE_CALLS[i], s) == 0)
        { 
            return 1; 
        }
    }
    return 0;
};

void help()
{
   printf("Available Commands. Type:\n");
   printf("cal : to display a calendar for this month.\n");
   printf("date : to display the date.\n");
   printf("ls : to display the contents of the current directory.\n");
   printf("ps : to display current processes.\n");
   printf("pwd : prints the address of current directory.\n");
   printf("who : prints the username of the current user.\n");
};

int main(int argc, char* argv[])
{
    int i, MAX_CMD_NUMBER;
    char command[MAX_CMD_LENGTH];
    
    /*
     * Determine number of Commands
     */

    if (atoi(argv[1]) > 0 && atoi(argv[1]) < 10)
    {
        MAX_CMD_NUMBER = atoi(argv[1]);
    }
    else
    {
        MAX_CMD_NUMBER = 10;
    }

    /*
     * Accept input
     */

    for (i = 0; i < MAX_CMD_NUMBER; i++)
    {
        printf("COMMAND-> ");
        fflush(stdout);
        scanf("%s", command);  // takes in the user's single-string command
        
        if (strcmp(command, "quit") == 0)
        {
            i = MAX_CMD_NUMBER;  // terminate the loop
        }
        else if (strcmp(command, "help") == 0)
        {
            help();
        }
        else if (isAcceptableCommand(command) == 1)
        {
            int rc = fork();
            if (rc < 0) {
                // fork failed; exit
                exit(1);
            } 
            else if (rc == 0) 
            {
                // Child Does the Command
                char *args[]={command,NULL};
                execvp(args[0],args);
                exit(0);
            }
            else 
            {
                int wc = wait(NULL); // Parent Waits
            }
        }
        else
        {
            printf("Command %s is unrecognized.\n", command);
            printf("Type \"help\" for list of commands.\n");
        }
    }
}

