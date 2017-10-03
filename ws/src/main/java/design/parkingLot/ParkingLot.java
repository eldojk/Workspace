package design.parkingLot;

import java.util.Map;

/**
 * Created by joseph
 */
public class ParkingLot {
    private String parkingLotId;
    private String zipCode;

    private Map<Size, ParkingBay> spots;

    public void parkVehicle(Vehicle vehicle) throws IndexOutOfBoundsException {
        Size size = vehicle.getSize();

        switch (size) {
            case S:
                ParkingBay sBay = spots.get(Size.S);

                if (sBay.hasFreeSpots()) {
                    sBay.parkVehicle(vehicle);
                    break;
                }

            case M:
                ParkingBay mBay = spots.get(Size.M);

                if (mBay.hasFreeSpots()) {
                    mBay.parkVehicle(vehicle);
                    break;
                }

            case L:
                ParkingBay lBay = spots.get(Size.L);

                if (lBay.hasFreeSpots()) {
                    lBay.parkVehicle(vehicle);
                    break;
                }

            case XL:
                ParkingBay xlBay = spots.get(Size.XL);

                if (xlBay.hasFreeSpots()) {
                    xlBay.parkVehicle(vehicle);
                    break;
                }
        }
    }

    public Vehicle unParkVehicle(String vehicleId) {

        for (Size size : spots.keySet()) {
            ParkingBay bay = spots.get(size);

            if (bay.isVehiclePresent(vehicleId)) {
                 return bay.unParkVehicle(vehicleId);
            }
        }

        return null;
    }
}
