package design.callCentre;

/**
 * Created by joseph
 */
public class Supervisor extends Employee {

    public Supervisor(String name, Rank rank, CallCentre callCentre) {
        super(name, rank, callCentre);
    }

    @Override
    public void escalateCall() {
        Call call = getCall();
        call.setCallRank(Rank.DIRECTOR);
        escalate();
    }
}
