#include <iostream>
#include <string>

//methods--------------------------------------------------------------------
int calc(int a,int b){
  int c = a+b;
  return c;
}
void tru(){
  int col = 15;
  int row = 20;
  for(int i = 0; i < row; i++){// nested for loop
    for(int j = 0; j < col; j++){
      std::cout << "*";
      
    }
    std::cout << std::endl;
  }
}
//main------------------------------------------------------------------------
int main() {
  int c = 1234, d = 3124;
  std::cout << "Hello World!" << std::endl;
  std::cout << "C: " << c << " D: " << d << std::endl;
  std::cout << c + d << std::endl;
  
  if(d>c){
    std::cout << d <<" (D) is the larger number" << std::endl;
  }
  else{
    std::cout << c << " (C) is the larger number" << std::endl;
  }
  std::cout << calc(c,d) << std::endl;
  tru();
}