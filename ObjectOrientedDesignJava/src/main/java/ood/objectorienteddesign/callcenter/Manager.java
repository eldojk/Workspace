package ood.objectorienteddesign.callcenter;

public class Manager extends Employee implements ICallHandler {

	public Manager() {
		rank = Rank.MANAGER;
	}

	public void recieveCall(Call call) {
		System.out.println("Manager taking call");
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
