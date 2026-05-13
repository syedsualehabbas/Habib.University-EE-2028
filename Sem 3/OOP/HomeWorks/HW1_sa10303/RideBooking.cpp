// SYED SUALEH ABBAS
// sa10303
// Section: L-1

#include <iostream>
#include <string>
using namespace std;

// Constants
const int MAX_RIDES = 100;
const int MAX_DRIVERS = 50;
const int START_RIDE_ID = 100001;

// Struct Definition
struct Ride {
    string riderName;
    int rideID;
    string driverName;
    string pickupLocation;
    string dropoffLocation;
    double fare;
    string status; // "Ongoing", "Completed", "Cancelled"
};

// Global Variables
Ride rideDetails[MAX_RIDES];
int rideCount = 0; // Keeps track of total rides
string Drivers[MAX_DRIVERS];
int driverCount = 0; // Keeps track of total drivers
string Riders[MAX_DRIVERS];
int riderCount = 0; // Keeps track of total riders

// ================= Function Definitions =================

int IsAvailable(string driverName, Ride rides[]){
    // TODO: Searches through the array 
    //       Checks if the given driverName has an Ongoing ride
    //       If the given driverName has an Ongoing ride returns 1, otherwise returns 0
    for(int i=0; i<rideCount; i++){  
        if(rides[i].driverName==driverName && rides[i].status=="Ongoing") return 1; 
    }
    return 0; 
}

