#include<stdio.h>
#include<stdlib.h>
struct node{
int data;
struct node *next;
};

struct node* create(int n){
    struct node* HEAD = NULL;
    struct node* newNode = NULL;
    struct node* ptr = NULL;
     printf("Creating the linkedList\n");
    for(int i=0;i<n;i++){
    struct node* newNode = (struct node*) malloc(sizeof(struct node));
    printf("enter the Element to the likedList\n");
    scanf("%d",&(newNode->data));
    newNode->next = NULL;
             if(HEAD == NULL){
                  HEAD = newNode;
              }else{
                    ptr = HEAD;
                    while(ptr->next != NULL){
                    ptr = ptr->next;
                     }
                    ptr->next = newNode;
                }
    }
    return HEAD;
}
//in linkedList just create a list and insert where you want ,
// end ---> while
// use double pinter concept where to memory pointed bt two pointers,
struct node* InsertAtFirst(struct node* HEAD,int data){
    struct node* Newnode = (struct node*)malloc(sizeof(struct node));
    Newnode->data = data;
    Newnode->next = HEAD;
    return Newnode;
}

struct node* InsertAtLast(struct node* HEAD,int data){
    struct node* Newnode = (struct node*)malloc(sizeof(struct node));
    Newnode->data = data;
    Newnode->next = NULL;
    struct node* curr=HEAD;
    while(curr->next != NULL){
        curr = curr->next;
    }
    curr->next = Newnode;
    return HEAD;

}

int main(){
    //simple eexample--------------------->
    // struct node *head,*second;
    // head = (struct node *)malloc(sizeof(struct node));
    // second = (struct node *)malloc(sizeof(struct node));
    // head->data = 1;
    // head->next = second;
    // second->data = 2;
    // second->next = NULL;
    int n;
    struct node *head;
    printf("Enter the NUmber of LinkedList\n");
    scanf("%d",&n);
    head = create(n);
    //before insertion
    struct node *curr = head;
   while(curr != NULL){
    printf("Before Insert front-->%d\n", curr->data);
    curr = curr->next;
   }
   head = InsertAtLast(head,6);
    //Traversing the linked list
    curr = head; 
   while(curr != NULL){
    printf("After Inserting at Back--->%d\n", curr->data);
    curr = curr->next;
   } 
    return 0;
}

//use do while for circular linkedlist
//in linkedlist you can't leave the head and move the head so you assign the another pinter which moves


