package ood.objectorienteddesign.callcenter;

public interface ICallHandler {
	public Rank getRank();
	
	public void recieveCall(Call call);
	
	public void escalateCall();
	
	public void endCall();
}
