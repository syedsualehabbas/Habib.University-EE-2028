#include "BigNum.h"
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

//default constructor
BigNum::BigNum(){
    digits.push_back('0');
}

//Copy Constructor, makes deep copy of bigNum.
BigNum::BigNum(const BigNum& bigNum){
    digits=bigNum.digits;
}

//convert string into a format that BigNum class can handle.
BigNum::BigNum(const string& numStr){
    int start = 0;
    while(start<numStr.length()-1 && numStr[start]=='0'){
        start++;
    }
    for(int i=numStr.length()-1; i>=start; i--){
        if(numStr[i]>='0' && numStr[i]<='9'){
            digits.push_back(numStr[i]);
        }
    }
    if(digits.empty()){
        digits.push_back('0');
    }
}
//constructor initializes a BigNum object with the value represented by the integer num.
BigNum::BigNum(const int num){
    if(num==0){
        digits.push_back('0');
        return;
    }
    int temp=num;
    if(temp<0) temp=-temp;
    while(temp>0){
        digits.push_back('0'+temp%10);
        temp=temp/10;
    }
}
//destructor
BigNum::~BigNum(){
    digits.clear();
}


//*************** INPUT OUTPUT OPERATIONS ****************

void BigNum::input(){
    clear();
    string console_input;
    cout<<"Enter a Number: ";
    cin>> console_input;
    int index=0;

    //Leading zeros not needed:-
    while((index<console_input.length()-1)&&console_input[index]=='0'){
        index++;
    }

    //copying the value now:-
    for(int i=console_input.length()-1; i>=index; i--){
        digits.push_back(console_input[i]);
    }
}

void BigNum::print() {
    int size=digits.size();
    for (int i = size - 1; i >= 0; i--) {
        cout << digits[i];
        int digitsLeft = i;
        if (digitsLeft > 0 && digitsLeft % 3 == 0) {
            cout << ',';
        }
    }
    cout << endl;
}


//************* Writing to file ************************
//(for my understangind of input output to file)
// ofstream outFile("numbers.txt");
// outFile << "The number is: ";  // Write string
// outFile << 123;                // Write integer
// outFile << '\n';               // Write newline
// outFile.close();
//******************************************************

void BigNum::inputFromFile(const string& fileName){
    clear();

    ifstream file(fileName);

    if(!file.is_open()){
        cout<<"Error while opening the file."<<endl;
        digits.push_back('0');
        return;
    }
    string file_input;
    file>>file_input;
    file.close();

    //checking if file is empty
    if(file_input.empty()){
        digits.push_back('0');
        return;
    }

    //checking if all are digits:
    bool is_digit=true;
    for(int i=0; i<=file_input.length()-1; i++){
        if('0'>file_input[i] || '9'< file_input[i]){
            is_digit=false;
            digits.push_back('0');
            return;
        }
    }
    //removing leading zeros:
    int index=0;
    while((index<file_input.length()-1)&&file_input[index]=='0'){
        index++;
    }

    //pushing values in vector.
    for(int i=file_input.length()-1; i>=index; i--){
        digits.push_back(file_input[i]);
    }

}

void BigNum::printToFile(const string& fileName){
    ofstream file(fileName);

    if(!file.is_open()){
        cout<<"Error: could not open the file "<<fileName<<endl;
        return;
    }

    for(int i=digits.size()-1; i>=0; i--){
        file<<digits[i];
    }
    file.close();
}

//******** INITIALIZATION / ASSIGNMENT OPERATIONS **********

void BigNum::copy(const BigNum& bigNum){
    digits.clear();
    digits=bigNum.digits;
}

void BigNum::operator=(const BigNum& bigNum){
    if (this==&bigNum) {
        return;
    }
    digits.clear();
    digits=bigNum.digits;
}

void BigNum::zerofy(){
    digits.clear();
    digits.push_back('0');//clears the vector the push the value zero.
}

void BigNum::clear(){
    digits.clear();//clears the whole vector.
}

//************** ARITHMETIC OPERATORS *****************

//------------------------------------------------------------------
//ADDITION:-

