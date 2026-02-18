const booksContainer = document.getElementById('books-container');
const paginationDiv = document.getElementById('pagination');

let currentQuery = '';
let currentPage = 1;
let currentSize = 3;

// ====== Add Book ======
document.getElementById('add-book-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const publisher = document.getElementById('publisher').value;
    const image_url = document.getElementById('image_url').value;

    const res = await fetch('http://127.0.0.1:8000/create', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({title, author, publisher, image_url})
    });

    const data = await res.json();
    alert(data.message);
    document.getElementById('add-book-form').reset();
});

// ====== Search Books ======
async function searchBooks(query=currentQuery, page=currentPage, size=currentSize) {
    const res = await fetch(`http://127.0.0.1:8000/search?q=${encodeURIComponent(query)}&page=${page}&size=${size}`);
    const data = await res.json();
    displayBooks(data.Results);
    setupPagination(data.Total_Results, page, size);
}

// ====== Display Books ======
function displayBooks(books) {
    booksContainer.innerHTML = '';
    books.forEach(book => {
        const div = document.createElement('div');
        div.className = 'book-card';
        div.innerHTML = `
            <img src="${book.image_url}" onclick="window.open('${book.image_url}','_blank')">
            <div class="book-title">${book.title}</div>
            <div class="book-author">${book.author}</div>
            <div class="book-publisher">${book.publisher}</div>
        `;
        booksContainer.appendChild(div);
    });
}

// ====== Pagination ======
function setupPagination(total, page, size) {
    paginationDiv.innerHTML = '';
    const totalPages = Math.ceil(total / size);
    for(let i=1;i<=totalPages;i++){
        const btn = document.createElement('button');
        btn.textContent = i;
        if(i === page) btn.style.opacity = 0.5;
        btn.onclick = () => { currentPage = i; searchBooks(); };
        paginationDiv.appendChild(btn);
    }
}

// ====== Search Form Submit ======
document.getElementById('search-form').addEventListener('submit', (e)=>{
    e.preventDefault();
    currentQuery = document.getElementById('search-query').value;
    currentPage = parseInt(document.getElementById('page').value) || 1;
    currentSize = parseInt(document.getElementById('size').value) || 3;
    searchBooks();
});

// ====== Press Enter to Search ======
document.getElementById('search-query').addEventListener('keypress', (e)=>{
    if(e.key === 'Enter'){
        e.preventDefault();
        currentQuery = document.getElementById('search-query').value;
        currentPage = parseInt(document.getElementById('page').value) || 1;
        currentSize = parseInt(document.getElementById('size').value) || 3;
        searchBooks();
    }
});
