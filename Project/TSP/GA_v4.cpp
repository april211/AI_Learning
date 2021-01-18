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

const double PI = 3.1415926535897;    // 圆周率
const double E = 2.718281828459045;   // 自然底数
const double A = -2111114;            // 适应度函数尺度变换参数
const double K = 4.0;                 // 适应度函数尺度变换参数
const double earth_radius = 6375.000; // 地球半径
const int city_num = 34;              // 城市总数目
const int population_size = 400;      // 种群规模
const int num_of_iteration = 1800;    // 迭代次数
const int group_size = 3;             // 锦标赛每组随机选择个体数
const double cross_coef1 = 0.7;       // 自适应交叉概率系数
const double cross_coef2 = 0.4;       // 自适应交叉概率系数
const double cross_cata = 0.7;        // 自适应交叉概率
const double mutation_coef1 = 0.30;   // 自适应变异概率系数
const double mutation_coef2 = 0.15;   // 自适应变异概率系数
const double mutation_cata = 0.30;    // 自适应变异概率
typedef int Status;

// 随机数种子扰动因子
int random_disturb = 1114;

// 迭代数
int iter = 0;

// 全局最优个体信息，会不断变动
int best_id = DEFAULT_SET;
double best_fit = DEFAULT_SET * 1.0;
double avg_fit = 0.0;

// 城市类
class City
{
protected:
    int id$;           // 城市编号
    string name$;      // 城市名
    double latitude$;  // 城市纬度
    double longitude$; // 城市经度
public:
    // 构造函数
    City() : id$(DEFAULT_SET), latitude$(1.0 * DEFAULT_SET), longitude$(1.0 * DEFAULT_SET) {}
    City(int id, string name, double latitude, double longitude) : id$(id), name$(name), latitude$(latitude), longitude$(longitude) {}
    City(const City &tt) : id$(tt.id$), name$(tt.name$), latitude$(tt.latitude$), longitude$(tt.longitude$) {}

    // 析构函数
    ~City() {}

    // 重载运算符
    bool operator==(const City &c)
    {
        // 城市编号、经纬度均相等时才可以判相等
        if (id$ == c.id$ && latitude$ == c.latitude$ && longitude$ == c.longitude$ && name$ == c.name$)
            return true;
        else
            return false;
    }

    bool operator!=(const City &c)
    {
        if (id$ != c.id$ || latitude$ != c.latitude$ || longitude$ != c.longitude$ || name$ != c.name$)
            return true;
        else
            return false;
    }

    City operator=(const City &tt)
    {
        id$ = tt.id$, latitude$ = tt.latitude$, longitude$ = tt.longitude$, name$ = tt.name$;
        return (*this);
    }

    // 类内操作
    int Get_Id() const { return id$; }
    double Get_Latitude() const { return latitude$; }
    double Get_Longitude() const { return longitude$; }
    string Get_Name() const { return name$; }

    // 声明友元类
    friend class Chrome;
};

// 标准城市索引
vector<City> city_lib;

// 染色体类
class Chrome
{
public:
    double sum_miles$;        // 道路总里程
    double fitness$;          // 个体适应度
    double cumu_odds$;        // 累计概率
    vector<City> city_array$; // 城市访问顺序的数组

public:
    // 构造函数
    Chrome() : fitness$(1.0 * DEFAULT_SET), cumu_odds$(DEFAULT_SET), sum_miles$(1.0 * DEFAULT_SET)
    {
        City tt;
        for (int i = 0; i < city_num; i++)
        {
            city_array$.push_back(tt);
        }
    }
    Chrome(const Chrome &tt) : fitness$(tt.fitness$), cumu_odds$(tt.cumu_odds$), sum_miles$(tt.sum_miles$)
    {
        city_array$.clear();               // 先清除
        for (int i = 0; i < city_num; i++) // 深拷贝
        {
            city_array$.push_back(tt.city_array$[i]);
        }
    }

    // 析构函数
    ~Chrome() {}

    // 重载运算符
    bool operator==(const Chrome &c)
    {
        // 城市顺序相同即可，增强鲁棒性
        bool flag = true;
        for (int i = 0; i < city_num; i++)
        {
            if (city_array$[i] != c.city_array$[i])
            {
                flag = false;
                break;
            }
        }
        return flag;
    }

    bool operator!=(const Chrome &c)
    {
        bool flag = false;
        for (int i = 0; i < city_num; i++)
        {
            if (city_array$[i] != c.city_array$[i])
            {
                flag = true;
                break;
            }
        }
        return flag;
    }

    Chrome operator=(const Chrome &tt)
    {
        fitness$ = tt.fitness$;
        cumu_odds$ = tt.cumu_odds$;
        sum_miles$ = tt.sum_miles$;
        city_array$.clear();               // 先清除
        for (int i = 0; i < city_num; i++) // 深拷贝
        {
            city_array$.push_back(tt.city_array$[i]);
        }
        return (*this);
    }

