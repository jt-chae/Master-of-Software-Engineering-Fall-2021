import java.util.concurrent.ArrayBlockingQueue;

public class Producer implements Runnable {
    private ArrayBlockingQueue queue; //add the object type ArrayBlockingQueue
    private boolean running = true;
    private int id;

    public Producer(ArrayBlockingQueue q, int n) { //add the object type ArrayBlockingQueue
	queue = q;
	id = n;
    }

    public void stop() {
	running = false;
    }

    public void run() {
	int count = 0;
	while (running) {
	    int n = RandomUtils.randomInteger();
	    try {
		Thread.sleep(n);
		Message msg = new Message("message-" + n);
		queue.put(msg); // Put the message in the queue with q.put()
		count++;
		RandomUtils.print("Produced " + msg.get(), id);
	    } catch (InterruptedException e) {
		e.printStackTrace();
	    }
	}
	// Put the stop message in the queue so that the consumer knows when to stop
	Message msg = new Message("stop");
	try {
	    queue.put(msg); // Put this final message in the queue with q.put()
	} catch (InterruptedException e) {
	    e.printStackTrace();
	}
	RandomUtils.print("Messages sent: " + count, id);
    }
}
