package Repository;

import Entity.Mage;
import Entity.Tower;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import java.util.List;

public class MageRepository extends BaseRepository<Mage, String> {
    public MageRepository(EntityManagerFactory emf, Class<Mage> clazz) {
        super(emf, clazz);
    }

    public List<Mage> getMagesFromTower(Tower tower) {
        EntityManager em = getEmf().createEntityManager();
        List<Mage> list = em.createQuery("SELECT mage from Mage mage WHERE mage.tower=:tower", Mage.class)
                .setParameter("tower", tower).getResultList();
        em.close();
        return list;
    }
}
