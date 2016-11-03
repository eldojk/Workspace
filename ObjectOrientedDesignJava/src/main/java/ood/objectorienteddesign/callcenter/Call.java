package ood.objectorienteddesign.callcenter;

public class Call {
	private String number;
	private CallStatus status;

	public Call(String number) {
		this.number = number;
		this.status = CallStatus.CONNECTING;
	}

	public String getNumber() {
		return number;
	}

	public void setNumber(String number) {
		this.number = number;
	}

	public CallStatus getStatus() {
		return status;
	}

	public void setStatus(CallStatus status) {
		this.status = status;
	}

	public void drop() {
		status = CallStatus.DROPPED;
	}

	public void attend() {
		status = CallStatus.ATTENDING;
	}

	public void finish() {
		status = CallStatus.RESOLVED;
	}

	public void markUnResolved() {
		status = CallStatus.UNRESOLVED;
	}
}
