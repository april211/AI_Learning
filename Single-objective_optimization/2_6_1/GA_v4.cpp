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

const int bits_snum = 39;           // 二进制编码位数
const int bits_x1 = 21;             // 坐标 1 所占的二进制编码位数
const int bits_x2 = 18;             // 坐标 2 所占的二进制编码位数
const int population_size = 80;     // 种群规模
const int num_of_iteration = 1000;  // 迭代次数
const double cross_coef1 = 0.55;    // 自适应交叉概率系数（针对较好个体）
const double cross_coef2 = 0.7;     // 自适应交叉概率系数（针对较坏个体）
const double cross_floor = 0.35;    // 自适应交叉概率地板值
const double mutation_coef1 = 0.45; // 自适应变异概率系数（针对较好个体）
const double mutation_coef2 = 0.7;  // 自适应变异概率系数（针对较坏个体）
const double mutation_floor = 0.2;  // 自适应变异概率地板值

typedef int Status;

// 全局最优个体信息，会不断变动
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
    double Get_X1() const
    {
        return x1$;
    }

    // 获取坐标 2（十进制）
    double Get_X2() const
    {
        return x2$;
    }

    // 获取该个体的适应度
    double Get_Fitness() const
    {
        return fitness$;
    }

    // 获取该个体的累计概率
    double Get_Cumula_Prob() const
    {
        return cumula_prob$;
    }

    // 获取一个指定的二进制位
    int Get_Bit(int pos) const
    {
        return x_bincode$[pos];
    }

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

