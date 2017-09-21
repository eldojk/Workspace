package design.callCentre;

/**
 * Created by joseph
 */
public class Operator extends Employee {

    public Operator(String name, Rank rank, CallCentre callCentre) {
        super(name, rank, callCentre);
    }

    @Override
    public void escalateCall() {
        Call call = getCall();
        call.setCallRank(Rank.SUPERVISOR);
        escalate();
    }
}
