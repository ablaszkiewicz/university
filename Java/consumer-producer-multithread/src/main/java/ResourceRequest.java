import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class ResourceRequest {
    private ResourceType resourceType;
    private int amount;

    public ResourceRequest(ResourceType resourceType, int amount) {
        this.resourceType = resourceType;
        this.amount = amount;
    }
}
