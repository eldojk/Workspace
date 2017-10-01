package design.callCentre;

/**
 * Created by joseph
 */
public class Call {
    private CallState state;
    private Employee callOwner;
    private Rank callRank;

    public Call() {
        state = CallState.READY;
    }

    public CallState getState() {
        return state;
    }

    public void setState(CallState state) {
        this.state = state;
    }

    public Employee getCallOwner() {
        return callOwner;
    }

    public void setCallOwner(Employee callOwner) {
        this.callOwner = callOwner;
    }

    public Rank getCallRank() {
        return callRank;
    }

    public void setCallRank(Rank callRank) {
        this.callRank = callRank;
    }
}
