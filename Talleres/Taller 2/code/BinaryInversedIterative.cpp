#include <iostream>
#include <cmath>
using namespace std;

// Convert an integer number into binary list
string DecimalToBinary(int n)
{
    string binary = "";
    int i = 0;
    while (n > 0)
    {
        char c = n % 2 + '0';
        binary += c;
        n = n / 2;
        i++;
    }
    return binary;
}

// Invert a chain given a list begin and end
string InvertChainInt(string S)
{
    if (S.size() == 1)
    {
        string aux = "";
        aux += S[0];
        return aux;
    }
    string result = "";
    for (int i = S.size() - 1; i >= 0; i--)
    {
        result += S[i];
    }
    return result;
}

int BinaryToDecimal(string S)
{
    int decimal = 0;
    int i = 0;
    string aux = InvertChainInt(S);
    for (int i = 0; i < aux.size(); i++)
    {
        int c = aux[i] - '0';
        int p = c * pow(2, aux.size() - i - 1);
        decimal += p;
    }
    return decimal;
}
