import java.util.*;

public enum ResourceType {
    WOOD,
    GOLD,
    STEEL;

    private static final List<ResourceType> VALUES = List.of(values());
    private static final int SIZE = VALUES.size();
    private static final Random RANDOM = new Random();

    public static ResourceType randomResourceType()  {
        return VALUES.get(RANDOM.nextInt(SIZE));
    }

    public static List<ResourceType> getResources() {
        return VALUES;
    }
}
