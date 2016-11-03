package ood.objectorienteddesign.callcenter;

public class Employee {
	protected Rank rank;
	protected Call currentCall;

	public Rank getRank() {
		return rank;
	}

	public boolean isFree() {
		return currentCall == null;
	}
}
