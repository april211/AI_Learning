#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;
#define pi 3.14
#define population 200 //种群
#define iteration 500  //迭代
#define SWAP 45        //交叉
#define variation 3    //变异
const double x1min = -2.9;
const double x1max = 12;
const double x2min = 4.2;
const double x2max = 5.7;
int code[population][39];

double legend = 0;

double decode(int *code) //解码
{
    int x1 = 0, x2 = 0; //x1,x2代表第几个分成点
    //前21位x1,后18位x2
    for (int i = 20; i >= 0; i--)
    {
        x1 += pow(2, 20 - i) * code[i];
    }
    for (int i = 38; i >= 21; i--)
    {
        x2 += pow(2, 38 - i) * code[i];
    }
    double x11, x22;
    x11 = x1min + x1 * (x1max - x1min) / (pow(2, 21) - 1);
    x22 = x2min + x2 * (x2max - x2min) / (pow(2, 18) - 1);

    double fit = 21.5 + x11 * sin(4 * pi * x11) + x22 * sin(20 * pi * x22);
    return fit;
}

void create()
{
    for (int i = 0; i < population; i++)
        for (int j = 0; j < 39; j++)
            code[i][j] = rand() % 2;
}
void sel()
{
    int copy[population][39];
    for (int i = 0; i < 39 * population; i++)
        *(*copy + i) = *(*code + i);
    double fitness[population], sum = 0, pro = 0, odds[population];
    for (int i = 0; i < population; i++)
    {
        fitness[i] = decode(code[i]);
        legend = max(legend, fitness[i]);
        sum += fitness[i];
    }
    for (int i = 0; i < population; i++)
    {
        pro += fitness[i] / sum;
        odds[i] = pro;
    }
    int k;
    for (int i = 0; i < population; i++)
    {
        double R = rand() % 1000 / 1000;
        for (k = 0; k < population && R > odds[k]; k++)
            memcpy(code[i], copy[k], 39);
    }
}
void swa() //交叉
{
    for (int i = 0; i < population / 2; i++)
    {
        int R = rand() % 100;
        if (R > SWAP)
            continue;

        int a = rand() % population,
            b = rand() % population;

        int S = rand() % 38;
        for (int j = 0; j <= S; j++)
        {
            code[a][j] = code[a][j] ^ code[b][j];
            code[b][j] = code[a][j] ^ code[b][j];
            code[a][j] = code[a][j] ^ code[b][j];
        }
    }
}
void var() //变异
{
    for (int i = 0; i < population / 2; i++)
    {
        int R = rand() % 100;
        if (R > variation)
            continue;

        int V = rand() % 38;
        code[i][V] = 1 - code[i][V];
    }
}
int main()
{
    srand(time(0));
    int N = 0;
    for (int n = 0; n < 100; n++)
    { //共求100次
        create();
        for (int i = 0; i < iteration; i++)
        {
            sel();
            swa();
            var();
        }
        printf("%lf\n", legend);
        if (legend > 38.0)
            N++;
        legend = 0;
    }
    printf("\n所得结果大于38的概率:%.2lf", (double)N / 100);
}