void BigNum::increment() {
    int carry = 1;  //We want to add 1.
    int i = 0;      // Start from first digit (as our vector is stored reverse).

    while ((carry) && (i<digits.size())){
        int digit=(digits[i]-'0')+carry;  //gettin gvalue from ascii value.
        digits[i]='0'+(digit%10);      
        carry=digit/10;
        i++;
    }
    // If still carry, add new digit
    if(carry){
        digits.push_back('0'+carry);
    }
}

BigNum BigNum::add(const BigNum& bigNum){
    BigNum result;
    result.clear();

    int carry=0;
    int max_size=max(digits.size(), bigNum.digits.size());
    for(int i=0; (i<max_size)||(carry); i++){
        int sum=carry;
        if(i<digits.size()){
            sum+=(digits[i]-'0');
        }
        if(i<bigNum.digits.size()){
            sum+=(bigNum.digits[i]-'0');
        }
        result.digits.push_back('0'+(sum%10));
        carry=sum/10;
    }
    return result;
}

BigNum BigNum::add(const int num){
    BigNum temp(num);
    return add(temp);//makes num an object then use add funtion.
}

void BigNum::compoundAdd(const BigNum& bigNum){
    int carry=0;
    int max_size=max(digits.size(), bigNum.digits.size());
    for(int i=0; (i<max_size)||carry; i++){
        int sum=carry;
        if(i<digits.size()){
            sum+=digits[i]-'0';
        }
        else digits.push_back('0');
        if(i<bigNum.digits.size()) sum+=(bigNum.digits[i]-'0');
        if(i<digits.size()) digits[i]='0'+(sum%10);  
        else digits.push_back('0'+(sum%10));  
        carry=sum/10;
    }
}
void BigNum::compoundAdd(const int num){
    BigNum integer(num);
    compoundAdd(integer);
}

//-----------------------------------------------------------------
// SUBTRACTION:-

void BigNum::decrement(){
    int borrow=1, i=0;
    if (digits.size()==1 && digits[0]=='0'){
        return; 
    }
    while(borrow && (i<digits.size())){
        int digit=(digits[i]-'0')-borrow;
        if(digit<0){
            digit+=10;
            borrow=1;
        }
        else borrow=0;
    
    digits[i] = '0' + digit;
    i++;
    }
    while(digits.size()>1 && digits[digits.size()-1]== '0'){
        digits.pop_back();
    }
}

BigNum BigNum::subtract(const BigNum& other){
    BigNum result;
    result.clear();
    int borrow=0;
    for(int i=0; i<digits.size(); i++){
        int digit1=digits[i]-'0';
        int digit2=0;
        if(i<other.digits.size()){
            digit2=other.digits[i]-'0';
        }
        int difference=digit1-digit2-borrow;
        if(difference<0){
            difference+=10;
            borrow=1;
        }
        else borrow=0;
        result.digits.push_back('0'+difference);
    }
    while (result.digits.size()>1 && result.digits[result.digits.size()-1]=='0'){
        result.digits.pop_back();
    }
    return result;
}

BigNum BigNum::subtract(const int other){
    BigNum result(other);
    return subtract(result);
}

void BigNum::compoundSubtract(const BigNum& bigNum){
    int borrow=0;
    for(int i=0; i<digits.size(); i++){
        int digit1=digits[i]-'0';
        int digit2=0;
        if (i<bigNum.digits.size()) digit2=bigNum.digits[i]-'0';
        int difference=digit1-digit2-borrow;
        if (difference<0){
            difference+=10;
            borrow=1;
        } 
        else borrow=0;
        digits[i]='0'+difference;
    }
    while(digits.size()>1 && digits[digits.size()-1]=='0'){
        digits.pop_back();
    }
}

void BigNum::compoundSubtract(const int num){
    BigNum temp(num);
    compoundSubtract(temp);
}

//-----------------------------------------------------------------
// MULTIPLICATION AND DIVISION:-

