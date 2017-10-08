package design.parkingLot;

import java.util.*;

/**
 * Created by joseph
 */
public class ParkingBay {
    private Size size;
    private Stack<Spot> freeSpots;

    private Map<String, Spot> lookupMap;

    public ParkingBay(int numSpots, Size size) {
        freeSpots = new Stack<>();
        lookupMap = new HashMap<>();

        while (numSpots > 0) {
            freeSpots.push(new Spot(String.valueOf(numSpots), size));
        }
    }

    private Size getSize() {
        return size;
    }

    public void parkVehicle(Vehicle vehicle) throws IndexOutOfBoundsException {
        if (freeSpots.empty())
            throw new IndexOutOfBoundsException("Out of free spots");

        Spot spot = freeSpots.pop();
        spot.setVehicle(vehicle);
        lookupMap.put(vehicle.getVehicleId(), spot);
    }

    public boolean isVehiclePresent(String vehicleId) {
        return lookupMap.get(vehicleId) != null;
    }

    public Vehicle unParkVehicle(String vehicleId) {
        Spot spot = lookupMap.get(vehicleId);

        if (spot == null) {
            return null;
        }

        Vehicle vehicle = spot.getVehicle();
        spot.setVehicle(null);
        freeSpots.push(spot);

        return vehicle;
    }

    public boolean hasFreeSpots() {
        return !freeSpots.empty();
    }
}
