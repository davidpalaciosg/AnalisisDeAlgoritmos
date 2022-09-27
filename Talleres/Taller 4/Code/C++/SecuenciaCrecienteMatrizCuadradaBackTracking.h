#ifndef _SECUENCIACRECIENTEMATRIZCUADRADABACKTRACKING_H
#define _SECUENCIACRECIENTEMATRIZCUADRADABACKTRACKING_H

#include <iostream>
#include <vector>
using namespace std;

//Busca la mayor longitud de secuencias crecientes en una matriz cuadrada
unsigned int secuenciaCrecienteEnMatrizCuadradaBacktrack(
    vector<vector<unsigned int>>A,
    unsigned int i,
    unsigned int j,
    vector<vector<unsigned int>> &M,
    vector<vector<pair<unsigned int, unsigned int>>> &B
);

//Genera la secuencia creciente de mayor longitud en una matriz cuadrada
vector<unsigned int> secuenciaCrecienteEnMatriz(vector<vector<unsigned int>>A);
#endif