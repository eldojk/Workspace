package design.callCentre;

import sun.reflect.generics.reflectiveObjects.NotImplementedException;

/**
 * Created by joseph
 */
public class Director extends Employee {

    public Director(String name, Rank rank, CallCentre callCentre) {
        super(name, rank, callCentre);
    }

    @Override
    public void escalateCall() {
        throw new NotImplementedException();
    }
}
