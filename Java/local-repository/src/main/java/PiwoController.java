import java.util.Optional;

public class PiwoController {
    private PiwoRepository piwoRepository;

    public PiwoController(PiwoRepository piwoRepository) {
        this.piwoRepository = piwoRepository;
    }

    public String find(String name) {
        Piwo piwo = piwoRepository.find(name);
        if(piwo.getName() == null) {
            return "not found";
        } else {
            return piwo.toString();
        }
    }

    public String delete(String name) {
        try {
            piwoRepository.remove(name);
            return "done";
        } catch (IllegalArgumentException ex) {
            return "not found";
        }
    }

    public String insert(String name, int alcoholPercentage) {
        try {
            piwoRepository.insert(new Piwo(name, alcoholPercentage));
            return "done";
        } catch (IllegalArgumentException ex) {
            return "bad request";
        }
    }
}
