#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <random>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

#define INF 999999
#define DEFAULT_SET -1
#define FALSE 0
#define TRUE 1
#define OK 1
#define ERROR -1
#define mach_num 4                 // 机器数目（工序数目）为 4
#define jobs_num 5                 // 工件数目为 5
#define cross_probability 0.6      // 交叉概率 == 0.6
#define mutation_probability 0.005 // 变异概率 == 0.1
#define population_size 30         // 种群规模 == 20
#define num_of_iteration 50        // 迭代次数 == 50
#define cross_group_num 4          // 参与交叉的组数：4，有 8个个体  (12*(2/3))
#define best_time 213              // 最优解时的时间
typedef int Status;

class Job
{
public:
    int id$;                  // 工件编号
    vector<int> expt_proc_t$; // 该工件在各工序中的预期加工时长
    vector<int> real_proc_t$; // 该工件在各工序中的实际加工时长
public:
    // 构造函数
    Job() : id$(DEFAULT_SET)
    {
        for (int i = 0; i < mach_num + 1; i++)
        {
            expt_proc_t$.push_back(DEFAULT_SET);
            real_proc_t$.push_back(DEFAULT_SET);
        }
    }

    Job(int id, int *proc_t) : id$(id)
    {
        for (int i = 0; i < mach_num + 1; i++)
        {
            real_proc_t$.push_back(DEFAULT_SET);
            expt_proc_t$.push_back(proc_t[i]);
        }
    }

    Job(const Job &tt) : id$(tt.id$)
    {
        expt_proc_t$.clear();
        real_proc_t$.clear();
        expt_proc_t$.push_back(DEFAULT_SET); // 工序编号从 1开始
        real_proc_t$.push_back(DEFAULT_SET);

        for (int i = 1; i < mach_num + 1; i++)
        {
            expt_proc_t$.push_back(tt.expt_proc_t$[i]);
            real_proc_t$.push_back(tt.real_proc_t$[i]);
        }
    }

    // 析构函数
    ~Job() {}

    // 重载运算符
    bool operator==(const Job &j1)
    {
        if (this->id$ == j1.id$)
            return true; // 编号一致即可判相等
        else
            return false;
    }

    bool operator!=(const Job &j1)
    {
        if (this->id$ != j1.id$)
            return true; // 编号不一致即可以判不相等
        else
            return false;
    }

    Job operator=(const Job &tt)
    {
        this->id$ = tt.id$;
        expt_proc_t$.clear();
        real_proc_t$.clear();
        expt_proc_t$.push_back(DEFAULT_SET); // 工序编号从 1开始
        real_proc_t$.push_back(DEFAULT_SET);

        for (int i = 1; i < mach_num + 1; i++)
        {
            expt_proc_t$.push_back(tt.expt_proc_t$[i]);
            real_proc_t$.push_back(tt.real_proc_t$[i]);
        }
        return (*this);
    }

    int GetId() const { return id$; }
};

// 存储个体的一些重要信息
typedef struct Info
{
    int id;             // 该个体在群体集的位置下标
    int maxc;           // 该个体的最大流程时间
    double fitness;     // 个体的适应度
    double cumula_prob; // 该个体的累计概率
} Info;

int Max(const int &a, const int &b)
{
    return (a > b) ? a : b;
}

// 判断两个自定义工件向量是否相等
bool JobVecIsEqual(vector<Job> &v1, vector<Job> &v2)
{
    bool flag = true;
    for (int i = 0; i < jobs_num; i++)
    {
        if (v1[i] != v2[i])
            flag = false;
    }
    return flag;
}

bool Fitness_Greater(const Info &a, const Info &b)
{
    return (a.fitness > b.fitness);
}

// 初始化种群
Status initialize(vector<vector<Job>> &orders, vector<Job> &single, vector<Job> &job_finder)
{
    std::default_random_engine e1;
    e1.seed((unsigned int)time(NULL) * 10013);
    std::uniform_int_distribution<unsigned> u1(1, jobs_num); //随机数分布对象

    // 初始化种群
    for (int i = 0; i < population_size; i++)
    {
        while (single.size() < jobs_num) // 当满足个数条件时执行
        {
            int pivot_id = u1(e1);                                             // 工件编号随机基准值（1~5）
            Job tt(job_finder[pivot_id]);                                      // 调用工件索引进行复制
            vector<Job>::iterator pt = find(single.begin(), single.end(), tt); // 对该基因进行查找
            //printf("aha!-->%d\n", pivot_id);
            if (pt == single.end()) // 该染色体还没有该型基因，则可以加入
            {
                single.push_back(tt);
            }
            else
                continue;
        }
        vector<vector<Job>>::iterator it;
        bool already_have = false;
        for (it = orders.begin(); it != orders.end(); it++)
        {
            if (JobVecIsEqual((*it), single)) // 如果找到一个相同的，放弃该记录
                already_have = true;
        }
        if (!already_have)
        {
            orders.push_back(single);
        }
        else
        {
            i--;
        }
        single.clear(); // 清空，准备下一次
    }
    return OK;
}

