import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class Warehouse {
    private final int MAX_CAPACITY = 10;
    private final Map<ResourceType, Integer> resourcesAmount = new HashMap<ResourceType, Integer>();

    public Warehouse() {
        initializeResourcesAmount();
    }

    public synchronized void take(ResourceRequest request) throws InterruptedException {
        while(!hasSufficientResources(request)) {
            wait();
        }
        notifyAll();
        processSellRequest(request);
    }

    public synchronized void put(ResourceRequest request) throws InterruptedException {
        while(!hasSufficientCapacity(request)) {
            wait();
        }
        notifyAll();
        processBuyRequest(request);
    }

    private void processBuyRequest(ResourceRequest request) {
        System.out.println("Got " + request.getAmount() + " " + request.getResourceType());

        ResourceType resourceType = request.getResourceType();
        int amountToBeAdded = request.getAmount();

        int currentAmount = resourcesAmount.get(resourceType);

        resourcesAmount.put(resourceType, currentAmount + amountToBeAdded);
    }

    private void processSellRequest(ResourceRequest request) {
        System.out.println("Sold " + request.getAmount() + " " + request.getResourceType());

        ResourceType resourceType = request.getResourceType();
        int amountToBeSubtracted = request.getAmount();

        int currentAmount = resourcesAmount.get(resourceType);

        resourcesAmount.put(resourceType, currentAmount - amountToBeSubtracted);
    }

    private boolean hasSufficientResources(ResourceRequest request) {
        return resourcesAmount.get(request.getResourceType()) > request.getAmount();
    }

    private boolean hasSufficientCapacity(ResourceRequest request) {
        return resourcesAmount.get(request.getResourceType()) < MAX_CAPACITY;
    }

    private void initializeResourcesAmount() {
        List<ResourceType> resourceTypes = ResourceType.getResources();

        for(ResourceType resourceType : resourceTypes) {
            resourcesAmount.put(resourceType, 0);
        }
    }
}
