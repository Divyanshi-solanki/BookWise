document.addEventListener('DOMContentLoaded', () => {
    const searchBtn = document.getElementById('search-btn');
    const bookInput = document.getElementById('book-title');
    const resultsContainer = document.getElementById('results-container');
    const errorToast = document.getElementById('error-message');
    
    const resTitle = document.getElementById('res-title');
    const resAuthors = document.getElementById('res-authors');
    const resSummary = document.getElementById('res-summary');
    const resDescription = document.getElementById('res-description');

    const handleSearch = async () => {
        const title = bookInput.value.trim();
        if (!title) return;

        // Reset UI
        resultsContainer.classList.add('hidden');
        errorToast.classList.add('hidden');
        searchBtn.classList.add('loading');
        searchBtn.disabled = true;

        try {
            const response = await fetch(`/book?title=${encodeURIComponent(title)}`);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Something went wrong');
            }

            // Populate Results
            resTitle.textContent = data.title;
            resAuthors.textContent = Array.isArray(data.authors) 
                ? data.authors.join(', ') 
                : data.authors;
            resSummary.textContent = data.summary;
            resDescription.textContent = data.description;

            // Show Results
            resultsContainer.classList.remove('hidden');
            resultsContainer.scrollIntoView({ behavior: 'smooth' });

        } catch (error) {
            showError(error.message);
        } finally {
            searchBtn.classList.remove('loading');
            searchBtn.disabled = false;
        }
    };

    const showError = (msg) => {
        errorToast.textContent = msg;
        errorToast.classList.remove('hidden');
        setTimeout(() => {
            errorToast.classList.add('hidden');
        }, 5000);
    };

    searchBtn.addEventListener('click', handleSearch);
    
    bookInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleSearch();
        }
    });
});