// 计算种群中每个个体的每个基因（工件）在每道工序结束时的时间
Status jobs_proc_time(vector<vector<Job>> &orders)
{
    for (int i = 0; i < population_size; i++)
    {
        // 工件排列顺序下标是从 0开始的，工序是从 1开始算起的
        // 序列中第一个工件在第一台机器上加工完成的时间就是它在第一台机器上的预计时间
        orders[i][0].real_proc_t$[1] = orders[i][0].expt_proc_t$[1];

        //第一个工件在第 j个机器上加工完成的时间
        for (int j = 2; j < mach_num + 1; j++)
        {
            orders[i][0].real_proc_t$[j] = orders[i][0].real_proc_t$[j - 1] + orders[i][0].expt_proc_t$[j];
        }

        // 第 m个工件完成第一道工序的时间等于它前一个工件在这个工序完成时的时刻加上这个工件在第一道工序的预期时间
        for (int m = 1; m < jobs_num; m++)
        {
            orders[i][m].real_proc_t$[1] = orders[i][m - 1].real_proc_t$[1] + orders[i][m].expt_proc_t$[1];
        }

        // 第 k个工件在第 j 道工序完成的时刻等于 max()
        for (int j = 2; j < mach_num + 1; j++)
        {
            for (int k = 1; k < jobs_num; k++)
            {
                orders[i][k].real_proc_t$[j] = Max(orders[i][k - 1].real_proc_t$[j], orders[i][k].real_proc_t$[j - 1]) + orders[i][k].expt_proc_t$[j];
            }
        }
    }
    return OK;
}

// 计算种群中每个个体的适应度
Status chrome_fitnesses(vector<vector<Job>> &orders, vector<Info> &chrome_list1, int chrome_num)
{
    for (int i = 0; i < chrome_num; i++)
    {
        int maxc = orders[i][jobs_num - 1].real_proc_t$[mach_num]; // 该个体对应的最大流程时间
        double fitness = 1.0 / (maxc * 1.0);
        Info tt; // 初始化该个体的染色体信息
        tt.id = i;
        tt.maxc = maxc;
        tt.fitness = fitness;
        tt.cumula_prob = DEFAULT_SET;
        chrome_list1.push_back(tt); // 有效元素下标从 0开始
    }
    return OK;
}

// 轮盘赌选择 + 复制
Status select(vector<vector<Job>> &orders, vector<Info> &chrome_list1, vector<vector<Job>> &random_chosen) // 个体适应度、种群
{
    // 计算选择概率分母
    double sum_fitness = 0;
    for (int i = 0; i < population_size; i++)
    {
        sum_fitness += chrome_list1[i].fitness;
    }

    // 计算个体的选择概率
    for (int i = 0; i < population_size; i++)
    {
        chrome_list1[i].cumula_prob = chrome_list1[i].fitness / sum_fitness;
    }

    // 计算个体的累积概率
    for (int i = 1; i < population_size; i++)
    {
        chrome_list1[i].cumula_prob += chrome_list1[i - 1].cumula_prob;
    } // printf("%lf", chrome_list[population_size-1].cumula_prob);  // 1.000000

    // 生成随机小数，选择个体
    double m2 = 0.0, n2 = 1.0;
    std::default_random_engine e2;
    e2.seed((unsigned int)time(NULL) * 10013);
    std::uniform_real_distribution<double> u2(m2, n2);

    int chosen_cnt = 0; // 个体选择计数器

    // 在 20个个体中选择复制 20个个体（染色体），可能有重复个体
    while (chosen_cnt < population_size)
    {
        double random_lf_1 = u2(e2);
        for (int j = 0; j < population_size; j++)
            if (chrome_list1[j].cumula_prob >= random_lf_1) // 选中
            {
                random_chosen.push_back(orders[chrome_list1[j].id]); // 从原始种群中复制个体
                ++chosen_cnt;
                break;
            }
    }

    // 更新种群中个体的完成时间
    jobs_proc_time(random_chosen);

    // 对 random_chosen 中的每个个体向量（染色体）求个体适应度，结果信息保存到 chrome_list1
    chrome_fitnesses(random_chosen, chrome_list1, population_size);

    // 按照适应度从大到小排序
    sort(chrome_list1.begin(), chrome_list1.end(), Fitness_Greater);

    return OK;
}

