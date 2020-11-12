/* 

Author: (Brandon Hosley, bhosl2, bhosl2@uis.edu)
 
Compile: (compile using gcc)
 
Brief Description: (This program similates a job scheduler and handler 
      by parsing a series of prefix expressions and posting the result.
      The program uses semaphores to manage concurrent processing of 
      the operations.)

*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h> 
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include "semshm.c"

#define NUM_OF_SEMS 12         /* the number of sems to create */
#define OK_TO_LOAD0 0
#define OK_TO_LOAD1 1
#define OK_TO_LOAD2 2
#define OK_TO_EXEC0 3
#define OK_TO_EXEC1 4
#define OK_TO_EXEC2 5
#define OK_TO_SET_OUTPUT0 6
#define OK_TO_SET_OUTPUT1 7
#define OK_TO_SET_OUTPUT2 8
#define OK_TO_PRINT0 6
#define OK_TO_PRINT1 10
#define OK_TO_PRINT2 11
#define HOWMANY_PROCESSES 3
#define HOWMANY_JOBS 3
#define TRUE 1
#define FALSE 0

int my_semid, my_shrmemid;    /* semaphore id and shared memory ids */
int my_key;                   /* key used to get shared memory */
int my_semval;
char *my_shrmemaddr;          /* address of shared memory */
typedef struct _pcb
   {int start_loc, num_instructions, output_loc;}
   pcb_type;
typedef struct _mem
   {char operation; int operand1, operand2, result;}
   memory_type;
pcb_type *pcbs;
memory_type *memory;
int *load_job, *print_job, size_of_memory, s, i, concurrent_processes;

/* functions to be invoked later */
void P();              /* acquire semaphore */
void V();              /*release semaphore */
static void semcall(); /* call semop */
void init_sem();       /* initialize semaphores */
void remove_shrmem();  /* remove shared memory */
void remove_sem();     /* remove semaphores */
void driver();         /* driver for forking processes */
void loader();
void cpu();
void printer();
void execute_memory();
void print_memory();
int fill_memory();	

int main (int argc,char* argv[]) 
{ /* this program uses semaphores and shared memory. Semaphores are
     used to protect the shared memory which serves as a message area
     for and sender and receiver process                             */
   int i ;
   setbuf(stdout, NULL);  
   // Check for process switch
   if (*argv[1]=='3')
   {
      concurrent_processes = 3;
   }
   else if (*argv[1]=='2')
   {
      concurrent_processes = 2;
   }
   else
   {
      puts("Invalid number of concurrent processes");
      exit(0);
   } 
   /* get semaphore id and a given number of semaphores */
   if ((my_semid = semtran(NUM_OF_SEMS)) != -1) 
   {
   /* initialize the semaphores */
   init_sem(my_semid,OK_TO_LOAD0, 1);
   init_sem(my_semid,OK_TO_LOAD1, 1);
   init_sem(my_semid,OK_TO_EXEC0, 0);
   init_sem(my_semid,OK_TO_EXEC1, 0);
   init_sem(my_semid,OK_TO_SET_OUTPUT0, 1);
   init_sem(my_semid,OK_TO_SET_OUTPUT1, 1);
   init_sem(my_semid,OK_TO_PRINT0, 0);
   init_sem(my_semid,OK_TO_PRINT1, 0);
   }
   if (concurrent_processes=='3')
   {
      concurrent_processes = 3;
      init_sem(my_semid,OK_TO_LOAD2, 1);
      init_sem(my_semid,OK_TO_EXEC2, 0);
      init_sem(my_semid,OK_TO_SET_OUTPUT2, 1);
      init_sem(my_semid,OK_TO_PRINT2, 0);
   }
   /* get shared memory segement id and attach it to my_shrmemaddr */
   size_of_memory = 2*sizeof(*load_job) + 2*sizeof(*print_job) + 
                    4*sizeof(*pcbs) + (20*concurrent_processes) * sizeof(*memory);
    if ((get_attach_shrmem(size_of_memory,&my_shrmemaddr,&my_shrmemid)) != -1)
    /* connect to shared memory at my_shrmemaddr */
    load_job = (int *) my_shrmemaddr;
   print_job = load_job + 2;
   pcbs = (pcb_type *) (print_job + 2);
   memory = (memory_type *) (pcbs + 4);
   /* call driver to do the work of forking senders and receivers */
   driver(argv[2]); // Pass the name of the input file
   /* wait until all processes have completed their work */
    if (concurrent_processes=='2')
        for (i = 1; i <= HOWMANY_PROCESSES; i++) wait(&s);
    else
        for (i = 1; i <= HOWMANY_PROCESSES; i++) wait(&s);
   printf("The End.\n\n");
   remove_sem(my_semid); /* remove the semaphores */
   remove_shrmem(my_shrmemid, my_shrmemaddr); /* remove the shared memory */
   exit(0);
}  /* end of main */

