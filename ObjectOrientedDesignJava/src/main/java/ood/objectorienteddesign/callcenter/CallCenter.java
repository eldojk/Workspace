package ood.objectorienteddesign.callcenter;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Call Center (SingleTon)
 * 
 * @author eldo.joseph
 *
 */
public class CallCenter {
	private static CallCenter instance;
	private List<Queue<ICallHandler>> callHandlerQueue;
	private List<Call> droppedCalls;
	private List<Call> unresolvedCalls;

	private ICallHandler getCallHandler(Rank rank) {
		ICallHandler employee;

		switch (rank) {
		case ATTENDER:
			employee = new Attender();
			break;

		case MANAGER:
			employee = new Manager();
			break;

		default:
			employee = new Director();
			break;
		}

		return employee;
	}

	private Queue<ICallHandler> createCallHandlers(Rank rank, int number) {
		Queue<ICallHandler> queue = new LinkedList<ICallHandler>();
		while (number != 0) {
			queue.add(getCallHandler(rank));
			--number;
		}

		return queue;
	}

	/**
	 * Get a free call handler
	 * 
	 * @return
	 */
	private ICallHandler getFreeCallHandler() {
		if (callHandlerQueue.get(Rank.ATTENDER.ordinal()).peek() != null) {

			return callHandlerQueue.get(Rank.ATTENDER.ordinal()).poll();

		} else if (callHandlerQueue.get(Rank.MANAGER.ordinal()).peek() != null) {

			return callHandlerQueue.get(Rank.MANAGER.ordinal()).poll();

		} else {

			return callHandlerQueue.get(Rank.DIRECTOR.ordinal()).poll();

		}
	}

	/**
	 * Get a handler to handle an escalated call
	 * 
	 * @param rank
	 * @return
	 */
	private ICallHandler getEscalatedCallHandler(Rank rank) {
		ICallHandler escalationHandler;

		switch (rank) {
		case ATTENDER:
			escalationHandler = callHandlerQueue.get(Rank.MANAGER.ordinal())
					.poll();
			if (escalationHandler != null)
				return escalationHandler;

		case MANAGER:
			escalationHandler = callHandlerQueue.get(Rank.DIRECTOR.ordinal())
					.poll();
			break;

		default:
			escalationHandler = null;
			break;
		}

		return escalationHandler;
	}

	private CallCenter() {
		callHandlerQueue = new ArrayList<Queue<ICallHandler>>();
		callHandlerQueue.add(createCallHandlers(Rank.ATTENDER, 10));
		callHandlerQueue.add(createCallHandlers(Rank.MANAGER, 4));
		callHandlerQueue.add(createCallHandlers(Rank.DIRECTOR, 2));
	}

	/**
	 * Get Singleton CallCenter instance
	 * 
	 * @return
	 */
	public static CallCenter getInstance() {
		if (instance == null) {
			instance = new CallCenter();
		}

		return instance;
	}

	/**
	 * Assign a call to someone free
	 * 
	 * @param call
	 */
	public void assignCall(Call call) {
		ICallHandler callHandler = getFreeCallHandler();

		if (callHandler == null) {
			call.drop();
			droppedCalls.add(call);
			return;
		}

		callHandler.recieveCall(call);
	}

	/**
	 * Request an escalation for a call from someone with a rank
	 *
	 * @param call
	 * @param rank
	 */
	public void requestEscalation(Call call, Rank rank) {
		ICallHandler escalatedCallHandler = getEscalatedCallHandler(rank);

		if (escalatedCallHandler == null) {
			call.markUnResolved();
			unresolvedCalls.add(call);
			return;
		}

		escalatedCallHandler.recieveCall(call);
	}

	/**
	 * Free a call handler and push them back to queue
	 * 
	 * @param callHandler
	 */
	public void reAssignCallHandler(ICallHandler callHandler) {
		callHandlerQueue.get(callHandler.getRank().ordinal()).add(callHandler);
	}
}
