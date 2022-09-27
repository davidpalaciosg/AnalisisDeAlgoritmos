/*
    Taller 4 - Análisis de Algoritmos
    Profesor: Leonardo Flórez Valencia
    Autores:
    - David Enrique Palacios García
    - Karen Sofía Coral Godoy

    Manual de uso en terminal:
    1. Compilar y encadenar:
        g++ -o main *.cpp
    2. Ejecutar:
        ./main <n>
        - <n> es el tamaño de la matriz cuadrada
*/

#include "SecuenciaCrecienteMatrizCuadradaBackTracking.h"
#include <time.h>
vector<vector<unsigned int>> crearMatrizAleatoria(unsigned int n)
{
    vector<vector<unsigned int>> A(n, vector<unsigned int>(n));
    int v = 1;
    //Crear la matriz con valores de 1 a n*n
    for (unsigned int i = 0; i < n; i++)
    {
        for (unsigned int j = 0; j < n; j++)
        {
            A[i][j] = v;
            v++;
        }
    }
    //Mezclar la matriz
    for (unsigned int i = 0; i < n; i++)
    {
        for (unsigned int j = 0; j < n; j++)
        {
            unsigned int i2 = rand() % n;
            unsigned int j2 = rand() % n;
            unsigned int aux = A[i][j];
            A[i][j] = A[i2][j2];
            A[i2][j2] = aux;
        }
    }

    return A;
}

void printMatriz(vector<vector<unsigned int>> A)
{
    cout<<"MATRIZ A: "<<endl;
    for (unsigned int i = 0; i < A.size(); i++)
    {
        for (unsigned int j = 0; j < A.size(); j++)
        {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}

int main(int argc, char const *argv[])
{
    if (argc != 2)
    {
        cout << "Error: debe ingresar el tamaño de la matriz cuadrada" << endl;
        return -1;
    }

    unsigned int n = atoi(argv[1]);
    srand(time(NULL));
    vector<vector<unsigned int>> A = crearMatrizAleatoria(n);
    printMatriz(A);

    cout<<"Secuencia creciente de mayor longitud: "<<endl;
    vector<unsigned int> secuencia = secuenciaCrecienteEnMatriz(A);
    for (unsigned int i = 0; i < secuencia.size(); i++)
    {
        cout << secuencia[i] << " ";
    }
    cout << endl;
    return 0;
}