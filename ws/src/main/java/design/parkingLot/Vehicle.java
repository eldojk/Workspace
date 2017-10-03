package design.parkingLot;

/**
 * Created by joseph
 */
public abstract class Vehicle {
    private String vehicleId;

    public String getVehicleId() {
        return vehicleId;
    }

    public Vehicle(String vehicleId) {
        this.vehicleId = vehicleId;
    }

    public abstract Size getSize();
}