// 1 - 断点交叉算子
Status cross_over(vector<vector<Job>> &random_chosen, vector<Info> &chrome_list1)
{
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * 10013);
    std::uniform_real_distribution<double> u1(0.0, 1.0);
    std::uniform_int_distribution<unsigned> u2(0, population_size - 1);
    std::uniform_int_distribution<unsigned> u3(1, jobs_num - 1);

    // 两个一组进行交叉，真正最多执行 10次
    for (int i = 0; i < population_size / 2; i++) // chosen_num / 2
    {
        double cross_g = u1(e);

        // 若随机数小于交叉概率，执行交叉操作
        if (cross_probability >= cross_g)
        {
            // printf("Cross over!\n");
            // 记录当前最好的个体，对其进行保护
            int best_id_1 = chrome_list1[0].id;
            // printf("Protect: %d\n", best_id_1);
            int chrome1 = u2(e), chrome2 = u2(e); // 即将由随机数选出的两个个体（染色体）
            while ((chrome1 == chrome2) || (chrome1 == best_id_1) || (chrome2 == best_id_1))
            { // 不会将最优个体拿来交叉，即当随机数与最佳序号相等时，继续执行
                chrome1 = u2(e);
                chrome2 = u2(e);
            }

            // 得到随机断点，断点后的片段将参与交叉
            int break_point = u3(e);

            // 存储两个剪切下来的片段，以建立映射
            vector<Job> cut_part1;
            vector<Job> cut_part2;

            // 保存切片，并逐一交换基因
            for (int j = break_point; j < jobs_num; j++)
            {
                // 依次序保存交换部分，准备 PMX
                cut_part1.push_back(random_chosen[chrome1][j]);
                cut_part2.push_back(random_chosen[chrome2][j]);

                // 依次序交换
                Job tt(random_chosen[chrome1][j]);
                random_chosen[chrome1][j] = random_chosen[chrome2][j];
                random_chosen[chrome2][j] = tt;
            }

            // 交换部分的长度
            int cross_len = cut_part1.size();

            // 冲突消解，使用 PMX消解方法（共两组）
            // 寻找是否有重复基因（冲突点）
            for (int j = 0; j < break_point; j++)
            {
                vector<Job>::iterator cpt = find(cut_part2.begin(), cut_part2.end(), random_chosen[chrome1][j]);
                while (cpt != cut_part2.end()) // 仍存在冲突
                {
                    random_chosen[chrome1][j] = cut_part1[cpt - cut_part2.begin()];            // 映射赋值
                    cpt = find(cut_part2.begin(), cut_part2.end(), random_chosen[chrome1][j]); // 继续针对该点寻找
                }
            }
            for (int j = 0; j < break_point; j++)
            {
                vector<Job>::iterator cpt = find(cut_part1.begin(), cut_part1.end(), random_chosen[chrome2][j]);
                while (cpt != cut_part1.end()) // 仍存在冲突
                {
                    random_chosen[chrome2][j] = cut_part2[cpt - cut_part1.begin()];            // 映射赋值
                    cpt = find(cut_part1.begin(), cut_part1.end(), random_chosen[chrome2][j]); // 继续针对该点寻找
                }
            }
            chrome_list1.clear();

            // 更新种群中个体的完成时间
            jobs_proc_time(random_chosen);

            // 对 random_chosen 中的每个个体向量（染色体）求个体适应度，结果信息保存到 chrome_list1
            chrome_fitnesses(random_chosen, chrome_list1, population_size);

            // 按照适应度从大到小排序
            sort(chrome_list1.begin(), chrome_list1.end(), Fitness_Greater);
        }
    }
    return OK;
}

