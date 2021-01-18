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

const double E = 2.71828182845904;  // 自然底数
const int goods_sum = 8;            // 物品总数目
const int population_size = 20;    // 种群规模
const int num_of_iteration = 10;   // 迭代次数
const int group_size = 3;           // 锦标赛每组随机选择个体数
const double cross_coef1 = 0.7;     // 自适应交叉概率系数
const double cross_coef2 = 0.4;     // 自适应交叉概率系数
const double cross_cata = 0.7;      // 自适应交叉概率
const double mutation_coef1 = 0.30; // 自适应变异概率系数
const double mutation_coef2 = 0.15; // 自适应变异概率系数
const double mutation_cata = 0.30;  // 自适应变异概率
typedef int Status;

// 随机数种子扰动因子
int random_disturb = 1114;

// 迭代数
int iter = 0;

// 全局最优个体信息，会不断变动
int best_id = DEFAULT_SET;
double best_fit = DEFAULT_SET * 1.0;
double avg_fit = 0.0;

// 货物信息
typedef struct Goods
{
    int id;       // 物品编号
    double c;     // 物品利润
    double w;     // 物品重量
    double ratio; // c/w 的比率
} Goods;

// 货物信息索引
vector<Goods> goods_list;
double sum_weight = 0.0;

// 读入货物信息
Status Read()
{
    goods_list.clear();
    Goods tt0;
    tt0.w = 30.0, tt0.c = 47.0, tt0.id = 0, tt0.ratio = tt0.c / tt0.w;
    goods_list.push_back(tt0);
    Goods tt1;
    tt1.w = 40.0, tt1.c = 30.0, tt1.id = 1, tt1.ratio = tt1.c / tt1.w;
    goods_list.push_back(tt1);
    Goods tt2;
    tt2.w = 20.0, tt2.c = 9.0, tt2.id = 2, tt2.ratio = tt2.c / tt2.w;
    goods_list.push_back(tt2);
    Goods tt3;
    tt3.w = 5.0, tt3.c = 8.0, tt3.id = 3, tt3.ratio = tt3.c / tt3.w;
    goods_list.push_back(tt3);
    Goods tt4;
    tt4.w = 15.0, tt4.c = 15.0, tt4.id = 4, tt4.ratio = tt4.c / tt4.w;
    goods_list.push_back(tt4);
    Goods tt5;
    tt5.w = 60.0, tt5.c = 66.0, tt5.id = 5, tt5.ratio = tt5.c / tt5.w;
    goods_list.push_back(tt5);
    Goods tt6;
    tt6.w = 25.0, tt6.c = 12.0, tt6.id = 6, tt6.ratio = tt6.c / tt6.w;
    goods_list.push_back(tt6);
    Goods tt7;
    tt7.w = 10.0, tt7.c = 11.0, tt7.id = 7, tt7.ratio = tt7.c / tt7.w;
    goods_list.push_back(tt7);
    return OK;
}

// 计算货物的总重量
Status Cal_Sum_Weight()
{
    sum_weight = 0.0;
    for (int i = 0; i < goods_sum; i++)
    {
        sum_weight += goods_list[i].w;
    }
    return OK;
}

// 背包类
class Knapsack
{
public:
    double weight$;           // 当前载重量
    double sumc$;             // 背包内物品总价值
    double goods_num$;        // 已装载物品数量
    double fitness$;          // 背包的适应度
    vector<int> goods_array$; // 装载货物的信息（二进制编码）

public:
    const double pack_capacity = 100.0; // 背包容量

public:
    Knapsack() : weight$(DEFAULT_SET * 1.0), goods_num$(DEFAULT_SET * 1.0), fitness$(DEFAULT_SET * 1.0), sumc$(DEFAULT_SET * 1.0)
    {
        goods_array$.clear();
        for (int i = 0; i < goods_sum; i++)
        {
            goods_array$.push_back(0);
        }
    }
    Knapsack(const Knapsack &tt) : weight$(tt.weight$), goods_num$(tt.goods_num$), fitness$(tt.fitness$), sumc$(tt.sumc$)
    {
        goods_array$.clear();
        for (int i = 0; i < goods_sum; i++)
        {
            goods_array$.push_back(tt.goods_array$[i]); //***
        }
    }
    ~Knapsack() {}

public:
    bool operator==(const Knapsack &k)
    {
        bool flag = true;
        for (int i = 0; i < goods_sum; i++)
        {
            if (goods_array$[i] != k.goods_array$[i])
            {
                flag = false;
                break;
            }
        }
        return flag;
    }

