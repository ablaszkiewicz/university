package Entity;

import lombok.*;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import java.util.List;

@Getter
@Setter
@EqualsAndHashCode
@Entity
@ToString
@NoArgsConstructor
public class Tower {
    @Id
    private String name;

    private int height;

    @OneToMany(mappedBy = "tower")
    @ToString.Exclude
    private List<Mage> mages;

    public Tower(String name, int height) {
        this.name = name;
        this.height = height;
    }
}
