class Main {

    static class InsufficientFundsError extends Exception {
        public InsufficientFundsError(String message) {
            super(message);
        }
    }

    static class BankAccount {

        private static int accCounter = 100;

        private int accNumber;
        private String name;
        private double balance;

        public BankAccount(String name, double balance) {
            accCounter++;
            this.accNumber = accCounter;
            this.name = name;
            this.balance = balance;
        }

        public void deposit(double amount) {
            balance += amount;
        }

        public void withdraw(double amount) throws InsufficientFundsError {
            if (amount > 0 && amount <= balance) {
                balance -= amount;
            } else {
                throw new InsufficientFundsError("Not Enough Funds you rookie");
            }
        }

        public double getBalance() {
            return balance;
        }

        public String details() {
            return accNumber + ", " + name + ", " + balance;
        }
    }

    public static void main(String[] args) {

        BankAccount harshith = new BankAccount("Harshith", 100000);
        BankAccount reddy = new BankAccount("Reddy", 1000055555);

        System.out.println(harshith.details());
        System.out.println(reddy.details());
    }
}