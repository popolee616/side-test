#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

using namespace std;

void writer (const char* message, int count, FILE* stream) {
    for (; count >0; --count) {
        fprintf(stream, "%s\n", message);
        fflush(stream);
        sleep(1);
    }
}

void reader (FILE* stream) {
    char buffer[1024];
    /* Read until we hit the end of the stream.  fgets reads until either a newline or the end-of-file.  */
    while (!feof (stream)
           && !ferror (stream)
           && fgets (buffer, sizeof (buffer), stream) != NULL)
        fputs (buffer, stdout);
}

int main() {
    int fds[2];
    pid_t pid;

    pipe(fds);
    pid = fork();
    if (pid == (pid_t) 0) {
        FILE* stream;
        close (fds[1]);
        stream = fopen(fds[0], "r");
        reader (stream);
        close (fds[0]);
    }
    else {
        FILE* stream;
        close (fds[0]);
        stream = fopen(fds[1], "w");
        writer ("Hello, world.", 5, stream);
        close (fds[1]);
    }
    return 0;
}