    // 计算两个城市的距离
    double City_Distance(const City &c1, const City &c2)
    {
        //printf("%lf.\n", c1.Get_Latitude());
        double sla1 = sin(c1.latitude$ * PI / 180.0), cla1 = cos(c1.latitude$ * PI / 180.0),
               slo1 = sin(c1.longitude$ * PI / 180.0), clo1 = cos(c1.longitude$ * PI / 180.0);
        double sla2 = sin(c2.latitude$ * PI / 180.0), cla2 = cos(c2.latitude$ * PI / 180.0),
               slo2 = sin(c2.longitude$ * PI / 180.0), clo2 = cos(c2.longitude$ * PI / 180.0);

        double x1 = cla1 * clo1;
        double x2 = cla2 * clo2;

        double y1 = cla1 * slo1;
        double y2 = cla2 * slo2;

        double z1 = sla1;
        double z2 = sla2;

        double dot_product = x1 * x2 + y1 * y2 + z1 * z2;

        double angle = acos(dot_product);

        return fabs(angle * earth_radius);
    }

    // （当发生交叉变异时）刷新个体适应度和总里程（重新求总里程）
    Status Refresh_Fitness()
    {
        double sum = 0.0;
        for (int i = 0; i < city_num - 1; i++)
        {
            sum += City_Distance(city_array$[i], city_array$[i + 1]);
        }
        sum += City_Distance(city_array$[0], city_array$[city_num-1]);  // 闭环
        sum_miles$ = sum; // 更新最新里程
        //printf("miles: %lf.\n", sum);
        fitness$ = 1e6 / sum; // 总里程越大，个体适应度越小
        fitness$ = pow(fitness$, K);
        // printf("fitness: %lf.\n", fitness$);
        //fitness$ = pow(E, -A * fitness$);
        return OK;
    }

