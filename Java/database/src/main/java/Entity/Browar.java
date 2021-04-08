package Entity;

import lombok.*;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import java.util.List;

@Getter
@Setter
@EqualsAndHashCode
@Entity
@ToString
@NoArgsConstructor
public class Browar {
    @Id
    private String name;

    private long wartosc;

    @OneToMany(mappedBy = "browar")
    @ToString.Exclude
    private List<Piwo> piwa;

    public Browar(String name, long wartosc) {
        this.name = name;
        this.wartosc = wartosc;
    }
}