void driver(char filename[]) /* driver to fork processes to handle the work */
{
   int pid;
   
   if (( pid = fork() ) == -1) syserr("fork");
   if ( pid == 0 )
   {
      loader(filename);
      exit(0);
   }
   if (( pid = fork() ) == -1) syserr("fork");
   if ( pid == 0 )
   {
      cpu();
      exit(0);
   }
   if (( pid = fork() ) == -1) syserr("fork");
   if ( pid == 0 )
   {
      printer();
      exit(0);
   }
} /* end of driver */

void loader(char filename[])
{
   FILE *fid;
   int memory_to_load, current_job, more_jobs, job_read;
   
   if ((fid = fopen (filename, "r")) == 0)
   {
      puts ("Unable to open file for reading.");
      exit(0);
   }

   more_jobs = concurrent_processes;    
   current_job = 0; 
   while (more_jobs)
   {
      if (current_job == 0)
      {
         P(my_semid, OK_TO_LOAD0);
         memory_to_load = 0;
         pcbs[current_job].start_loc = 0;
         pcbs[current_job].output_loc = 30;
         pcbs[current_job].num_instructions = 0;
         job_read = fill_memory(fid, memory_to_load);
         if (job_read != 4)
         {
            more_jobs = more_jobs - 1;
            load_job[current_job] = -1;
         }
         else
            load_job[current_job] = 1;
         V(my_semid, OK_TO_EXEC0);
      }                            
      else if (current_job == 1) 
      {
         P(my_semid, OK_TO_LOAD1);
         memory_to_load = 10;
         pcbs[current_job].start_loc = 10;
         pcbs[current_job].output_loc = 40;
         pcbs[current_job].num_instructions = 0;
         job_read = fill_memory(fid, memory_to_load);
         if (job_read != 4)
         {
            more_jobs = more_jobs - 1;
            load_job[current_job] = -1;
         }
         else
            load_job[current_job] = 1;
         V(my_semid, OK_TO_EXEC1);
      }
      else
      {
         P(my_semid, OK_TO_LOAD2);
         memory_to_load = 10;
         pcbs[current_job].start_loc = 20;
         pcbs[current_job].output_loc = 50;
         pcbs[current_job].num_instructions = 0;
         job_read = fill_memory(fid, memory_to_load);
         if (job_read != 4)
         {
            more_jobs = more_jobs - 1;
            load_job[current_job] = -1;
         }
         else
            load_job[current_job] = 1;
         V(my_semid, OK_TO_EXEC2);
      }                            
      current_job = (current_job + 1) % concurrent_processes;
   } /* end while more_jobs */
   fclose(fid);
   return;
} /* end of load */

int fill_memory (FILE *fid, int memory_to_fill)
{
   int opcode_ok, end_of_job, bad_instruction, operand1, operand2, elements_read, current_pcb;
   char opcode, cr;

   if (memory_to_fill == 0)
      current_pcb = 0;
   else 
      current_pcb = 1;
   elements_read = TRUE;
   end_of_job = FALSE;
   while (elements_read )
   { 
      elements_read = fscanf (fid, "%c %d %d%c", &opcode, &operand1, &operand2,&cr);
      if (elements_read != 4)
      { 
         return(elements_read);
      }
      else
      {
         switch (opcode)
         {
            case '+':
               opcode_ok = TRUE;
               break;
            case '-':
               opcode_ok = TRUE;
               break;
            case '*':
               opcode_ok = TRUE;
               break;
            case '/':
               opcode_ok = TRUE;
               break;
            case '%':
               opcode_ok = TRUE;
               break;
            default :
               if (opcode == '?') 
               {
                  bad_instruction = FALSE;
                  end_of_job = TRUE;
               }
               else
               {
                  end_of_job = FALSE; 
                  opcode_ok = FALSE;
		          bad_instruction = TRUE;
		       };
         } /* end of switch */
      } /* end of else elements read was 4 */
      if (end_of_job == TRUE)
         return(elements_read);
      pcbs[current_pcb].num_instructions = pcbs[current_pcb].num_instructions + 1;
      memory[memory_to_fill].operation = opcode;
      memory[memory_to_fill].operand1 = operand1;
      memory[memory_to_fill].operand2 = operand2;
      memory_to_fill = memory_to_fill + 1;
   } /* end of while  for fill memory */
} /* end of fill memory */         

