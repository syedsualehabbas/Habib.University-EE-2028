#include<iostream>
using namespace std;
class square
{
    private:
        float length;
    public:
        void setlength(float l){
            length=l;
        }
        float calculate_area(){
            float area;
            area = length * length;
            return area;
        }
        void showdata(float area){
            cout<<"Area of square is "<<area<<endl;
        }
};
int main(){
    square length1, length2;
    length1.setlength(12.4);
    length2.setlength(10);
    float area1 = length1.calculate_area();
    float area2 = length2.calculate_area();
    length1.showdata(area1);
    length2.showdata(area2);

}