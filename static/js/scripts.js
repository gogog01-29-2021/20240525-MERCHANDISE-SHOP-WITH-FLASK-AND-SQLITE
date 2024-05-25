function fetchPurchases() {
    fetch('/get_purchases')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#purchases-table tbody');
            tableBody.innerHTML = '';
            data.forEach(purchase => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${purchase.purchase_id}</td>
                    <td>${purchase.customer_name}</td>
                    <td>${purchase.product_name}</td>
                    <td>${purchase.quantity}</td>
                    <td>${purchase.purchase_date}</td>
                `;
                tableBody.appendChild(row);
            });
        });
}

function addPurchase() {
    const customer_id = document.getElementById('customer_id').value;
    const product_id = document.getElementById('product_id').value;
    const quantity = document.getElementById('quantity').value;
    const purchase_date = document.getElementById('purchase_date').value;

    fetch('/add_purchase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            customer_id: customer_id,
            product_id: product_id,
            quantity: quantity,
            purchase_date: purchase_date
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchPurchases(); // Refresh the purchases list
    });
}
