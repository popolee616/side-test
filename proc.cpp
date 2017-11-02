#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <iostream>
#include <sys/types.h>

int main() {
	int BtoC[2];
	
	pipe(BtoC);
	
	pid_t child_pid;
	child_pid = fork();
	
	if (child_pid == 0) {
		dup2(BtoC[1], STDOUT_FILENO);
		close(BtoC[0]);
		close(BtoC[1]);
		execv("ece650-a2", nullptr);		
		perror("Error: during finding ece650-a2 in proc");
		return 1;		
	
	}else {
		dup2(BtoC[0], STDIN_FILENO);
		close(BtoC[1]);
		close(BtoC[0]);
		
		while (!std::cin.eof()) {
			std::string line;
			std::getline(std::cin, line);
			if (line.size () > 0)
				std::cout << line << std::endl;
		}
	} 
	
	return 0;
	
}
