from abc import ABC, abstractmethod;
from datetime import datetime;

class User(ABC) :
    def __init__(self, name, email) -> None:
        self.name = name;
        self.email = email;
        # Todo : Set Id dynamically;
        self.__id = 0;
        self.wallet = 0;

    @abstractmethod
    def display_profile(self) :
        raise NotImplementedError;



class Rider(User) :
    def __init__(self, name, email, location) -> None:
        self.current_ride = None;
        self.wallet = 0;
        self.location = location;
        super().__init__(name, email);

    def display_profile(self):
        print(f'Rider with name {self.name} and email is {self.email}');
    
    def recharge(self, amount) :
        if amount > 0 :
            self.wallet += amount;
        else :
            print('Invalid Amount');

    def ride_request(self, location, destination) :
        if not self.current_ride :
            # Todo : Set Ride request functionality;
            # Todo : Set current ride via ride match;
            ride_request = RideRequest(self, destination);
            rider_matcher = RideMatch()
            self.current_ride = rider_matcher().find_driver(ride_request);

    def update_location (self, current) :
        self.location = current;




class Driver(User) :
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid);
        self.current_location = current_location;
        self.wallet = 0;
    
    def display_profile(self):
        print(f'Driver with name {self.name} and email is {self.email}');

    def accept_ride(self, ride) :
        ride.set_driver(self);



class Ride :
    def __init__(self, start, end) -> None:
        self.start = start;
        self.end = end;
        self.driver = None;
        self.rider = None;
        self.start_time = None;
        self.end_time = None;
        self.fare = None;

    def set_driver(self, driver) :
        self.driver = driver;
    
    def set_rider(self, rider) :
        self.rider = rider;

    def start_ride(self) :
        self.start_ride = datetime.datetime.now();

    def end_ride(self) :
        self.end_ride = datetime.datetime.now();
        self.rider.wallet -= self.fare;
        self.driver.wallet += self.fare;


class RideRequest :
    def __init__(self, rider, destination) -> None:
        self.rider = rider;
        self.destination = destination;


class RideMatch :
    def __init__(self) -> None:
        self.available_drivers = [];

    def find_driver(self, ride_request) :
        if(len(self.available_drivers) > 0) :
            # Todo : Find the Closest Drivers
            driver = self.available_drivers[0];
            ride = Ride(ride_request.rider.location, ride_request.destination);
            driver.accept_ride(ride);
            return ride;