// 变异算子
Status mutation(vector<vector<Job>> &random_chosen, const vector<Job> &job_finder, vector<Info> &chrome_list1)
{
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * 10013);
    std::uniform_int_distribution<unsigned> u1(0, population_size - 1);
    std::uniform_int_distribution<unsigned> u2(0, jobs_num - 1);
    std::uniform_real_distribution<double> u3(0.0, 1.0);

    for (int i = 0; i < population_size; i++)
    {
        double mutate_g = u3(e);
        if (mutation_probability >= mutate_g)
        {
            // printf("Mutation!\n");
            // 记录当前最好的个体，对其进行保护
            int best_id = chrome_list1[0].id;
            int chrome = u1(e);        // 随机选定变异个体
            while (chrome == best_id)
            { // 不会将最优个体拿来交叉，即当随机数与最佳序号相等时，继续执行
                chrome = u1(e);
            }
            
            int mutate_point = u2(e);  // 随机选定变异个体上的变异基因
            Job tt(job_finder[u2(e)]); // 随机选定替换后的基因（注意：两个随机数并不一定相同）
            vector<Job>::iterator confront_point = find(random_chosen[chrome].begin(), random_chosen[chrome].end(), tt);
            (*confront_point) = random_chosen[chrome][mutate_point]; // 冲突解决
            random_chosen[chrome][mutate_point] = tt;

            // 更新种群中个体的完成时间
            jobs_proc_time(random_chosen);

            // 对 random_chosen 中的每个个体向量（染色体）求个体适应度，结果信息保存到 chrome_list1
            chrome_fitnesses(random_chosen, chrome_list1, population_size);

            // 按照适应度从大到小排序
            sort(chrome_list1.begin(), chrome_list1.end(), Fitness_Greater);
        }
    }
    return OK;
}

int main()
{
    // 定义 5个工件在 4个工序的预期工作时间（第一个有效元素为下标为 1的元素，0号特殊处理）
    int ex_proc_t1[] = {0, 31, 41, 25, 30}, ex_proc_t2[] = {0, 19, 55, 3, 34}, ex_proc_t3[] = {0, 23, 42, 27, 6},
        ex_proc_t4[] = {0, 13, 22, 14, 13}, ex_proc_t5[] = {0, 33, 5, 57, 19};

    // 构建 5个工件
    Job j1(1, ex_proc_t1), j2(2, ex_proc_t2), j3(3, ex_proc_t3), j4(4, ex_proc_t4), j5(5, ex_proc_t5);

    // 按照工件的序号构建工件的索引，便于后期查找使用
    vector<Job> job_finder;

    // 这里为了使工件编号与数组下标一致，第一个元素特殊处理
    job_finder.push_back(j1), job_finder.push_back(j1), job_finder.push_back(j2);
    job_finder.push_back(j3), job_finder.push_back(j4), job_finder.push_back(j5);

    // 染色体（单个加工序列）
    vector<Job> single;

    // 种群（工件加工顺序集），需要初始化
    vector<vector<Job>> orders;

    // 记录个体适应度，用小数表示
    vector<Info> chrome_list1;

    // 随机被选中的个体（染色体）的集合
    vector<vector<Job>> random_chosen;

    // 一波迭代后的种群个体信息
    vector<Info> chrome_list2;

    // 记录最优解最早出现的代数
    int best_solution_itnum = 0;
    bool flag = false;

    // 形成初始种群
    initialize(orders, single, job_finder);

    for (int i = 0; i < num_of_iteration; i++)
    {
        // 求种群中个体的完成时间
        jobs_proc_time(orders);

        // 对 orders 中的每个个体向量（染色体）求个体适应度，结果信息保存到 chrome_list1
        chrome_fitnesses(orders, chrome_list1, population_size);

        // 按照适应度从大到小排序
        sort(chrome_list1.begin(), chrome_list1.end(), Fitness_Greater);

        if (chrome_list1[0].maxc != best_time && !flag)
        {
            ++best_solution_itnum;
        }
        else if (chrome_list1[0].maxc == best_time && !flag)
        {
            flag = true;
        }

        // 轮盘赌选择
        select(orders, chrome_list1, random_chosen);

        // 针对轮盘赌形成的新种群执行交叉操作
        cross_over(random_chosen, chrome_list1);

        // 变异操作
        mutation(random_chosen, job_finder, chrome_list1);

        // 新种群作为下一次迭代的种群
        orders.clear();
        orders = random_chosen;
        random_chosen.clear();
        chrome_list1.clear();
        single.clear();
    }

    // 求种群中个体的完成时间
    jobs_proc_time(orders);

    // 对 random_chosen 中的每个个体向量（染色体）求个体适应度，结果信息保存到 chrome_list2
    chrome_fitnesses(orders, chrome_list2, population_size);

    // 按照适应度从大到小排序
    sort(chrome_list2.begin(), chrome_list2.end(), Fitness_Greater);

    printf("Best is: \n");
    int best_id = chrome_list2[0].id;
    for (int j = 0; j < jobs_num; j++)
    {
        printf("%d ", orders[best_id][j].GetId());
    }
    printf("\nFitness: %lf, procedure time: %d.\n", chrome_list2[0].fitness, chrome_list2[0].maxc);
    printf("Iteration num: %d\n", best_solution_itnum);

    return 0;
}