void cpu()
{
   int memory_to_execute, current_job, where_to_output, memory_to_output, more_jobs;
   
   current_job = 0;    
   more_jobs = concurrent_processes;
   while (more_jobs)
   {                                                                  
      if (current_job == 0)                                            
      {                                                              
         P(my_semid, OK_TO_EXEC0);
         if (load_job[current_job] == -1)
         {
            more_jobs = more_jobs -1;
            P(my_semid, OK_TO_SET_OUTPUT0);
            print_job[current_job] = -1;
            V(my_semid, OK_TO_LOAD0);
            V(my_semid, OK_TO_PRINT0);
         }
         else
         {  
            execute_memory(current_job);
            P(my_semid, OK_TO_SET_OUTPUT0);
            pcbs[current_job + 2] = pcbs[current_job];
            memory_to_output = pcbs[current_job + 2].start_loc;
            where_to_output = pcbs[current_job + 2].output_loc;
            for (i = 1; i <= pcbs[current_job + 2].num_instructions; i++)
            {
               memory[where_to_output] = memory[memory_to_output];
               memory_to_output = memory_to_output + 1;
               where_to_output = where_to_output + 1;
            }
            load_job[current_job] = 0;
            print_job[current_job] = 1;
            V(my_semid, OK_TO_LOAD0);
            V(my_semid, OK_TO_PRINT0);
         } /* end for else for load job[current_job] != -1  */
      }  
      else if (current_job == 1)
      {        
         P(my_semid, OK_TO_EXEC1);
         if (load_job[current_job] == -1)
         {
            more_jobs = more_jobs -1;
            P(my_semid, OK_TO_SET_OUTPUT1);
            print_job[current_job] = -1;
            V(my_semid, OK_TO_LOAD1);
            V(my_semid, OK_TO_PRINT1);
         }
         else
         {            
            execute_memory(current_job);
            P(my_semid, OK_TO_SET_OUTPUT1);                                       
            pcbs[current_job + 2] = pcbs[1];
            memory_to_output = pcbs[current_job + 2].start_loc;
            where_to_output = pcbs[current_job + 2].output_loc;
            for (i = 1; i <= pcbs[current_job + 2].num_instructions; i++)
            {
               memory[where_to_output] = memory[memory_to_output];
               memory_to_output = memory_to_output + 1;
               where_to_output = where_to_output + 1;
            }
            load_job[current_job] = 0;
            print_job[current_job] = 1;
            V(my_semid, OK_TO_LOAD1);
            V(my_semid, OK_TO_PRINT1);
         } /* end for else for load job[1] != -1  */
      }
      else /* current_job != 0 */
      {        
         P(my_semid, OK_TO_EXEC2);
         if (load_job[current_job] == -1)
         {
            more_jobs = more_jobs -1;
            P(my_semid, OK_TO_SET_OUTPUT2);
            print_job[current_job] = -1;
            V(my_semid, OK_TO_LOAD2);
            V(my_semid, OK_TO_PRINT2);
         }
         else
         {            
            execute_memory(current_job);
            P(my_semid, OK_TO_SET_OUTPUT2);                                       
            pcbs[current_job + 2] = pcbs[1];
            memory_to_output = pcbs[current_job + 2].start_loc;
            where_to_output = pcbs[current_job + 2].output_loc;
            for (i = 1; i <= pcbs[current_job + 2].num_instructions; i++)
            {
               memory[where_to_output] = memory[memory_to_output];
               memory_to_output = memory_to_output + 1;
               where_to_output = where_to_output + 1;
            }
            load_job[current_job] = 0;
            print_job[current_job] = 1;
            V(my_semid, OK_TO_LOAD2);
            V(my_semid, OK_TO_PRINT2);
         } /* end for else for load job[1] != -1  */
      }
      current_job = (current_job + 1) % concurrent_processes;
   } /* end while more jobs */                                    
} /* end of cpu */

