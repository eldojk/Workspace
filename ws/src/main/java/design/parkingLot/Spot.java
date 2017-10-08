package design.parkingLot;

/**
 * Created by joseph
 */
public class Spot {
    private String spotId;
    private Size size;
    private Vehicle vehicle;

    public Spot(String spotId, Size size) {
        this.spotId = spotId;
        this.size = size;
    }

    public String getSpotId() {
        return spotId;
    }

    public void setSpotId(String spotId) {
        this.spotId = spotId;
    }

    public Size getSize() {
        return size;
    }

    public void setSize(Size size) {
        this.size = size;
    }

    public Vehicle getVehicle() {
        return vehicle;
    }

    public void setVehicle(Vehicle vehicle) {
        this.vehicle = vehicle;
    }

    public boolean isFree() {
        return vehicle == null;
    }
}
