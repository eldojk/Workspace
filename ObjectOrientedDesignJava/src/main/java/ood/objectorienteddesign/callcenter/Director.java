package ood.objectorienteddesign.callcenter;

public class Director extends Employee implements ICallHandler {

	public Director() {
		rank = Rank.DIRECTOR;
	}

	public void recieveCall(Call call) {
		System.out.println("Director taking call");
		currentCall = call;
		currentCall.attend();
	}

	public void escalateCall() {
		CallCenter myCallCenter = CallCenter.getInstance();
		myCallCenter.requestEscalation(currentCall, rank);
	}

	public void endCall() {
		currentCall.finish();
		currentCall = null;
		CallCenter myCallCenter = CallCenter.getInstance();
		myCallCenter.reAssignCallHandler(this);
	}

}
