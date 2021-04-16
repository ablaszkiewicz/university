import lombok.*;

@Setter
@Getter
@ToString
@EqualsAndHashCode
@NoArgsConstructor
public class Piwo {
    private String name;
    @ToString.Exclude
    private int alcoholPercentage;

    public Piwo(String name, int alcoholPercentage) {
        this.name = name;
        this.alcoholPercentage = alcoholPercentage;
    }
}
