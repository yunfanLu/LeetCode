#include <iostream>
#include <vector>
#include <cstdio>

const int MAX_V = 1234;

struct vertex
{
  std::vector<vertex *> edge;
};

void cin_groupu_table()
{
  std::vector<int> G[MAX_V];
  int V, E;
  scanf("%d %d", &V, &E);
  for (int i = 0; i < E; i++)
  {
    int s, t;
    scanf("%d %d\n", &s, &t);
    G[s].push_back(t);
    // G[t].push_back(G[s]);
  }
}

void cin_grouph_martix()
{
  vertex G[MAX_V];
  int V, E;
  scanf("%d %d", &V, &E);
  for (int i = 0; i < E; i ++){
    int s, t;
    scanf("%d %d", &s, &t);
    G[s].edge.push_back(&G[s]);
  }
}

int main()
{
  cin_grouph_martix();
  cin_groupu_table();
  return 0;
}
