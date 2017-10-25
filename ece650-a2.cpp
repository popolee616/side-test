#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <unordered_map>
#include <sstream>
#include <string>
#include <algorithm>

#include <stdio.h>
#include <cstdio>

using namespace std;

class Graph {
private:
    vector< list<unsigned> > adj_list;
    vector<bool> isVisited;
    unsigned number_nodes;

    vector<unsigned> bfs(int src) {

        queue<unsigned> q;
        vector<unsigned> previous_node(number_nodes, -1);
        for (unsigned i=0; i<previous_node.size(); i++) {
            previous_node[i] = i;
        }

        isVisited.clear();
        isVisited.resize(number_nodes+1, false);

        q.push(src);
        isVisited[src] = true;

        while(!q.empty()) {
            //get the first element in queue
            int parent_node = q.front();
            //enQueue child_node
            for (auto child_node:adj_list[parent_node]) {
                if (!isVisited[child_node]) {// check if child_node is already enQueueed
                    q.push(child_node);
                    isVisited[child_node] = true;
                    //construct shortest_path from child_node to src
                    previous_node[child_node] = parent_node;
                }
            }
            //deQueue parent_node
            q.pop();
        }
        return previous_node;
    }

public:
    void init(unsigned N) {
        number_nodes = N;
        adj_list.resize(number_nodes+1);
        isVisited.resize(number_nodes+1, false);
    }

    //set edge to both v0 and v1
    void set_edge(unsigned v0, unsigned v1) {
        //v0 edge
        adj_list[v0].push_back(v1);
        //v1 edge
        adj_list[v1].push_back(v0);
    }

    void set_graph(unsigned N, list<pair<unsigned,unsigned>> edges) {
        //set V
        init(N);
        //set edges
        for ( auto &edge:edges ) {
            set_edge(edge.first,edge.second);
        }
    }

    void get_shortest_path(unsigned src, unsigned dst) {
        list<unsigned> stp;
        //push destination into stp
        if (src == dst) stp.push_front(dst);
        else {
            vector<unsigned> path = bfs(src);
            unsigned pre = path[dst];

            if (pre != dst) {
                stp.push_front(dst);
                while (pre != src) {
                    stp.push_front(pre);
                    pre = path[pre];
                }
                stp.push_front(pre);
            }
        }
        for (auto tmp:stp) {
            if (tmp != stp.back() ) cout << tmp << "-";
            else cout << tmp;
        }
        if (stp.size() > 0) {
            cout << endl;//end of line shortest path
        } else {
            fprintf(stderr,"Error: no shortest path\n");
        }
    }
};

class Input {
public:
    unsigned number_nodes = -1;
    vector<unsigned> edges;
    list< pair<unsigned,unsigned> > pair_edges;
    unsigned v0,v1;
    bool E_already_valid = false;

    void get_input() {
        while (!cin.eof()) {
            string line;
            getline(cin, line);

            //check s before whitespaces are deleted
            if (line.front()=='s') {
                char type3 = ' ';
                unsigned tmp0,tmp1 = -1;
                stringstream input;

                input << line;
                //stringstream input uses whitespace to recognize items in it
                input >> type3 >> tmp0 >> tmp1;
                if (input.fail()) {
                    fprintf(stderr,"Error:fail to catch an int argument in s\n");
                } else if (tmp0 >= number_nodes || tmp1 >= number_nodes) {
                    fprintf(stderr,"Error:vertex does not exist[s]\n");
                } else {
                    v0 = tmp0;
                    v1 = tmp1;

                    pair_edges.clear();
                    set_pair_edges();

                    Graph graph;
                    graph.set_graph(number_nodes, pair_edges);
                    graph.get_shortest_path(v0, v1);
                }
            } else {
                //delete all whitespaces in a line to ignore them
                line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end());

                if (line.front() == 'V') {
                    E_already_valid = false;
                    istringstream input(line.substr(1,line.size()-1));
                    while (!input.eof()) {
                        unsigned num;
                        input >> num;

                        if (!input.fail()) {
                            number_nodes = num;
                        }
                        if (input.eof())
                            break;
                    }
                } else if (line.front() == 'E') {
                    if (E_already_valid) {
                        fprintf(stderr,"Error: already has a valid E\n");
                    } else {
                        edges.clear();
                        istringstream input(line.substr(2, line.size()-1));
                        string s;
                        while (getline(input, s, '<')) {
                            //deal with int
                            unsigned num;
                            input >> num;
                            if (!input.fail()) {
                                edges.push_back(num);
                            }

                            //deal with char
                            char symbol;
                            input >> symbol;

                            //deal with int
                            input >> num;
                            if (!input.fail()) {
                                edges.push_back(num);
                            }

                            //deal with char
                            input >> symbol;
                            //deal with char
                            input >> symbol;
                        }

                        bool edge_Error = false;
                        for (std::vector<unsigned>::iterator it=edges.begin(); it != edges.end(); ++it) {
                            if (*it+1 > number_nodes) {
                                fprintf(stderr,"Error:vertex does not exist[E]\n");
                                edge_Error = true;
                                break;
                            }
                        }
                        if (!edge_Error) {
                            E_already_valid = true;
                        }
                    }
                }
            }
        }
    }

    void set_pair_edges() {
        for (unsigned i=0; i<edges.size(); i=i+2) {
            pair_edges.push_back( make_pair(edges[i],edges[i+1]) );
        }
    }
};

int main() {

    Input input;
    input.get_input();

    return 0;
}

