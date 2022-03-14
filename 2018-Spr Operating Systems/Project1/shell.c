#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <time.h>
#include <unistd.h>
#include <limits.h>
#include <sys/procfs.h> 

#define MAX_CMD_NUMBER 5   // this shell program accepts no more than this amount of commands
#define MAX_CMD_LENGTH 80  // the max length of characters for each command

int main(int argc, char* argv[])
{
   int i;
   char command[MAX_CMD_LENGTH];
   
   for (i=0; i< MAX_CMD_NUMBER; i++) {
      printf("COMMAND-> ");
      fflush(stdout);
      scanf("%s", command);  // takes in the user's single-string command
      if (strcmp(command, "quit") == 0)
      {
         i = MAX_CMD_NUMBER;  // terminate the loop
      } 
      else if (strcmp(command, "cal") == 0)
      {
         pid_t  pid;
         pid = fork();
         if (pid == 0)
            cal();
      }
      else if (strcmp(command, "date") == 0)
      {
         pid_t  pid;
         pid = fork();
         if (pid == 0)
            date();
      }
      else if (strcmp(command, "ls") == 0)
      {
         pid_t  pid;
         pid = fork();
         if (pid == 0)
            ls(int argc, char* argv[]);
      }
      else if (strcmp(command, "ps") == 0)
      {
         pid_t  pid;
         pid = fork();
         if (pid == 0)
            ps();
      }
      else if (strcmp(command, "pwd") == 0)
      {
         pid_t  pid;
         pid = fork();
         if (pid == 0)
            pwd();
      }
      else if (strcmp(command, "who") == 0)
      {
         pid_t  pid;
         pid = fork();
         if (pid == 0)
            who();
      }
      else if (strcmp(command, "help") == 0)
      {
         pid_t  pid;
         pid = fork();
         if (pid == 0)
            help();
      }
      else
         printf("Command %s is unrecognized.\n Type \"help\" for list of commands", command);
   }
};
void cal(){};
void date()
{
   time_t current_time = time(NULL);
   struct tm *tm = localtime(&current_time);
   printf("\nCurrent Date and Time:\n");
   printf("%s\n", asctime(tm));
};
void ls(int argc, char* argv[])
{
    DIR *mydir;
    struct dirent *myfile;
    struct stat mystat;

    char buf[512];
    mydir = opendir(argv[1]);
    while((myfile = readdir(mydir)) != NULL)
    {
        sprintf(buf, "%s/%s", argv[1], myfile->d_name);
        stat(buf, &mystat);
        printf("%zu",mystat.st_size);
        printf(" %s\n", myfile->d_name);
    }
    closedir(mydir);
};
void ps()
{
   int fdproc; 
   DIR *dirp; 
   struct prpsinfo pinfo;  
   /* 
   * loop for each process in the system 
   */ 
   while(dirent = readdir(dirp)) { 
      if (dirent->d_name[0] != '.') { 
         strcpy(procbuf, "/proc/"); 
         strcat(procbuf, dirent->d_name); 
         if ((fdproc = open(procbuf, O_RDONLY)) < 0) 
         { 
            continue; 
         }; 
         /* 
         * get the ps status for the process 
         */ 
         if (ioctl(fdproc, PIOCPSINFO, &pinfo) < 0) 
         { 
            close(fdproc); 
            continue; 
         } ;
         close(fdproc); 
         } 
      }
};
void pwd()
{
   char cwd[PATH_MAX];
   if (getcwd(cwd, sizeof(cwd)) != NULL) 
   {
       printf("Current working dir: %s\n", cwd);
   }
};
void who(){};
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