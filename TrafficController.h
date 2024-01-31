// Include necessary headers
#include <iostream>
#include <cmath>
#include <chrono>
#include <thread>

// Include guard to prevent multiple inclusion of the same code
#ifndef TRAFFIC_CONTROLLER_H
#define TRAFFIC_CONTROLLER_H

// Class definition for TrafficController
class TrafficController {
public:
    TrafficController();  // Constructor

    // Simulating pinMode (not applicable in a non-Arduino environment)
    void setup();

    // Simulating digitalWrite and delay
    void loop(int potValueRoad1, int potValueRoad2);

    // Public wrapper method for testing
    int mapWrapper(int x, int in_min, int in_max, int out_min, int out_max);

private:
    // The actual map function
    int map(int x, int in_min, int in_max, int out_min, int out_max);
};

#endif // TRAFFIC_CONTROLLER_H

