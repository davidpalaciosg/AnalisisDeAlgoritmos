#include <iostream>
#include <cmath>
#include <chrono>
#include "BinaryInversedIterative.cpp"
#include "BinaryInversedDyV.cpp"

using namespace std;

void BinaryInversedIterative(int n, int interaction)
{
    string binary = DecimalToBinary(n);
    string inverted = InvertChainInt(binary);
    int decimal = BinaryToDecimal(inverted);
    if (interaction == 9)
    {
        cout << "Binary Inversed Iterative" << endl;
        cout << "Original: " << n << " " << inverted << endl;
        cout << "Inverso: " << decimal << " " << binary << endl;
    }
}

void BinaryInversedDyV(int n, int interaction)
{
    string binary = DecimalToBinaryDyV(n);
    string inverted = InvertChainDyV(binary, 0, binary.size() - 1);
    int decimal = BinaryToDecimalDyV(inverted);
    if (interaction == 9)
    {
        cout << "Binary Inversed DyV" << endl;
        cout << "Original: " << n << " " << inverted << endl;
        cout << "Inverso: " << decimal << " " << binary << endl;
    }
}

double DoExperiment(int n, int fun)
{
    int r = 10;
    double t = 0;
    for (int i = 0; i < r; i++)
    {
        auto start = chrono::steady_clock::now();
        if (fun == 1)
            BinaryInversedIterative(n, i);
        else if (fun == 2)
            BinaryInversedDyV(n, i);
        auto end = chrono::steady_clock::now();
        t += chrono::duration_cast<chrono::nanoseconds>(end - start).count();
    }
    return (t / double(r));
}

int main()
{
    int data[] = {10, 340, 1890, 14870, 354880, 1254690, 78465460, 988641540};
    // int data[] = {10,100,1000,10000,100000,1000000,10000000,100000000};
    int n;
    double interactive, dyv;
    for (int i = 0; i < 8; i++)
    {
        n = data[i];
        interactive = DoExperiment(n, 1);
        dyv = DoExperiment(n, 2);
        cout << n << " " << interactive << " ns " << dyv << " ns" << endl;
    }
    return 0;
}