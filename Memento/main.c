#include <stdio.h>
#include <stdlib.h>

typedef struct Originator{
  int valorAtual;
}originator;

typedef struct Memento{
  int valorAtual;
  int version;
}memento;

typedef struct caretaker{
  memento *mementos[2000];
}caretaker;

void addMemento(originator *o, caretaker *c){
  static int version = 0;
  memento *m;
  m = malloc(sizeof(memento));
  
  m->valorAtual = o->valorAtual;
  m->version = version;
  c->mementos[version] = m;
  version++;
  return;
}

int main(void){
  int versao; //numero de mementos;
  int choice;
  originator *o;
  o = malloc(sizeof(originator));
  o->valorAtual = 0;
  caretaker *c;
  c = malloc(sizeof(caretaker));
  printf("Implementação da Memento Pattern em C");
  while(1){
    printf("\n\n");
    printf("Digite 1 para alterar o valorAtual\n");
    printf("Digite 2 para imprimir o valorAtual\n");
    printf("Digite 3 para recuperar um valor antigo\n");
    printf("Digite 4 para sair do programa\n");
    printf("Digite a sua escolha: ");
    scanf("%d", &choice);
    switch(choice){
      case 1:
          if(o->valorAtual != 0){
            addMemento(o, c);
          }
          printf("Digite o novo valor: ");
          scanf("%d", &o->valorAtual);
          break;
      case 2:
          printf("O valor atual é: %d\n", o->valorAtual);
          break;
      case 3:
          if(o->valorAtual != 0){
            printf("Digite a versão que deseja restaurar: ");
            scanf("%d", &versao);
            addMemento(o, c);
            o->valorAtual = c->mementos[versao]->valorAtual;
          }else{
            printf("Não existe nenhuma versão ainda");
          }
          break;
      case 4:
          exit(1);
          break;
      default:
          printf("Digite uma escolha valida!\n");
          break;

    }
  }

  return 0;
}
