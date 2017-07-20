package workspace.ws.ds.algos.misc;

import java.util.ArrayList;
import java.util.List;

/**
 * msft
 * 
 * @author eldo.joseph
 *
 */
class PC {
	private final int CAPACITY = 5;
	private List<Integer> list = new ArrayList<Integer>();
	private int value = 0;

	public void produce() throws InterruptedException {

		synchronized (this) {

			while (true) {

				while (list.size() == CAPACITY) {
					wait();
				}

				list.add(++value);
				System.out.println("Produced " + value);

				notify();

				//Thread.sleep(1000);
			}
		}
	}

	public void consume() throws InterruptedException {

		synchronized (this) {

			while (true) {

				while (list.size() == 0) {
					wait();
				}

				int val = list.remove(0);
				System.out.println("Consumed " + val);

				notify();

				Thread.sleep(300);
			}
		}
	}
}

public class ProducerConsumer {
	public static void main(String[] args) throws InterruptedException {
		final PC pc = new PC();

		Thread t1 = new Thread(new Runnable() {

			@Override
			public void run() {
				try {
					pc.produce();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

		});

		Thread t2 = new Thread(new Runnable() {

			@Override
			public void run() {
				try {
					pc.consume();
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

		});

		t1.start();
		t2.start();

		t1.join();
		t2.join();
	}
}
