#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <random>
#include <stack>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::stack;
using std::vector;

#define INF 0x3f3f3f3f
#define FALSE 0
#define TRUE 1
#define OK 1
#define ERROR -2
#define DEFAULT_SET -1

const double PI = 3.14159265;            // 圆周率
const double x1max = 12.0;               // 坐标 1 上限
const double x1min = -2.9;               // 坐标 1 下限
const double x2max = 5.7;                // 坐标 2 上限
const double x2min = 4.2;                // 坐标 2 下限
const double x1_segmentaion = 2097151.0; // x1 坐标分割数
const double x2_segmentaion = 262143.0;  // x2 坐标分割数

const int bits_snum = 39;                 // 二进制编码位数
const int bits_x1 = 21;                   // 坐标 1 所占的二进制编码位数
const int bits_x2 = 18;                   // 坐标 2 所占的二进制编码位数
const double cross_probability = 0.7;     // 交叉概率
const double mutation_probability = 0.01; // 变异概率
const int population_size = 60;           // 种群规模
const int num_of_iteration = 1000;        // 迭代次数

typedef int Status;

// 最优个体信息，会不断变动
int best_id = DEFAULT_SET;
double best_fit = DEFAULT_SET * 1.0;

// 判断大小
int Max(const int &a, const int &b);

// 十进制数转二进制
void Dec_to_Bin(stack<int> &x_binary, int j);

// 点类（对应到：染色体（个体））
class Point
{
protected:
    double x1$;             // 自变量坐标 1
    double x2$;             // 自变量坐标 2
    double fitness$;        // 个体适应度（取与目标函数值一致）
    double cumula_prob$;    // 该个体的累计概率
    vector<int> x_bincode$; // 自变量二进制编码

public:
    // 构造函数
    Point() : x1$(DEFAULT_SET), x2$(DEFAULT_SET), fitness$(DEFAULT_SET), cumula_prob$(DEFAULT_SET) {}

    Point(double x1, double x2) : x1$(x1), x2$(x2), cumula_prob$(DEFAULT_SET)
    {
        // 初始适应度计算
        fitness$ = 21.5 + x1$ * sin(4.0 * PI * x1$) + x2$ * sin(20.0 * PI * x2$);
        Encode();
    }

    // 拷贝构造函数
    Point(const Point &tt) : x1$(tt.x1$), x2$(tt.x2$), fitness$(tt.fitness$), cumula_prob$(tt.cumula_prob$)
    {
        x_bincode$.clear(); // 先清空，再深拷贝
        for (int i = 0; i < bits_snum; i++)
        {
            x_bincode$.push_back(tt.x_bincode$[i]);
        }
    }

    // 析构函数
    ~Point() {}

    // 重载运算符
    bool operator==(const Point &d)
    {
        // 十进制坐标一致即可判相等
        if ((x1$ == d.x1$) && (x2$ == d.x2$))
            return true;
        else
            return false;
    }

    bool operator!=(const Point &d)
    {
        // 十进制坐标出现不一致即可以判不相等
        if ((x1$ != d.x1$) || (x2$ != d.x2$))
            return true;
        else
            return false;
    }

    Point operator=(const Point &tt)
    {
        x1$ = tt.x1$;
        x2$ = tt.x2$;
        fitness$ = tt.fitness$;
        cumula_prob$ = tt.cumula_prob$;

        x_bincode$.clear(); // 先清空，再深拷贝
        for (int i = 0; i < bits_snum; i++)
        {
            x_bincode$.push_back(tt.x_bincode$[i]);
        }
        return (*this);
    }

    // 获取坐标 1（十进制）
    double Get_X1() const { return x1$; }

    // 获取坐标 2（十进制）
    double Get_X2() const { return x2$; }

    // 获取该个体的适应度
    double Get_Fitness() const { return fitness$; }

    // 获取该个体的累计概率
    double Get_Cumula_Prob() const { return cumula_prob$; }

    // 获取一个指定的二进制位
    int Get_Bit(int pos) const { return x_bincode$[pos]; }

    // 设置坐标 1（十进制）
    Status Set_X1(double x1);

    // 设置坐标 2（十进制）
    Status Set_X2(double x2);

