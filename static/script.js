// script.js

document.addEventListener('DOMContentLoaded', function() {
    const currentPage = window.location.pathname.split('/').pop();

    switch(currentPage) {
        case 'index.html':
            handleCustomerInfoPage();
            break;
        case 'loan-purpose.html':
            handleLoanPurposePage();
            break;
        case 'loan-amount.html':
            handleLoanAmountPage();
            break;
        case 'personalized-quote.html':
            handlePersonalizedQuotePage();
            break;
        case 'application-successful.html':
            // No specific handling needed for this page
            break;
    }
});

function handleCustomerInfoPage() {
    const form = document.getElementById('customerForm');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        localStorage.setItem('customerInfo', JSON.stringify({
            earnings: document.getElementById('earnings').value,
            spends: document.getElementById('spends').value,
            rental: document.getElementById('rental').value,
            dependents: document.getElementById('dependents').value,
            maritalStatus: document.getElementById('maritalStatus').value
        }));
        window.location.href = 'loan-purpose.html';
    });
}

function handleLoanPurposePage() {
    const form = document.getElementById('purposeForm');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        localStorage.setItem('loanPurpose', document.getElementById('purpose').value);
        window.location.href = 'loan-amount.html';
    });
}

function handleLoanAmountPage() {
    const form = document.getElementById('amountForm');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        localStorage.setItem('loanAmount', document.getElementById('loanAmount').value);
        window.location.href = 'personalized-quote.html';
    });
}

function handlePersonalizedQuotePage() {
    const quoteDetails = document.getElementById('quoteDetails');
    const proceedButton = document.getElementById('proceed');
    const aiChatPopup = document.getElementById('aiChatPopup');
    const chatNowButton = document.getElementById('chatNow');
    const closePopupButton = document.getElementById('closePopup');

    const quote = generateQuote();
    quoteDetails.innerHTML = `
        <p>Loan Amount: $${quote.loanAmount}</p>
        <p>APR: ${quote.apr}%</p>
        <p>Monthly Payment: $${quote.monthlyPayment}</p>
        <p>Tenure: ${quote.tenure} months</p>
    `;

    setTimeout(function() {
        aiChatPopup.style.display = 'block';
    }, 5000);

    chatNowButton.addEventListener('click', function() {
        console.log("Opening AI chat...");
        // Implement AI chat functionality here
        aiChatPopup.style.display = 'none';
    });

    closePopupButton.addEventListener('click', function() {
        aiChatPopup.style.display = 'none';
    });

    proceedButton.addEventListener('click', function() {
        window.location.href = 'application-successful.html';
    });
}

function generateQuote() {
    const loanAmount = localStorage.getItem('loanAmount');
    return {
        loanAmount: loanAmount,
        apr: (Math.random() * 10 + 5).toFixed(2),
        monthlyPayment: (loanAmount / 12).toFixed(2),
        tenure: 12
    };
}