bool Fitness_Greater(const Point &a, const Point &b);

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
    int success_cnt = 0;
    int trial = 100;

    for (int i = 0; i < trial; i++)
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

        if (bests_history[best_id].Get_Fitness() > 38.0)
            ++success_cnt;

        printf("Trial %d:\n", i + 1);
        printf("Best point is: \n");
        printf("(%.5lf, %.5lf, %.5lf);", bests_history[best_id].Get_X1(), bests_history[best_id].Get_X2(), bests_history[best_id].Get_Fitness());
        printf("\nFitness: %.5lf.\n", bests_history[best_id].Get_Fitness());
    }

    printf("Successful probability: %.2lf\n", (success_cnt * 1.0) / (trial * 1.0));

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
    static std::default_random_engine e1, e2;
    e1.seed((unsigned int)time(NULL) * 10013), e2.seed((unsigned int)time(NULL) * 10013);
    static std::uniform_real_distribution<double> u1(x1min, x1max);
    static std::uniform_real_distribution<double> u2(x2min, x2max);

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
        // 先通过随机数选出两个个体
        int chrome1 = u2(e), chrome2 = u2(e); // 即将由随机数选出的两个个体（染色体）
        while ((chrome1 == chrome2) || (chrome1 == best_id) || (chrome2 == best_id))
        {
            // 不会将最优个体拿来交叉，即当随机数与最佳序号相等时，继续执行
            chrome1 = u2(e);
            chrome2 = u2(e);
        }

        // 计算这对个体发生交叉的概率
        double cross_probability = 0;
        double chrome1_fit = random_chosen[chrome1].Get_Fitness();
        double chrome2_fit = random_chosen[chrome2].Get_Fitness();

        // 被选择的两个个体中较大的适应度
        double greater_fitness = (chrome1_fit > chrome2_fit) ? chrome1_fit : chrome2_fit;

        // 种群中最好的适应度
        double best_fitness = random_chosen[best_id].Get_Fitness();

        // 种群个体平均适应度
        double avg_fitness = 0;
        for (int i = 0; i < population_size; i++)
        {
            avg_fitness += random_chosen[i].Get_Fitness();
        }
        avg_fitness /= population_size;

        if (greater_fitness > avg_fitness) // 这意味着两个个体质量较高，应当降低交叉概率
        {
            cross_probability = (cross_coef1 * (best_fitness - greater_fitness)) / (best_fitness - avg_fitness);
        }
        else // 这意味着两个个体质量较差，应当提高交叉概率
        {
            cross_probability = cross_coef2;
        }

        // 当交叉概率过低时，设置为下限值，避免局部最优
        if (cross_probability < cross_floor)
        {
            cross_probability = cross_floor;
        }

        //printf("Cross_probability: %.5lf.\n", cross_probability);

        // 随机生成此次交叉发生的概率
        double cross_g = u1(e);

        // 若随机数小于自适应交叉概率，执行交叉操作
        if (cross_probability >= cross_g)
        {
            //printf("Cross over!\n");
            // 记录当前最好的个体，对其进行保护

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
        // 随机选定变异个体
        int chrome = u1(e);
        while (chrome == best_id)
        {
            // 不会将最优个体拿来交叉，即当随机数与最佳序号相等时，继续执行
            chrome = u1(e);
        }

        // 计算这个个体发生交叉的概率
        double mutation_probability = 0;
        double chrome_fit = random_chosen[chrome].Get_Fitness();

        // 种群中最好的适应度
        double best_fitness = random_chosen[best_id].Get_Fitness();

        // 种群个体平均适应度
        double avg_fitness = 0;
        for (int i = 0; i < population_size; i++)
        {
            avg_fitness += random_chosen[i].Get_Fitness();
        }
        avg_fitness /= population_size;

        if (chrome_fit > avg_fitness) // 这意味着两个个体质量较高，应当降低变异概率
        {
            mutation_probability = (mutation_coef1 * (best_fitness - chrome_fit)) / (best_fitness - avg_fitness);
        }
        else // 这意味着两个个体质量较差，应当提高变异概率
        {
            mutation_probability = mutation_coef2;
        }

        // 当变异概率过低时，设定为下限值，避免局部最优
        if (mutation_probability < mutation_floor)
        {
            mutation_probability = mutation_floor;
        }

        //printf("Mutation_probability: %.5lf.\n", mutation_probability);

        double mutate_g = u3(e);
        if (mutation_probability >= mutate_g)
        {
            //printf("Mutation!\n");

            // 随机选定变异个体上的变异基因位并修改
            int mutate_point = u2(e);
            // printf("Mutation point: %d, cnt: %d.\n", mutate_point, ik);

            (random_chosen[chrome].Get_Bit(mutate_point) == 1) ? (random_chosen[chrome].Set_Bit(mutate_point, 0)) : (random_chosen[chrome].Set_Bit(mutate_point, 1));

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


/*
Trial 1:
Best point is:
(11.61816, 5.32284, 38.34916);
Fitness: 38.34916.
Trial 2:
Best point is:
(11.62780, 5.62487, 38.74530);
Fitness: 38.74530.
Trial 3:
Best point is:
(11.62000, 5.52579, 38.61606);
Fitness: 38.61606.
Trial 4:
Best point is:
(11.65343, 5.62646, 38.02035);
Fitness: 38.02035.
Trial 5:
Best point is:
(11.64084, 5.52468, 38.43453);
Fitness: 38.43453.
Trial 6:
Best point is:
(11.12590, 5.22906, 37.68530);
Fitness: 37.68530.
Trial 7:
Best point is:
(11.62532, 5.22764, 38.28094);
Fitness: 38.28094.
Trial 8:
Best point is:
(11.62985, 5.42686, 38.49799);
Fitness: 38.49799.
Trial 9:
Best point is:
(11.61983, 5.22974, 38.09446);
Fitness: 38.09446.
Trial 10:
Best point is:
(10.12397, 5.62542, 37.24660);
Fitness: 37.24660.
Trial 11:
Best point is:
(11.61596, 5.42264, 38.40422);
Fitness: 38.40422.
Trial 12:
Best point is:
(11.62224, 5.61412, 37.46730);
Fitness: 37.46730.
Trial 13:
Best point is:
(11.62602, 5.62306, 38.70620);
Fitness: 38.70620.
Trial 14:
Best point is:
(9.60918, 5.62855, 36.40916);
Fitness: 36.40916.
Trial 15:
Best point is:
(9.60600, 5.32574, 36.15345);
Fitness: 36.15345.
Trial 16:
Best point is:
(11.62142, 5.62253, 38.66490);
Fitness: 38.66490.
Trial 17:
Best point is:
(11.62431, 5.62380, 38.73183);
Fitness: 38.73183.
Trial 18:
Best point is:
(11.63031, 5.61871, 38.29032);
Fitness: 38.29032.
Trial 19:
Best point is:
(10.13576, 4.73852, 34.67223);
Fitness: 34.67223.
Trial 20:
Best point is:
(11.62846, 5.32559, 38.43944);
Fitness: 38.43944.
Trial 21:
Best point is:
(11.65840, 5.22567, 37.36721);
Fitness: 37.36721.
Trial 22:
Best point is:
(9.62745, 5.32910, 36.27652);
Fitness: 36.27652.
Trial 23:
Best point is:
(11.12307, 5.32274, 37.88918);
Fitness: 37.88918.
Trial 24:
Best point is:
(11.62325, 5.42542, 38.54396);
Fitness: 38.54396.
Trial 25:
Best point is:
(11.14253, 5.52538, 37.89717);
Fitness: 37.89717.
Trial 26:
Best point is:
(11.61703, 5.62727, 38.62904);
Fitness: 38.62904.
Trial 27:
Best point is:
(11.62294, 4.52664, 37.62154);
Fitness: 37.62154.
Trial 28:
Best point is:
(9.62367, 5.33071, 36.11371);
Fitness: 36.11371.
Trial 29:
Best point is:
(11.13698, 5.52335, 38.00490);
Fitness: 38.00490.
Trial 30:
Best point is:
(11.11493, 5.23307, 37.10107);
Fitness: 37.10107.
Trial 31:
Best point is:
(11.63068, 5.42439, 38.52139);
Fitness: 38.52139.
Trial 32:
Best point is:
(11.64299, 5.33090, 37.81562);
Fitness: 37.81562.
Trial 33:
Best point is:
(11.12214, 5.52418, 38.13174);
Fitness: 38.13174.
Trial 34:
Best point is:
(11.62456, 5.52462, 38.64741);
Fitness: 38.64741.
Trial 35:
Best point is:
(11.11058, 5.62509, 38.05356);
Fitness: 38.05356.
Trial 36:
Best point is:
(11.61671, 5.62518, 38.67849);
Fitness: 38.67849.
Trial 37:
Best point is:
(11.62229, 5.62534, 38.73962);
Fitness: 38.73962.
Trial 38:
Best point is:
(10.61942, 5.52081, 37.42426);
Fitness: 37.42426.
Trial 39:
Best point is:
(10.13352, 5.62207, 37.10226);
Fitness: 37.10226.
Trial 40:
Best point is:
(11.60600, 5.62744, 38.33824);
Fitness: 38.33824.
Trial 41:
Best point is:
(11.63661, 5.42535, 38.43696);
Fitness: 38.43696.
Trial 42:
Best point is:
(11.63988, 5.52501, 38.46212);
Fitness: 38.46212.
Trial 43:
Best point is:
(11.63418, 5.22519, 38.28159);
Fitness: 38.28159.
Trial 44:
Best point is:
(11.63214, 5.62247, 38.63673);
Fitness: 38.63673.
Trial 45:
Best point is:
(11.61695, 5.43075, 38.13734);
Fitness: 38.13734.
Trial 46:
Best point is:
(10.65809, 5.51941, 36.43224);
Fitness: 36.43224.
Trial 47:
Best point is:
(11.62662, 5.62632, 38.73112);
Fitness: 38.73112.
Trial 48:
Best point is:
(11.61877, 5.42827, 38.39729);
Fitness: 38.39729.
Trial 49:
Best point is:
(11.12146, 5.02176, 37.52874);
Fitness: 37.52874.
Trial 50:
Best point is:
(11.63644, 4.72402, 37.73146);
Fitness: 37.73146.
Trial 51:
Best point is:
(11.61634, 5.62098, 38.49015);
Fitness: 38.49015.
Trial 52:
Best point is:
(11.62141, 5.42705, 38.49185);
Fitness: 38.49185.
Trial 53:
Best point is:
(11.62535, 5.62517, 38.75008);
Fitness: 38.75008.
Trial 54:
Best point is:
(11.62782, 5.12125, 38.10050);
Fitness: 38.10050.
Trial 55:
Best point is:
(11.10352, 5.62738, 37.76601);
Fitness: 37.76601.
Trial 56:
Best point is:
(10.62319, 4.62350, 36.72330);
Fitness: 36.72330.
Trial 57:
Best point is:
(10.61653, 5.62556, 37.67859);
Fitness: 37.67859.
Trial 58:
Best point is:
(11.61671, 5.32385, 38.36359);
Fitness: 38.36359.
Trial 59:
Best point is:
(11.12197, 5.62565, 38.23492);
Fitness: 38.23492.
Trial 60:
Best point is:
(11.64485, 5.32712, 38.06461);
Fitness: 38.06461.
Trial 61:
Best point is:
(11.63019, 5.22542, 38.32903);
Fitness: 38.32903.
Trial 62:
Best point is:
(11.62111, 5.52416, 38.62361);
Fitness: 38.62361.
Trial 63:
Best point is:
(11.62427, 5.62564, 38.74486);
Fitness: 38.74486.
Trial 64:
Best point is:
(11.62940, 5.12545, 38.23503);
Fitness: 38.23503.
Trial 65:
Best point is:
(11.62144, 5.42385, 38.51942);
Fitness: 38.51942.
Trial 66:
Best point is:
(11.63277, 5.32075, 38.20978);
Fitness: 38.20978.
Trial 67:
Best point is:
(11.60650, 5.52373, 38.30043);
Fitness: 38.30043.
Trial 68:
Best point is:
(11.62635, 5.52559, 38.64645);
Fitness: 38.64645.
Trial 69:
Best point is:
(11.12876, 4.92377, 37.52546);
Fitness: 37.52546.
Trial 70:
Best point is:
(11.62318, 5.52526, 38.64466);
Fitness: 38.64466.
Trial 71:
Best point is:
(11.62611, 5.42176, 38.43469);
Fitness: 38.43469.
Trial 72:
Best point is:
(11.61857, 5.62492, 38.70548);
Fitness: 38.70548.
Trial 73:
Best point is:
(11.63624, 5.31172, 36.58869);
Fitness: 36.58869.
Trial 74:
Best point is:
(11.65397, 5.52394, 37.90178);
Fitness: 37.90178.
Trial 75:
Best point is:
(9.62882, 5.62581, 36.73630);
Fitness: 36.73630.
Trial 76:
Best point is:
(11.10108, 5.42813, 37.42717);
Fitness: 37.42717.
Trial 77:
Best point is:
(11.61342, 5.62406, 38.60478);
Fitness: 38.60478.
Trial 78:
Best point is:
(11.63667, 5.51795, 37.99664);
Fitness: 37.99664.
Trial 79:
Best point is:
(11.62505, 5.02558, 38.14729);
Fitness: 38.14729.
Trial 80:
Best point is:
(11.62957, 5.32266, 38.37581);
Fitness: 38.37581.
Trial 81:
Best point is:
(11.62099, 5.32548, 38.42931);
Fitness: 38.42931.
Trial 82:
Best point is:
(11.12665, 5.52366, 38.12845);
Fitness: 38.12845.
Trial 83:
Best point is:
(7.62654, 5.62504, 34.75013);
Fitness: 34.75013.
Trial 84:
Best point is:
(11.11539, 5.62275, 38.10113);
Fitness: 38.10113.
Trial 85:
Best point is:
(11.60361, 5.62542, 38.31049);
Fitness: 38.31049.
Trial 86:
Best point is:
(11.61629, 5.32725, 38.32069);
Fitness: 38.32069.
Trial 87:
Best point is:
(10.12438, 5.52233, 37.06886);
Fitness: 37.06886.
Trial 88:
Best point is:
(11.62839, 4.92511, 38.04281);
Fitness: 38.04281.
Trial 89:
Best point is:
(8.11937, 4.62796, 34.14698);
Fitness: 34.14698.
Trial 90:
Best point is:
(11.10913, 5.53033, 37.61158);
Fitness: 37.61158.
Trial 91:
Best point is:
(11.61700, 4.62569, 37.67961);
Fitness: 37.67961.
Trial 92:
Best point is:
(11.61632, 5.62865, 38.52894);
Fitness: 38.52894.
Trial 93:
Best point is:
(11.61575, 5.13388, 37.39248);
Fitness: 37.39248.
Trial 94:
Best point is:
(11.62022, 5.62485, 38.72381);
Fitness: 38.72381.
Trial 95:
Best point is:
(11.62394, 5.62359, 38.72454);
Fitness: 38.72454.
Trial 96:
Best point is:
(10.12065, 5.62710, 37.18391);
Fitness: 37.18391.
Trial 97:
Best point is:
(11.62167, 5.62793, 38.64426);
Fitness: 38.64426.
Trial 98:
Best point is:
(11.11777, 5.02806, 37.50708);
Fitness: 37.50708.
Trial 99:
Best point is:
(11.61971, 5.42342, 38.49071);
Fitness: 38.49071.
Trial 100:
Best point is:
(9.62424, 5.22563, 36.34529);
Fitness: 36.34529.
Successful probability: 0.63 */