    bool operator!=(const Knapsack &k)
    {
        bool flag = false;
        for (int i = 0; i < goods_sum; i++)
        {
            if (goods_array$[i] != k.goods_array$[i])
            {
                flag = true;
                break;
            }
        }
        return flag;
    }

    Knapsack operator=(const Knapsack &tt)
    {
        weight$ = tt.weight$, goods_num$ = tt.goods_num$, fitness$ = tt.fitness$, sumc$ = tt.sumc$;
        goods_array$.clear();
        for (int i = 0; i < goods_sum; i++)
        {
            goods_array$.push_back(tt.goods_array$[i]); //***
        }
        return (*this);
    }

public:
    // 刷新背包适应度等信息
    Status Refresh_Status()
    {
        double delta = std::min(pack_capacity, fabs(sum_weight - pack_capacity));
        double p = 0.0;
        double ttsumw = 0.0, ttsumc = 0.0;
        int ttcnt = 0;
        for (int i = 0; i < goods_sum; i++)
        {
            ttsumw += (goods_list[i].w) * goods_array$[i];
            ttsumc += (goods_list[i].c) * goods_array$[i];
            ttcnt += goods_array$[i];
        }
        p = 1.0 - (fabs(ttsumw - pack_capacity) / delta);
        weight$ = ttsumw;
        sumc$ = ttsumc;
        goods_num$ = ttcnt;
        fitness$ = ttsumc * p;
        return OK;
    }

    // 解码（到最后输出结果前才使用）
    Status Decode(vector<int> &ans, double &sumc)
    {
        // 存储被选中的物品的序号
        vector<int> chosen;
        for (int i = 0; i < goods_sum; i++)
        {
            if (goods_array$[i] == 1)
            {
                chosen.push_back(i);
            }
        }

        int size = chosen.size();
        ans.clear();

        if (size != 0)
        {
            // 按照比率，由大到小排序
            for (int i = 0; i < size - 1; i++)
            {
                for (int j = 0; j < size - i - 1; j++)
                {
                    if (goods_list[chosen[j]].ratio < goods_list[chosen[j + 1]].ratio)
                    {
                        int temp = chosen[j];
                        chosen[j] = chosen[j + 1];
                        chosen[j + 1] = temp;
                    }
                }
            }

            // 由初始二进制编码获得结果信息
            int cnt = 0;
            double now_w = 0.0, now_c = 0.0;
            while (cnt < size)
            {
                if (now_w + goods_list[chosen[cnt]].w <= pack_capacity)
                {
                    now_w += goods_list[chosen[cnt]].w;
                    now_c += goods_list[chosen[cnt]].c;
                    ans.push_back(chosen[cnt]);
                    sumc = now_c;
                    cnt++;
                }
                else // now_w > pack_capacity
                {
                    break; // 背包已满，结束循环
                }
            }
            // 修正原二进制编码为可行编码
            size = ans.size();
            goods_array$.clear();
            for (int i = 0; i < goods_sum; i++)
            {
                goods_array$.push_back(0);
            }
            for (int i = 0; i < size; i++)
            {
                goods_array$[ans[i]] = 1;
            }
        }
        else
        {
            sumc = 0;
        }
        Refresh_Status();
        return OK;
    }

