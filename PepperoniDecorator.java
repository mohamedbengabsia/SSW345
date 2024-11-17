public class PepperoniDecorator extends ToppingDecorator {
    public PepperoniDecorator(Pizza pizza) {
        super(pizza);
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", pepperoni";
    }

    @Override
    public double getCost() {
        return super.getCost() + 1.50;
    }
}
