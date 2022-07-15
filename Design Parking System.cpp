class ParkingSystem {
private:
    int big{};
    int medium{};
    int small{};
    public:
    
    ParkingSystem(int big, int medium, int small):big(big),medium(medium),small(small) {
        
    }
    
    bool addCar(int carType) {
        switch(carType){
            case 1:
                if(big==0)
                    return false;
                    big--;
                return true;
            case 2:
                if(medium==0)
                    return false;
                medium--;
                return true;
            case 3:
                if(small==0)
                    return false;
                small--;
                return true;
        }
        return false;
    }
};