    // 设置坐标（十进制）
    Status Set_Coordinate(double x1, double x2);

    // 修改累计概率
    Status Set_Cumula_Prob(double cumula_prob);

    // 编辑一个指定的二进制位
    Status Set_Bit(int pos, int bit);

    // 将传入的二进制数组赋值给内部的二进制数组
    Status Set_Bvector(const vector<int> &tt);

    // 编码 (Decimal to Binary)
    Status Encode();

    // 解码并更新十进制坐标值 (Binary to Decimal)
    Status Decode();

    // 刷新该个体的适应度（坐标值改变的情况下）
    Status Refresh_Fitness();
};

// 更新全局最优个体信息
Status Refresh_Bestinfo(const vector<Point> &population)
{
    best_id = DEFAULT_SET, best_fit = DEFAULT_SET * 1.0;
    for (int i = 0; i < population_size; i++)
    {
        if (population[i].Get_Fitness() > best_fit)
        {
            best_id = i;
            best_fit = population[i].Get_Fitness();
        }
    }
    return OK;
}
bool Fitness_Greater(const Point &a, const Point &b);

// 初始化种群
Status initialize(vector<Point> &origin);

// 轮盘赌选择 + 复制
Status select(vector<Point> &origin, vector<Point> &random_chosen); // 个体适应度、种群

// 1 - 断点交叉算子
Status cross_over(vector<Point> &random_chosen);

// 变异算子
Status mutation(vector<Point> &random_chosen);

int main()
{
    // 初始种群
    vector<Point> origin;

    // 单个点
    Point single;

    // 选择复制后的种群
    vector<Point> random_chosen;

    // 每次迭代后产生的最优个体
    vector<Point> bests_history;

    // 形成初始化种群
    initialize(origin);
    Refresh_Bestinfo(origin);

    // 迭代
    for (int i = 0; i < num_of_iteration; i++)
    {
        // 执行 选择算子
        select(origin, random_chosen);

        Refresh_Bestinfo(random_chosen);

        // 执行 1-断点交叉算子
        cross_over(random_chosen);

        // 执行变异算子
        mutation(random_chosen);

        // 保留此次迭代的最优个体信息
        bests_history.push_back(random_chosen[best_id]);

        origin.clear();
        origin = random_chosen;
        random_chosen.clear();
    }

    // 更新全局最优个体信息
    Refresh_Bestinfo(bests_history);
    for (int i = 0; i < population_size; i++)
    {
        printf("%.6lf\n", bests_history[i].Get_Fitness());
    }

    printf("Best id: %d.\n", best_id);
    printf("Best point is: \n");
    printf("(%.5lf, %.5lf);", bests_history[best_id].Get_X1(), bests_history[best_id].Get_X2());
    printf("\nFitness: %lf.\n", bests_history[best_id].Get_Fitness());

    return 0;
}

// 十进制转二进制
void Dec_to_Bin(stack<int> &x_binary, int j)
{
    if (j == 0)
        return;
    else
    {
        x_binary.push(j % 2);
        Dec_to_Bin(x_binary, j / 2);
    }
}

// 判断大小
int Max(const int &a, const int &b)
{
    return (a > b) ? a : b;
}

// 设置坐标 1（十进制）
Status Point::Set_X1(double x1)
{
    x1$ = x1;
    return OK;
}

// 设置坐标 2（十进制）
Status Point::Set_X2(double x2)
{
    x2$ = x2;
    return OK;
}

// 设置坐标（十进制）
Status Point::Set_Coordinate(double x1, double x2)
{
    x1$ = x1, x2$ = x2;
    return OK;
}

// 修改累计概率
Status Point::Set_Cumula_Prob(double cumula_prob)
{
    cumula_prob$ = cumula_prob;
    return OK;
}

// 编辑一个指定的二进制位
Status Point::Set_Bit(int pos, int bit)
{
    x_bincode$[pos] = bit;
    return OK;
}

// 将传入的二进制数组赋值给内部的二进制数组
Status Point::Set_Bvector(const vector<int> &tt)
{
    x_bincode$.clear();
    for (int i = 0; i < bits_snum; i++)
    {
        x_bincode$.push_back(tt[i]);
    }
    return OK;
}

