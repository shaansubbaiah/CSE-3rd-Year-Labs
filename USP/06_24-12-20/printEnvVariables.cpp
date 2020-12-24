#include <iostream>

using namespace std;

int main(int argc, char** argv, char** env) {
    // env is a null terminated array of strings
    while (*env)
        printf("%s\n", *env++);
    return 0;
}
