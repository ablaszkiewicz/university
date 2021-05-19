import java.util.concurrent.ThreadLocalRandom;

public class Consumer implements Runnable {
    private final int MIN_INTERVAL = 1;
    private final int MAX_INTERVAL = 2;
    private final int MIN_AMOUNT = 2;
    private final int MAX_AMOUNT = 5;

    private final Warehouse warehouse;

    public Consumer(Warehouse warehouse) {
        this.warehouse = warehouse;
    }

    @Override
    public void run() {
        while(!Thread.interrupted()) {
            try {
                ResourceRequest resourceRequest = buyRequest();
                warehouse.requestResource(resourceRequest);
            } catch(InterruptedException e) {
                System.out.println("Producer's thread got interrupted");
            }
        }
    }

    private ResourceRequest buyRequest() {
        waitForRandom();
        return formResourceRequest();
    }

    private void waitForRandom() {
        try {
            int waitTime = ThreadLocalRandom.current().nextInt(MIN_INTERVAL * 1000, MAX_INTERVAL * 1000);
            Thread.sleep(waitTime);
        } catch (InterruptedException e) {
            System.out.println("Producer's thread got interrupted");
        }
    }

    private ResourceRequest formResourceRequest() {
        int amount = ThreadLocalRandom.current().nextInt(MIN_AMOUNT, MAX_AMOUNT);
        ResourceType type = ResourceType.randomResourceType();
        return new ResourceRequest(type, amount);
    }
}