void execute_memory(int current_job)
{  
   int memory_to_execute, i;

   if (current_job == 0)
      memory_to_execute = 0;
   else 
      memory_to_execute = 10;
   for ( i = 1; i <= pcbs[current_job].num_instructions; i++)
   {
      switch (memory[memory_to_execute].operation)        
      {                                                  
         case '+':                                          
            memory[memory_to_execute].result =              
               memory[memory_to_execute].operand1 +         
               memory[memory_to_execute].operand2 ;         
            break;                                          
         case '-':                                         
            memory[memory_to_execute].result =              
               memory[memory_to_execute].operand1 -         
               memory[memory_to_execute].operand2 ;         
            break;                                          
         case '*':                                         
            memory[memory_to_execute].result =              
               memory[memory_to_execute].operand1 *         
               memory[memory_to_execute].operand2 ;         
            break;                                          
         case '/':                                         
            memory[memory_to_execute].result =              
               memory[memory_to_execute].operand1 /         
               memory[memory_to_execute].operand2 ;         
            break;                                          
         case '%':                                         
            memory[memory_to_execute].result =              
               memory[memory_to_execute].operand1 %         
               memory[memory_to_execute].operand2 ;         
            break;                                          
      } /* end of switch */                              
      memory_to_execute = memory_to_execute + 1;        
   }
}  /* end execute_memory */

void printer() /* print jobs */
{
   int memory_to_print, current_print_job, more_print_jobs;

   current_print_job = 0;
   more_print_jobs = concurrent_processes;
   while (more_print_jobs)  
   {
      if (current_print_job == 0)
      {
         P(my_semid, OK_TO_PRINT0);
         if (print_job[current_print_job] == -1)
         {
            more_print_jobs = more_print_jobs - 1;
            V(my_semid, OK_TO_SET_OUTPUT0);
         }
         else
         {
            memory_to_print = 20;
            print_memory(current_print_job, memory_to_print); 
            print_job[current_print_job] = 0;
            V(my_semid, OK_TO_SET_OUTPUT0);
         }
      } /* end for current_print_job == 0 */
      else if (current_print_job == 1)
      {
         P(my_semid, OK_TO_PRINT1);
         if (print_job[current_print_job] == -1)
         {
            more_print_jobs = more_print_jobs - 1;
            V(my_semid, OK_TO_SET_OUTPUT1);
         }
         else
         {
            memory_to_print = 30;
            print_memory(current_print_job, memory_to_print);
            print_job[current_print_job] = 0;
            V(my_semid, OK_TO_SET_OUTPUT1);
         }
      } 
      else 
      {
         P(my_semid, OK_TO_PRINT2);
         if (print_job[current_print_job] == -1)
         {
            more_print_jobs = more_print_jobs - 1;
            V(my_semid, OK_TO_SET_OUTPUT2);
         }
         else
         {
            memory_to_print = 40;
            print_memory(current_print_job, memory_to_print);
            print_job[current_print_job] = 0;
            V(my_semid, OK_TO_SET_OUTPUT2);
         }
      } /* end of else for current_print_job */
      current_print_job = (current_print_job + 1) % concurrent_processes;
   }  /* end of while */
} /* end of printer */

void print_memory(int current_print_job, int memory_to_print)
{
   int i;
   
   printf("output for current job %d \n", current_print_job);
   for (i = 1; i <= pcbs[current_print_job + 2].num_instructions; i++)
   {
      printf("%c %d %d %d \n",
	     memory[memory_to_print].operation,
         memory[memory_to_print].operand1,
         memory[memory_to_print].operand2,
         memory[memory_to_print].result );
      memory_to_print = memory_to_print + 1;
   }
   printf("\n");   
} /* end of print_memory */
