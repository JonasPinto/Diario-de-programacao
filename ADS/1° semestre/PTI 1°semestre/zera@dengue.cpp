#include <stdio.h> 
#include <stdlib.h> 
  
struct No { 
    int chave; 
    struct No* prox; 
}; 
  
struct Fila { 
    struct No *inicio, *fim; 
}; 
  
struct No* newNode(int k) 
{ 
    struct No* temp = (struct No*)malloc(sizeof(struct No)); 
    temp->chave = k; 
    temp->prox = NULL; 
    return temp; 
} 
  
struct Fila* inicia_Fila() 
{ 
    struct Fila* q = (struct Fila*)malloc(sizeof(struct Fila)); 
    q->inicio = q->fim = NULL; 
    return q; 
} 
  
void insere_fila(struct Fila* q, int k) 
{ 
    
    struct No* temp = newNode(k); 
  
    if (q->fim == NULL) { 
        q->inicio = q->fim = temp; 
        return; 
    } 
  
    q->fim->prox = temp; 
    q->fim = temp; 
} 
  
void remove_fila(struct Fila* q) 
{ 
    // If Fila is empty, return NULL. 
    if (q->inicio == NULL) 
        return; 
  
    
    struct No* temp = q->inicio; 
  
    q->inicio = q->inicio->prox; 
  

    if (q->inicio == NULL) 
        q->fim = NULL; 
  
    free(temp); 
} 
  
bool search(struct Node* inicio, int x) 
{ 
    struct Node* atual = inicio;  
    while (atual != NULL) 
    { 
        if (atual->chave== x) 
            return true; 
        atual= atual->prox; 
    } 
    return false; 
}


int main() 
{ 
    struct Fila* q = inicia_Fila(); 
    insere_fila(q, 10); 
    insere_fila(q, 20); 
    remove_fila(q); 
    remove_fila(q); 
    insere_fila(q, 30); 
    insere_fila(q, 40); 
    insere_fila(q, 50); 
    remove_fila(q); 
    printf("Fila Inicio : %d \n", q->inicio->chave); 
    printf("Fila Fim : %d", q->fim->chave); 
    return 0; 
}
