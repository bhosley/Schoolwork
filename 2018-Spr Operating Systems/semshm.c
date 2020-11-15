/* There is no need to modify this C program file for CSC389 projects. */

/* ------------------- semshm.c ---------------------------- */
/* Semaphore and shared memory routines -------------------- */

#define BADADDR (char *)(-1)  /* used in getting shared memeory */ 

void syserr();         /* print error messages */

void remove_sem(int sid) /* Used to remove semaphore with id sid */
{ 
   (void)semctl(sid,0,IPC_RMID,0);
}

int semtran(int nsems) /* Used to translate semaphore key to ID; Number of semaphores in the array of semaphores */
{
   int sid;
   
   if ((sid = semget(IPC_PRIVATE,nsems,0666|IPC_CREAT)) == -1)
      syserr("semget");
   return(sid); /* Returns the semaphore id in sid */
}

static void semcall(int sid, struct sembuf sb) /* Calls semop to perform the operation described in the structure sb        */
{
   if (semop(sid,&sb,1) == -1)
      syserr("semop");
}

void P(int sid, int which_sem) /* Will setup the sb structure for decrementing */
                       /* the semaphore for sid then calls semcall above */
                       /* to perform the P operation on the semaphore    */
{
   struct sembuf sb;
   
   sb.sem_num = which_sem;
   sb.sem_op = -1;
   sb.sem_flg = 0;
   semcall(sid,sb);
}

void V(int sid, int which_sem) /* Will setup the sb structure for incrementing   */
                       /* the semaphore for sid then calls semcall above */
                       /* to perform the V operation on the semaphore    */
{
   struct sembuf sb;
   
   sb.sem_num = which_sem;
   sb.sem_op = 1;
   sb.sem_flg = 0;
   semcall(sid,sb);
} 

int getsem_val(int sid, int which_sem) /* Used to get the value of a semaphore  */
                               /* mainly used for testing and debugging */
{
   int value_of_sem;
  
   value_of_sem = semctl(sid,which_sem,GETVAL,0);
   return(value_of_sem); /* Will return the value of the semaphore */
}

void init_sem(int sid, int which_sem, int init_val) /* Used to initialize the value of a semaphore (which_sem)to the value init_val */
{
   union semun {
      int val;
      struct semid_ds *buf;
      ushort *array;
   } semctl_arg;

   semctl_arg.val = init_val;
   /* for the sun and hp use the line below */
   /*  (void) semctl(sid,which_sem,SETVAL, semctl_arg);*/
   /* for linux use the line below and comment out the aboveline */
   (void) semctl(sid,which_sem,SETVAL, init_val);
}

void syserr(char *msg) /* print system call error message and terminate */
{
    printf("*** ERROR: called syserr() with message [%s].\n", msg);
    exit(1);
}  

int get_attach_shrmem(int num_bytes, char **addr, int *segid) /* get and attach shared memory */
                        /* for num_bytes in size and attach to address addr */
                        /* and store the id of the segment in segid */
{
   /*  char *shmat(); */
   if ((*segid = shmget(IPC_PRIVATE,num_bytes,0666|IPC_CREAT)) == -1)
       return(0);
   if ((*addr = shmat(*segid,0,0)) == BADADDR)
       return(0);
   return(1);
}

void remove_shrmem(int segid, char *addr) /* remove the shared memory with segment id segid and address addr             */
{ 
   (void)shmdt(addr);
   (void)shmctl(segid, IPC_RMID,0);
}