    // 2-断点交叉算子（仅完成对染色体上部分基因的交换）
    Status Cross_Over(Chrome &another_chrome)
    {\
        // printf("Cross over Started!\n");
        ++random_disturb;
        std::default_random_engine e;
        e.seed((unsigned int)time(NULL) * abs(random_disturb));
        std::uniform_real_distribution<double> u1(0.0, 1.0);
        std::uniform_int_distribution<unsigned> u2(1, city_num - 1);

        // 计算这对个体发生交叉的概率
        double cross_odds = 0.0;
        double chrome1_fit = fitness$;
        double chrome2_fit = another_chrome.fitness$;

        double greater_fitness = (chrome1_fit > chrome2_fit) ? chrome1_fit : chrome2_fit;

        // 避免局部最优
        if (fabs(best_fit - avg_fit) < 6000.0 && iter < num_of_iteration / 3)
        {
            cross_odds = cross_cata;
            // printf("Adjusted cross_odds: %lf.\n", cross_odds);
        }
        else
        {
            cross_odds = cross_coef2 + ((cross_coef1 - cross_coef2) / (1.0 + pow(E, (10.0 * (greater_fitness - avg_fit) / (best_fit - avg_fit)))));
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

            // 交换部分的长度
            int cross_len = break_point2 - break_point1;

            // 两条染色体剩余部分序列
            vector<City> rest1;
            vector<City> rest2;
            rest1.clear(), rest2.clear();

            // 获取个体1 剩余部分
            for (int i = 0; i < city_num; i++)
            {
                vector<City>::iterator cpt = find(another_chrome.city_array$.begin() + break_point1, another_chrome.city_array$.begin() + break_point2, city_array$[i]);
                if (cpt == another_chrome.city_array$.begin() + break_point2)
                {
                    rest1.push_back(city_array$[i]);
                }
            }

            // 获取个体2 剩余部分
            for (int i = 0; i < city_num; i++)
            {
                vector<City>::iterator cpt = find(city_array$.begin() + break_point1, city_array$.begin() + break_point2, another_chrome.city_array$[i]);
                if (cpt == city_array$.begin() + break_point2)
                {
                    rest2.push_back(another_chrome.city_array$[i]);
                }
            }

            // 逐一交换基因（ break_point2不参与）
            for (int j = break_point1; j < break_point2; j++)
            {
                // 依次序交换
                City tt(city_array$[j]);
                city_array$[j] = another_chrome.city_array$[j];
                another_chrome.city_array$[j] = tt;
            }

            int cnt = 0;
            for (int i = 0; i < break_point1; i++)
            {
                city_array$[i] = rest1[cnt];
                another_chrome.city_array$[i] = rest2[cnt];
                ++cnt;
            }
            for (int i = break_point2; i < city_num; i++)
            {
                city_array$[i] = rest1[cnt];
                another_chrome.city_array$[i] = rest2[cnt];
                ++cnt;
            }
            // printf("I'm alive!\n");
            // 更新两条染色体的里程数（适应度）
            Refresh_Fitness();
            another_chrome.Refresh_Fitness();
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
        std::uniform_int_distribution<unsigned> u1(0, city_num - 1);
        std::uniform_real_distribution<double> u2(0.0, 1.0);

        // 计算这个个体发生变异的概率
        double mutation_odds = 0;
        // printf("%lf %lf\n", best_fit, avg_fit);
        // 避免局部最优
        if (fabs(best_fit - avg_fit) < 6000.0)
        {
            mutation_odds = mutation_cata;
            //printf("Adjusted mutation_odds: %lf.\n", mutation_odds);
        }
        else
        {
            mutation_odds = mutation_coef2 + ((mutation_coef1 - mutation_coef2) / (1.0 + pow(E, (10.0 * (fitness$ - avg_fit) / (best_fit - avg_fit)))));
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

            City ttc(city_array$[mutate_point2]);

            // 后移
            for (int i = mutate_point2 - 1; i > mutate_point1; i--)
            {
                city_array$[i + 1] = city_array$[i];
            }

            // 互换位置
            city_array$[mutate_point1 + 1] = ttc;

            // 更新适应度
            Refresh_Fitness();
        }
        //printf("Mutation end!\n");
        return OK;
    }
};

// 读入城市信息
Status Read();

// 初始化种群
Status Initialize(vector<Chrome> &origin);

// 轮盘赌选择
Status Select_Wheel(vector<Chrome> &origin, vector<Chrome> &random_chosen);

// 锦标赛选择
Status Select_Tourn(vector<Chrome> &origin, vector<Chrome> &random_chosen);

// 更新全局最优个体信息
Status Refresh_Bestinfo(const vector<Chrome> &population)
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
    ++random_disturb;
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * abs(random_disturb));
    std::uniform_int_distribution<unsigned> u(0, population_size - 1);

    // 初始种群
    vector<Chrome> origin;

    // 轮盘赌选择后的种群
    vector<Chrome> random_chosen;

    // 每次迭代后产生的最优个体
    vector<Chrome> bests_history;

    // 初始化城市数据
    Read();

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

        // 新种群作为下一次迭代的种群
        origin.clear();
        origin = random_chosen;
        random_chosen.clear();
        Refresh_Bestinfo(origin);
        bests_history.push_back(origin[best_id]);
        printf("Iter: (%d / %d).\n", iter, num_of_iteration);
    }

    Refresh_Bestinfo(bests_history);
    printf("Best miles is: %.5lf.\n", bests_history[best_id].sum_miles$);
    for (int i = 0; i < city_num; i++)
    {
        if (i == 0)
            cout << bests_history[best_id].city_array$[i].Get_Name();
        else
            cout << " -> " << bests_history[best_id].city_array$[i].Get_Name();
    }
    cout << " -> " << bests_history[best_id].city_array$[0].Get_Name();

    return 0;
}

// 排序信息
typedef struct SortInfo
{
    int id;
    double random_value;
} SortInfo;

bool Smaller(const SortInfo &a, const SortInfo &b)
{
    return (a.random_value < b.random_value);
}

// 初始化种群
Status Initialize(vector<Chrome> &origin)
{
    ++random_disturb;
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * abs(random_disturb));
    std::uniform_real_distribution<double> u1(0.0, 100.0);

    for (int j = 0; j < population_size; j++)
    {
        // 随机数信息列
        vector<SortInfo> r_array;
        for (int i = 0; i < city_num; i++)
        {
            SortInfo tt;
            tt.id = i;
            tt.random_value = u1(e);
            r_array.push_back(tt);
        }

        // 排序，打乱原始编号顺序
        sort(r_array.begin(), r_array.end(), Smaller);
        Chrome tt;
        for (int i = 0; i < city_num; i++)
        {
            City ttt(city_lib[r_array[i].id]);
            tt.city_array$[i] = ttt;
        }
        tt.Refresh_Fitness();
        origin.push_back(tt);
    }
    return OK;
}

