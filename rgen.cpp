// an example of reading random numbers from /dev/urandom
// https://stackoverflow.com/questions/35726331/c-extracting-random-numbers-from-dev-urandom
#include <iostream>
#include <fstream>
#include <string>
int main(void) {
    // open /dev/urandom to read
    std::ifstream urandom("/dev/urandom");

    // check that it did not fail
    if (urandom.fail()) {
        std::cerr << "Error: cannot open /dev/urandom\n";
        return 1;
    }

    // read a random 8-bit value.
    // Have to use read() method for low-level reading
    unsigned random_value = 42;
    unsigned num=0;

    static const char alphanum[] =
        " "
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";
    std::string s;
    for (int i=0; i<15; i++) {
        urandom.read((char*)&random_value, sizeof(random_value));
       	num = random_value % (sizeof(alphanum)-1);
       	s += alphanum[num];
    }
	std::cout << "ASCII a: " << s << "\n";
    urandom.close();
    return 0;
}