bool Fitness_Greater(const Point &a, const Point &b)
{
    return (a.Get_Fitness() > b.Get_Fitness());
}

// 编码 (Decimal to Binary)
Status Point::Encode()
{
    // 针对非法十进制坐标返回错误代码
    if (x1$ > x1max || x1$ < x1min || x2$ > x2max || x2$ < x2min)
        return ERROR;

    //printf("Encode!\n");
    // 由 十进制坐标 获得 十进制数字串 j
    int j1 = ((x1$ - x1min) / (x1max - x1min)) * x1_segmentaion;
    int j2 = ((x2$ - x2min) / (x2max - x2min)) * x2_segmentaion;
    //printf("--%d %d--\n", j1, j2);

    stack<int> tt1, tt2;

    Dec_to_Bin(tt1, j1);
    Dec_to_Bin(tt2, j2);

    int size1 = tt1.size(), size2 = tt2.size();
    x_bincode$.clear();

    // 前导零
    for (int i = 0; i < bits_x1 - size1; i++)
    {
        x_bincode$.push_back(0);
    }

    for (int i = 0; i < size1; i++)
    {
        x_bincode$.push_back(tt1.top());
        tt1.pop();
    }

    // 前导零
    for (int i = 0; i < bits_x2 - size2; i++)
    {
        x_bincode$.push_back(0);
    }

    for (int i = 0; i < size2; i++)
    {
        x_bincode$.push_back(tt2.top());
        tt2.pop();
    }
    return OK;
}

// 解码并更新十进制坐标值 (Binary to Decimal)
Status Point::Decode()
{
    //printf("Decode!\n");
    int j1 = 0, j2 = 0;
    for (int i = 0; i < bits_x1; i++)
    {
        j1 += x_bincode$[i] * pow(2.0, bits_x1 - i - 1);
    }

    for (int i = bits_x1; i < bits_snum; i++)
    {
        j2 += x_bincode$[i] * pow(2.0, bits_snum - i - 1);
    }

    x1$ = x1min + j1 * ((x1max - x1min) / x1_segmentaion);
    x2$ = x2min + j2 * ((x2max - x2min) / x2_segmentaion);
    return OK;
}

// 刷新该个体的适应度（坐标值改变的情况下）
Status Point::Refresh_Fitness()
{
    fitness$ = 21.5 + x1$ * sin(4.0 * PI * x1$) + x2$ * sin(20.0 * PI * x2$);
    return OK;
}

// 初始化种群
Status initialize(vector<Point> &origin)
{
    //printf("Init!\n");
    std::default_random_engine e1, e2;
    e1.seed((unsigned int)time(NULL) * 10013), e2.seed((unsigned int)time(NULL) * 10013);
    std::uniform_real_distribution<double> u1(x1min, x1max);
    std::uniform_real_distribution<double> u2(x2min, x2max);

    // 随机产生个体
    for (int i = 0; i < population_size; i++)
    {
        Point tt(u1(e1), u2(e2)); // 初始适应度已在构造时计算，二进制码已生成
        vector<Point>::iterator pt = find(origin.begin(), origin.end(), tt);

        // 已有该个体
        if (pt != origin.end())
        {
            --i;
        }
        else
        {
            origin.push_back(tt);
        }
    }
    return OK;
}

// 轮盘赌选择 + 复制
Status select(vector<Point> &origin, vector<Point> &random_chosen) // 个体适应度、种群
{
    //printf("Select!\n");
    // 计算选择概率分母
    double sum_fitness = 0.0;
    for (int i = 0; i < population_size; i++)
    {
        sum_fitness += origin[i].Get_Fitness();
    }

    // 计算个体的选择概率
    for (int i = 0; i < population_size; i++)
    {
        origin[i].Set_Cumula_Prob(origin[i].Get_Fitness() / sum_fitness);
    }

    // 计算个体的累积概率
    double sum_prob = origin[0].Get_Cumula_Prob();
    for (int i = 1; i < population_size; i++)
    {
        sum_prob += origin[i].Get_Cumula_Prob();
        origin[i].Set_Cumula_Prob(sum_prob);
    }
    //printf("%lf\n", sum_prob);

    static int ik = 0;
    ik++;
    // 生成随机小数，选择个体
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * ik);
    std::uniform_real_distribution<double> u(0.0, 1.0);

    int chosen_cnt = 0; // 个体选择计数器

    // 在 20个个体中选择复制 20个个体（染色体），可能有重复个体
    while (chosen_cnt < population_size)
    {
        double random_lf_1 = u(e);
        for (int j = 0; j < population_size; j++)
        {
            if (origin[j].Get_Cumula_Prob() >= random_lf_1) // 选中
            {
                random_chosen.push_back(origin[j]); // 从原始种群中复制个体
                ++chosen_cnt;
                break;
            }
        }
    }
    return OK;
}

