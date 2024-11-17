public class MushroomDecorator extends ToppingDecorator {
    public MushroomDecorator(Pizza pizza) {
        super(pizza);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", mushrooms";
    }

    @Override
    public double getCost() {
        return super.getCost() + 1.25;
    }
}
