// an example of reading random numbers from /dev/urandom
// https://stackoverflow.com/questions/35726331/c-extracting-random-numbers-from-dev-urandom
#include <iostream>
#include <fstream>
int main(void) {
    int maxn=122;int minn=65;
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
    int time = 26;

    while （time >0） {
        urandom.read((char*)&random_value, sizeof(random_value));
        num = minn + (random_value % (maxn-minn+1));
        std::cout << "ASCII a: " << static_cast<char>(num) << "\n";
        time--;
    }
    // cast to integer to see the numeric value of the character
//    std::cout << "Random character: " << (unsigned int)ch << "\n";
//    std::cout << "ASCII Random character: " << static_cast<char>((unsigned int)ch) << "\n";
//    std::cout << "ASCII a: " << static_cast<char>(65) << "\n";

    // close random stream
    urandom.close();
    return 0;
}
