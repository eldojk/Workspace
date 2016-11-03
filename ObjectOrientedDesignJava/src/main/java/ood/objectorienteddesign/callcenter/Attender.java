package ood.objectorienteddesign.callcenter;

public class Attender extends Employee implements ICallHandler {

	public Attender() {
		rank = Rank.ATTENDER;
	}

	public void recieveCall(Call call) {
		System.out.println("Attender taking call");
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
