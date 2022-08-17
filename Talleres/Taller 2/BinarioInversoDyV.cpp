#include <iostream>
#include <cmath>
using namespace std;

//Convert an integer number into binary list
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

//Invert a chain given a list begin and end
string InvertChain(string S, int l, int r)
{
    if(l==r)
    {
        string aux = "";
        aux+=S[l];
        return aux;
    }

    int q = (l+r)/2;
    string left = InvertChain(S,l,q);
    string right = InvertChain(S,q+1,r);
    string result = "";

    for(int i=0;i<right.size();i++)
    {
        result+=right[i];
    }
    for(int i=0;i<left.size();i++)
    {
        result+=left[i];
    }
    return result;
}

int BinaryToDecimal(string S)
{
    int decimal = 0;
    int i=0;
    string aux = InvertChain(S,0,S.size()-1);
    for(int i=0;i<aux.size();i++)
    {
        int c = aux[i]-'0';
        int p = c * pow(2,aux.size()-i-1);
        decimal+=p;
    }
    return decimal;
}

int main()
{
    int n=345;
    cout<<"DIVIDE AND CONQUER"<<endl;
    cout<<"Decimal: "<<n<<endl;
    string binary = DecimalToBinary(n);
    cout << "Binary: " << binary << endl;
    string inverted = InvertChain(binary,0,binary.size()-1);
    cout << "Inverted: " << inverted << endl;
    int decimal = BinaryToDecimal(inverted);
    cout << "Decimal: " << decimal << endl;
    return 0;
}