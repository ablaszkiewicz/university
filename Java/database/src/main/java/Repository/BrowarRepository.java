package Repository;

import Entity.Browar;
import Entity.Piwo;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import java.util.List;

public class BrowarRepository extends BaseRepository<Browar, String> {
    public BrowarRepository(EntityManagerFactory emf, Class<Browar> clazz) {
        super(emf, clazz);
    }

    public List<Browar> getBrowarsWithBeerCheaperThan(long price) {
        EntityManager em = getEmf().createEntityManager();
        List<Browar> list = em.createQuery("SELECT piwo.browar from Piwo piwo WHERE piwo.cena <:price", Browar.class)
                .setParameter("price", price).getResultList();
        em.close();
        return list;
    }
}
