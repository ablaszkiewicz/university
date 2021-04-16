import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;


public class RepositoryTest {
    private PiwoRepository piwoRepository;

    @BeforeEach
    public void setup() {
        piwoRepository = new PiwoRepository();
    }

    @Test
    @DisplayName("Should return an exception when adding 2 piwo with same name")
    public void testDoubleInsert() {
        Piwo piwo = new Piwo();
        piwo.setName("Piwo");
        piwoRepository.insert(piwo);
        Throwable e = assertThrows(IllegalArgumentException.class, () -> piwoRepository.insert(piwo));
    }

    @Test
    @DisplayName("Should return an exception when removing piwo which doesn't exist")
    public void testEmptyRemove() {
        Throwable e = assertThrows(IllegalArgumentException.class, () -> piwoRepository.remove("piwko"));
    }

    @Test
    @DisplayName("Should return saved piwo")
    public void testFind(){
        Piwo piwo = new Piwo();
        piwo.setName("piweczko");
        piwoRepository.insert(piwo);
        assertEquals(piwoRepository.find("piweczko"), piwo, "Should return saved piwo");
    }

    @Test
    @DisplayName("Should return empty object")
    public void testEmptyLoad(){
        assertEquals(piwoRepository.find("piwero"), new Piwo(), "Should ");
    }
}
