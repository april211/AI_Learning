#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <time.h>
using namespace std;
ofstream outfile;
#define machinenumber 6      //机器的总数（等于每道工序的并行机个数×工序数）
#define parallel 2           //每道工序的并行机个数
#define ordernumber 3        //工序数
#define workpiecesnumber 6   //工件总数
#define populationnumber 200 //每一代种群的个体数

double crossoverrate = 0.6;                              //交叉概率
double mutationrate = 0.05;                              //变异概率
int G = 100;                                             //循环代数100
int usetime[workpiecesnumber][ordernumber];              //第几个工件第几道工序的加工用时；
int machinetime[ordernumber][parallel] = {0};            //第几道工序的第几台并行机器的统计时间；
int starttime[workpiecesnumber][ordernumber][parallel];  //第几个工件第几道工序在第几台并行机上开始加工的时间；
int finishtime[workpiecesnumber][ordernumber][parallel]; //第几个工件第几道工序在第几台并行机上完成加工的时间；
int ttime[populationnumber];                             //个体的makespan；                                                    ？？？？？？？？？？？？？？？？？？？？？？？
int a[populationnumber][workpiecesnumber];               //第几代的染色体顺序，即工件加工顺序；
int times[100];                                          //用来存储已知用时的数组；
int makespan;                                            //总的流程加工时间；
int flg7;                                                //暂时存储流程加工时间；
double fits[populationnumber];                           //存储每一代种群每一个个体的适应度，便于进行选择操作；
                                                         //？？？？？？？？？？？？？？？？