BigNum BigNum::multiply(const BigNum& other){
    BigNum result;
    result.clear();
    int result_size = digits.size()+other.digits.size();
    for(int i=0; i<result_size; i++){
        result.digits.push_back('0');
    }
    for (int i = 0; i < digits.size(); i++) {
        int carry = 0;
        int digit1 = digits[i] - '0';
        
        for (int j=0; j<other.digits.size() || carry; j++){
            int digit2=0;
            if (j<other.digits.size()) digit2=other.digits[j]-'0';
            //position in result
            int position=i+j;
            int currentDigit=result.digits[position]-'0';
            int multipy= digit1*digit2+carry+currentDigit;
            result.digits[position]='0'+(multipy%10);
            carry=multipy/10;
        }
    }
    while (result.digits.size()>1 && result.digits[result.digits.size()-1]=='0'){
        result.digits.pop_back();
    }
    return result;
}

//--------------------------------------------------------------------
// DIVISION:-

BigNum BigNum::div(const BigNum& other) {
    // Check for division by zero
    if (other.digits.size() == 1&& other.digits[0]=='0'){
        cout<<"Invalid operation"<<endl;
        return BigNum(0);
    }
    if (this->lessThan(other)){
        return BigNum(0);
    }
    if (this->equals(other)){
        return BigNum(1);
    }

    BigNum result(0); //store the quotient
    BigNum current(0);
    for (int i=digits.size()-1; i>=0;i--){
        current.digits.insert(current.digits.begin(), digits[i]);
        while(current.digits.size()>1 && current.digits[current.digits.size()-1]=='0'){
            current.digits.pop_back();
        }
        int count=0;
        //Count how many times 'other' fits into 'current'.
        while (!current.lessThan(other)){
            current.compoundSubtract(other);
            count++;
        }
        //Add count to result
        result.digits.insert(result.digits.begin(),'0'+count);
    }
    while(result.digits.size()>1 && result.digits[result.digits.size()-1]=='0'){
        result.digits.pop_back();
    }
    return result;
}

//-------------------------------------------------------------------------------
//MODULUS:-
BigNum BigNum::mod(const BigNum& other) {
    if (other.digits.size()==1 && other.digits[0]=='0'){
        cout<<"Invalid operation"<<endl;
        return BigNum(0);
    }
    if (this->lessThan(other)) return *this;
    if (this->equals(other)){
        return BigNum(0);
    }
    BigNum current(0);
    for (int i=digits.size()-1; i>=0; i--){
        current.digits.insert(current.digits.begin(),digits[i]);
        while (current.digits.size()>1 && current.digits[current.digits.size()-1]=='0'){
            current.digits.pop_back();
        }
        // Subtract 'other' as many time possible.
        while (!current.lessThan(other)){
            current.compoundSubtract(other);
        }
    }
    return current;
}

//---------------------------------------------------------------------------------
//****************************** BOOL OPERATORS ***********************************

bool BigNum::equals(const BigNum& other) {
    //if sizes are different
    if (digits.size() != other.digits.size()) return false;
    //Compare digit by digit
    for (int i = 0; i < digits.size(); i++) {
        if (digits[i] != other.digits[i]) {
            return false; 
        }
    }
    return true;
}

bool BigNum::notEquals(const BigNum& other) {
    return !equals(other);
}

bool BigNum::lessThan(const BigNum& other) {
    if (digits.size() < other.digits.size()) return true;
    if (digits.size() > other.digits.size()) return false;
    // if they have same number of digits; compare each of them.
    //going from most significant.
    for (int i=digits.size()-1; i>=0; i--){
        if (digits[i]<other.digits[i]) return true; 
        if (digits[i]>other.digits[i]) return false;
        // If equal, then continue.
    }
    return false;
}

bool BigNum::greaterThan(const BigNum& other) {
    if (digits.size()>other.digits.size()) {
        return true;
    }
    if (digits.size()<other.digits.size()) {
        return false;
    }
    for (int i=digits.size()-1; i>=0; i--) {
        if (digits[i]>other.digits[i]) return true;
        if (digits[i]<other.digits[i]) return false; 
        // If equal, then continue
    }
    return false;
}