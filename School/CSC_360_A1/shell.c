#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

#define BUFF_SIZE 1000
#define TOKEN_BUFF 100

int shell_cd(char **args){

    chdir(args[1]);
    return(1);
}

int shell_exit(void){
    return(0);
}


char *shell_line_input(void){

    int buff = BUFF_SIZE;
    char *line_buffer = malloc(sizeof(char)*buff);
    int current_position;
    int current_character

    while(1){

        current_character = getchar();
        if(current_character == '\n' || current_character == EOF){
            line_buffer[current_position] = '\0';
            return line_buffer;
        }else{
            line_buffer[current_position] = current_character;
        }
        current_position += 1;

        if(current_position >= buff){
            buff += BUFF_SIZE;
            line_buffer = realloc(line_buffer,buff * sizeof(char));
        }
    }  
}

char **shell_line_tokens(char *input){
    int tokbuff = TOKEN_BUFF;
    char **list_of_tokens = malloc(sizeof(char*) * tokbuff);
    char *token;
    int tok_position = 0;

    token = strtok(input," \t\r\n\v\f"); //splits based off ASCII white space characters  \t\r\n\v\f

    while (token != NULL){
        list_of_tokens[tok_position] = token;
        tok_position += 1;

        if(tok_position >= tokbuff){
            tokbuff += TOKEN_BUFF;
            list_of_tokens = realloc(list_of_tokens,sizeof(char*) * tokbuff)
        }
        token = strtok(NULL," \t\r\n\v\f");
    }
    list_of_tokens[tok_position] = NULL;
    return list_of_tokens;
}

int child_exec(char **args){
    pid_t child;
    pid_t wait_child;
    int child_status;

    child = fork()
    if (child == 0){
        //in the child process
        execvp(args[0],args);
    }else{
        wait_child = waitpid(child,&child_status,WUNTRACED);
        while(!WIFSIGNALED(child_status) && !WIFEXITED(child_status)){
            wait_child = waitpid(child,&child_status,WUNTRACED);
        }
    }
    return(1); 
}

int shell_execute(char **args){
    if(args[0] == NULL){
        return(1);
    }
    if(strcmp(args[0],"shell_cd") == 0){
        return(shell_cd(args));
    }
    if(strcmp(args[0],"shell_exit") == 0){
        return(shell_exit());
    }
    return(child_exec(args));
}



void shell_loop(void){

    char *input_line;
    char **args;
    int loop_status;

    printf("> ");
    input_line = shell_line_input();
    args = shell_line_tokens(input_line);
    loop_status = shell_execute(args);

    free(input_line);
    free(args);

    while(loop_status == 1){
        printf("> ");
        input_line = shell_line_input();
        args = shell_line_tokens(input_line);
        loop_status = shell_execute(args);

        free(input_line);
        free(args);

    }

}




int main(int argc,char **argv   ){


shell_loop();


    return 0;
}