#include <iostream>
#include <string>
using namespace std;

int main() {
  string message = "happy birthday rowan";
  string colours[5] = {"\33[103m", "\33[107m", "\33[45;97m", "\33[40;97m", "\33[0m"};
  for(int colour = 0; colour < 4; colour++){
  	for(int y = 0; y < 2; y++){
  		cout << colours[colour]<< message<< colours [4];
  		
  	}
  }
}
