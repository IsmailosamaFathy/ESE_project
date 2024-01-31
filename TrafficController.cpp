// Include necessary headers
#include <iostream>
#include <cmath>
#include <chrono>
#include <thread>

// Include the header file with class declaration
#include "TrafficController.h"

// Constructor definition
TrafficController::TrafficController() {
    // Constructor implementation, if needed
}

void TrafficController::setup() {
    std::cout << "Simulating pinMode" << std::endl;
}

void TrafficController::loop(int potValueRoad1, int potValueRoad2) {
    int durationRoad1 = map(potValueRoad1, 0, 1023, 5000, 15000);
    int durationRoad2 = map(potValueRoad2, 0, 1023, 5000, 15000);

    std::cout << "Road 1 Duration: " << durationRoad1 << std::endl;
    std::cout << "Road 2 Duration: " << durationRoad2 << std::endl;

    if (potValueRoad1 > potValueRoad2) {
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));

        std::this_thread::sleep_for(std::chrono::milliseconds(2000));

        std::this_thread::sleep_for(std::chrono::milliseconds(durationRoad1));
    } else {
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));

        std::this_thread::sleep_for(std::chrono::milliseconds(2000));

        std::this_thread::sleep_for(std::chrono::milliseconds(durationRoad2));
    }

    std::cout << "Simulating digitalWrite for turning off all LEDs" << std::endl;
}

int TrafficController::map(int x, int in_min, int in_max, int out_min, int out_max) {
    return static_cast<int>(std::round((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min));
}

int TrafficController::mapWrapper(int x, int in_min, int in_max, int out_min, int out_max) {
    return map(x, in_min, in_max, out_min, out_max);
}
