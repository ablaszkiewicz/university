package Repository;

import Entity.Piwo;
import Entity.Browar;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import java.util.List;

public class PiwoRepository extends BaseRepository<Piwo, String> {
    public PiwoRepository(EntityManagerFactory emf, Class<Piwo> clazz) {
        super(emf, clazz);
    }
}
