package Repository;

import Entity.Tower;

import javax.persistence.EntityManagerFactory;

public class TowerRepository extends BaseRepository<Tower, String> {
    public TowerRepository(EntityManagerFactory emf, Class<Tower> clazz) {
        super(emf, clazz);
    }
}