int GetFare(int distance){
    //TODO: Calculate and return the fare based on the given scheme
    //      Distance < 2KM : 50 + (50 * distance)
    //      2KM < Distance < 5KM : 150 + (80 * (distance - 2)) 
    //      Distance > 5KM : 390 + (100 * (distance - 5))
    int fare;
    if(distance<2) fare=50+(50*distance);
    else if (distance>=2 && distance <=5) fare=150+(80*(distance-2)); 
    else if (distance>5) fare=390+(100*(distance-5));
    return fare;
}
Ride BookRide(string name) {
    // TODO: Prompt user for pickup, drop-off, distance
    //       Displays all available drivers. Hint use the IsAvailable function and the Drivers array.
    //       Prompts the user to select a driver
    //       Calculates the fare by calling the GetFare function.
    //       Set ride status to "Ongoing" and generate Ride ID
    //       If there is no driver avaliable then output an error message, generate a Ride ID, set ride status to "Cancelled" and driverName to ""
    string pickup, dropoff, selected_driver, distance_string;
    int distance, fare;
    while (true) {
        cout<<"Enter your pickup location: ";
        getline(cin, pickup);
        cout<<"Enter your drop-off location: ";
        getline(cin, dropoff);
        if (pickup == dropoff) {
            cout<<"Pickup and drop-off cannot be the same. Please enter again.\n";
        } 
        else {
            break;
        }
    }
    while (true){ //runs until returns/ breaks
        cout <<"Enter distance: ";
        getline(cin, distance_string);
        try {
            distance = stoi(distance_string);
            if (distance>0){ //if distance is in negative, it raises an error.
                break;
            } 
            else{
                cout << "Distance must be greater than zero. Please enter again.\n";
            }
        } 
        catch (...){
            cout<<"Invalid input. Please enter a valid number."<<endl;
        }
    }
    fare=GetFare(distance);
    bool hasAvailableDriver=false;
    cout<<"Checking for available drivers...\n";
    for (int i=0; i<driverCount; i++){
        if (IsAvailable(Drivers[i], rideDetails)==0){ 
            if (!hasAvailableDriver){
                cout<<"Available drivers: ";
            }
            cout<<Drivers[i]<<" ";
            hasAvailableDriver=true;
        }
    }
    Ride newRide;
    newRide.riderName=name;
    newRide.dropoffLocation=dropoff;
    newRide.pickupLocation=pickup;
    newRide.fare=fare;
    newRide.rideID=START_RIDE_ID+rideCount;

    if (hasAvailableDriver){
        cout<<endl<<"Please select your driver: ";
        while(true) {
            getline(cin,selected_driver);
            bool validDriver=false;
            for(int i=0; i<driverCount; i++) {
                if(Drivers[i]==selected_driver && IsAvailable(Drivers[i],rideDetails)==0){
                    validDriver=true;
                    break;
                }
            }
            if(validDriver){
                break;
            } 
            else{
                cout<<"Invalid driver selection. Please select from available drivers: ";
            }
        }
        newRide.driverName=selected_driver;
        newRide.status="Ongoing";
    } else {
        cout<<"No drivers available. Ride cancelled."<<endl;
        newRide.driverName="";
        newRide.status="Cancelled";
    }

    rideDetails[rideCount]=newRide;
    rideCount+=1;

    return newRide;
}
void ViewRides(string name, Ride rides[], string status = ""){
    // TODO: Loop through the array and print rides where name matches riderName or driverName
    //       Displays all rides for that name regardless of status if status is ""
    //       Displays rides for that name and status if a status value was passed
    bool found=false; 

    for (int i=0; i<rideCount; i++) {  
        if (status=="") {
            if (rides[i].riderName==name || rides[i].driverName==name){
                cout<<"Ride ID: "<<rides[i].rideID<< ", Status: "<<rides[i].status<<", Fare: "<<rides[i].fare<<endl;
                found=true;
            }
        } 
        else{
            if ((rides[i].riderName==name || rides[i].driverName==name) && rides[i].status == status) {
                cout <<"Ride ID: "<<rides[i].rideID<<", Status: "<< rides[i].status<<", Fare: "<< rides[i].fare<<endl;
                found=true;
            }
        }
    }
    if (!found){
        cout<<"No rides available."<<endl;
    }
}
int ChangeStatus(string name, Ride rides[], int count) {
    // TODO: Show ongoing rides for the name. Hint: Call ViewRides and use the third parameter 
    //       Ask user to enter the Ride ID to update
    //       Return the Ride ID so status can be updated in main
    cout<<"Ongoing rides for "<<name<<":"<<endl;
    ViewRides(name,rides,"Ongoing");
    int ongoingCount = 0;
    for (int i = 0; i < count; i++) {
        if ((rides[i].riderName == name || rides[i].driverName == name)&& rides[i].status=="Ongoing"){
            ongoingCount++;
        }
    }
    if (ongoingCount== 0){ //if there is no ride/ or ongoing ride.
        cout<<"No ongoing rides available."<<endl;
        return -1;
    }
    string rideStr;
    int rideID;
    while (true){
        cout<<"Enter Ride ID to update: "; //out of so many rides, user have to enter the ride id in order to change status of ride.
        getline(cin,rideStr);
        try{
            rideID =stoi(rideStr);
        } 
        catch (...){ //if there is something which may not be converted to an integer.
            cout << "Invalid input. Please enter a valid Ride ID.\n"; //if the user enters wrong id
            continue;
        }
        bool found=false;
        for (int i=0; i<count; i++) {
            if (rides[i].rideID==rideID && (rides[i].riderName== name || rides[i].driverName==name) && rides[i].status=="Ongoing"){
                return rideID; 
            }
        }

        cout<<"Invalid Ride ID or no ongoing rides with this ID.\n";
    }
}
double CalculateTotal(string driverName, Ride rides[]) {
    // TODO: Add up fares of rides where driverName matches and status is "Completed"
    double total=0.0;
    for(int i=0;i<rideCount; i++){ //calculate total fare completed rides for a driver.
        if(rides[i].driverName==driverName && rides[i].status=="Completed"){
            total+=rides[i].fare;
        }
    }
    return total;
}