int initialization()                                     //初始化种群；
{
    for (int i = 0; i < populationnumber; i++) //首先生成一个工件个数的全排列的个体；
        for (int j = 0; j < workpiecesnumber; j++)
        {
            a[i][j] = j + 1;
        }

    for (int i = 0; i < populationnumber; i++) //将全排列的个体中随机选取两个基因位交换，重复工件个数次，以形成随机初始种群；
        for (int j = 0; j < workpiecesnumber; j++)
        {
            int flg1 = rand() % workpiecesnumber;
            int flg2 = rand() % workpiecesnumber;
            int flg3 = a[i][flg1];
            a[i][flg1] = a[i][flg2];
            a[i][flg2] = flg3;
        }

    for (int i = 0; i < populationnumber; i++)
    {
        for (int j = 0; j < workpiecesnumber; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}

int fitness(int c) //计算适应度函数，c代表某个体；
{
    int totaltime; //总的加工流程时间（makespan）；
    int temp1[workpiecesnumber] = {0};
    int temp2[workpiecesnumber] = {0};
    int temp3[workpiecesnumber] = {0};

    for (int j = 0; j < workpiecesnumber; j++) //temp1暂时存储个体c的基因序列，以便进行不同流程之间的加工时记录工件加工先后顺序；
    {
        temp1[j] = a[c][j];
    }

    for (int i = 0; i < ordernumber; i++)
    {
        for (int j = 0; j < workpiecesnumber; j++) //该循环的目的是通过比较所有机器的当前工作时间，找出最先空闲的机器，便于新的工件生产；
        {
            int m = machinetime[i][0]; //先记录第i道工序的第一台并行机器的当前工作时间；
            int n = 0;
            for (int p = 0; p < parallel; p++) //与其他并行机器进行比较，找出时间最小的机器；
            {
                if (m > machinetime[i][p])
                {
                    m = machinetime[i][p];
                    n = p;
                }
            }
            int q = temp1[j];                                               //按顺序提取temp1中的工件号，对工件进行加工；
            starttime[q - 1][i][n] = max(machinetime[i][n], temp3[j]);      //开始加工时间取该机器的当前时间和该工件上一道工序完工时间的最大值；
            machinetime[i][n] = starttime[q - 1][i][n] + usetime[q - 1][i]; //机器的累计加工时间等于机器开始加工的时刻，加上该工件加工所用的时间；
            finishtime[q - 1][i][n] = machinetime[i][n];                    //工件的完工时间就是该机器当前的累计加工时间；
            temp2[j] = finishtime[q - 1][i][n];                             //将每个工件的完工时间赋予temp2，根据完工时间的快慢，便于决定下一道工序的工件加工顺序；
        }

        int flg2[workpiecesnumber] = {0}; //生成暂时数组，便于将temp1和temp2中的工件重新排列；
        for (int s = 0; s < workpiecesnumber; s++)
        {
            flg2[s] = temp1[s];
        }

        for (int e = 0; e < workpiecesnumber - 1; e++)
        {
            for (int ee = 0; ee < workpiecesnumber - 1 - e; ee++) // 由于temp2存储工件上一道工序的完工时间，在进行下一道工序生产时，按照先完工先生产的
            {                                                     //原则，因此，该循环的目的在于将temp2中按照加工时间从小到大排列，同时temp1相应进行变换
                if (temp2[ee] > temp2[ee + 1])                    //来记录temp2中的工件号；
                {
                    int flg5 = temp2[ee];
                    int flg6 = flg2[ee];
                    temp2[ee] = temp2[ee + 1];
                    flg2[ee] = flg2[ee + 1];
                    temp2[ee + 1] = flg5;
                    flg2[ee + 1] = flg6;
                }
            }
        }
        for (int e = 0; e < workpiecesnumber; e++) //更新temp1，temp2的数据，开始下一道工序；
        {
            temp1[e] = flg2[e];
            temp3[e] = temp2[e];
        }
    }
    totaltime = 0;
    for (int i = 0; i < parallel; i++) //比较最后一道工序机器的累计加工时间，最大时间就是该流程的加工时间；
        if (totaltime < machinetime[ordernumber - 1][i])
        {
            totaltime = machinetime[ordernumber - 1][i];
        }
    for (int i = 0; i < workpiecesnumber; i++) //将数组归零，便于下一个个体的加工时间统计；
        for (int j = 0; j < ordernumber; j++)
            for (int t = 0; t < parallel; t++)
            {
                starttime[i][j][t] = 0;
                finishtime[i][j][t] = 0;
                machinetime[j][t] = 0;
            }
    makespan = totaltime;
    fits[c] = 1.000 / makespan; //将makespan取倒数作为适应度函数；
}

int gant(int c) //该函数是为了将最后的结果便于清晰明朗的展示并做成甘特图，对问题的结果以及问题的解决并没有影响；
{

    int totaltime;
    char machine[ordernumber * parallel][100] = {"0"};

    int temp1[workpiecesnumber] = {0}; //jiagongshunxu
    int temp2[workpiecesnumber] = {0}; //shangyibuzhou de wan cheng shijian
    int temp3[workpiecesnumber] = {0};

    //////////////////////////////////////////
    for (int j = 0; j < workpiecesnumber; j++)
    {
        temp1[j] = a[c][j];
    }
    for (int i = 0; i < ordernumber; i++)

    {

        for (int j = 0; j < workpiecesnumber; j++)
        {

            int m = machinetime[i][0];
            int n = 0;

            for (int p = 0; p < parallel; p++) //找出时间最小的机器；
            {
                if (m > machinetime[i][p])
                {
                    m = machinetime[i][p];
                    n = p;
                }
            }
            int q = temp1[j];

            starttime[q - 1][i][n] = max(machinetime[i][n], temp3[j]);
            machinetime[i][n] = starttime[q - 1][i][n] + usetime[q - 1][i];
            finishtime[q - 1][i][n] = machinetime[i][n];
            temp2[j] = finishtime[q - 1][i][n];
            //cout<<"start:"<<starttime[q-1][i][n]<<"   use:"<<usetime[q-1][i]<<"  machine:"<<machinetime[i][n]<<"   finish:"<<finishtime[q-1][i][n]<<endl;
            for (int h = starttime[q - 1][i][n]; h < finishtime[q - 1][i][n]; h++)
            {
                if (q == 1)
                    machine[i * 2 + n][h] = '1';
                else if (q == 2)
                    machine[i * 2 + n][h] = '2';
                else if (q == 3)
                    machine[i * 2 + n][h] = '3';
                else if (q == 4)
                    machine[i * 2 + n][h] = '4';
                else if (q == 5)
                    machine[i * 2 + n][h] = '5';
                else
                    machine[i * 2 + n][h] = '6';
            }
        }

        int flg2[workpiecesnumber] = {0};
        for (int s = 0; s < workpiecesnumber; s++)
        {
            flg2[s] = temp1[s];
        }
        for (int e = 0; e < workpiecesnumber - 1; e++)
        {
            for (int ee = 0; ee < workpiecesnumber - 1 - e; ee++)
            {
                if (temp2[ee] > temp2[ee + 1])
                {
                    int flg5 = temp2[ee];
                    int flg6 = flg2[ee];
                    temp2[ee] = temp2[ee + 1];
                    flg2[ee] = flg2[ee + 1];
                    temp2[ee + 1] = flg5;
                    flg2[ee + 1] = flg6;
                    //swap(temp2[ee],temp2[ee+1]);
                    //swap(flg2[ee],flg2[ee+1]);
                }
            }
        }

        for (int e = 0; e < workpiecesnumber; e++)
        {
            temp1[e] = flg2[e];
            temp3[e] = temp2[e];
            //cout<<"temp3=="<<temp3[e]<<endl;
        }
    }

    totaltime = 0;
    for (int i = 0; i < parallel; i++)
        if (totaltime < machinetime[ordernumber - 1][i])
        {
            totaltime = machinetime[ordernumber - 1][i];
        }
    cout << "total=" << totaltime << endl;
    outfile << totaltime << endl; ///////////////////////////////////////////////////////////////////////////////
    flg7 = totaltime;
    for (int u = 0; u < ordernumber * parallel; u++)
    {
        for (int uu = 0; uu < 100; uu++)
        {
            outfile << machine[u][uu];
            cout << machine[u][uu];
        }
        outfile << endl;
        cout << endl;
    }
}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int select()
{
    double roulette[populationnumber + 1] = {0.00}; //记录轮盘赌的每一个概率区间；
    double pro_single[populationnumber];            //记录每个个体出现的概率，即个体的适应度除以总体适应度之和；
    double totalfitness = 0.00;                     //种群所有个体的适应度之和；
    int a1[populationnumber][workpiecesnumber];     //存储a中所有个体的染色体；

    for (int i = 0; i < populationnumber; i++) //计算所有个体适应度的总和；
    {
        totalfitness = totalfitness + fits[i];
    }

    for (int i = 0; i < populationnumber; i++)
    {
        pro_single[i] = fits[i] / totalfitness;        //计算每个个体适应度与总体适应度之比；
        roulette[i + 1] = roulette[i] + pro_single[i]; //将每个个体的概率累加，构造轮盘赌；
    }

    for (int i = 0; i < populationnumber; i++)
    {
        for (int j = 0; j < workpiecesnumber; j++)
        {
            a1[i][j] = a[i][j]; //a1暂时存储a的值；
        }
    }

    for (int i = 0; i < populationnumber; i++)
    {
        int a2; //当识别出所属区间之后，a2记录区间的序号；
        double p = rand() % (1000) / (double)(1000);
        for (int j = 0; j < populationnumber; j++)
        {
            if (p >= roulette[j] && p < roulette[j + 1])
                a2 = j;
        }
        for (int m = 0; m < workpiecesnumber; m++)
        {
            a[i][m] = a1[a2][m];
        }
    }
}

int crossover()
/*种群中的个体随机进行两两配对，配对成功的两个个体作为父代1和父代2进行交叉操作。
随机生成两个不同的基因点位，子代1继承父代2基因位之间的基因片段，其余基因按顺序集成父代1中未重复的基因；
子代2继承父代1基因位之间的基因片段，其余基因按顺序集成父代2中未重复的基因。*/
{
    for (int i = 0; i < populationnumber / 2; i++) //将所有个体平均分成两部分，一部分为交叉的父代1，一部分为进行交叉的父代2；
    {
        int n1 = 1 + rand() % workpiecesnumber / 2; //该方法生成两个不同的基因位；
        int n2 = n1 + rand() % (workpiecesnumber - n1 - 1) + 1;
        int n3 = rand() % 10;
        if (n3 == 2) //n3=2的概率为0.1；若满足0.1的概率，那么就进行交叉操作；
        {
            int temp1[workpiecesnumber] = {0};
            int temp2[workpiecesnumber] = {0};
            for (int j = 0; j < workpiecesnumber; j++)
            {
                int flg1 = 0;
                int flg2 = 0;
                for (int p = n1; p < n2; p++) //将交叉点位之间的基因片段进行交叉，temp1和temp2记录没有发生重复的基因；
                {
                    if (a[2 * i + 1][p] == a[2 * i][j])
                        flg1 = 1;
                }
                if (flg1 == 0)
                {
                    temp1[j] = a[2 * i][j];
                }

                for (int p = n1; p < n2; p++)
                {
                    if (a[2 * i][p] == a[2 * i + 1][j])
                        flg2 = 1;
                }
                if (flg2 == 0)
                {
                    temp2[j] = a[2 * i + 1][j];
                }
            }

            for (int j = n1; j < n2; j++) //子代1继承父代2交叉点位之间的基因；子代2继承父代1交叉点位之间的基因；
            {
                int n4 = 0;
                n4 = a[2 * i][j];
                a[2 * i][j] = a[2 * i + 1][j];
                a[2 * i + 1][j] = n4;
            }
            for (int p = 0; p < n1; p++) //子代1第一交叉点之前的基因片段，按顺序依次继承父代1中未与子代1重复的基因；
            {
                for (int q = 0; q < workpiecesnumber; q++)
                {
                    if (temp1[q] != 0)
                    {
                        a[2 * i][p] = temp1[q];
                        temp1[q] = 0;
                        break;
                    }
                }
            }
            for (int p = 0; p < n1; p++) //子代2第一交叉点之前的基因片段，按顺序依次继承父代2中未与子代2重复的基因；
            {
                for (int m = 0; m < workpiecesnumber; m++)
                {
                    if (temp2[m] != 0)
                    {
                        a[2 * i + 1][p] = temp2[m];
                        temp2[m] = 0;
                        break;
                    }
                }
            }
            for (int p = n2; p < workpiecesnumber; p++) //子代1第2交叉点之后的基因片段，按顺序依次继承父代1中未与子代1重复的基因；
            {
                for (int q = 0; q < workpiecesnumber; q++)
                {
                    if (temp1[q] != 0)
                    {
                        a[2 * i][p] = temp1[q];
                        temp1[q] = 0;
                        break;
                    }
                }
            }
            for (int p = n2; p < workpiecesnumber; p++) //子代2第2交叉点之后的基因片段，按顺序依次继承父代2中未与子代2重复的基因；
            {
                for (int m = 0; m < workpiecesnumber; m++)
                {
                    if (temp2[m] != 0)
                    {
                        a[2 * i + 1][p] = temp2[m];
                        temp2[m] = 0;
                        break;
                    }
                }
            }
        }
    }
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

int mutation() //变异操作为两点变异，随机生成两个基因位，并交换两个基因的位置；
{
    int n3 = rand() % 20;
    if (n3 == 2)
    {
        for (int i = 0; i < populationnumber; i++)
        {
            int b1 = rand() % workpiecesnumber;
            int b2 = rand() % workpiecesnumber;
            int b3 = a[i][b1];
            a[i][b1] = a[i][b2];
            a[i][b2] = b3;
        }
    }
}
int main()
{
    ifstream ifs("input.txt");
    outfile.open("output.txt");
    if (!ifs)
    {
        cout << "打开文件失败！" << endl;
    }
    int l = 0;
    while (ifs >> times[l])
    {
        l++;
    }
    ifs.close(); //读入已知的加工时间；
    for (int i = 0; times[i] != 0; i++)
    {
        cout << times[i] << "  ";
    }
    cout << endl;
    for (int i = 0; i < workpiecesnumber; i++)
    {

        for (int j = 0; j < ordernumber; j++)
        {
            usetime[i][j] = times[ordernumber * i + j];
            cout << usetime[i][j] << "  ";
        }

        cout << endl;
    }
    cout << "//////////////////////////////////////////////////" << endl;
    ;
    srand(time(NULL));
    initialization(); //初始化种群；
    for (int g = 0; g < G; g++)
    {
        for (int c = 0; c < populationnumber; c++) //计算每个个体适应度并存在ttime中；
        {
            fitness(c);
            ttime[c] = makespan;
        }
        select();    //选择操作；
        crossover(); //交叉操作；
        mutation();  //变异操作；
    }

    int flg8 = ttime[0];
    int flg9 = 0;
    for (int c = 0; c < populationnumber - 1; c++) //计算最后一代每个个体的适应度，并找出最优个体；
    {

        if (ttime[c] < flg8)
        {
            flg8 = ttime[c];
            flg9 = c;
        }
    }
    gant(flg9); //画出简易的流程图；
    outfile.close();
    return 0;
}