    // 2-断点交叉算子（仅完成对染色体上部分基因的交换）
    Status Cross_Over(Knapsack &another_chrome)
    {
        // printf("Cross over Started!\n");
        ++random_disturb;
        std::default_random_engine e;
        e.seed((unsigned int)time(NULL) * abs(random_disturb));
        std::uniform_real_distribution<double> u1(0.0, 1.0);
        std::uniform_int_distribution<unsigned> u2(1, goods_sum - 1);

        // 计算这对个体发生交叉的概率
        double cross_odds = 0.0;
        double chrome1_fit = fitness$;
        double chrome2_fit = another_chrome.fitness$;

        double greater_fitness = (chrome1_fit > chrome2_fit) ? chrome1_fit : chrome2_fit;

        // 避免局部最优
        if (fabs(best_fit - avg_fit) < 0.3 && iter < num_of_iteration / 3)
        {
            cross_odds = cross_cata;
            printf("Adjusted cross_odds: %lf.\n", cross_odds);
        }
        else
        {
            cross_odds = cross_coef2 + ((cross_coef1 - cross_coef2) / (1.0 + pow(E, (10.0 * (greater_fitness - avg_fit) / (best_fit - avg_fit)))));
            //printf("Cross_odds: %lf.\n", cross_odds);
        }

        double cross_g = u1(e);

        // 若随机数小于交叉概率，执行交叉操作
        if (cross_odds >= cross_g)
        {
            // 得到随机断点，断点后的片段将参与交叉
            int break_point1 = u2(e);
            int break_point2 = u2(e);
            while (break_point1 >= break_point2) // break_point1 < break_point2
            {
                break_point1 = u2(e);
                break_point2 = u2(e);
            }

            // printf("%d %d\n", break_point1, break_point2);

            // 逐一交换基因（ break_point2不参与）
            for (int j = break_point1; j < break_point2; j++)
            {
                // 依次序交换
                int tt = goods_array$[j];
                goods_array$[j] = another_chrome.goods_array$[j];
                another_chrome.goods_array$[j] = tt;
            }
            // printf("I'm alive!\n");
            // 更新两条染色体的里程数（适应度）
            Refresh_Status();
            another_chrome.Refresh_Status();
        }
        // printf("Cross over end!\n");
        return OK;
    }

    // 变异算子
    Status Mutation()
    {
        //printf("Mutation Started!\n");
        ++random_disturb;
        std::default_random_engine e;
        e.seed((unsigned int)time(NULL) * abs(random_disturb));
        std::uniform_int_distribution<unsigned> u1(0, goods_sum - 1);
        std::uniform_real_distribution<double> u2(0.0, 1.0);

        // 计算这个个体发生变异的概率
        double mutation_odds = 0;
        // printf("%lf %lf\n", best_fit, avg_fit);
        // 避免局部最优
        if (fabs(best_fit - avg_fit) < 0.3)
        {
            mutation_odds = mutation_cata;
            printf("Adjusted mutation_odds: %lf.\n", mutation_odds);
        }
        else
        {
            mutation_odds = mutation_coef2 + ((mutation_coef1 - mutation_coef2) / (1.0 + pow(E, (10.0 * (fitness$ - avg_fit) / (best_fit - avg_fit)))));
            //printf("Mutation_odds: %lf.\n", mutation_odds);
        }

        double mutate_g = u2(e);
        if (mutation_odds >= mutate_g)
        {
            int mutate_point1 = u1(e); // 随机选定变异个体上的两个变异基因
            int mutate_point2 = u1(e);
            while (mutate_point1 >= mutate_point2) // mutate_point1 < mutate_point2
            {
                mutate_point1 = u1(e);
                mutate_point2 = u1(e);
            }

            int ttc = goods_array$[mutate_point2];

            // 后移
            for (int i = mutate_point2 - 1; i > mutate_point1; i--)
            {
                goods_array$[i + 1] = goods_array$[i];
            }

            // 互换位置
            goods_array$[mutate_point1 + 1] = ttc;

            // 更新适应度
            Refresh_Status();
        }
        //printf("Mutation end!\n");
        return OK;
    }
};

// 初始化种群
Status Initialize(vector<Knapsack> &origin);

// 锦标赛选择
Status Select_Tourn(vector<Knapsack> &origin, vector<Knapsack> &random_chosen);

