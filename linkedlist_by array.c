#include <stdio.h>
#include <stdlib.h>
#define MAX_LIST_SIZE 100 // 리스트 최대 크기

typedef int element; // 항목 정의
typedef struct{
    element array[MAX_LIST_SIZE];
    int size; // 리스트에 저장된 항목의 개수
} ArrayListType;

void error(char *message){ // 오류 처리 함수
    fprintf(stderr,"%s\n", message);
    exit(1);
}

void init(ArrayListType *a){ // 리스트 초기화 함수
    a->size = 0;
}

int is_empty(ArrayListType *a){
    return a->size == 0;
}

int is_full(ArrayListType *a){
    return a->size == MAX_LIST_SIZE;
}

element get_entry(ArrayListType *a, int pos){
    if(pos<0 || pos >= a->size){
        error("위치 오류\n");
    }
    return a->array[pos];
}

void print_list(ArrayListType *a){
    int i;
    for(i=0; i<a->size; i++){
        printf("%d->", a->array[i]);
    }
    printf("\n");
}

void insert_last(ArrayListType *a, element item){
    if(a->size >= MAX_LIST_SIZE){
        error("리스트 overflow\n");
    }
    a->array[a->size++] = item;
}

void insert(ArrayListType *a, int pos, element item){
    if(!is_full(a) && (pos >= 0) && (pos <= a->size)){
        for(int i = (a->size - 1); i >= pos; i--){
            a->array[i+1] = a->array[i];
        }
        a->array[pos] = item;
        a->size++;
    }
}

element delete(ArrayListType *a, int pos){
    element item;

    if(pos<0 || pos>=a->size){
        error("위치 오류");
    }
    item = a->array[pos];

    for(int i= pos; i<(a->size -1); i++){
        a->array[i] = a->array[i+1];
    }
    a->size--;
    return item;
}


int main(){

    ArrayListType list;

    init(&list);
    insert(&list, 0, 10); print_list(&list);
    insert(&list, 0, 20); print_list(&list);
    insert(&list, 0, 30); print_list(&list);
    insert_last(&list, 40); print_list(&list);
    delete(&list,0); print_list(&list);

    return 0;
}

// get_entry -> O(1), insert or delete -> O(n) 최악임. insert_last -> O(1)
// 따라서 동적으로 크기 변할 수 있고 삭제/삽입 시 데이터 이동 필요 없는 포인터 활용 연결 리스트를 구현 및 사용함
