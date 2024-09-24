document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('financialForm');
    let总收入 = 0;
    let总支出 = 0;

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const income = parseFloat(form.income.value) || 0;
        const expense = parseFloat(form.expense.value) || 0;

        总收入 += income;
        总支出 += expense;

        updateUI();
    });

    function updateUI() {
        document.getElementById('totalIncome').textContent =总收入;
        document.getElementById('totalExpense').textContent =总支出;
        document.getElementById('netIncome').textContent =总收入 -总支出;
    }
});