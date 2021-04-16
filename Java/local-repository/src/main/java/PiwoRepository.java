import java.util.ArrayList;
import java.util.Optional;

public class PiwoRepository {
    private ArrayList<Piwo> piwos = new ArrayList<Piwo>();

    public Piwo find(String name) {
        Piwo searched = piwos.stream().filter(piwo -> piwo.getName().equals(name)).findFirst().orElse(new Piwo());
        return searched;
    }

    public void remove(String name) throws IllegalArgumentException {
        for(Piwo piwo : piwos) {
            if(piwo.getName().equals(name)) {
                piwos.remove(piwo);
                return;
            }
        }
        throw new IllegalArgumentException("Piwo " + name + " not found.");
    }

    public void insert(Piwo piwo) throws IllegalArgumentException {
        if(piwos.contains(piwo)) {
            throw new IllegalArgumentException("Piwo with this name already exists.");
        } else {
            piwos.add(piwo);
        }
    }
}