// 轮盘赌选择
Status Select_Wheel(vector<Chrome> &origin, vector<Chrome> &random_chosen)
{
    ++random_disturb;
    //printf("Select Started!\n");
    // 计算选择概率分母
    double sum_fitness = 0.0;
    for (int i = 0; i < population_size; i++)
    {
        sum_fitness += origin[i].fitness$;
    }

    // 计算个体的选择概率
    for (int i = 0; i < population_size; i++)
    {
        origin[i].cumu_odds$ = origin[i].fitness$ / sum_fitness;
    }

    // 计算个体的累积概率
    for (int i = 1; i < population_size; i++)
    {
        origin[i].cumu_odds$ += origin[i - 1].cumu_odds$;
    }

    // 生成随机小数，选择个体
    std::default_random_engine e;
    e.seed((unsigned int)time(NULL) * abs(random_disturb));
    std::uniform_real_distribution<double> u(0.0, 1.0);

    int chosen_cnt = 0; // 个体选择计数器

    // 选择复制个体（染色体），可能有重复个体
    while (chosen_cnt < population_size)
    { //printf("ddd\n");
        double random_lf_1 = u(e);
        for (int j = 0; j < population_size; j++)
        {
            if (origin[j].cumu_odds$ >= random_lf_1) // 选中
            {
                random_chosen.push_back(origin[j]); // 从原始种群中复制个体
                ++chosen_cnt;
                break;
            }
        }
    }
    //printf("Select end!\n");
    return OK;
}

// 锦标赛选择
Status Select_Tourn(vector<Chrome> &origin, vector<Chrome> &random_chosen)
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
        vector<Chrome> group;                // 锦标赛小组
        for (int i = 0; i < group_size; i++) // 随机选取 group_size 个个体进入小组
        {
            int id = u(e);
            origin[id].Refresh_Fitness();
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

// 读入城市信息
Status Read()
{
    city_lib.clear();
    City tt1(0, "Harbin", 45.45, 126.38);
    city_lib.push_back(tt1);
    //printf("%lf.\n", city_lib[0].Get_Latitude());

    City tt2(1, "Urumqi", 43.46, 87.36);
    city_lib.push_back(tt2);

    City tt3(2, "Hohhot", 40.48, 111.38);
    city_lib.push_back(tt3);

    City tt4(3, "Tianjin", 39.10, 117.10);
    city_lib.push_back(tt4);

    City tt5(4, "Shijiazhuang", 38.03, 114.26);
    city_lib.push_back(tt5);

    City tt6(5, "Jinan", 36.40, 117.02);
    city_lib.push_back(tt6);

    City tt7(6, "Lanzhou", 36.03, 103.50);
    city_lib.push_back(tt7);

    City tt8(7, "Xi`an", 34.15, 108.55);
    city_lib.push_back(tt8);

    City tt9(8, "Shanghai", 31.12, 121.26);
    city_lib.push_back(tt9);

    City tt10(9, "Nanjing", 32.03, 118.46);
    city_lib.push_back(tt10);

    City tt11(10, "Hangzhou", 30.15, 120.10);
    city_lib.push_back(tt11);

    City tt12(11, "Chongqing", 29.33, 106.33);
    city_lib.push_back(tt12);

    City tt13(12, "Changsha", 28.12, 112.55);
    city_lib.push_back(tt13);

    City tt14(13, "Fuzhou", 26.02, 119.19);
    city_lib.push_back(tt14);

    City tt15(14, "Taibei", 25.02, 121.31);
    city_lib.push_back(tt15);

    City tt16(15, "Nanning", 22.47, 108.21);
    city_lib.push_back(tt16);

    City tt17(16, "Hongkong", 22.15, 114.15);
    city_lib.push_back(tt17);

    City tt18(17, "Changchun", 43.55, 125.18);
    city_lib.push_back(tt18);

    City tt19(18, "Shenyang", 41.48, 123.23);
    city_lib.push_back(tt19);

    City tt20(19, "Beijing", 39.54, 116.28);
    city_lib.push_back(tt20);

    City tt21(20, "Yinchuan", 38.28, 106.13);
    city_lib.push_back(tt21);

    City tt22(21, "Taiyuan", 37.51, 112.33);
    city_lib.push_back(tt22);

    City tt23(22, "Xining", 36.37, 101.49);
    city_lib.push_back(tt23);

    City tt24(23, "Zhengzhou", 34.44, 113.42);
    city_lib.push_back(tt24);

    City tt25(24, "Hefei", 31.51, 117.16);
    city_lib.push_back(tt25);

    City tt26(25, "Wuhan", 30.37, 114.20);
    city_lib.push_back(tt26);

    City tt27(26, "Chengdu", 30.39, 104.04);
    city_lib.push_back(tt27);

    City tt28(27, "Lasa", 29.39, 91.02);
    city_lib.push_back(tt28);

    City tt29(28, "Nanchang", 28.41, 115.53);
    city_lib.push_back(tt29);

    City tt30(29, "Guiyang", 26.34, 106.43);
    city_lib.push_back(tt30);

    City tt31(30, "Kunming", 25.03, 102.42);
    city_lib.push_back(tt31);

    City tt32(31, "Guangzhou", 23.10, 113.18);
    city_lib.push_back(tt32);

    City tt33(32, "Aomen", 22.20, 113.50);
    city_lib.push_back(tt33);

    City tt34(33, "Haikou", 20.03, 110.10);
    city_lib.push_back(tt34);

    return OK;
}
