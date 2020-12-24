#include <stdio.h>
#include <unistd.h>

using namespace std;

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <Source> <Destination>\n", argv[0]);
        return 0;
    }
    if (link(argv[1], argv[2]) == -1) {
        printf("Link Error\n");
        return 1;
    }
    printf("Files Linked Successfully\n");
    return 0;
}