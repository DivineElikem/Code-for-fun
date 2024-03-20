#include <iostream>
using namespace std;

int main(){
    const int secret = 129;
    int guess;
    cout<<"Welcome to my guessing game \n"
        <<"I have a secret number\n"
        <<"Guess the number\n"
        <<"What's your guess?\n";
    
    while(guess != secret){
    cin>>guess;
    if(guess < secret)
        cout<<"Guess is less than the secret number"<<endl;
    else if(guess > secret)
        cout<<"Guess is greater than the secret number"<<endl;
    else
        cout<<"You nailed it buddy!!!";
    
    }
    return 0;
}