// ================= Main Function =================
int main() {
    // TODO:
    // - Display main menu
    // - Ask the user if they are a Rider (1) or Driver (2)
    // - Prompt for name
    // - If the user is a Driver and the name is not in the Drivers list add it to the list
    // - Based on role, display the appropriate menu
    // - Use the provided functions to implement menu options
    // - Ensure ride count does not exceed MAX_RIDES
    // - Validate menu inputs

    int RD, input1,input2;
    string name;
    while(true){
        string input;
        int input1;
        cout<<"***********************************************************"<<endl;
        cout<<"Welcome to the Ride Booking Simulation program! \nAre you a Rider (1) or a Driver (2)? \nEnter your role: ";
        while(true) {
            cin >> input;
            if(input == "1") {
                input1 = 1;
                break;
            }   
            else if(input == "2") {
                input1 = 2;
                break;
            }   
            else {
                cout<<"Please Enter a Valid Input (1 or 2): ";
            }
        }
        cin.ignore();
        cout<<"Please enter your name: ";
        getline(cin, name);
        int a=0;
        // logged in as rider:- 
        if(input1==1){
            for(int i=0; i<riderCount; i++){ 
                if(name==Riders[i]) a=1;
            }
            if (a==0 && riderCount < MAX_DRIVERS){
                Riders[riderCount]=name; 
                riderCount+=1;
            } else if (a==0 && riderCount >= MAX_DRIVERS) {
                cout << "Maximum rider limit reached." << endl;
            }
            string input;
            int input2;
            cout << "Welcome "<<name<<". Please Select an Option: \n1. Book a Ride. \n2. View My Rides. \n3. Cancel a Ride. \n4. Return to Main Menu. \nOption: ";
            while(true) {    //checks if the input is correct and asks until correct input is given.
                cin>>input;
                if(input == "1") {
                    input2 = 1;
                    break;
                } else if(input == "2") {
                    input2 = 2;
                    break;
                } else if(input == "3") {
                    input2 = 3;
                    break;
                } else if(input == "4") {
                    input2 = 4;
                    break;
                } else {
                    cout<<"Please Enter a Valid Option (1-4): ";
                }
            }
            cin.ignore(); 
            if(input2==1){  //condional statemnts for execution upon users input.
                if(rideCount >= MAX_RIDES) {
                    cout << "Maximum ride limit reached. Cannot book more rides." << endl;
                } else {
                    BookRide(name);
                }
            }
            else if(input2==2) {
                ViewRides(name, rideDetails);
            }
            else if(input2==3){
                int rideID = ChangeStatus(name, rideDetails, rideCount);
                if(rideID!=-1){
                    for(int i=0;i<rideCount;i++){
                        if(rideDetails[i].rideID==rideID){
                            rideDetails[i].status="Cancelled";
                            cout<<"Ride "<<rideID<<" has been Cancelled."<<endl;
                        }
                    }
                }
            }
            else if(input2==4) {
                continue; 
            }
        }
        // logged in as driver:-
        if (input1==2){
            while(true){
                if (name.length() < 3 || name.length()>30){
                    cout << "Driver name must be between 3 and 30 characters."<< endl;
                    cout<<"Please enter your name: ";
                    getline(cin, name);
                }
                else break;
            }
            for(int i=0; i<driverCount; i++){ 
                if(name==Drivers[i]) a=1;
            }
            if (a==0 && driverCount < MAX_DRIVERS){
                Drivers[driverCount]=name; 
                driverCount+=1;
            } else if (a==0 && driverCount >= MAX_DRIVERS) {
                cout << "Maximum driver limit reached." << endl;
            }
            string input;
            cout<<"Welcome "<<name<<". Please Select an Option: \n1. View Assigned Rides. \n2. Mark Ride as Completed. \n3. View All Rides. \n4. Calculate Total Fare. \n5. Return to Main Menu.\nOption: ";
            while(true) { //checks if the input is correct.
                cin >> input;
                if(input=="1") {
                    input2 =1;
                    break;
                } else if(input=="2") {
                    input2=2;
                    break;
                } else if(input== "3") {
                    input2=3;
                    break;
                } else if(input=="4") {
                    input2=4;
                    break;
                } else if(input=="5") {
                    input2=5;
                    break;
                } else {
                    cout<<"Please Enter a Valid Option (1-5): ";
                }
            }
            cin.ignore(); 
            if(input2==1){
                ViewRides(name, rideDetails, "Ongoing");
            }
            else if(input2==2){
                int rideID = ChangeStatus(name, rideDetails, rideCount);
                if(rideID!=-1){
                    for(int i=0;i<rideCount;i++){
                        if(rideDetails[i].rideID==rideID){
                            rideDetails[i].status="Completed";
                            cout<<"Ride "<<rideID<<" has been marked as Completed."<<endl;
                        }
                    }
                }
            }
            else if(input2==3){
                ViewRides(name, rideDetails);
            }
            else if(input2==4){
                cout<<"Total fare earned: "<<CalculateTotal(name, rideDetails)<<endl;
            }
            else if(input2==5){
                continue; 
            }
        }
    }
}