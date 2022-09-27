/*
    Taller 4 - Análisis de Algoritmos
    Profesor: Leonardo Flórez Valencia
    Autores:
    - David Enrique Palacios García
    - Karen Sofía Coral Godoy
*/
#include "SecuenciaCrecienteMatrizCuadradaBackTracking.h"

unsigned int secuenciaCrecienteEnMatrizCuadradaBacktrack(
    vector<vector<unsigned int>>A,
    unsigned int i,
    unsigned int j,
    vector<vector<unsigned int>> &M,
    vector<vector<pair<unsigned int, unsigned int>>> &B
    )
{
    if (i<0 || j<0 || i>=A.size() || j>=A.size())
        return 0;

    if (M[i][j] != 0)
        return M[i][j];
    
    unsigned int q = 1;
    unsigned int sup, inf, izq, der;

    //Fila superior
    if(i>0)
    {
        if(A[i][j]+1 == A[i-1][j])
        {
            sup = 1 + secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i-1, j, M, B);
            B[i][j] = make_pair(i-1, j);
        } 
    }

    //Fila inferior
    if(i<A.size()-1)
    {
        if(A[i][j]+1 == A[i+1][j])
        {
            inf = 1 + secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i+1, j, M, B);
            B[i][j] = make_pair(i+1, j);
        } 
    }

    //Columna izquierda
    if (j>0)
    {
        if(A[i][j]+1 == A[i][j-1])
        {
            izq = 1 + secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i, j-1, M, B);
            B[i][j] = make_pair(i, j-1);
        } 
    }

    //Columna derecha
    if (j<A.size()-1)
    {
        if(A[i][j]+1 == A[i][j+1])
        {
            der = 1 + secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i, j+1, M, B);
            B[i][j] = make_pair(i, j+1);
        } 
    }
    q = max(q, max(sup, max(inf, max(izq, der))));
    M[i][j] = q;
    return M[i][j];
}

vector<unsigned int> secuenciaCrecienteEnMatriz(vector<vector<unsigned int>>A)
{
    //Crear tabla de memoización y tabla de backtracking
    vector<vector<unsigned int>> M(A.size(), vector<unsigned int>(A[0].size(), 0));
    vector<vector<pair<unsigned int, unsigned int>>> B(A.size(), vector<pair<unsigned int, unsigned int>>(A[0].size(), make_pair(0,0)));
    unsigned int q = 1;

    //Casos base
    for(unsigned int i=0; i<A.size(); i++)
    {
        for(unsigned int j=0; j<A.size(); j++)
        {
            B[i][j] = make_pair(i, j);
        }
    }

    pair<unsigned int, unsigned int> pos_actual = make_pair(0,0);
    for (unsigned int i=0; i<A.size(); i++)
    {
        for(unsigned int j=0; j<A.size(); j++)
        {
            q = max(q, secuenciaCrecienteEnMatrizCuadradaBacktrack(A, i, j, M, B));
            //Obtener la posición de la secuencia más larga
            if (q == M[i][j])
                pos_actual = make_pair(i, j);
        }
    }

    //Backtracking para obtener la secuencia
    vector<unsigned int> resultado;
    //Mientras no se llegue a la posición inicial
    while (pos_actual!=B[pos_actual.first][pos_actual.second])
    {
        resultado.push_back(A[pos_actual.first][pos_actual.second]);
        pos_actual = B[pos_actual.first][pos_actual.second];
    }
    //Agregar la posición inicial
    resultado.push_back(A[pos_actual.first][pos_actual.second]);

    return resultado;
}
