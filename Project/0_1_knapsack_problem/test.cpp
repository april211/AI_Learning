#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <random>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

#define INF 0x3f3f3f3f
#define DEFAULT_SET -1
#define FALSE 0
#define TRUE 1
#define OK 1
#define ERROR -1

int random_disturb = 1114;

int main()
{
    random_disturb++;
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * abs(random_disturb));
    std::uniform_real_distribution<double> u(0.0, 1.0);

    for(int i = 0; i< 10; i++)
    {
        printf("%d ", int(u(e)+0.5));
    }


    return 0;
}