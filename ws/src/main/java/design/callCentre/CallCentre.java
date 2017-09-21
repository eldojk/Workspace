package design.callCentre;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by joseph
 */
public class CallCentre {
    private List<Call> directorCallQueue;
    private List<Call> supervisorCallQueue;
    private List<Call> operatorCallQueue;

    private List<Employee> directors;
    private List<Employee> supervisors;
    private List<Employee> operators;

    public CallCentre(List<Employee> directors, List<Employee> supervisors, List<Employee> operators) {
        directorCallQueue = new LinkedList<>();
        supervisorCallQueue = new LinkedList<>();
        operatorCallQueue = new LinkedList<>();
        this.directors = directors;
        this.supervisors = supervisors;
        this.operators = operators;
    }

    private Call deQueueCall(List<Call> callQueue) {
        int lastIndex = callQueue.size() - 1;

        if (lastIndex == -1)
            return null;

        return callQueue.remove(lastIndex);
    }

    public Call deQueueCall(Rank rank) {
        switch (rank) {
            case DIRECTOR:
                return deQueueCall(directorCallQueue);

            case OPERATOR:
                return deQueueCall(operatorCallQueue);

            case SUPERVISOR:
                return deQueueCall(supervisorCallQueue);

            default:
                return null;
        }
    }

    private boolean assignToFreeEmployee(List<Employee> employees, Call call) {
        for (Employee employee : employees) {
            if (employee.isFree()) {
                employee.attendCall(call);
                return true;
            }
        }

        return false;
    }

    public void notifyCallEscalation(Call call) {
        boolean isAssigned = false;

        switch (call.getCallRank()) {
            case OPERATOR:
                isAssigned = assignToFreeEmployee(operators, call);

                if (isAssigned)
                    break;

            case SUPERVISOR:
                isAssigned = assignToFreeEmployee(supervisors, call);

                if (isAssigned)
                    break;

            case DIRECTOR:
                isAssigned = assignToFreeEmployee(directors, call);
                break;
        }

        if (!isAssigned) {
            switch (call.getCallRank()) {
                case OPERATOR:
                    deQueueCall(operatorCallQueue);
                    break;

                case SUPERVISOR:
                    deQueueCall(supervisorCallQueue);
                    break;

                case DIRECTOR:
                    deQueueCall(directorCallQueue);
                    break;
            }
        }
    }
}
