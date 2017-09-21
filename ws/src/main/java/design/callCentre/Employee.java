package design.callCentre;

/**
 * Created by joseph
 */
public abstract class Employee {
    private String name;
    private Rank rank;
    private Call call;
    private CallCentre callCentre;

    public Employee(String name, Rank rank, CallCentre callCentre) {
        this.name = name;
        this.rank = rank;
        this.callCentre = callCentre;
    }

    public void attendCall(Call call) {
        this.call = call;
        this.call.setCallOwner(this);
        this.call.setState(CallState.IN_PROGRESS);
    }

    public void finishCall() {
        if (call == null)
            return;

        call.setCallOwner(null);
        call.setState(CallState.COMPLETED);
        call = null;
    }

    public boolean isFree() {
        return this.call == null;
    }

    protected void escalate() {
        Call myCall = call;
        myCall.setCallOwner(null);
        call = null;
        callCentre.notifyCallEscalation(call);
    }

    public abstract void escalateCall();

    protected Call getCall() {
        return call;
    }
}
