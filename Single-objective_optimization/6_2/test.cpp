#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <random>
#include <stack>
#include <vector>

const double PI = 3.1415926;

int main()
{
    double x = -0.52478;

    double fitness$ = 0.4 + (sin(PI * 4.0 * x) / (PI * 4.0 * x)) + 1.1 * (sin(PI * (4.0 * x + 2.0)) / (PI * (4.0 * x + 2.0))) + 0.8 * (sin(PI * (x - 2.0)) / (PI * (x - 2.0))) + 0.7 * (sin(PI * (6.0 * x - 4.0)) / (PI * (6.0 * x - 4.0)));

    printf("%.6lf", fitness$);

    return 0;
}