// 1 - 断点交叉算子
Status cross_over(vector<Point> &random_chosen)
{
    static int ik = 0;
    ik++;
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * ik);
    std::uniform_real_distribution<double> u1(0.0, 1.0);
    std::uniform_int_distribution<unsigned> u2(0, population_size - 1);
    std::uniform_int_distribution<unsigned> u3(1, bits_snum - 1);

    for (int i = 0; i < population_size / 2; i++)
    {
        double cross_g = u1(e);

        // 若随机数小于交叉概率，执行交叉操作
        if (cross_probability >= cross_g)
        {
            //printf("Cross over!\n");
            // 记录当前最好的个体，对其进行保护
            int chrome1 = u2(e), chrome2 = u2(e); // 即将由随机数选出的两个个体（染色体）
            while ((chrome1 == chrome2) || (chrome1 == best_id) || (chrome2 == best_id))
            { // 不会将最优个体拿来交叉，即当随机数与最佳序号相等时，继续执行
                chrome1 = u2(e);
                chrome2 = u2(e);
            }

            // 得到随机断点，断点后的片段将参与交叉
            int break_point = u3(e);
            // printf("Break point: %d.\n", break_point);

            // 逐一交换基因
            for (int j = break_point; j < bits_snum; j++)
            {
                int tt = random_chosen[chrome2].Get_Bit(j);
                random_chosen[chrome2].Set_Bit(j, random_chosen[chrome1].Get_Bit(j));
                random_chosen[chrome1].Set_Bit(j, tt);
            }

            // 无条件更新种群中个体的信息，确保实时正确
            for (int j = 0; j < population_size; j++)
            {
                random_chosen[j].Decode();          // 更新十进制坐标
                random_chosen[j].Refresh_Fitness(); // 更新适应度
            }
            Refresh_Bestinfo(random_chosen);
        }
    }
    return OK;
}

// 变异算子
Status mutation(vector<Point> &random_chosen)
{
    static int ik = 0;
    ik++;
    std::mt19937 e;
    e.seed((unsigned int)time(NULL) * ik);
    std::uniform_int_distribution<unsigned> u1(0, population_size - 1);
    std::uniform_int_distribution<unsigned> u2(0, bits_snum - 1);
    std::uniform_real_distribution<double> u3(0.0, 1.0);

    for (int i = 0; i < population_size; i++)
    {
        double mutate_g = u3(e);
        if (mutation_probability >= mutate_g)
        {
            //printf("Mutation!\n");

            // 随机选定变异个体
            int chrome = u1(e);

            while (chrome == best_id)
            { // 不会将最优个体拿来交叉，即当随机数与最佳序号相等时，继续执行
                chrome = u1(e);
            }

            // 随机选定变异个体上的变异基因位并修改
            int mutate_point = u2(e);
            // printf("Mutation point: %d, cnt: %d.\n", mutate_point, ik);

            (random_chosen[chrome].Get_Bit(mutate_point) == 1) ? (random_chosen[chrome].Set_Bit(mutate_point, 0)) : (random_chosen[chrome].Set_Bit(mutate_point, 1));

            // 无条件更新种群中个体的信息
            for (int j = 0; j < population_size; j++)
            {
                random_chosen[j].Decode();          // 更新十进制坐标
                random_chosen[j].Refresh_Fitness(); // 更新适应度
            }
            Refresh_Bestinfo(random_chosen);
        }
    }
    return OK;
}