// 更新全局最优个体信息
Status Refresh_Bestinfo(const vector<Knapsack> &population)
{
    best_id = DEFAULT_SET, best_fit = DEFAULT_SET * 1.0, avg_fit = 0.0;
    for (int i = 0; i < population_size; i++)
    {
        if (population[i].fitness$ > best_fit)
        {
            best_id = i;
            best_fit = population[i].fitness$;
        }
        avg_fit += population[i].fitness$;
    }
    avg_fit /= population_size;
    return OK;
}

int main()
{
    // 初始化标准物品列表
    Read();
    Cal_Sum_Weight();

    ++random_disturb;
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * abs(random_disturb));
    std::uniform_int_distribution<unsigned> u(0, population_size - 1);

    // 初始种群
    vector<Knapsack> origin;

    // 选择种群
    vector<Knapsack> random_chosen;

    // 历史最优个体
    vector<Knapsack> bests_history;

    // 种群初始化
    Initialize(origin);

    for (iter = 0; iter < num_of_iteration; iter++)
    {
        // 执行选择算子
        Select_Tourn(origin, random_chosen);

        // 执行交叉算子
        for (int j = 0; j < population_size / 2; j++)
        {
            Refresh_Bestinfo(random_chosen);
            int cross_id_1 = u(e);
            int cross_id_2 = u(e);
            while (cross_id_1 == cross_id_2)
            {
                cross_id_1 = u(e);
                cross_id_2 = u(e);
            }
            random_chosen[cross_id_1].Cross_Over(random_chosen[cross_id_2]);
        }

        // 执行变异算子
        for (int j = 0; j < population_size; j++)
        {
            Refresh_Bestinfo(random_chosen);
            int mutate_id = u(e);
            random_chosen[mutate_id].Mutation();
        }

        // 修正
        for (int i = 0; i < population_size; i++)
        {
            vector<int> tans;
            double sc = 0.0;
            random_chosen[i].Decode(tans, sc);
        }

        // 新种群作为下一次迭代的种群
        origin.clear();
        origin = random_chosen;
        random_chosen.clear();
        bests_history.push_back(origin[best_id]);
        printf("Iter: (%d / %d).\n", iter, num_of_iteration);
    }

    Refresh_Bestinfo(bests_history);
    printf("Best is: %.2lf.\n", bests_history[best_id].sumc$);
    printf("Should bring: \n");
    vector<int> ans;
    double sumc = 0.0;
    bests_history[best_id].Decode(ans, sumc);
    for (int i = 0; i < ans.size(); i++)
    {
        printf("%d ", ans[i] + 1);
    }

    return 0;
}

// 初始化种群
Status Initialize(vector<Knapsack> &origin)
{
    ++random_disturb;
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * abs(random_disturb));
    std::uniform_real_distribution<double> u(0.0, 1.0);

    origin.clear();
    for (int i = 0; i < population_size; i++)
    {
        Knapsack tt;
        for (int j = 0; j < goods_sum; j++)
        {
            int r = int(u(e) + 0.5); // r == 0 or 1
            tt.goods_array$[j] = r;
        }
        tt.Refresh_Status();
        origin.push_back(tt);
    }
    return OK;
}

// 锦标赛选择
Status Select_Tourn(vector<Knapsack> &origin, vector<Knapsack> &random_chosen)
{
    ++random_disturb;

    // 生成随机小数，选择个体
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * abs(random_disturb));
    std::uniform_real_distribution<double> u(0, population_size - 1);

    // 选择个体计数器
    int chosen_cnt = 0;

    while (chosen_cnt < population_size)
    {
        vector<Knapsack> group;              // 锦标赛小组
        for (int i = 0; i < group_size; i++) // 随机选取 group_size 个个体进入小组
        {
            int id = u(e);
            origin[id].Refresh_Status();
            group.push_back(origin[id]);
        }

        // 寻找该随机小组中的最优个体
        int tt_best_id = DEFAULT_SET;
        double tt_best_fit = 1.0 * DEFAULT_SET;
        for (int i = 0; i < group_size; i++)
        {
            if (tt_best_fit < group[i].fitness$)
            {
                tt_best_fit = group[i].fitness$;
                tt_best_id = i;
            }
        }
        random_chosen.push_back(group[tt_best_id]);
        ++chosen_cnt;
    }

    return OK;
}
