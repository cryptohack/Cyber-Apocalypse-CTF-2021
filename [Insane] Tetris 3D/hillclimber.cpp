#include <bits/stdc++.h>
#include <random>
using namespace std;

inline int idx(char x) { return x - 'A'; }
inline int dec(string x) {
    return 26*26*26*idx(x[0]) + 26*26*idx(x[1]) + 26*idx(x[2]) + idx(x[3]);
}

double qgrams[26*26*26*26];
void fillqgram(string x) {
    for (int i = 0; i < 26*26*26*26; i++)
        qgrams[i] = -1;
    for (int i = 0; i < x.length() - 3; i++) {
        qgrams[dec(x.substr(i, 4))]++;
    }
    for (int i = 0; i < 26*26*26*26; i++) {
        if (qgrams[i] == -1) qgrams[i] = -24;
        else qgrams[i] = log10((qgrams[i] + 1) / (x.length() - 3));
    }
}

double score(string x) {
    double res = 0;
    for (int i = 0; i < x.length() - 3; i++) {
        res += qgrams[dec(x.substr(i, 4))];
    }
    return res / (x.length() - 3);
}

string decrypt(string x, vector<string> keys) {
    string res = x;
    for (int i = 0; i < x.length(); i++) {
        res[i] = keys[i%keys.size()][x[i] - 'A'];
    }
    return res;
}

string shuffled() {
    string x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    random_shuffle(x.begin(), x.end());
    return x;
}

pair<string, vector<string>> hillclimb(string c, int K) {
    vector<string> keys(K);
    for (int i = 0; i < K; i++) keys[i] = shuffled();
    int outer = 0;
    double best = -numeric_limits<double>::infinity();
    vector<string> bestk = keys;

    while (outer < 5000 * K * K / c.length()) {
        cout << "iterate" << endl;
        for (int i = 0; i < K; i++) {
            keys[i] = shuffled();
            double target = score(decrypt(c, keys));
            int fails = 0;
            while (fails < 1000) {
                int a = rand() % 26;
                int b = rand() % 26;
                swap(keys[i][a], keys[i][b]);
                double ts = score(decrypt(c, keys));
                if (ts > target) {
                    target = ts;
                    fails = 0;
                } else {
                    swap(keys[i][a], keys[i][b]);
                    fails++;
                }
            }
            if (target > best) {
                best = target;
                bestk = keys;
                outer = 0;
                cout << "improved " << best << endl;
            } else {
                outer++;
            }
        }
    }

    return {decrypt(c, bestk), bestk};
}

int main(int argc, char** argv) {
    if (argc < 4) {
        cerr << "Usage: hillclimber quadgram_reference.txt encrypted.txt keysize" << endl;
        return 1;
    }
    {
        ifstream qf(argv[1]);
        stringstream qfref;
        qfref << qf.rdbuf();
        fillqgram(qfref.str());
    }
    int K = atoi(argv[3]);
    ifstream cf(argv[2]);
    stringstream cs;
    cs << cf.rdbuf();
    auto res = hillclimb(cs.str(), K);
    cout << res.first << endl;
    for (auto k : res.second) cout << k << endl;
}
